from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--no-sandbox")


driver = webdriver.Chrome(options=chrome_options)
driver.get(url='https://www.google.com/')

#어떤 element를 찾을 수 있는지를 최대 5초 동안 매 0.5초마다 시도한다. 
# expected_conditions(EC)는 만약 element를 찾을 수 있었으면 True를, 아니라면 False를 반환한다.
try:
    element = WebDriverWait(driver, 100).until(
        # EC.presence_of_element_located((By.CLASS_NAME, 'gLFyf'))   
        EC.presence_of_element_located((By.CLASS_NAME, 'gb_Ad')) 
    )
    print(element)
finally:
    driver.quit()
