# CaptionBot

The goal of this Discord bot is to caption images posted by other users in a text channel and express the captions using the Text-To-Speech feature in Discord. The bot will utilize a pre-trained deep learning algorithm to make these captions.

## How To Use:
1. After cloning this repository and installing all dependencies, download the pre-trained encoder and decoder models from Yunjey Choi's tutorial (link in the resources section).
2. Place the .pkl files into a new directory labeled **/models**.
3. Add your Discord bot key to **main.py**, add your bot to your server. Run **main.py** and the bot will work once an image is posted.

## Notes of Interest:
- Currently, there is an issue where the program cannot open the .pkl files on Unix based OS's. Because of this fact, to our knowledge, this program can only be run on a  Windows computer.

## Resources:
- [Mohammad Shahebaz's Medium article about constructing an image captioning model.](https://medium.com/analytics-vidhya/introduction-to-image-caption-generation-using-the-avengers-infinity-war-characters-6f14df09dbe5)
- [Yunjey Choi's pyTorch tutorial series about Image Captioning (where **model.py**, **build_vocab.py**, and **sample.py** are adapted from.](https://github.com/yunjey/pytorch-tutorial/tree/master/tutorials/03-advanced/image_captioning)
  - The Pickled model files can also be found on the tutorial page's ReadMe.
