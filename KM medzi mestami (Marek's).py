import requests
import re


page = requests.get("http://www.kolko-km-je.ubytovaniesr.sk")
page.encoding = "windows-1250"
page_text = page.text
# print(page_text)
hrany = open("grafy/hrany.txt", 'r', encoding="UTF-8")
hrany = hrany.readlines()
mesta = [i.strip().split(';') for i in hrany]

matches = re.findall(r'<option value=.*?</option>', page_text)
values = {}
a = 0
for i in matches[1:3108]:
    temp = i[14:-9]
    temp = temp.split(' >')
    temp[0] = temp[0].strip("""'""")
    values[temp[1]] = temp[0]

new_hrany = open("grafy/hrany2", 'w', encoding="UTF-8")
numbers = '0123456789'
for i in mesta:
    obce1 = i[0]
    obce2 = i[1]
    data = {"obce1": values[obce1], "obce2": values[obce2]}
    website = requests.post("http://www.kolko-km-je.ubytovaniesr.sk", data=data)
    pattern = r'<h2>Odpov.*?</h2>'
    result = re.findall(pattern, website.text)
    result = result[0][13:]
    i = 0
    true_result = ''
    print(result)
    while result[i] in numbers:
        true_result += result[i]
        i += 1
    new_hrany.write(f"{obce1};{obce2};{true_result}\n")
print("FINISHED")