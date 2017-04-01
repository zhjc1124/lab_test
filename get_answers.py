import requests
from bs4 import BeautifulSoup
import re
import time
session = requests.Session()

base_url = 'http://202.198.17.5/'

answers = []


def get_tk(tikubh):
    tkurl = 'http://202.198.17.5/redir.php?catalog_id=6&cmd=learning&tikubh=' + tikubh
    while True:
        try:
            response = session.get(tkurl)
        except Exception:
            time.sleep(3)
            print('sleep')
            continue
        break
    soup = BeautifulSoup(response.content.decode('gbk'))
    pages = re.search(r'第 1/(\d*?) 页', soup.text).group(1)
    print(tikubh, 'ALL:', pages)
    for page in range(1, int(pages)+1):
        print(tikubh, page)
        while True:
            try:
                response = session.get(tkurl + '&page=' + str(page))
            except Exception:
                time.sleep(3)
                print('sleep')
                continue
            break

        soup = BeautifulSoup(response.content.decode('gbk'))
        shiti = soup.find('div', {'class': 'shiti-content'}).text.replace('    ', '').replace('\n\n', '').replace('\t', '')
        with open('shiti.txt', 'a+', encoding='utf8') as f:
            f.write(shiti)

        answers.append(shiti.split('\n')[:-1])
tikubhs = ['1436', '1467', '1471', '1484', '1485', '1486', '3800', '6206', '6207']

for tikubh in tikubhs:
    get_tk(tikubh)


with open('shiti.txt', encoding='utf8') as f:
    txt = f.read()
txt = txt.replace('\n）', '）').replace('：A', '：\nA').replace('：\nA）', '：A）').replace('？A', '？\nA')
pat = re.compile(r'）.*?、')
txt = pat.subn('）\n', txt)
pat = re.compile('\n\\d*?、')
txt = pat.subn('\n', txt[0])[0]
with open('answers.txt', 'w', encoding='utf8') as f:
    f.write(txt)
print(len(answers))