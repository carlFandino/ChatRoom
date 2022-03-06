"""
MIT License

Copyright (c) 2021 CarlFandino

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""



import socket
import threading
import sys,time

class Server:
	def __init__(self):
		try:
		    self.ip = socket.gethostbyname(socket.gethostname())
		    self.port = 8080
		    self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		    self.socket.bind((self.ip,self.port))
		    self.socket.listen(5)
		    self.numberOfOnline = 0
		    self.messages = []


		    self.users = {}
		    self.clients = []

		    threading.Thread(target=self.start).start()
		except KeyboardInterrupt:
			sys.exit()
	def broadcast(self,message):
		for client in self.clients:
			client.send(str(message).encode())
		self.messages.append(message)


	def handle(self,addr,conn):
		connected = True
		self.clients.append(conn)
		conn.send(f"\nloadMessage \n{[(i) for i in self.messages]}\n".encode())
		while connected:
		    
		    try:
		    	data = conn.recv(1024).decode()
		    	data = str(data)
		    	
		    	if data.split()[0] == "nickname":
		    		self.users[str(addr)] = data.split()[1]
		    		self.userJoined(data.split()[1])


		    	if data.split()[0] == "quit":
		    		self.userQuit(self.users[str(addr)])
		    		self.users.pop(str(addr))


		    	if data.split()[0] == "chat":
		    		self.userChat(self.users[str(addr)],data.replace('chat',''))



		    

		   
		    except ConnectionResetError:
			    #print(f"{self.users[str(addr)]} left.")
			    self.clients.pop(self.clients.index(conn))
			    connected = False
		    except ConnectionAbortedError:
		    	self.clients.pop(self.clients.index(conn))
		    	connected = False
		    except:
		    	pass
		


	def start(self):
		print("SERVER RUNNING...")
		while True:
			self.conn, self.addr = self.socket.accept()
			threading.Thread(target=self.handle,args=(self.addr,self.conn,),daemon=True).start()

	def userChat(self,name,chat):
		self.broadcast(f"chat from {name} : {chat}")

	def userJoined(self,name):
		self.broadcast(f"join {name} joined.")
		self.numberOfOnline += 1

	def userQuit(self,name):
		self.broadcast(f"left {name} left.")
		self.numberOfOnline -= 1

Server()
