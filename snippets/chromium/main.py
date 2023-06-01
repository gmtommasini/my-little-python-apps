from  selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# folder where I downloaded the chrome driver
chrome_driver_path = 'E:\Documents\Estudo\prog\chromedriver_win32\chromedriver.exe'
serv = Service(chrome_driver_path)
driver = webdriver.Chrome(service=serv)
# web_site = "https://www.amazon.ca/dp/B00BD73Y52?tag=camelcamelcam-20&linkCode=ogi&th=1&language=en_CA"
# web_site = "https://www.python.org/"
web_site = "https://en.wikipedia.org/wiki/Main_Page"

driver.get(web_site)

# WIKI
art_count =  driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# print(art_count.get_attribute("innerHTML"))
print(art_count.text)


# PYTHON.ORG
# events_list = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li')
# events_list = driver.find_elements(By.XPATH, '//div[contains(@class, "event-widget")]/div/ul/li')
# events_list = driver.find_elements(By.CSS_SELECTOR, '.event-widget li')

# events ={}
# for i,tag in enumerate (events_list):
#   t = tag.find_element(By.XPATH, './time').text
#   a = tag.find_element(By.XPATH, './a').text
#   # print(t), print(a)
#   # event = { str(i):{
#   #     'time': t,
#   #     'name': a
#   #   }}
#   # events |= event
#   events[i]={
#             'time': t,
#             'name': a
#             }
# # print(events)



#  AMAZON - learning
# driver.get(web_site)
# price = driver.find_element(By.ID,"sns-base-price").get_attribute('innerText')
# print(price)

# search_bar = driver.find_element(By.NAME, "field-keywords")
# print(search_bar.get_attribute("placeholder"))

# sub_qnt= driver.find_element(By.XPATH,'//*[@id="rcxsubsQuan"]')
# print(sub_qnt.get_attribute("innerHTML"))


# driver.close()



driver.quit()
