
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as BS
import requests
import time


options = webdriver.ChromeOptions()

options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36")

driver = webdriver.Chrome(executable_path="/home/compasspro1/Рабочий стол/python_work1/Parsing/Выкройки Korfiati/crome/chromedriver", 
                          options=options)


url = "https://korfiati.ru/vyikroyki-odezhdyi/ready-made-patterns/"

req = requests.get(url)

soup = BS(req.content, "lxml")


"""Описание выкройки и ссылка на неё"""


args = []
html = soup.select("div.post-thumbnail")
сщгте = ()
for elements in html:
    driver.get(url = url)
    urls = elements.select_one("a")
    title = urls.get("title")
    item_url = urls.get("href")
    img = elements.select_one("img")
    img_item = img.get("src")
    for dec in soup.select("div.entry.excerpt p "):
        decs = dec.text
    args.append((title, decs, item_url, img_item ))
    print(item_url)
    time.sleep(5)
    driver.get(url = item_url)
    driver.find_element(By.XPATH, '//*[@id="plag-a-downloads-count"]').click()
    time.sleep(5)
    for i in range(10):
        driver.switch_to.window(driver.window_handles[i+1])
        driver.find_element(By.XPATH, '//*[@id="downloads-button-full"]').click()
        time.sleep(5)
    
              

  
        # //*[@id="page"]/div/div/div/section/div[2]/nav/div/a[3]
        # //*[@id="page"]/div/div/div/section/div[2]/nav/div/a[4]
   
        
    # /html/body/div[1]/div/div/div/div/section/div[2]/article/div/div[2]/div[1]/p[7]/a
    # driver.find_element(By.ID, 'downloads-button-full').click()
    # time.sleep(50)
    
    
    # div.pad.group p button sub
    
    
    
    
    
    
    
    # driver.find_element(By.CSS_SELECTOR , "div.wp-pagenavi .nextpostslink").click()
    # time.sleep(4)
    
    
# def pages (counter):
#     return "//div/a[counter]"
    

# def downladpage():
#     counter = [1, 2, 3, 4, 5, 6]
#     for count in counter: 
#         a = pages(count)
#         driver.click(a)

        
    


    
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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