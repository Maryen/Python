import csv
import urllib.request
from bs4 import BeautifulSoup
import xlwt


def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()


def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    
  
    link_list = []
    title_list = []
    price_list = []

    table = soup.find_all('ul', class_= 'items-list util-clearfix')
    for i in table:
        details = i.select('div.detail')
        for i in details:
            detail = i.select('a')
            for i in detail:
                link_list.append(str('http:'+i.attrs['href']))
                title_list.append(str(i.attrs['title']))

    """
    нумерованый список названий товаров
    
    c = 1
    for i in title_list:
         print(str(c)+ ' ' + title_list[c] + '\n')
         c +=1
    """

    price_in_teg = soup.select('div.detail b')
    for i in price_in_teg:
        price = i.get_text()
        price_text = price.replace('\xa0', '') #почему выводит это \xa0?
        price_list.append(str(price_text))
    #print(price_list)
    #print(len(price_list))

    #Вывод всех данных по товарам:
    
    for i in range(len(price_list)):
        print(str(i) + ' {} \n {} \n {} \n'.format(link_list[i],title_list[i],price_list[i]))
    
    print('len link_list', len(link_list))
    print('len title_list', len(title_list))
    print('len price_list', len(price_list))

    #return link_list,title_list,price_list
    
#def save(*args,**kwargs):
    book = xlwt.Workbook('utf8')
    font = xlwt.easyxf('font: height 240,name Arial,colour_index black, bold off,\
    italic off; align: wrap on, vert top, horiz left;\
    pattern: pattern solid, fore_colour white;')
    sheet = book.add_sheet('sheetname')
    l = 0
    for i in link_list:
        sheet.write(l,0,str(i),font)
        l += 1

    d = 0
    for i in title_list:
        sheet.write(d,1,str(i),font)
        d += 1

    p = 0
    for i in price_list:
        sheet.write(p,2,str(i),font)
        p += 1

    sheet.row(0).height = 2000
    sheet.col(0).width = 15000
    sheet.row(1).height = 2000
    sheet.col(1).width = 20000
    sheet.row(1).height = 2500
    sheet.col(2).width = 7000
    sheet.portrait = False
    sheet.set_print_scaling(85)
    book.save('dreami.xls')


#save(link_list,title_list,price_list)

def main():
    parse(get_html('http://ru.aliexpress.com/store/group/Phones/1986585_506350288.html'))



if __name__ == '__main__':
    main()