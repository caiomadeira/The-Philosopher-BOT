# Imports All assets

# This class is like a tunnel for templates and streamming
from adapters.twitter_adapter import TwitterAdapter
from views.Templates.primary.primary_template import PrimaryTemplate


class Manager:
    def __init__(self, data):
        self.data = data
        DataOb = TwitterAdapter()
        get_status_information = DataOb.data_statusinfo_organized(data=data)
        self.extracted_hashtag = self.extract_hashtag_from_statusinfo_dict(statusinfo_dict=get_status_information)

    def which_hashtag(self):
        if 'testephilo' == self.extracted_hashtag:
            print("TestePhilo na hashtag - Iniciando PhiloBotEngine")
            Temp = PrimaryTemplate(data=self.data)
            Temp.default_template()

        elif 'testemaker' == self.extracted_hashtag:
            print("TesteMaker na hashtag - Iniciando PhiloMakerEngine")

    def extract_hashtag_from_statusinfo_dict(self, statusinfo_dict):
        for text in statusinfo_dict['Status Hashtag Typed']:
            return str(text['text'])

    def random_template(self):
        pass
