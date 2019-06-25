import re

import requests
from bs4 import BeautifulSoup
from lxml import etree


def get_index(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("ok")
            return response.text
    except Exception as e:
        print(e)
    return


def parse_index(content):
    soup = BeautifulSoup(content,'lxml')

    # useful = soup.select('.ylist ylist--condensed li strong')[0].text
    # for i in useful:
    #    print(i)
    laji = soup.select('.ylist--condensed li')
    useful,funny,cool=0,0,0 #设置默认值，防止为空
    for i in laji:
        if "Useful" in i.get_text():
            useful = re.findall('\d+',i.get_text())[0]
            print("useful",useful)
        if "Funny" in i.get_text():
            funny = re.findall('\d+',i.get_text())[0]
            print("funny:",funny)
        if "Cool" in i.get_text():
            cool = re.findall('\d+',i.get_text())[0]
            print("cool",cool)

def main():
    url = 'https://www.yelp.com/user_details?userid=S6iRmxMYksS4vMbqwJfXsA'
    content = get_index(url)
    if content:
        parse_index(content)
    else:
        print('没有东西')


if __name__ == '__main__':
    main()
