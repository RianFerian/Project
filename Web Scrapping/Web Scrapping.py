import requests
import re
import time
from datetime import datetime

# Scraping Function
def Autoscraping():
    for i in range(repeat):
        page = requests.get(url)

        result = re.findall(r'{"viewCount":{"runs":\[{"text":(.*?)}', page.text)

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        with open('web_scraping_log.txt', 'a') as log_file:
            log_message = "\n" + str(current_time) + " " + str(result)
            log_file.write(log_message)

        print(current_time, " ", result)
        time.sleep(interval)


url = input('URL LINK?\n')
interval = input('Interval (Minute)?\n')
repeat = int(input('How many repeat?\n'))

try:
    interval = int(interval)*60-1
    Autoscraping()
except ValueError:
    print("Interval must in number")



# pyinstaller "D:\Users\rian.ferian\Desktop\Project\Web Scrapping\Web Scrapping.py" --onefile
