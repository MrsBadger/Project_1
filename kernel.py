import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime

comfTrainsIndices = [] #Будем держать здесь индексы ласточек
def site(url):
    response = urllib.request.urlopen(url)
    return response.read()

#Вынимаем время отправки из расписания tutu.ru
def parse(html):
    parsedPage = BeautifulSoup(html, "html.parser")
    aTagData = parsedPage.find_all('a', class_='depTimeLink_1NA_N')
    departureTime = []

    for i in range(len(aTagData)):
         strTagData = str(aTagData[i])
         aTagParsed = BeautifulSoup(strTagData, "html.parser")
         tempTime = aTagParsed.get_text()
         departureTime.append(tempTime)
         departureTime[i] = datetime.strptime(tempTime, "%H:%M").time()

    return departureTime

def popSchedule():
    trainDepTimeList = [] #Лист, в который будем складывать время отправки электричек
    tempDepTimeList = parse(site('https://www.tutu.ru/spb/rasp.php?st1=2181&st2=181'))

    for i in range(len(tempDepTimeList)):
        if not datetime.now().time() > tempDepTimeList[i]:
            tempStr = str(tempDepTimeList[i])
            trainDepTimeList.append(tempStr)
    return trainDepTimeList

