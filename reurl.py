import requests
from loguru import logger
logger.add("infcontent.log",format = "{time} {level} {message}", level = "DEBUG")
print("Здесь будут комманды")
inmenu = input("Введите: ")
if inmenu == "Инф":
    req = input("Enter URL: ")
    res = requests.get(req, verify = True)
    print(res)
    logger.debug("1")
    print(res.content)
    logger.debug("2")
    print(res.headers)
    logger.debug("3")
while inmenu == "Наз":
    inmenu1 = input("Введите: ")
    if inmenu1 == "Инф":
        req = input("Enter URL: ")
        res = requests.get(req)
        logger.debug("1")
        print(res)
        print(res.content)
        logger.debug("2")
        print(res.headers)
        logger.debug("3")
    if inmenu1 == "Вых":
        print("Вых")