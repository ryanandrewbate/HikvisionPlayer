import os, sys, time, pygame
from dotenv import load_dotenv
from hikvisionapi import Client
import Channel, ScreenGrid


host = ""
client = None
screen = None
username = ""
password = ""
channels = []


def load_parameters():
	global cols, rows, host, username, password, channels

	load_dotenv()

	if os.getenv("protocol") != "":
		host = "http://" + os.getenv("remote_host")
	else:
		host = os.getenv("protocol") + "://" + os.getenv("remote_host")

	username = os.getenv("username")
	password = os.getenv("password")
	channels = os.getenv("channels").split(',')

	cols = 2
	rows = 2

def main():
	global client, host, username, password, channel
	
	load_parameters()
	try:
		client = Client(host,username,password)
	except:
		print("Could not connect to remote host.")
	grid = ScreenGrid.ScreenGrid(2,2)
	
	chans = []

	for counter,channel in enumerate(channels):
		chans.append(Channel.Channel(channel,counter,client,grid))
	

	while True:
		for chan in chans:
			chan.run()
			time.sleep(1)
		
		for event in pygame.event.get():
			if(event.type == pygame.KEYUP and event.key == pygame.K_c and event.mod & pygame.KMOD_CTRL):
				pygame.quit()
				sys.exit()


if __name__== "__main__":
  main()