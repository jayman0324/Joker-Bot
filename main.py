import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(name="Hi", type=0))
    print("Bot now connected!")
    print("------------------------------")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$ping'):
        await message.channel.send('pong!')

client.run('TOKEN')

##THIS IS REWRITE THOUGH
