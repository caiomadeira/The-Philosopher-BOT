"""
Philosopher Bot
---------------
Created by Caio Madeira
Co-worker: Rodrigo Carmo

instagram: @sudomadeira
Twitter: @bot_philospher
Avaliable on Discord too!

"""
from Images.reference import IMG_PATH
from PIL import Image
import glob

path = IMG_PATH

PHILOSOPHERS_LIST = []

for filename in glob.glob(f'{IMG_PATH}/*.png'):
    im = Image.open(filename)
    PHILOSOPHERS_LIST.append(im)
