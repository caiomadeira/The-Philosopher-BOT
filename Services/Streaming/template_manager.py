# Imports All Assets
from _Twitter.Templates import *

# This class is like a tunnel for templates and streamming
from Services.Streaming.DataObtainer.data_obtainer import DataObtainer
from Views.Templates.default_template import DefaultTemplate


class Template_Manager:
    def __init__(self, data):
        self.data = data
        DataOb = DataObtainer()
        get_status_information = DataOb.data_statusinfo_organized(data=data)
        self.extracted_hashtag = self.extract_hashtag_from_statusinfo_dict(statusinfo_dict=get_status_information)
        # print("\nget hastag =::::::::", get_status_information, "\n\n\n")

        # print("\nExtracted hashtag =::::::::", self.extracted_hashtag, "\n\n\n")

    def which_hashtag(self):
        if 'testephilo' == self.extracted_hashtag:
            print("TestePhilo na hashtag - Iniciando PhiloBotEngine")
            Temp = DefaultTemplate(data=self.data)
            Temp.default_template()

        elif 'testemaker' == self.extracted_hashtag:
            print("TesteMaker na hashtag - Iniciando PhiloMakerEngine")

    def extract_hashtag_from_statusinfo_dict(self, statusinfo_dict):
        for text in statusinfo_dict['Status Hashtag Typed']:
            return str(text['text'])

    def random_template(self):
        pass
