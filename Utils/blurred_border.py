from PIL import Image, ImageFilter


def blur_image_func(img):
    radius, diameter = 20, 40

    # # open an image
    # img = Image.open(r"C:\Users\Caio Madeira\Documents\GitHub\The-Philosopher-BOT\services\66239289547982040514235179432371843301.png")

    # Paste image on white background
    background_size = (img.size[0] + diameter, img.size[1] + diameter)
    background = Image.new('RGB', background_size, (14, 14, 14))
    background.paste(img, (radius, radius))

    # create new images with white and black
    mask_size = (img.size[0] + diameter, img.size[1] + diameter)
    mask = Image.new('L', mask_size, 255)

    black_size = (img.size[0] - diameter, img.size[1] - diameter)
    black = Image.new('L', black_size, 0)

    # create blur mask
    mask.paste(black, (diameter, diameter))

    # Blur image and paste blurred edge according to mask
    blur = background.filter(ImageFilter.GaussianBlur(radius / 2))
    background.paste(blur, mask=mask)
    background.save("test_image_blurred.jpg", quality=100)

    # show blurred edged image in preview
