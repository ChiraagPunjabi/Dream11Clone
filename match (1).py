from bs4 import BeautifulSoup as soup
from urllib.request import urlopen, Request
from datetime import date


my_url = 'https://www.espncricinfo.com/live-cricket-match-schedule-fixtures'

req = Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

'''uClient = urlopen(my_url)
page_html = uClient.read()
uClient.close()
print(page_html)'''
page_soup = soup(webpage, "html.parser")
#print(page_soup)


containers = page_soup.find_all("div", attrs={"class": "description"})


hindi=page_soup.find_all("div", {"class": "status status-hindi"})
dates = (len(hindi))

#print(containers[6].get_text())
leng=(len(containers))
for i in range(leng):
    if i%2 != 0:
        containers[i] = '*'
    '''temp = containers[i].get_text()
    temp1 = temp.split(",")[0]
    print(temp1.replace("Check ",""))'''
for i in range (dates):
    containers.remove("*")
'''for i in range(dates):
    temp = containers[i].get_text()
    temp1 = temp.split(",")[0]
    print(temp1.replace("Check ",""))'''

    

for i in range(0,dates):
    day=hindi[i].get_text()
    if "today" in day or "tomorrow" in day:
        
        temp = containers[i].get_text()
        temp1 = temp.split(",")[0]
        temp2 =temp1.replace("Check ","")
        print(temp2)
       # if "Sweden Wmn" in temp2 or "New Zealand" in temp2 or "West Indies" in temp2 or "South Africa" in temp2:
            
               
        if "Sri Lanka" in temp2 or "New Zealand" in temp2 or "West Indies" in temp2 or "South Africa" in temp2 or "India" in temp2 or "Ireland" in temp2 or "UAE" in temp2 or "Afghanistan" in temp2 or "Zimbabwe" in temp2 or "Pakistan" in temp2 or "England" in temp2 or "Bangladesh" in temp2 or "Australia" in temp2:
            temp2 = temp2.replace("Sri Lanka","SriLanka")
            temp2 = temp2.replace("New Zealand","NewZealand")
            temp2 = temp2.replace("West Indies","WestIndies")
            temp2 = temp2.replace("South Africa","SouthAfrica")
            a = temp2.split(" ")[0]
            b = temp2.split(" ")[1]
            c = temp2.split(" ")[2]
            final = a+' '+b+' '+c
            print(final)   
            print(day)
