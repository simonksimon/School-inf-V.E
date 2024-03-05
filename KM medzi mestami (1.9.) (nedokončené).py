import requests
page=requests.get('http://kolko-km-je.ubytovaniesr.sk/')
page.encoding="windows-1250"
problem=page.text
print(problem)

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

f=open("hrany.txt","r")
file=f.readlines()
for i in range(len(file)):
    temp=file[i].split(";")
    temp[1]=temp[1][:-1]
    #print(temp)

#from bs4 import BeautifulSoup
#soup = BeautifulSoup(page.text, 'html.parser')
#form = soup.find('form')
#form.find('input', {'name': 'Z bodu'})['value'] = mesta[temp[0]]
#form.find('input', {'name': 'do bodu'})['value'] = mesta[temp[1]]
#response = requests.post('http://kolko-km-je.ubytovaniesr.sk/', data=form)
#response.encoding="windows-1250"
#solution=response.text
#result = soup.find('div', text='Odpoveď: ').find_next('div').text
#print(result)

#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#driver = webdriver.Edge()
#driver.get('http://kolko-km-je.ubytovaniesr.sk/')
#driver.find_element_by_name('Z bodu').send_keys('Bratislava')
#driver.find_element_by_name('do bodu').send_keys('Kosice')
#driver.find_element_by_name('ukáž výsledok').click()
#result = driver.find_element_by_xpath('//div[contains(text(), "Odpoveď: ")]').text
#print(result)
#driver.quit()

#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.by import By
#driver = webdriver.Edge()
#driver.get('http://kolko-km-je.ubytovaniesr.sk/')
#driver.find_element(By.XPATH, '//input[@name="Z bodu"]').send_keys('Bratislava')
#driver.find_element(By.XPATH, '//input[@name="do bodu"]').send_keys('Kosice')
#driver.find_element(By.XPATH, '//input[@value="ukáž výsledok"]').click()
#result = driver.find_element(By.XPATH, '//div[contains(text(), "Odpoveď: ")]').text
#print(result)
#driver.quit()
