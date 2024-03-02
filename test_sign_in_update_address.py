from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_update_address():
    username = 'example@gmail.com'  # here enter the exact id  by your own
    password = "password@123"    #enter the exact password by your own
    # this code is for the browser to be stay alive
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)

    # Maximizing the window
    driver.maximize_window()

    # Navigate to the webpage containing the hover element
    driver.get("https://www.amazon.in/gp/cart/view.html?ref_=nav_cart")

    # Hover over the element
    hover_element = driver.find_element(By.XPATH, "//span[@id='nav-link-accountList-nav-line-1']")
    action = ActionChains(driver)
    action.move_to_element(hover_element).perform()

    # Wait for the dropdown menu to appear (adjust timeout and condition as needed)
    wait = WebDriverWait(driver, 10)
    dropdown_menu = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='nav-action-inner']")))

    # Find and click on the desired button within the dropdown menu
    desired_button = dropdown_menu.find_element(By.XPATH, "//span[@class='nav-action-inner']")
    desired_button.click()

    # Entering to login page
    driver.find_element(By.XPATH, "//input[@id='ap_email']").send_keys(username)

    # clicking on continue
    driver.find_element(By.XPATH, "//input[@id='continue']").click()

    # enter password and continue
    driver.find_element(By.XPATH, "//input[@id='ap_password']").send_keys(password)
    driver.find_element(By.XPATH, "//input[@id='signInSubmit']").click()

    # navigating to the cart
    driver.get("https://www.amazon.in/ref=nav_logo")
    driver.find_element(By.XPATH, "//span[@id='nav-cart-count']").click()
    time.sleep(5)

    # clicking on proceed to checkout button
    driver.find_element(By.XPATH, "//input[@name='proceedToRetailCheckout']").click()
    time.sleep(5)

    # navigate to the address page
    driver.get("https://www.amazon.in/gp/buy/addressselect/handlers/display.html?_from=cheetah")
    driver.find_element(By.XPATH, "//a[@id='add-new-address-popover-link']").click()

    # Set the new address details
    new_address = {
        "name": "pappu kumar",
        "Mob_no": 1234567890,
        "address_line_1": "Apt 101",
        "city": "Gurgaon",
        "state": "Haryana",
        "Pin_code": "123005",
        "country": "India"
    }

    driver.find_element(By.XPATH, "//span[@id='address-ui-widgets-countryCode']//span[@role='button']").clear()
    driver.find_element(By.XPATH, "//span[@id='address-ui-widgets-countryCode']//span[@role='button']").send_keys(
        new_address["name"])

    driver.find_element(By.XPATH, "//input[@id='address-ui-widgets-enterAddressPhoneNumber']").clear()
    driver.find_element(By.XPATH, "//input[@id='address-ui-widgets-enterAddressPhoneNumber']").send_keys(
        new_address["Mob_no"])

    driver.find_element(By.XPATH, "//input[@id='address-ui-widgets-enterAddressLine1']").clear()
    driver.find_element(By.XPATH, "//input[@id='address-ui-widgets-enterAddressLine1']").send_keys(
        new_address["address_line_1"])

    driver.find_element(By.XPATH, "//input[@id='address-ui-widgets-enterAddressCity']").clear()
    driver.find_element(By.XPATH, "//input[@id='address-ui-widgets-enterAddressCity']").send_keys(new_address["city"])

    # Find the dropdown element by its ID, name, XPath, or other locators
    dropdown = Select(driver.find_element(By.ID, "dropdown_id"))
    ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
    dropdown.select_by_visible_text("HARYANA")

    driver.find_element(By.XPATH, "//input[@id='address-ui-widgets-enterAddressPostalCode']").clear()
    driver.find_element(By.XPATH, "//input[@id='address-ui-widgets-enterAddressPostalCode']").send_keys(
        new_address["Pin_code"])

    driver.find_element(By.ID, "address-ui-widgets-enterAddressCountryCode").clear()
    driver.find_element(By.ID, "address-ui-widgets-enterAddressCountryCode").send_keys(new_address["country"])

    # clicking on submit butttoon
    driver.find_element(By.XPATH, "//input[@aria-labelledby='address-ui-widgets-form-submit-button-announce']").click()

    print("Address changed successfully")
