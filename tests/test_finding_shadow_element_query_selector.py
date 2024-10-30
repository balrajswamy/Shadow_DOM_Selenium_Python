# test_javascript_executor.py
import time
import pytest
import allure
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


logger = logging.getLogger()

@allure.feature("JavaScript Executor")
@allure.story("Execute JS actions in Selenium")
@pytest.mark.smoke
class TestJSExecutor:

    @allure.step("Scroll to the element username(enter name)")
    def test_scroll_to_find_element_shadow_dom_using_xpath(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        time.sleep(3)
        driver.get("https://selectorshub.com/xpath-practice-page/")

        time.sleep(10)
        # Find element to interact with using shadow DOM approach
        user_name_element = driver.find_element(By.XPATH, '//div[@id="userName"]')
        driver.execute_script("arguments[0].scrollIntoView(true);", user_name_element)

        driver.execute_script("arguments[0].style.border='1px solid green'", user_name_element)
        time.sleep(10)

        input_box_pizza = driver.execute_script("return document.querySelector('div#userName').shadowRoot.querySelector('#app2').shadowRoot.querySelector('#pizza');")

        time.sleep(6)
        input_box_pizza.send_keys("QuerySelector")




        time.sleep(3)
        driver.quit()


