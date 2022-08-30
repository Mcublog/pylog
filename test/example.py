import logging

from pylogus import logger_init

log = logger_init(__name__, logging.DEBUG)

def example():
    log.info("This is a info msg")
    log.debug("This is a debug msg")
    log.warning("This is a warning msg")
    log.error("This is a error msg")

if __name__ == "__main__":
    example()
