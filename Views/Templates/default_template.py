from adapters.twitter_adapter import DataObtainer
from services.twitter_post import SendImage
from PIL import Image, ImageDraw, ImageFont
from views.Templates.random_philosopher import RandomPhilsopher

"""
1 - get data
2 - clean data
3 - do image

"""


class DefaultTemplate(DataObtainer):

    def __init__(self, data):
        # init information about status
        self.status_information = self.data_statusinfo_organized(data=data)
        self.user_information = self.data_userinfo_organized(data=data)
        self.status_situation = self.data_statussituation_organized(data=data)

        print("Default Template")
        print("Status situation: ", self.status_situation)
        print("Status Information: ", self.status_information)
        print("User information: ", self.user_information)

        # init template variables
        self.size_base = {"width": 1280, "height": 720}
        self.size_philosopher = {"x": 1280, "y": 0, "width": 800, "height": 720}
        self.color_base = (14, 14, 14)  # soft black

    # return informations
    def get_status(self):
        return self.status_information['Status Text']

    def get_status_id(self):
        return self.status_information['Status ID']

    def get_user_name(self):
        return self.user_information['User Name']

    # call all methods to all verification RT/quotes/empty string
    def do_data(self):
        pass

    def default_template(self):
        self.do_data()

        with Image.new('RGB', (self.size_base['width'], self.size_base['height']), self.color_base) as base:
            draw = ImageDraw.Draw(base)
            # philosopher img place
            draw.rectangle(xy=(self.size_philosopher["x"],
                               self.size_philosopher["y"],
                               self.size_philosopher["width"],
                               self.size_philosopher["height"]),
                           fill=(0, 192, 192))

            draw.rectangle(xy=(50, 100, 750, 600),
                           fill=(255, 192, 192))

            fnt_quote = ImageFont.truetype(r"C:\Users\caiom\Documents\GitHub\The-Philosopher-BOT\Font\myriad.otf", 40)

            fnt_author = ImageFont.truetype(r"C:\Users\caiom\Documents\GitHub\The-Philosopher-BOT\Font\times.ttf", 25)

            rand_philo = RandomPhilsopher().philosopher_image()
            philosopher_str_to_obj = Image.open(rand_philo)
            img_2 = philosopher_str_to_obj.resize((449, 584))
            base.paste(img_2, (629, 0))
            smooth_template = Image.open(r'C:\Users\caiom\Documents\GitHub\The-Philosopher-BOT\Assets\New_Img_Manipulation\layer_3.png')
            base.paste(smooth_template, (0, 0), smooth_template)

            # draw text, half opacity
            draw.text((200, 200), self.get_status(), font=fnt_quote, fill=(255, 255, 255, 128))
            # draw text, full opacity
            philo_name = RandomPhilsopher().philosopher_name(philosopher_img=rand_philo)
            draw.text((50, 650), philo_name, font=fnt_author, fill=(255, 255, 255, 255))

            base.save('finished2.png', quality=100)
            # base.show()
            SendImage().update(img_path='finished2.png',
                               status=self.get_status_id(),
                               post_username=self.get_user_name())
