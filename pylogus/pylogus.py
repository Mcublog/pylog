import logging
from logging import Logger

from colorama import Fore as Clr

logging.addLevelName(logging.INFO, f"{Clr.GREEN}[{logging.getLevelName(logging.INFO)}]")
logging.addLevelName(logging.DEBUG,
                     f"{Clr.CYAN}[{logging.getLevelName(logging.DEBUG)}]")
logging.addLevelName(logging.WARNING,
                     f"{Clr.YELLOW}[{logging.getLevelName(logging.WARNING)}]")
logging.addLevelName(logging.ERROR, f"{Clr.RED}[{logging.getLevelName(logging.ERROR)}]")
LOG_FORMAT = '%(levelname)s%(asctime)s' + ': ' + '%(module)s: %(message)s' + f'{Clr.RESET}'


def logger_init(module_name: str, log_level: int) -> Logger:
    logging.basicConfig(format=LOG_FORMAT)
    log = logging.getLogger(module_name)
    log.setLevel(log_level)
    return log
