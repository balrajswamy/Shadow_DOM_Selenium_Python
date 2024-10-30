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

        driver.execute_script("arguments[0].style.border='6px solid red'", user_name_element)
        time.sleep(10)


        #WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@id='userName']")))

        # Step 2: Access the shadow root of `#userName`
        user_name_shadow_root = driver.execute_script("return arguments[0].shadowRoot", user_name_element)

        time.sleep(1)
        # Step 3: Access the `#app2` element inside the first shadow root
        app2_element = user_name_shadow_root.find_element(By.CSS_SELECTOR, "#app2")
        time.sleep(1)
        # Step 4: Access the shadow root of `#app2`
        app2_shadow_root = driver.execute_script("return arguments[0].shadowRoot", app2_element)
        time.sleep(1)
        # Step 5: Access the `#pizza` input field within the nested shadow root
        pizza_input = app2_shadow_root.find_element(By.CSS_SELECTOR, "#pizza")
        time.sleep(1)
        # Interact with the input field
        pizza_input.send_keys("Farm house")




        time.sleep(10)
        driver.quit()


