from bs4 import BeautifulSoup
import urllib.request



url = "http://naver.com"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,"html.parser")
    # print(soup)
    # title = soup.title.name #title은 테그의 네임
    # print(title)
    # title1 = soup.title.string # title 진짜이름을 가지고 온다
    # print(title1)
    # title2 = soup.title.parent.name# title이 포함되어있는 부모 테그를 가지고 온다
    # print(title2)

    # print(soup.div)
    # print(soup.p)
    # print(soup.a)

def search():
    f = soup.find("div")#첫번째 div를 찾아서 출력
    print(f)
    f_all = soup.find_all("div") #리스트형태로 반환
    # for ff in f_all:
    #     print(ff)
    find_by_id = soup.find_all("div",{"id":"id1"})
    print(find_by_id)
    find_get = soup.find("a").get("href")#속성값만 축출하고 싶을때 사용
    find_get1 = soup.find("a").get_text()
    print(find_get1)
    site_names = soup.find_all("a")
    for name in site_names:
        print(name.get_text())



search()