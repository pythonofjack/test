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
# options.headless = True # 크롬을 뛰우지 않는다
# driver = ChromeDriverManager().install() #버전3용
# service = Service(ChromeDriverManager().install()) #버전4용
# driver = webdriver.Chrome(options=options)

now = datetime.datetime.now()
now_date = now.date()

def start(func):
    def wrapper(*args, **kwargs):
        url1 = "https://www.naver.com"
        # url2 = str(now_date)
        # url = url1+url2
        
        driver.get(url1)
        time.sleep(2)
        func(*args, **kwargs)
    return wrapper

@start
def screen_shot():
    driver.save_screenshot("naver.png")# 화면 스크린샷,저장
    driver.quit()#크롬전체닫기

@start
def newtab_click():
    # driver.find_element(By.LINK_TEXT,"블로그").click()
    driver.find_element(By.PARTIAL_LINK_TEXT,"블로").click() # 일부분만 일치하는 것들도 찾아준다
    # driver.find_element(By.LINK_TEXT,"블로그").send_keys(Keys.CONTROL+Keys.ENTER) # 위와동일
    driver.switch_to.window(driver.window_handles[-1])#마지막탭으로 이동
    time.sleep(1)
    # driver.close()#작업중인 탭닫기
    driver.switch_to.window(driver.window_handles[0])#메인창으로 이동

'''
<input id="query" name="query" type="search" title="검색어를 입력해 주세요.
" placeholder="검색어를 입력해 주세요." maxlength="255" autocomplete="off" 
class="search_input" data-atcmp-element="">
'''
@start
def naver_search():    
    
    # time.sleep(1)
    # driver.find_element(By.ID,"query").send_keys("파이썬")
    # time.sleep(1)
    # driver.find_element(By.CSS_SELECTOR,"#query").send_keys("아나콘다")# class는 .   id는 # 을 앞에 붙인다. 예)"#query",".search_input"    
    # driver.find_element(By.CSS_SELECTOR,"[title='검색어를 입력해 주세요.']").send_keys("판다스")
    # driver.find_element(By.CSS_SELECTOR,"[placeholder='검색어를 입력해 주세요.']").send_keys("판다스"+Keys.ENTER)
    
    # driver.back()
    # driver.forward()
    # driver.refresh()
    # driver.find_element(By.CLASS_NAME,"search_input").send_keys("정지권"+Keys.ENTER)
    # driver.forward()
    t_name = driver.find_elements(By.TAG_NAME,("div"))
    for t in t_name:
        print(t.get_attribute("class"))
    driver.get("http://daum.net")
    driver.find_element(By.CLASS_NAME,("tf_keyword")).send_keys("python"+Keys.ENTER)
    time.sleep(2)

    driver.quit()#크롬전체닫기

@start
def naver_login():
    
    log_in = driver.find_element(By.CLASS_NAME,("MyView-module__link_login___HpHMW"))
    log_in.click()
    driver.find_element(By.ID,("id")).send_keys("ozeek")
    time.sleep(1)
    driver.find_element(By.ID,("pw")).send_keys("wjdwlrnjs72++")
    time.sleep(1)
    driver.find_element(By.ID,("log.login")).click()
    time.sleep(1)
    # webdriver(driver,10).until(EC.presence_of_element_located((By.XPATH," ")))
    driver.quit()#크롬전체닫기




def google_movie():
    url = "https://play.google.com/store/movies?hl=ko&gl=HT"
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
              ,"Accept-Language":"ko-KR,ko"}
    bw = webdriver.Chrome(options=options)
    bw.get(url)
'''
단계별 스크롤내리기
bw.execute_script("window.scrollTo(0, 1080)")
끝까지 내리기
bw.execute_script("window.scrollTo(0, document.body.scrollHeight)")
반복적으로 스크롤내리기
prev_height = bw.execute_script("return document.body.scrollHeight")
while True:
    bw.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)
    current_height = bw.execute_script("return document.body.scrollHeight")
    if current_height == prev_height:
        break
    prev_height = current_height

        
'''

# screen_shot()
# newtab_click()
# naver_search()
# naver_login()
google_movie()