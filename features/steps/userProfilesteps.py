
from behave import *
from selenium import webdriver
import time

@given('I launch browser')
def launchBrowser(context):

    context.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
    context.driver.implicitly_wait(10)
    context.driver.maximize_window()



@when('I open user login page')
def loginPage(context):
    context.driver.get("http://127.0.0.1:8000/")
    time.sleep(10)



@when('Enter username,password and click login button')
def userLogin(context):
    context.driver.find_element_by_css_selector("#id_username")
    context.driver.find_element_by_css_selector("#id_password")
    context.driver.find_element_by_css_selector("#login").click()
    time.sleep(10)


@then('Welcome page displayed with user profile Which shows Username,Name,Company_name and Role')
def welcomePage(context):
    context.driver.find_element_by_css_selector("#welcome")
    context.driver.close()
    context.driver.quit()



