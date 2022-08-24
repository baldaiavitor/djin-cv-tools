import numpy as np
from PIL import ImageFont, ImageDraw, Image
from enum import IntEnum
from djin_cv_tools.colors import BasicColors
from djin_cv_tools.colors import BGRA
import os

dirname = os.path.dirname(__file__)
fontpath = os.path.join(dirname, 'hgrpp1.ttc')


class OutputFormats(IntEnum):
    OpenCV=1
    JetsonInference=2
    NumpyArray=3

def putJapaneseText(img, text, position=(0,0), color=BasicColors.Black,fontSize=12,fontFile=fontpath, outputFormat=OutputFormats.NumpyArray):
    if outputFormat == OutputFormats.JetsonInference:
        raise Exception("Not Implemented")

    if outputFormat == OutputFormats.OpenCV:
        raise Exception("Not Implemented")

    font = ImageFont.truetype(fontpath, fontSize)
    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)
    draw.text(position, text, font = font , fill = BGRA(color) ) 

    return np.array(img_pil)