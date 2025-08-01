from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # or provide full path to chromedriver
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_valid_login(driver):
    driver.get("https://example.com/login")  # Replace with real URL
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("password123")
    driver.find_element(By.ID, "login-btn").click()
    assert "dashboard" in driver.current_url

def test_invalid_login(driver):
    driver.get("https://example.com/login")
    driver.find_element(By.ID, "username").send_keys("wrong")
    driver.find_element(By.ID, "password").send_keys("wrongpass")
    driver.find_element(By.ID, "login-btn").click()
    error = driver.find_element(By.CLASS_NAME, "error").text
    assert error == "Invalid credentials"
