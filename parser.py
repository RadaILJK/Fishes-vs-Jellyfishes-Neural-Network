from selenium import webdriver
import requests
from titles import *


browser = webdriver.Chrome('C:\\RADA\\chromedriver_win32\\chromedriver.exe')  
j = 943
for i in range(len(titles)):
    
    print(i, " ", urls[i], titles[i])
    browser.get("https://yandex.ru/images/search?from=tabbar&text=" + titles[i])

    data = browser.page_source
    
    try:
        # j = 0
        # получаем кусок кода, содержащий ссылку (но не только ее)
        data = data.split('img_href&quot;:&quot;')
        data.pop(0)
        data = data[:-1]
        
        for kartinka in data:
            #print (j)
            try:
                # оставляем только ссылку на изображение (очищаем блок кода от всего, кроме ссылки)
                kartinka = kartinka.split('&quot;')
                kartinka = kartinka[0]
                p = requests.get(kartinka)
                out = open("jellyfishes\\"+urls[i]+str(j)+".png", "wb")
                out.write(p.content)
                out.close()
            except:
                print ('картинка не скачалась')
            j += 1

    except Exception as e:
        # вывод информации об ошибке
        error = tr.TracebackException(exc_type =type(e),exc_traceback = e.__traceback__ , exc_value =e).stack[-1]
        print('{} in {} row:{} | arguments:{}'.format(e, error.lineno, error.line))             

    #input ('дальше?')
