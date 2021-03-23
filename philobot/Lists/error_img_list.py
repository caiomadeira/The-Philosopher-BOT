from Templates.Error_Philobot.reference import PHILOBOT_ERROR_IMG_PATH
from Templates.Error_Philomaker.reference import PHILOMAKER_ERROR_IMG_PATH
import glob


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

                  ERROR PHILOBOT 
                  
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

PHILOBOT_ERROR_IMAGE_COLLECTION = []

for filename in glob.glob(f'{PHILOBOT_ERROR_IMG_PATH}/*.png'):

    PHILOBOT_ERROR_IMAGE_COLLECTION.append(filename)

for filename in glob.glob(f'{PHILOBOT_ERROR_IMG_PATH}/*.gif'):

    PHILOBOT_ERROR_IMAGE_COLLECTION.append(filename)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

                  ERROR PHILOMAKER

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""

PHILOMAKER_ERROR_IMAGE_COLLECTION = []

# IMG
for filename in glob.glob(f'{PHILOMAKER_ERROR_IMG_PATH}/*.png'):
    PHILOMAKER_ERROR_IMAGE_COLLECTION.append(filename)

# USER
for filename in glob.glob(f'{PHILOMAKER_ERROR_IMG_PATH}/*.png'):
    PHILOMAKER_ERROR_IMAGE_COLLECTION.append(filename)
