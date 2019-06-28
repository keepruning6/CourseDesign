
from socket import * 
from time import ctime 

HOST=''
PORT=8988
BUFSIZ=1024
ADDR=(HOST,PORT)

def timesoc():
	tcpSerSock =socket(AF_INET,SOCK_STREAM)
	tcpSerSock.bind(ADDR)
	tcpSerSock.listen(5)

	while True:
		print 'waiting for connection'
		tcpCliSock, addr =tcpSerSock.accept()
		print '...connention from:',addr
		while True:
			data =tcpCliSock.recv(BUFSIZ)
			if not data:
				break
			tcpCliSock.send('[%s] %s' %(ctime(),data))
			print data
		tcpCliSock.close()
	tcpSerSock.close()

if __name__=='__main__':
	timesoc()