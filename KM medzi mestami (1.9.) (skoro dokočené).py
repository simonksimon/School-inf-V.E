import requests
page=requests.get('http://kolko-km-je.ubytovaniesr.sk/')
page.encoding="windows-1250"
problem=page.text
#print(problem)

čísla="0123456789"
mesta={}
i=0
while i < len(problem):
    if problem[i:i+15]=="<option value='" and problem[i+16] in čísla:
        y=1
        while problem[i+14+y]!="'" and y<1000000:
            y+=1
        temp1 = problem[i + 15:i + 14 + y]
        #print(temp1)
        u=1
        while problem[i+17+y+u]!="<" and u<1000000:
            u+=1
        temp2 = problem[i+17+y:i+17+y+u]
        #print(temp2)
        mesta[temp2]=temp1
    i+=1
#print(mesta)

f=open("hrany.txt","r", encoding="utf-8")
file=f.readlines()
for i in range(len(file)):
    temp=file[i].split(";")
    temp[1]=temp[1][:-1]
    #print(temp)


#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import Select, WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#driver = webdriver.Edge()
#driver.get('http://kolko-km-je.ubytovaniesr.sk/')
#wait = WebDriverWait(driver, 10)
#suhlas_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="fc-consent-root"]//button[contains(text(), "Súhlas")]')))
#select_from = Select(driver.find_element(By.NAME, 'obce1'))
#select_to = Select(driver.find_element(By.NAME, 'obce2'))
#select_from.select_by_visible_text('Bratislava')
#select_to.select_by_visible_text('Košice')
#driver.find_element(By.XPATH, '//input[@value="ukáž výsledok"]').click()
#result = driver.find_element(By.XPATH, '//div[contains(text(), "Odpoveď: ")]').text
#print(result)