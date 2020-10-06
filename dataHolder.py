import os
import discord
from dotenv import load_dotenv

class data():
    def __init__(self):

        #Loading token from outside of code using dotenv module
        load_dotenv()
        self.TOKEN = str(os.getenv('DISCORD_TOKEN'))
        self.ADMIN = int(os.getenv('DISCORD_ADMIN'))
        self.client = discord.Client()

        #Defining global variables
        self.guildSize = 0
        self.channelCount = {}
        self.channelCountName = []
        self.channels = {}
        self.guildNew = True


    def messageCheck(self):
        #If a channel is created, reset the server count variable to iterate through all channels again
        self.guildNew = True
        for guild in self.client.guilds:
            for channel in guild.text_channels:
                if channel.name not in list(self.channelCount.keys()):
                    self.guildNew = False
                    self.guildSize = 0
                    break
            if self.guildSize == 0:
                break
        
        #If bot is added to another server, completely recreates common channels list
        if self.guildSize != len(self.client.guilds):
            self.resetVars()
            self.defineVars()


    #Self explanatory, resetting variables
    def resetVars(self):
        self.guildSize = len(self.client.guilds)
        self.channels = {}
        self.channelCount = {}
        self.channelCountName = []


    #Self explanatory, defining variables
    def defineVars(self):
        if self.guildNew:
            print(f'\n{self.client.user} is connected to the following guilds:')
        else:
            print('New Channel created.')
        for guild in self.client.guilds:
            if self.guildNew:
                print(f'{guild.name} (id: {guild.id})')

            #Increase channel name count
            for channel in guild.text_channels:
                try:
                    self.channelCount[channel.name] += 1
                except:
                    self.channelCount[channel.name] = 1
        if self.guildNew:
            print('\n')

        #If there's more than 1 channel with the same name add their name to channels Dictionary
        for channel in self.channelCount:
            if self.channelCount[channel] > 1:
                self.channels[channel] = []
                self.channelCountName.append(channel)

        #Finding the IDs of the channels and listing them under their common channel name
        for guild in self.client.guilds:
            for channel in self.channels:
                for chan in guild.text_channels:
                    if chan.name == channel:
                        self.channels[channel].append(chan.id)


    #Create and run BOT
    def runBot(self):
        self.client.run(self.TOKEN)
