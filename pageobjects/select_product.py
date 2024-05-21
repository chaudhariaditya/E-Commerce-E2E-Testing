from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time


class AddProduct:

    Text_Men_XP = (By.XPATH, "//span[@aria-label='MEN']")
    Text_Jens_Option_XP = (By.XPATH, "//a[normalize-space()='Jeans']")
    Text_Click_Jens_XP=(By.XPATH,"//*[@id='main-content']/div[1]/div/div[7]")
    Text_SizeMen_XP = (By.XPATH, "//span[normalize-space()='28']")
    Text_Add_ToBag_XP = (By.XPATH, "//div[@class='btn-gold']")
    Text_Home_XP =(By.XPATH,"//*[@id='appContainer']/div[2]/div/div/div/div[1]/ul/li[1]/a")
    Text_Women_XP=(By.XPATH,"//span[@aria-label='WOMEN']")
    Text_Kurta_Option_XP = (By.XPATH, "//div[@class='column column-2']//a[@title='Kurtas'][normalize-space()='Kurtas']")
    Text_Click_Kurta_XP= (By.XPATH,"//*[@id='main-content']/div[1]/div/div[11]")
    Text_SizeWomen_XP= (By.XPATH,"//span[normalize-space()='L']")




    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def Option_Men(self):
        action = ActionChains(self.driver)
        self.wait.until(expected_conditions.visibility_of_element_located(self.Text_Men_XP))
        action.move_to_element(self.driver.find_element(*AddProduct.Text_Men_XP)).move_to_element(self.driver.find_element(*AddProduct.Text_Jens_Option_XP)).click().perform()
    def Select_Jens(self):
        self.driver.find_element(*AddProduct.Text_Click_Jens_XP).click()
        open = self.driver.window_handles
        self.driver.switch_to.window(open[1])
        time.sleep(3)

        self.driver.find_element(*AddProduct.Text_SizeMen_XP).click()
        time.sleep(2)

        self.driver.find_element(*AddProduct.Text_Add_ToBag_XP)
        self.driver.close()
        self.driver.switch_to.window(open[0])
        time.sleep(3)

    def click_Home(self):
        self.driver.find_element(*AddProduct.Text_Home_XP).click()
        time.sleep(3)

    def Option_Women(self):
        action = ActionChains(self.driver)
        self.wait.until(expected_conditions.visibility_of_element_located(self.Text_Men_XP))
        action.move_to_element(self.driver.find_element(*AddProduct.Text_Women_XP)).move_to_element(self.driver.find_element(*AddProduct.Text_Kurta_Option_XP)).click().perform()

    def Select_Kurta(self):
        self.driver.find_element(*AddProduct.Text_Click_Kurta_XP).click()
        time.sleep(3)
        open = self.driver.window_handles
        self.driver.switch_to.window(open[1])
        time.sleep(3)

        self.driver.find_element(*AddProduct.Text_SizeWomen_XP).click()
        self.driver.find_element(*AddProduct.Text_Add_ToBag_XP)
        self.driver.close()
        self.driver.switch_to.window(open[0])
        time.sleep(3)

    def click_Home(self):
        self.driver.back()
        #self.driver.find_element(*AddProduct.Text_Home_XP).click()

