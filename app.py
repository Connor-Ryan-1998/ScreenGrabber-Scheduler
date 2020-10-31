from selenium import webdriver
from time import sleep
import time
from datetime import datetime, date
import schedule

# Example https://finviz.com/screener.ashx?v=410&s=ta_topgainers
url = input('Enter a url: ')
scheduleTime = input('Supply the date 24 hour: ')
date = "screenshot_" + str(date.today()) + ".png"


def screengrab(url, date):
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get(str(url))
    sleep(1)
    driver.get_screenshot_as_file('./screengrabs/'+date)
    driver.quit()
    print("Completed " + str(date))


schedule.every().day.at(str(scheduleTime)).do(screengrab, url, date)
try:
    print("Press Ctrl-C to terminate while statement")
    while True:
        schedule.run_pending()
        time.sleep(60)  # wait one minute
except KeyboardInterrupt:
    print("Program Terminated")
    pass
