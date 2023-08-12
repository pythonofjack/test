from bs4 import BeautifulSoup
import requests
import datetime


now = datetime.datetime.now()
now_date = now.date()

# header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}

# url1 = "https://timeline.google.com/maps/timeline?hl=ko&authuser=0&pli=1&rapt=AEjHL4NN5LbCMuiiEpU8o5qMlgg9G2QgVyhs1dA_5RCUwI_Flcju7sBI3fLnXLianBeW_0uOaATRcl9kChIg4ER1QgbL5TXNaw&pb=!1m2!1m1!1s"
# url2 = str(now_date)
# url = url1+url2
# req = urllib.request.Request(url,headers=header)
# html = urllib.request.urlopen(req).read()
# soup = BeautifulSoup(html,"html.parser")
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

# res = requests.get(url)
# res.raise_for_status()#프로그램에 문제발생시 종료
# soup = BeautifulSoup(res.text, "lxml")

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


# def time_line():
    # print(soup)
    # print(soup.title)
    # print(soup.title.get_text())
    # print(soup.div)
    # print(soup.div.attrs)
    # print(soup.a["href"])
    # print(soup.find(attrs={"class":"timeline-header-title-container"}))


def google_news():
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}

    url1 = "https://news.google.com/home?hl=ko&gl=KR&ceid=KR:ko"
    # url2 = str(now_date)
    # url = url1+url2
    res = requests.get(url1)
    res.raise_for_status()#프로그램에 문제발생시 종료
    soup = BeautifulSoup(res.text, "lxml")
    print(soup.get_text())
    print(soup.find("a")["href"])

# search()
# time_line()
google_news()