import time
from lib2to3.pgen2 import driver
from pageobjects.select_product import AddProduct
from selenium import webdriver
from utilities.Logger import LogGenerator


class Test_Product:
    log = LogGenerator.logen()
    def test_title01(self, setup):
        self.log.info("TestCase test_titel01 Started ")
        self.driver = setup

        if self.driver.title == "Online Shopping for Women, Men, Kids – Clothing, Footwear | AJIO":
            time.sleep(3)
            self.driver.save_screenshot("D:\\Ajio\\Screenshots\\test_titel01pass.png")
            assert True
            self.log.info("TestCase test_titel01 Pass ")
        else:
            time.sleep(3)
            self.driver.save_screenshot("D:\\Ajio\\Screenshots\\test_titel01fail.png")
            self.log.info("TestCase test_titel01 fail ")
            assert False

    def test_addproduct(self, setup):
        self.driver = setup
        self.search = AddProduct(self.driver)
        self.search.Option_Men()
        self.log.info("Men option clicked")
        self.search.Select_Jens()
        time.sleep(3)
        self.log.info("option selected")
        self.search.click_Home()
        self.log.info("Home page ")
        self.search.Option_Women()
        self.log.info("Women Option Clicked")
        self.search.Select_Kurta()
        self.search.click_Home()
        time.sleep(3)






