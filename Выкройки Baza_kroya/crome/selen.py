
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as BS
import requests
import time
import sqlite3
from pathlib import Path


options = webdriver.ChromeOptions()
download_path = r'/home/compasspro1/Рабочий стол/python_work1/Parsing/Выкройки Baza_kroya/download'
options.add_experimental_option('prefs', {
"download.default_directory": download_path,
"download.prompt_for_download": False, 
"download.directory_upgrade": True,
"plugins.always_open_pdf_externally": True 
})

options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36")

driver = webdriver.Chrome(executable_path="/home/compasspro1/Рабочий стол/python_work1/Parsing/Выкройки Baza_kroya/crome/chromedriver", 
                          options=options )

url = "https://baza-kroya.ru/page/44?brands=burda"

id = 0

args = []

list_prom = []
   
# for i in range(46):

#     if i == 0:
#         url = url
#     else:
#         url = f"https://baza-kroya.ru/page/{i+1}?brands=burda"    
          
req = requests.get(url)

soup = BS(req.content, "lxml")

"""Описание выкройки и ссылка на неё"""

html = soup.select("div.pattern-card")

for elements in html:
    id += 1
    urls = elements.select_one("a")
    item_url = urls.get("href")
    img = urls.select_one("img")
    img_item = img.get("data-src")
    name = img.get("alt")
    el_text = name.split("-", 2)
    dec = el_text[-1]
    name1 = el_text[0]
    driver.get(url=item_url)
    time.sleep(5)
    try:                                
        driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/section/div/div[2]/div[2]/ul[1]/li[1]/div/a").click()
        time.sleep(0.5)
        # driver.window_handles[1]
        # time.sleep(3)
        # driver.window_handles[0]
        # time.sleep(6)
        # driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/section/div/div[2]/div[2]/span").click()
        # time.sleep(0.2)
        # driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/section/div/div[2]/div[2]/ul[2]/li[1]/div/a").click()
        # time.sleep(3)
        
        if  id >= 1088:
            time.sleep(50)
        time.sleep(1)

    except:
        list_prom.append([id, name1, dec, item_url, img_item,False])  
        continue
        
    list_prom.append([id, name1, dec, item_url, img_item,True])  
    print(f"ELEMENT = {id}")
       
files = [str(f.absolute()) for f in Path("/home/compasspro1/Рабочий стол/python_work1/Parsing/Выкройки Baza_kroya/download").rglob("*")]
print(len(files))
delta = 1
for i in range(len(list_prom)):
    if list_prom[i][-1] == True: 
        index= list_prom[i][0]-delta
        args.append(tuple(list_prom[i][:-1] + [files[index]]))
    else: 
        args.append(tuple(list_prom[i][:-1] + ['нет данных']))
        delta += 1
print(list_prom)    
print(*args, sep='\n')       
# print(f"id = {id} file = {a} ")

        
    

"""Преренос информации в базу данных"""

con = sqlite3.connect("patterns.sqlite")

cursor = con.cursor() 

cursor.executemany("INSERT INTO patterns VALUES (?,?,?,?,?,?)", args )

con.commit()
con.close()
    

    
    

    
    
    
    
























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