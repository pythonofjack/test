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


url = "https://timeline.google.com/maps/timeline?hl=ko&authuser=0&pli=1&rapt=AEjHL4NoDZCRdfZtNrrqCgKRLlmYtmRgFBKI8ko_9AATpFGkVQXV1CKDSPBFvmPkcZ2Gi3GMBSgEKTbIa6PFX0We4eVd8l4ISQ&pb"
bw = webdriver.Chrome(options=options)
bw.get(url)
bw.find_element(By.XPATH,("//*[@id='identifierId']")).send_keys("javaofjk")
bw.find_element(By.XPATH,("//*[@id='identifierNext']/div/button/span")).click()
WebDriverWait(bw,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='password']/div[1]/div/div[1]/div")))
bw.find_element(By.XPATH,("//*[@id='password']/div[1]/div/div[1]/div")).send_keys("ak382525")



