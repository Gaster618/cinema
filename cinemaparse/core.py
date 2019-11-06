'''for my homework'''
import requests as re
from bs4 import BeautifulSoup as bs

class CinemaParser:
    '''parser for subscity.ru'''
    def __init__(self, city='msk'):
        '''just init, nothign else'''
        self.city = city
        self.content = ''

    def extract_raw_content(self):
        '''download content from subscity.com'''
        link = 'https://' + self.city + '.subscity.ru'
        get_all_content = re.get(link)
        self.content = get_all_content.text

    def print_raw_content(self):
        '''print raw content from subscity.ru'''
        soup = bs(self.content, 'html.parser')
        print(soup.prettify())

MSK_PARSER = CinemaParser()
MSK_PARSER.extract_raw_content()
MSK_PARSER.print_raw_content()
