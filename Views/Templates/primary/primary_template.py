import os
from adapters.twitter_adapter import TwitterAdapter
from PIL import Image, ImageDraw, ImageFont
from views.Templates.manager.philosopher import RandomPhilosopher
from services.twitter_upload import TwitterUpload
from resources.fonts.path import path as font_path
from utils.string_utils.string_utils import StringUtils


class PrimaryTemplate(TwitterAdapter):

    def __init__(self, data):
        # init information about status
        self.status_information = self.data_statusinfo_organized(data=data)
        self.user_information = self.data_userinfo_organized(data=data)
        self.status_situation = self.data_statussituation_organized(data=data)

        # init variables
        self.quote_dicts = {"quote_20": {"xy": (250, 300), "wrap": 20, "color": (255, 255, 255, 128), "fontsize": 55},
                            "quote_20_80": {"xy": (75, 300), "wrap": 35, "color": (255, 255, 255, 128), "fontsize": 40},
                            "quote_80_120": {"xy": (100, 200), "wrap": 40, "color": (255, 255, 255, 128), "fontsize": 30},
                            "quote_120_280": {"xy": (100, 200), "wrap": 40, "color": (255, 255, 255, 128), "fontsize": 30}}

        self.size_base = {"width": 1280, "height": 720}
        self.size_philosopher = {"x": 1280, "y": 0, "width": 1280, "height": 720}
        self.color_base = (14, 14, 14)  # soft black

        # utils
        self.__str_util = StringUtils()

    # return informations
    def __get_status(self):
        return self.status_information['Status Text']

    def __get_status_id(self):
        return self.status_information['Status ID']

    def __get_user_name(self):
        return self.user_information['User Name']

    # call all methods to all verification RT/quotes/empty string
    def do_data(self):
        pass

    def default_template(self):
        self.do_data()

        with Image.new('RGB', (self.size_base['width'], self.size_base['height']), self.color_base) as base:
            draw = ImageDraw.Draw(base)
            # self.text_area(draw=draw)
            # fnt_quote = ImageFont.truetype(font_path + "/myriad.otf", 40)
            fnt_author = ImageFont.truetype(font_path + "/times.ttf", 25)

            # PHILOSOPHER IMAGE: select random frame
            philo = self.__philosopher_primary(base=base)

            # draw text, half opacity
            self.__quote(text=self.__get_status(),
                         draw=draw)
            # put markdown
            self.__markdown(base=base, path="../" + os.getenv('markdown'))
            # draw text, full opacity
            self.__author(color=(255, 255, 255, 255),
                          pos=(50, 650),
                          font=fnt_author,
                          draw=draw,
                          philo=philo)

            name = TwitterUpload().hashable_name() + ".png"
            base.save(name, quality=100)
            base.show()
            # self.__upload(idd=self.__get_status_id(), user=self.__get_user_name(), name=name)

    @staticmethod
    def __philosopher_primary(base):
        philo = RandomPhilosopher().philosopher_image()
        obj = Image.open(philo)
        resize = obj.resize((450, 690))
        base.paste(resize, (815, 15))
        return philo

    # @staticmethod
    # def __philosopher_secondary(base, draw):
    #     philo = RandomPhilsopher().philosopher_image()
    #     obj = Image.open(philo)
    #     resized = obj.resize((450, 690))
    #     draw.rectangle(xy=(1280, 0, 800, 720), fill=(250, 250, 250))
    #     base.paste(resized, (815, 15))
    #     return philo

    @staticmethod
    def __upload(idd, name, user):
        TwitterUpload().update(image=name, status=idd, user=user)

    def __quote(self, text, draw):
        self.__str_util.quote_util(text=text, draw=draw, font_path=font_path, quote_dict=self.quote_dicts,
                                   string_list=['#testephilo', '#TESTEphilo'], font="myriad.otf")
        return self.__str_util

    @staticmethod
    def __author(color, font, draw, pos, philo):
        author = RandomPhilosopher().philosopher_name(philosopher_img=philo)
        return draw.text(pos, author, font=font, fill=color)

    @staticmethod
    def __markdown(base, path):
        markdw = Image.open(path)
        base.paste(markdw, (550, 650), markdw)
