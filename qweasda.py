import csv
import urllib.request
from bs4 import BeautifulSoup
import xlwt

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def parse(html):
    soup = BeautifulSoup(html, 'html.parser')

    colour_list = []
    colours = soup.find_all('ul','sku-attr-list util-clearfix')
    for i in colours:
        curent_colour = i.select('li.item-sku-image a')
        for j in curent_colour:
            colour_list.append(str(j.attrs['title']))
    #print(colour_list)

    set_list = []
    sets = soup.select('ul.sku-attr-list util-clearfix span')
    
    """
    for i in sets:
        curent_set = i.select('span')
        for j in curent_set:
            set_ = i.get_text()
        set_list.append(str(get_text()))
    print(set_list)
    """


    

"""
=>>
['Mi5 Prime  Gold 64G', 'Mi5 Gold  32G', 'Mi5 Pro Black 128G', 'Mi5 Prime White 64G', 'Mi5 Prime Black 64G', 'Mi5 White 32G', 'Mi5 Black 32G', 'Mi5 Pro White 128G']
['Gold', 'Silver White', 'Dark Grey']
Не должны отображатся но отображаются   
"""


"""
table = soup.find_all('ul', class_= 'items-list util-clearfix')
    for i in table:
        details = i.select('div.detail')
        for i in details:
            detail = i.select('a')
            for i in detail:
                link_list.append(str('http:'+i.attrs['href']))
                title_list.append(str(i.attrs['title']))

price_in_teg = soup.select('div.detail b')
    for i in price_in_teg:
        price = i.get_text()
        price_text = price.replace('\xa0', '') #почему выводит это \xa0?
        price_list.append(str(price_text))
    #print(price_list)
    #print(len(price_list))
"""
    

def main():
    link_list = ['http://ru.aliexpress.com/store/product/Original-xiaomi-Mi5-snapdragon-820-3GB-64GB-5-15-3000mAh-16ML-NFC-dual-sim-4K-video/1986585_32632847013.html',
                 'http://ru.aliexpress.com/store/product/Xiaomi-Redmi-note3-Pro-Prime-snapdragon-650-3G-32G-4000mAh-13ML-1080P-5-5-screen-octa/1986585_32636040211.html']
    for i in link_list:
        parse(get_html(i))

if __name__ == '__main__':
    main()
