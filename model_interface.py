# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 21:09:05 2020

@author: Jacob's PC
"""
import sample

from PIL import Image
import requests
from io import BytesIO

from build_vocab import Vocabulary


def get_extension(url: str) -> str:
    
    return url.split(".")[-1]

def get_caption(dis_url: str) -> str:
    
    extension = get_extension(dis_url)
    response = requests.get(dis_url)
    img = Image.open(BytesIO(response.content))
    
    img.save(f"./testImage.{extension}")

    return sample.main(f"./testImage.{extension}")

