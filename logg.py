import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="my_log.log",
    format="%(ascTime)s - %(module)s - %(levelName)s - %(funcName)s - %(message)s",
    datefmt='%d-%m-%Y %H:%M:%S'
)
