import discord
import PIL
from PIL import Image
import requests
from io import BytesIO
import cv2 as cv
import model_interface

from build_vocab import Vocabulary

import nest_asyncio
nest_asyncio.apply()

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#TODO:
# -video captioning function

#testing opencv
def captionVideo(frame_cycle = 240):
    video_stream = cv.VideoCapture('/Users/zachdoramebarajas/Downloads/test2.mov')
    while video_stream.isOpened():
        ret, frame = video_stream.read()
        for i in range(frame_cycle):
            if i == frame_cycle:
                ret, frame = video_stream.read()
                cv.imshow("screen", frame)
                cv.waitKey(1)
            else:
                cv.imshow("screen", frame)
                cv.waitKey(1)
                #this is extremely slow, in actuality we wouldn't display the frames, we'd only send them
                #to the hypothesis function



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    try:
        img_url = message.attachments[0].url
        caption = model_interface.get_caption(img_url)
        caption = "This picture is " + caption[8:-5]
        await message.channel.send(caption, tts=True)
    except (IndexError, TypeError):
        try:
            img_url = message.content

            #PIL image object created to catch illegitimate URLs
            resp = requests.get(img_url)
            img = PIL.Image.open(BytesIO(resp.content))

            caption = model_interface.get_caption(img_url)
            caption = "This picture is " + caption[8:-5]
            print(img_url)
            await message.channel.send(caption, tts=True)

            #not sure how many exceptions PIL can possibly throw, so we use a bare except
        except:
            print("Image not detected")

client.run('')