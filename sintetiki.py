from bs4 import BeautifulSoup
import urllib.request
import time
global title_list
title_list = []
#Lib for html
def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

#Parse the shop
def parse(html):
    soup = BeautifulSoup(html, 'html.parser')

    table = soup.find_all('div', class_="container")
    for i in table:
        title = i.select('div.caption')
        for i in title:
            phones = i.select('a')
            for i in phones:
                #phones_ = i.get_text()
                #title_list.append(phones_)
                link = str(i.attrs['href'])
                parce_price(get_html(link))
                

    #Check the pagination 
    pages_ = soup.find('a',class_="nextpostslink")
    if pages_ is None:
        print('Готово, хозяин...', '\n')
        #No more pages for pagination'
        print("Список телефонов на сайте:", title_list)
        print("Число телефонов на сайте: ", len(title_list))
    pages = soup.find_all('a',class_="nextpostslink")
    for page in pages:
        next_page_link = (str(page.attrs['href']))
        print('Листаем страницы...')
        #Pagination to the next page: 
        print("->", next_page_link + '\n')
        time.sleep(3)
        parse(get_html(next_page_link))
        #print(next_page_link)


def parce_price(html):
    soup = BeautifulSoup(html, 'html.parser')
    prices = soup.select('div.blog-content')
    for i in prices:
        phone_name = (i.select('header.page-header'))
        for name in phone_name:
             name_tag = i.select('h1')
             for names in name_tag:
                 print(name.get_text())
        phone_price = i.find_all('a')
        for price in phone_price:
            print(price.get_text())
    
 
#The magic
def main():
    print("Делаем дела...")
    seller_link_list = ['http://sintetiki.net/analytics/']
    for seller_link in seller_link_list:
        parse(get_html(seller_link))


        
if __name__ == '__main__':
    main()
