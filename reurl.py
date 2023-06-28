import requests
from loguru import logger
logger.add("infcontent.log",format = "{time} {level} {message}", level = "DEBUG")
print("[1] Information \n [2] Back \n [3] Exit")
inmenu = input("Enter command: ")
if inmenu == "Information":
    req = input("Enter URL: ")
    res = requests.get(req, verify = True)
    print(res)
    logger.debug("1")
    print(res.content)
    logger.debug("2")
    print(res.headers)
    logger.debug("3")
while inmenu == "Back":
    inmenu1 = input("Введите: ")
    if inmenu1 == "Information":
        req = input("Enter URL: ")
        res = requests.get(req)
        logger.debug("1")
        print(res)
        print(res.content)
        logger.debug("2")
        print(res.headers)
        logger.debug("3")
if inmenu == "Exit":
        print("Exited")