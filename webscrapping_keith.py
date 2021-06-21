import requests, csv, re
from bs4 import BeautifulSoup
import pandas as pd

url = requests.get("https://keithgalli.github.io/web-scraping/webpage.html").text
soup = BeautifulSoup(url, 'lxml')
body = soup.body


"""scrapping all links of the website"""
for link in body.find_all('a'):
    href = [link['href']]
    print(href)
print('---------------------------------------')


"""scrapping table of the website, saving as csv file"""
table = body.select("table.hockey-stats")[0]

t_head = table.find('thead').find_all('th')
t_head = [head.text for head in t_head]

# csv_file = open('keith_webscraped.csv','w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(t_head)

t_body = table.find('tbody').find_all('tr')
l = []
for tr in t_body:
    all_td = tr.find_all('td')
    row = [td.text.strip() for td in all_td]
    # csv_writer.writerow(row)
    l.append(row)

# csv_file.close()

df = pd.DataFrame(l,columns=t_head)
print(df)
print('---------------------------------------')


"""scrapping 'fun-facts' line that contain word 'is' """
lists = body.find('ul', class_='fun-facts').find_all('li')
line = [line for line in lists]
line_with_is = [line_with_is.find(text=re.compile('is')) for line_with_is in line]
line_with_is = [line_with_is for line_with_is in line_with_is if line_with_is]
for final_line in line_with_is:
    print(final_line)
print('---------------------------------------')

"""scrapping images and saving it """
url = "https://keithgalli.github.io/web-scraping/"
pictures = body.find('div', class_='row').find_all('div', class_='column')
pic_list = []
for picture in pictures:
    pic_url = picture.find('img')['src']
    full_url = url+pic_url
    pic_list.append(full_url)
print(pic_list)
print('---------------------------------------')
# lake_pic = requests.get(pic_list[0]).content
# with open('lake.jpg','wb') as handler:
#     handler.write(lake_pic)


"""scrapping secret messages """
file_list = body.find_all('div', class_='block')
href_list = []
for fil in file_list:
    li = fil.find('ul').find_all('li')
    for href in li:
        hrefs = href.find('a')['href']
        href_list.append(hrefs)

url = "https://keithgalli.github.io/web-scraping/"
for href in href_list:
    full_url = url+href
    sm_page = requests.get(full_url).text
    soup = BeautifulSoup(sm_page, 'lxml')
    sm_body = soup.body
    secret_word = sm_body.find('p',id='secret-word')
    print(secret_word)