import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#TODO:
# -make bot detect poor urls

def validEnd(imageExt):
    img_type = ['jpg', 'jpeg', 'JPG', 'JPEG', 'png', 'PNG']
    for extension in img_type:
        if imageExt.endswith(extension):
            return True


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    try:
        img_url = message.attachments[0].url
        print(img_url)
        await message.channel.send(img_url)
    except IndexError:
        try:
            img_url = message.content
            if img_url.startswith("https://cdn.discordapp.com/attachments/") and validEnd(img_url):
                print(img_url)
                await message.channel.send(img_url)
            else:
                raise IndexError
        except IndexError:
            print("Image not detected")

client.run('NzM5MjI0NjA2NDQzMDQ0ODc4.XyXWkA.w6YH6c5M-FeaS82LGUfL_XBNDyQ')