
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as BS
import requests
import time


options = webdriver.ChromeOptions()

options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36")

url = "https://grasser.ru/auth/"


driver = webdriver.Chrome(executable_path="/home/compasspro1/Рабочий стол/python_work1/Parsing/crome/chromedriver", 
                          options=options)

url2 = "https://grasser.ru/vykrojki/besplatnye-vykrojki/"

req = requests.get(url2)

soup = BS(req.content, "lxml")

html = soup.select("div.catalog-three div.catalog__info a ")

driver.get(url=url)
email_input = driver.find_element(By.CSS_SELECTOR, "div.main__form-block input.text-16-19[name='USER_LOGIN']").send_keys("2fasa13@mail.ru")
time.sleep(0.2)
pass_input = driver.find_element(By.CSS_SELECTOR,"div.main__form-block input.text-16-19[name='USER_PASSWORD").send_keys("Dark34rus")
time.sleep(0.2)
login_button = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div[1]/form/button").click()

for elements in html:
    item_url = elements.get("href")
    url3 = f"https://grasser.ru{item_url}"
    driver.get(url=url3) 
    time.sleep(5)
    
    try:
        driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div/div/span[5]").click()
        time.sleep(0.2)
        driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[2]/div[1]/div[3]/div/div/span[3]").click()
        time.sleep(0.2)
        driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[2]/div[1]/div[5]/a[1]").click()
        time.sleep(60)
    
    except:
        driver.find_element(By.CSS_SELECTOR,"div.product__digits").click()
        time.sleep(0.2)
        driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[2]/div[1]/div[4]/a[1]").click()
        time.sleep(60)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# try:
    
#     driver.get(url=url)

#     print(f"url:{driver.current_url}")
    
#     time.sleep(1)
#     # """входн на сайт"""
    
#     email_input = driver.find_element(By.CSS_SELECTOR, "div.main__form-block input.text-16-19[name='USER_LOGIN']").send_keys("2fasa13@mail.ru")
#     time.sleep(0.2)
#     pass_input = driver.find_element(By.CSS_SELECTOR,"div.main__form-block input.text-16-19[name='USER_PASSWORD").send_keys("Dark34rus")
#     time.sleep(0.2)
#     login_button = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div[2]/div[1]/form/button").click()
#     time.sleep(0.2)
    
#     driver.get(url="https://grasser.ru/vykrojki/besplatnye-vykrojki/")
#     time.sleep(0.2)
    
   
        
    # for ur in url3:
    #     f = driver.find_element("ur").
    #     # driver.get(ur).click()
    #     time.sleep(0.2)
    
    # html = driver.select("div.catalog-three div.catalog__info a ")
    # for elements in html:
    #     item_url = elements.get("href")
    #     url = f"https://grasser.ru{item_url}"
    #     print(url)
    
    
    # items = driver.find_element(By.CSS_SELECTOR,"div.catalog-three")
    # items[1].click()
    # print(items, "**************************")
    # for i in items:
    #    print(i) 
   
    # click1 = driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div/div/span[4]").click()
    # time.sleep(1)
    # click2 = driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div/div/span[10]").click()
    # time.sleep(1)
    # click1 = driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[2]/div[1]/div[5]/a[1]").click()
    # print(f"url:{driver.current_url}")
    # time.sleep(2)
    
    
    # driver.close()
    
    # driver.switch_to.window(driver.window_handles)
    # print(f"url:{driver.current_url}")
    # time.sleep(1)
    
    # for click in site.range():
    
    
    
    #     # click = driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[2]/div[5]/div").click()
        
    #     time.sleep(5)
    # click_1 = driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/div/div").click()
    
    

    # pasword_input = driver.find_element_by_id("text-16-19 full-width input-gray-border main__form-input").send_keys(password)

    # driver.find_element_by_name("commit").click()

# except Exception as ex:
#     print(ex)
    
# finally:
#     driver.close()
#     driver.quit()    

























# username = "2fasa13@mail.ru"
# password = "Dark34rus"



# # перейти на страницу входа в github
# driver.get("https://grasser.ru/auth/")
# # найти поле имени пользователя / электронной почты и отправить само имя пользователя в поле ввода
# driver.find_element_by_id("text-16-19 full-width input-gray-border main__form-input").send_keys(username)
# # найти поле ввода пароля и также вставить пароль
# driver.find_element_by_id("text-16-19 full-width input-gray-border main__form-input").send_keys(password)
# # нажмите кнопку входа в систему
# driver.find_element_by_name("brown-button full-width").click()


# WebDriverWait(driver=driver, timeout=10).until(
#     lambda x: x.execute_script("return document.readyState === 'complete'")
# )
# error_message = "Incorrect username or password."
# # получаем ошибки (если есть)
# errors = driver.find_elements_by_class_name("flash-error")
# # при необходимости распечатать ошибки
# # для e в ошибках:
# #     print(e.text)
# # если мы находим это сообщение об ошибке в составе error, значит вход не выполнен
# if any(error_message in e.text for e in errors):
#     print("[!] Login failed")
# else:
#     print("[+] Login successful")