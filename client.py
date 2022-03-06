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



from PyQt5 import QtWidgets,QtCore,QtGui,uic
import socket
import threading,time



class RegisterUi(QtWidgets.QWidget):
	def __init__(self,parent=None):
		super(RegisterUi,self).__init__(parent)
		uic.loadUi("register_ui.ui",self)


class MessageFrame(QtWidgets.QLabel):
	def __init__(self,animBool,y,text,sender,parent=None,x=650,width=151,height=31):
		super(MessageFrame,self).__init__()

		self.Message_2 = QtWidgets.QLabel(parent)
		self.Message_2.setEnabled(True)
		
		self.Message_2.setStyleSheet("border:none;\n"
"border-radius:10px;\n"
"background-color: rgb(255, 74, 74);\n"
"color: rgb(255, 255, 255);")
		self.Message_2.setAlignment(QtCore.Qt.AlignCenter)
		self.Message_2.setText(text)

		self.Message_2.setGeometry(QtCore.QRect(x, y,width, height))
		

		self.FromYou = QtWidgets.QLabel(parent)
		self.FromYou.setGeometry(QtCore.QRect(x+30, y-20, 111, 16))
		font = QtGui.QFont()
		font.setFamily("Microsoft JhengHei UI")
		font.setPointSize(10)
		font.setBold(False)
		font.setWeight(50)
		self.FromYou.setFont(font)
		self.FromYou.setStyleSheet("border:none;\n"
"border-radius:10px;\n"
"background-color:transparent;\n"
"color: rgb(0, 0, 0);")
		self.FromYou.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
		self.FromYou.setText(f"From {sender}")
		self.Message_2.show()
		self.FromYou.show()
		if animBool == True:
			self.anim(y)
		else:
			self.Message_2.setGeometry(QtCore.QRect(350, y, 151, 31))
			self.FromYou.setGeometry(QtCore.QRect(380, y-20, 111, 16))
	def anim(self,y):
		self.animMessage = QtCore.QPropertyAnimation(self.Message_2,b"pos")
		self.animMessage.setEndValue(QtCore.QPoint(350,y))
		self.animMessage.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
		self.animMessage.setDuration(100)
		self.animMessage.start()

		self.animMessage2 = QtCore.QPropertyAnimation(self.FromYou,b"pos")
		self.animMessage2.setEndValue(QtCore.QPoint(380,y-20))
		self.animMessage2.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
		self.animMessage2.setDuration(100)
		self.animMessage2.start()



class ClientMessage(QtWidgets.QLabel):
	def __init__(self,animBool,y,text,sender,parent=None,x=-200,width=151,height=31):
		super(ClientMessage,self).__init__()
		self.Message_3 = QtWidgets.QLabel(parent)
		self.Message_3.setGeometry(QtCore.QRect(x, y, width, height))
		self.Message_3.setStyleSheet("border:none;\n"
"border-radius:10px;\n"
"background-color: rgb(255, 152, 152);\n"
"color: rgb(255, 255, 255);")
		self.Message_3.setAlignment(QtCore.Qt.AlignCenter)
		self.Message_3.setObjectName("Message_3")
		self.Message_3.setText(text)
		

		self.FromClient = QtWidgets.QLabel(parent)
		self.FromClient.setGeometry(QtCore.QRect(30, 70, 111, 16))
		font = QtGui.QFont()
		font.setFamily("Microsoft JhengHei UI")
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.FromClient.setFont(font)
		self.FromClient.setStyleSheet("border:none;\n"
"border-radius:10px;\n"
"background-color:transparent;\n"
"color: rgb(0, 0, 0);")
		self.FromClient.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
		self.FromClient.setObjectName("FromClient")
		self.FromClient.setText(f"From {sender}")

		self.Message_3.show()
		self.FromClient.show()

		if animBool == True:
			self.anim(y)
		else:
			self.Message_3.setGeometry(QtCore.QRect(20,y,151,31))
			self.FromClient.setGeometry(QtCore.QRect(20, y-20, 111, 16))

	def anim(self,y):
		self.animMessage = QtCore.QPropertyAnimation(self.Message_3,b"pos")
		self.animMessage.setEndValue(QtCore.QPoint(20,y))
		self.animMessage.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
		self.animMessage.setDuration(100)
		self.animMessage.start()

		self.animMessage2 = QtCore.QPropertyAnimation(self.FromClient,b"pos")
		self.animMessage2.setEndValue(QtCore.QPoint(20,y-20))
		self.animMessage2.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
		self.animMessage2.setDuration(100)
		self.animMessage2.start()


class SystemMessage(QtWidgets.QLabel):
	def __init__(self,animBool,y,text,parent=None,x=690,width=151,height=31):
		super(SystemMessage,self).__init__()
		self.y = y
		self.x = x
		self.parent = parent
		self.width = width
		self.height = height
		self.text = text

		self.Message_5 = QtWidgets.QLabel(self.parent)
		self.Message_5.setGeometry(QtCore.QRect(self.x, self.y, self.width, self.height))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.Message_5.setFont(font)
		self.Message_5.setStyleSheet("border:none;\n"
"border-radius:10px;\n"
"background-color:transparent;\n"
"color: rgb(0, 0, 0);")
		self.Message_5.setAlignment(QtCore.Qt.AlignCenter)
		self.Message_5.setText(self.text)
		self.Message_5.show()

		if animBool == True:
			self.anim(y)
		else:
			self.Message_5.setGeometry(190,y,151,31)

	def anim(self,y):
		self.animMessage = QtCore.QPropertyAnimation(self.Message_5,b"pos")
		self.animMessage.setEndValue(QtCore.QPoint(190,y))
		self.animMessage.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
		self.animMessage.setDuration(100)
		self.animMessage.start()


class Client:
	def __init__(self,ip,port):
		self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.ip,self.port = ip,port



	def connect(self):
		self.socket.connect((self.ip,self.port))
		

	def sendMessage(self,message):
		self.socket.sendall(f"{message}".encode())

	def getServerMessage(self):
		try:
		
		
		    self.serverMessage = self.socket.recv(1024).decode()
		    return str(self.serverMessage)
		except:
			pass













class ChatRoom(QtWidgets.QMainWindow):
	messageFromClientSig = QtCore.pyqtSignal(bool,str,str)
	messageFromSystemSig = QtCore.pyqtSignal(bool,str)
	changeHeightMessageScroll = QtCore.pyqtSignal(int)
	messageFromMeSig = QtCore.pyqtSignal(str)
	changeNoOnline = QtCore.pyqtSignal(str)


	def __init__(self):
		super(ChatRoom,self).__init__()
		self.myname = ""
		self.client = Client(socket.gethostbyname(socket.gethostname()),8080)
		uic.loadUi("chat_room.ui",self)
		self.mainUi = [self.Title,self.messageScroll,self.messageText,self.sendButton]
		self.messageNo = 1
		self.loadMessages = []


		self.messageScrollHeight = 600
		
		self.regUi = RegisterUi(self)
		self.regUi.show()
		
		for i in self.mainUi:
			i.setVisible(False)
		self.setSize(391,211)
		self.pos_y = 20

		self.regUi.connectButton.clicked.connect(self.connect)
		self.sendButton.clicked.connect(self.sendMessage)

		self.messageFromSystemSig.connect(self.messageFromSystem)
		self.messageFromClientSig.connect(self.messageFromClient)
		self.messageFromMeSig.connect(self.__loadYourMessages__)
		self.changeHeightMessageScroll.connect(self.messageFrame.setMinimumHeight)



	def setSize(self,width,height):
		self.resize(width,height)
		self.setFixedSize(width,height)

	def connect(self):
		name = self.regUi.nameInput.text()
		self.myname = name
		if name == "":
			pass
		else:


		    try:
		        self.client.connect()
		        self.__joinMessage__(name)
		        self.regUi.loginFrame.setVisible(False)
		        self.setSize(577,648)   
		        threading.Thread(target=self.loopReceiveMessage,daemon=True).start()
		        for i in self.mainUi:
		    	    i.setVisible(True)
		    except ConnectionRefusedError:
		    	print("Can't Connect.")

		    
    
		    

	def sendMessage(self):
		if self.messageText.text() == "":
			pass
		else:
		    self.client.sendMessage(f"chat {self.messageText.text()}")
		    self.messageNo += 1
		    self.Message = MessageFrame(True,self.pos_y,self.messageText.text(),self.myname,self.messageFrame)
		    self.Message.setMinimumSize(QtCore.QSize(0, self.messageScrollHeight))
		    self.messageText.setText("")


	def __loadMessages__(self):
	    for i in self.loadMessages:
	    	if i.split()[0] == "chat":
	    		if i.split()[2] == self.myname:
	    			myMessage = i.split()
	    			text = ""
	    			for a in range(4):
	    				myMessage.pop(0)
	    			for b in myMessage:
	    				text += b+" "
	    			self.messageFromMeSig.emit(text)
	    			self.messageScrollHeight += 60

	    			self.changeHeightMessageScroll.emit(self.messageScrollHeight)
	    		else:
	    			message = i.split()
	    			text = ""
	    			for a in range(4):
	    				message.pop(0)
	    			for b in message:
	    				text += b+" "
	    			
	    			self.messageFromClientSig.emit(False,text,i.split()[2])
	    	
	    	if i.split()[0] == "join":
	    		if i.split()[1] == self.myname:
	    			self.messageFromSystemSig.emit(False,"You joined the chat.")
	    		else:
	    			self.messageFromSystemSig.emit(False,f"{i.split()[1]} joined the chat.")

	    	if i.split()[0] == "left":
	    		if i.split()[1] == self.myname:
	    			self.messageFromSystemSig.emit(False,"You left the chat.")
	    		else:
	    			self.messageFromSystemSig.emit(False,f"{i.split()[1]} left the chat.")

	
	def loopReceiveMessage(self):
		while True:


			try:
			    data = self.client.getServerMessage()
			    if data.split()[0] == "chat":
			    	if data.split()[2] == self.myname:
			    		self.pos_y += 60
			    		self.messageScrollHeight += 60
			    		self.changeHeightMessageScroll.emit(self.messageScrollHeight)
			    		message = data.split()
			    		text = ""
			    		for a in range(4):
			    			message.pop(0)
			    		for b in message:
			    			text += b+" "   

			    	else:
	    			    message = data.split()
	    			    text = ""
	    			    for a in range(4):
	    			    	message.pop(0)
	    			    for b in message:
	    			    	text += b+" "   
	    			    self.messageFromClientSig.emit(True,text,data.split()[2])

    
    
			    if data.split()[0] == "join":
			    	if data.split()[1] == self.myname:
			    		pass
			    	else:
			    		self.messageFromSystemSig.emit(True,f"{data.split()[1]} joined the chat.")
    
			    if data.split()[0] == "left":
			    	if data.split()[1] == self.myname:
			    		pass
			    	else:
			    		self.messageFromSystemSig.emit(True,f"{data.split()[1]} left the chat.")



			    if data.split()[0] == "loadMessage":
			    	listMessage = data.splitlines()[2].replace("[","").replace("]","").replace("'","")
			    	self.loadMessages =  listMessage.split(",")
			    	self.__loadMessages__()




	

			except Exception as e:
				pass
	





	def messageFromClient(self,animBool,text,sender):
		self.clientMessage = ClientMessage(animBool,self.pos_y,text,sender,self.messageFrame)
		self.pos_y += 60
		self.messageNo += 1
		self.messageScrollHeight += 60
		self.changeHeightMessageScroll.emit(self.messageScrollHeight)


	def messageFromSystem(self,animBool,text):
		self.SystemMessage = SystemMessage(animBool,self.pos_y,text,self.messageFrame)
		self.pos_y += 60
		self.messageNo += 1
		self.messageScrollHeight += 60
		self.changeHeightMessageScroll.emit(self.messageScrollHeight)


	def __loadYourMessages__(self,text):
		self.__MyMessage__ = MessageFrame(False,self.pos_y, text, self.myname, self.messageFrame)
		self.pos_y += 60
		self.messageScrollHeight += 60
		self.changeHeightMessageScroll.emit(self.messageScrollHeight)

	def __joinMessage__(self,name):
		self.client.sendMessage(f"nickname {name}")
		self.messageFromSystemSig.emit(True,"You joined the chat.")

	def __leftMessage__(self):
		self.client.sendMessage(f"quit")
		self.messageFromSystemSig.emit(True,"You left the chat.")

if __name__ == '__main__':
	app = QtWidgets.QApplication([])
	chatroom = ChatRoom()
	def quitting():
		try:
		    chatroom.__leftMessage__()
		except:
			pass

	chatroom.show()
	app.aboutToQuit.connect(quitting)
	app.exec()