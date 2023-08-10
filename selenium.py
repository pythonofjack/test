from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_experimental_option("detach",True)#브라우저 바로닫힘 방지
options.add_experimental_option("excludeSwitches",["emable-logging"])#알림방지
options.add_argument("--start-maximized")#화면최대크기
options.add_argument("--disable-blink-features=AutomationControlled")#자동화아님으로 눈속임
# driver = ChromeDriverManager().install() #버전3용
# service = Service(ChromeDriverManager().install()) #버전4용
driver = webdriver.Chrome(options=options)

def start(func):
    def wrapper(*args, **kwargs):
        url = "http://naver.com"
        driver.get(url)
        time.sleep(1)
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
    # driver.find_element(By.CLASS_NAME,"search_input").send_keys("정지권")
    # time.sleep(1)
    # driver.find_element(By.ID,"query").send_keys("파이썬")
    # time.sleep(1)
    # driver.find_element(By.CSS_SELECTOR,"#query").send_keys("아나콘다")# class는 .   id는 # 을 앞에 붙인다. 예)"#query",".search_input"    
    # driver.find_element(By.CSS_SELECTOR,"[title='검색어를 입력해 주세요.']").send_keys("판다스")
    driver.find_element(By.CSS_SELECTOR,"[placeholder='검색어를 입력해 주세요.']").send_keys("판다스"+Keys.ENTER)

# screen_shot()
# newtab_click()
naver_search()