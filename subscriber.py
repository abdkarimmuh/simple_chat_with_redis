from config import red
import sys 

if __name__ == '__main__':

	channel = sys.argv[1]

	pubsub = red.pubsub()

	pubsub.subscribe(channel)

	print('listening to' + channel)

	while True:
		for item in pubsub.listen():
			print(item['data'])