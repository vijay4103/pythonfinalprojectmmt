import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from mainfolder.objects.BookingPage import BookingPage
from mainfolder.objects.LoginPage import LoginPage
from mainfolder.utilities.BaseClass import BaseClass
from selenium import webdriver
from mainfolder.utilities.DBConnectionFile import DBConnectionFile


@pytest.mark.usefixtures("setup")
class TestBooking(BaseClass):
    def test_booking(self):
        logs = self.get_logger()
        try:
            logs.debug('Browser launched')
            db = DBConnectionFile()
            data = db.dbconnect()
            logs.debug('Website Launched')
            time.sleep(12)
            frameList = self.driver.find_elements(by=By.TAG_NAME, value="iframe")
            self.driver.switch_to.frame(frameList[3])
            time.sleep(2)
            self.driver.execute_script("document.elementFromPoint(0,0).click()")
            time.sleep(5)
            # login = LoginPage(self.driver)
            # logs.debug('Phone Number Entered')
            # login.usernameInputOption().send_keys(data[2])
            # login.continueBtnOption().click()
            # otp = input()
            # logs.debug('OTP Entered')
            # login.otpInputOption().send_keys(otp)
            # login.loginBtnOption().click()
            self.driver.execute_script("document.elementFromPoint(0,0).click()")
            bookObj = BookingPage(self.driver)
            bookObj.fromButtonOption().click()
            bookObj.fromInputOption().send_keys(data[0])
            bookObj.fromCityOption().click()
            logs.debug('From city selected')
            bookObj.toButtonOption().click()
            bookObj.toInputOption().send_keys(data[1])
            bookObj.toCityOption().click()
            logs.debug('To city selected')
            bookObj.nextBtnOption().click()
            time.sleep(3)
            dates = bookObj.dateChoicesOption()
            for d in dates:
                e = d.find_element(By.TAG_NAME, value="p")
                if e.text == '15':
                    e.click()
                    break
            logs.debug('Date selected')
            bookObj.classTravelOption().click()
            bookObj.adultTktsOption().click()
            bookObj.childTktsOption().click()
            logs.debug('Passenger selected')
            bookObj.applyTktsOption().click()
            bookObj.searchFlightOption().click()
            bookObj.adPopupOption().click()
            self.takescreenshot(self.driver)
            logs.debug('Successful booking')
        except Exception as ex:
            logs.error("Exception occurred ", ex)
            self.takescreenshot(self.driver)
