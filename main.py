import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#TODO:
# -make it work for all images and not just URL images

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    try:
        imgUrl = message.attachments[0].url
        print(imgUrl)
        await message.channel.send(imgUrl)
    except IndexError:
        print("Image not detected")

client.run('~~~')