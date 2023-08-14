from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime
import requests
from bs4 import BeautifulSoup


options = Options()
options.add_experimental_option("detach",True)#브라우저 바로닫힘 방지
options.add_experimental_option("excludeSwitches",["emable-logging"])#알림방지
options.add_argument("--start-maximized")#화면최대크기
options.add_argument("--disable-blink-features=AutomationControlled")#자동화아님으로 눈속임
options.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")



def url_finance():    
    url = "https://finance.naver.com/"
    return url

def login(url):
    bw = webdriver.Chrome(options=options)
    bw.get(url)
    # bw.find_element(By.XPATH,("//*[@id='gnb_login_button']/span[3]")).click()
    # bw.find_element(By.ID,("id")).send_keys("ozeek")
    # bw.find_element(By.ID,("pw")).send_keys("wjdwlrnjs72++")
    # bw.find_element(By.ID,("log.login")).click()

def break_news(url):
    bw = webdriver.Chrome(options=options)
    bw.get(url)
    bw.find_element(By.XPATH,('//*[@id="content"]/div[1]/div[1]/div[1]/div/a/em')).click()
    bw.find_element(By.XPATH,('//*[@id="newarea"]/div[1]/ul/li[3]/a/strong')).click()
    news = bw.find_elements(By.TAG_NAME,('a'))
    for n in news:
        print(n.get_attribute("title"))
        print(n.get_attribute("href"))





# login(url_finance())
break_news(url_finance())
