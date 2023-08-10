from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach",True)#브라우저 바로닫힘 방지

# chrome_driver = ChromeDriverManager().install() #버전3용
service = Service(ChromeDriverManager().install()) #버전4용

driver = webdriver.Chrome(service=service,options=options)

driver.get("http://naver.com")