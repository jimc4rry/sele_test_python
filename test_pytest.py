from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest




#@pytest.fixture()
def test_setup():
    global driver
    service = Service(executable_path="C:\\DRIVERS\\chromedriver_win32\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    #yield
    #driver.close()


def test_login():
    driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(3)
    usr = driver.find_element(By.NAME, "username")
    usr.send_keys("Admin")
    psw = driver.find_element(By.NAME, "password")
    psw.send_keys("admin123")
    time.sleep(0.5)
    driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
    time.sleep(4)

def test_title():
    act_title = driver.title
    exp_title = "OrangeHRM"
    if act_title == exp_title:
        print("Passed")
    else:
        print("Failed")

def test_expURL():
    exp_url = "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList"
    act_url = driver.current_url
    if act_url == exp_url:
        print("Passed")
    else:
        print("Failed")

def test_teardown():
    driver.close()
    driver.quit()

#pytest -v -s --html=report.html pytest_test.py

#git remote add origin https://github.com/jimc4rry/selenium_test.git
#git branch -M main
#git push -u origin main
