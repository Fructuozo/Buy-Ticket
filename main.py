from time import sleep
from login import login
from browser import open_browser
from buy import buyticket

def main_method():
    driver = open_browser()
    login(driver)
    buyticket(driver)
    input()

main_method()