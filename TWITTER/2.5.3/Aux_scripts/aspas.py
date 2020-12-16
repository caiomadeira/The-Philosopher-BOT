from PIL import Image, ImageFont, ImageDraw
import textwrap

img = Image.open('template.png')

fonte = ImageFont.truetype("../Font/myriad.otf", 30)

escrever = ImageDraw.Draw(img)
escrever.text(xy=(43, 110), text=textwrap.fill("AAAAA---343434AAAAAAAAAAA"), fill=(255, 255, 255), font=fonte)

# image_philo = Image.open("ada.png")
#  philo = 'ada.png'
#  img.paste(philo, (0, 0))
img.save('test_2.png')
img.show()
