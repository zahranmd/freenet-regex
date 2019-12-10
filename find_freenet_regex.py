import re
import freenet_regex
from bs4 import BeautifulSoup
from normalize import *



class freenet(object):

    def __init__(self, type):
        self.type = type

    # extract freenet addreses from text
    def extract_from_text(self, text):
        uri = []
        p = re.compile(self.get_regex())
        res = p.findall(str(text))

        if res==None:
            print("can't find any freenet address in this text")

        else:
            for u in res:
                uri.append(u[0])

        return uri

    # extract uris from href and check if it is freenet address or not
    def extract_from_html(self, html):
        uri = []

        soup = BeautifulSoup(html, 'lxml')
        tags = soup.find_all('a')
        
        for tag in tags:
            addr = tag.get('href')
            naddr = normal(addr)
            f = self.check(naddr)
            if f:
                uri.append(addr)
        return uri

    # check if a uri is freenet uri or not
    def check(self, uri):
        flag = False
        reg = self.get_regex()
        if re.match(reg, uri):
            flag = True
        return flag

    def get_regex(self):
        choices = {'ALL': freenet_regex.ALL, 'USK': freenet_regex.USK, 'SSK':freenet_regex.SSK, 'CHK':freenet_regex.CHK}

        result = choices.get(self.type, 'error')

        if(result=='error'):
            print("It's not a valid freenet type! please check README file for more information")
            exit()
        
        return result
