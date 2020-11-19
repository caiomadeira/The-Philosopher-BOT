import emoji, os
import base64
import io
from PIL import Image
from Hashtag.

def check_unicode(pegando_status2):
    global u
    global rem_ext
    local_path = r'C:\Users\caiom\Google Drive\Philosopher_BOT_PROJECT\TEST_VERSIONS\TEST-ENV\Emojis'

    unicode_images = []

    for u in pegando_status2:
        if u in emoji.UNICODE_EMOJI:

            for root, path, files in os.walk(local_path):
                for file in files:
                    rem_ext = file.replace('.png', '')
                    unicode_images.append(rem_ext)

        if any(str(u) in s for s in unicode_images):
            matching = [s for s in unicode_images if str(u) in s]
            print(matching)
            print('TEM SIM!')


def img_to_txt(filename):
    msg = b"<plain_txt_msg:img>"
    with open(filename, "rb") as imageFile:
        msg = msg + base64.b64encode(imageFile.read())
    msg = msg + b"<!plain_txt_msg>"
    return msg


def decode_img(msg):
    msg = msg[msg.find(b"<plain_txt_msg:img>") + len(b"<plain_txt_msg:img>"):
              msg.find(b"<!plain_txt_msg>")]
    msg = base64.b64decode(msg)
    buf = io.BytesIO(msg)
    img = Image.open(buf)
    return img


filename = '../Emojis/1f1e7.png'
msg = img_to_txt(filename)
img = decode_img(msg)
img.show()