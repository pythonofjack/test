from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)



bw = webdriver.Chrome(options=chrome_options)

bw.get("http://naver.com")