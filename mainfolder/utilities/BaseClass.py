import logging
import pytest


@pytest.mark.usefixtures("setup")
class BaseClass:
    def get_logger(self):
        logs = logging.getLogger(__name__)
        fileHandler = logging.FileHandler('../../logs/logfile.log')
        format = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s: %(message)s")
        logs.setLevel(logging.DEBUG)
        fileHandler.setFormatter(format)
        logs.addHandler(fileHandler)
        return logs

    def takescreenshot(self, driver):
        driver.save_screenshot("..//..//screenshot//result.png")
