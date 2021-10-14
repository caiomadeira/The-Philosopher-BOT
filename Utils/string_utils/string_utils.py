import textwrap
from PIL import ImageFont


class StringUtils:

    @staticmethod
    def count_letters(text):
        return len(text)

    @staticmethod
    def split_string(text):
        return list(text)

    @staticmethod
    def remove_string(text, string_list: list):
        for string in string_list:
            if string in text:
                return text.replace(string, '')

    def quote_util(self, text, draw, font_path, quote_dict: dict, string_list, font):
        formatted = self.remove_string(text=text, string_list=string_list)
        qtd_letters = self.count_letters(text=formatted)

        print("Qt chars in text:", qtd_letters)

        # bigger, centralized
        if qtd_letters <= 20:
            print("option 1 - Lower or Equal than 20")
            fnt = ImageFont.truetype(font_path + f"/{font}", quote_dict['quote_20']['fontsize'])
            return draw.text(xy=quote_dict['quote_20']['xy'],
                             text=textwrap.fill(str(formatted), quote_dict['quote_20']['wrap']),
                             fill=quote_dict['quote_20']['color'],
                             font=fnt)
            # bigger, centralized
        if 20 <= qtd_letters < 80:
            print("option 2 - Between 20 and 80")
            fnt = ImageFont.truetype(font_path + f"/{font}", quote_dict['quote_20_80']['fontsize'])
            return draw.text(xy=quote_dict['quote_20_80']['xy'],
                             text=textwrap.fill(str(formatted), quote_dict['quote_20_80']['wrap']),
                             fill=quote_dict['quote_20_80']['color'],
                             font=fnt)

            # small
        elif 80 <= qtd_letters < 120:
            print("option 3 - Between 80 and 120")
            fnt = ImageFont.truetype(font_path + "/myriad.otf", quote_dict['quote_80_120']['fontsize'])
            return draw.text(xy=quote_dict['quote_80_120']['xy'],
                             text=textwrap.fill(str(formatted), quote_dict['quote_80_120']['wrap']),
                             fill=quote_dict['quote_80_120']['color'],
                             font=fnt)
            # small, formatted
        elif 120 <= qtd_letters < 280:
            print("option 4 - Between 120 and 320")
            fnt = ImageFont.truetype(font_path + "/myriad.otf", quote_dict['quote_120_280']['fontsize'])
            return draw.text(xy=quote_dict['quote_120_280']['xy'],
                             text=textwrap.fill(str(formatted), quote_dict['quote_120_280']['wrap']),
                             fill=quote_dict['quote_120_280']['color'],
                             font=fnt)
