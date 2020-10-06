from dataHolder import data
Data = data()

@Data.client.event
async def on_ready():

    #When redefining variables they get set as local ones, so to make sure i specify as global
    global Data

    #Finding all common channels and storing their IDs in a list by name
    Data.guildSize = len(Data.client.guilds)
    Data.defineVars()
    

@Data.client.event
async def on_message(message):

    #When redefining variables they get set as local ones, so to make sure i specify as global
    global Data
    
    #Checking no outdated variables
    Data.messageCheck()

    #From here on ignore if message is sent by this BOT
    if message.author == Data.client.user:
        return

    #Making a way to disconnect/turn off the BOT via discord
    if message.author.id == Data.ADMIN and (message.content == 'Z!close' or message.content == 'Z!logout'):
        await Data.client.close()
        await Data.client.logout()

    #Create a help command to explain the BOT's purpose
    if message.content == 'Z!help':
        await message.channel.send('This bot currently connects all the common channels in every server it\'s in.')
    else:

        #The actual code for checking each message and their channel and sharing it to other channels with the same name
        for channel in Data.channels:
            if message.channel.id in Data.channels[channel]:
                for channelID in Data.channels[channel]:
                    if channelID != message.channel.id:
                        channelType = Data.client.get_channel(channelID)
                        await channelType.send(f'[{message.guild.name}] {message.author.display_name}: {message.content}')

#Run the bot
Data.runBot()
