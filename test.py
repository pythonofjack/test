from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach",True)#브라우저 바로닫힘 방지
options.add_experimental_option("excludeSwitches",["emable-logging"])#알림방지
options.add_argument("--start-maximized")#화면최대크기
options.add_argument("--disable-blink-features=AutomationControlled")#자동화아님으로 눈속임
# driver = ChromeDriverManager().install() #버전3용
service = Service(ChromeDriverManager().install()) #버전4용

driver = webdriver.Chrome(service=service,options=options)

driver.get("http://naver.com")

# driver.quit()#화면닫기