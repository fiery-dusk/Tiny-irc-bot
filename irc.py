import socket
import sys
from time import sleep

user='lurker'
channel='#'+raw_input('What channel do you want to use? ')
nick='el_fiery_dusko'

irc=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('connecting to server')

irc.connect(('irc.dongcorp.org', 6667))
irc.send('NICK '+nick+'\n')
irc.send('USER '+user+' '+user+' '+user+' :notevenalurkbot')
irc.send('JOIN '+channel+'\n')

try:
	while True:
		text=irc.recv(4096)
		print (text)
		if text.find(':lel') !=-1:
			x=1
			while x<=10:
				irc.send('PRIVMSG '+channel+' :lel \r\n')
				sleep(.1)
				x=x+1
		if text.find('PING') !=-1:
			irc.send('PONG %s\r\n' % text[1])
		
		if text.find('376') !=-1:
			irc.send('JOIN '+channel+'\n')
except(KeyboardInterrupt):
	irc.close()
	print('\n\nHave a nice day :)')
	sleep(1)

