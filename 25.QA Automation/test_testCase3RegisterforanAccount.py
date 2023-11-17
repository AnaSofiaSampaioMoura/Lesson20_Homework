# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTestCase3RegisterforanAccount():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testCase3RegisterforanAccount(self):
    self.driver.get("https://www.waterstones.com/")
    assert self.driver.title == "Buy books, stationery and gifts, online and in store | Waterstones"
    self.driver.find_element(By.CSS_SELECTOR, ".nav-account > .js-open-modal").click()
    self.driver.find_element(By.LINK_TEXT, "CREATE AN ACCOUNT").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".span6 > .heading-underline")
    assert len(elements) > 0
    self.driver.find_element(By.CSS_SELECTOR, ".button:nth-child(7)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".trigger").click()
    self.driver.find_element(By.CSS_SELECTOR, ".hover").click()
    self.driver.find_element(By.NAME, "user[firstname]").send_keys("Sofia")
    self.driver.find_element(By.NAME, "user[lastname]").send_keys("Moura")
    self.driver.find_element(By.NAME, "user[email]").send_keys("sofiamoura7@hotmail.com")
    self.driver.find_element(By.NAME, "user[confirmEmail]").send_keys("sofiamoura7@hotmail.com")
    self.driver.find_element(By.NAME, "user[password]").send_keys("lkKi72VzQOzDN@9")
    self.driver.find_element(By.NAME, "user[password_confirm]").send_keys("lkKi72VzQOzDN@9")
    self.driver.find_element(By.CSS_SELECTOR, ".reduced-margin > .ws-checkable-outer").click()
    self.driver.find_element(By.ID, "register").click()
  
