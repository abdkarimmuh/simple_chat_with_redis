from config import red

import sys

if __name__ == '__main__':

	name = sys.argv[1]
	channel = sys.argv[2]

print ('welcome to ' + channel)

while True:
	message = raw_input('enter a message ')

	message = name + ' says : ' + message

	red.publish(channel, message)
