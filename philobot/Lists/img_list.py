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

PHILOSOPHERS_LIST = []
PHILOSOPHERS_NAME = []

for filename in glob.glob(f'{IMG_PATH}/*.png'):
    PHILOSOPHERS_LIST.append(filename)
    PHILOSOPHERS_NAME.append(filename)






