from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from _ast import In

@given(u'Chrome browser is launched')
def step_launch_browser(context):
    opts=webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    opts.add_argument("start-maximized")
    context.driver=webdriver.Chrome(options=opts)
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    
@when(u'User navigates to OrangeHRM Login Page')
def step_navigate_to_orangehrm_login(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

@then(u'User should see page title as OrangeHRM')
def step_validate_navigation_to_orangehrm_login(context):
    expected_page_title="OrangeHRM"
    actual_page_title=context.driver.title
    assert expected_page_title == actual_page_title, "Title is not as expected"  

@when(u'User enter valid username, password and clicks on login button')
def step_enter_credentials(context):
    user_name=context.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input")
    user_name.send_keys('Admin')

    password_txt=context.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input")
    password_txt.send_keys('admin123')
    
    click_login=context.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")
    click_login.click()


@then(u'User should be on dashboard page')
def step_login_navigation_to_orangehrm_login(context):
    expected_url="dashboard/index"
    actual_url=context.driver.current_url
    assert expected_url in actual_url, "Login failed"
    
    
