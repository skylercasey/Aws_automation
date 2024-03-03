from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

def test_Add_to_cart():
    #this code is for the browser to be stay alive
    options=Options()
    options.add_experimental_option("detach",True)
    driver= webdriver.Chrome(options=options)

    #Maximizing the window
    driver.maximize_window()

    #getting the Amazon url and navigating to amazon
    driver.get("https://www.amazon.in/b/ref=surl_fashion/?_encoding=UTF8&node=6648217031&pd_rd_w=sC81d&content-id=amzn1.sym.fd3d60f7-29ad-49a0-9806-0537521c536e&pf_rd_p=fd3d60f7-29ad-49a0-9806-0537521c536e&pf_rd_r=XYDTAHJ1XQ9B9N3G9MAM&pd_rd_wg=SW9W5&pd_rd_r=a6216d69-4dc6-42bd-9aa9-872eb0380028")

    #going to search box and giving data
    search_box=driver.find_element(By.ID,"twotabsearchtextbox")
    search_box.send_keys("iPhone Xr")

    #submitting the form
    search_box.submit()
    time.sleep(4)  #giving some time to load page

    #selecting the product
    driver.find_element(By.XPATH,"//span[normalize-space()='Apple iPhone 13 (128GB) - Midnight']").click()
    time.sleep(4)

    #switching to the another tab as product page is opening in another url
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(4)

    #clicking to the Add to cart button
    driver.find_element(By.XPATH,"//div[@class='a-section a-spacing-none a-padding-none']//input[@id='add-to-cart-button']").click()
    time.sleep(5)

    # checkout button
    driver.get("https://www.amazon.in/gp/cart/view.html?ref_=nav_cart")
    print("Item added to the cart Successfully")
def test_delete_from_cart():
    # this code is for the browser to be stay alive
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)

    # Maximizing the window
    driver.maximize_window()

    # getting the Amazon url and navigating to amazon
    driver.get("https://www.amazon.in/b/ref=surl_fashion/?_encoding=UTF8&node=6648217031&pd_rd_w=sC81d&content-id=amzn1.sym.fd3d60f7-29ad-49a0-9806-0537521c536e&pf_rd_p=fd3d60f7-29ad-49a0-9806-0537521c536e&pf_rd_r=XYDTAHJ1XQ9B9N3G9MAM&pd_rd_wg=SW9W5&pd_rd_r=a6216d69-4dc6-42bd-9aa9-872eb0380028")

    # going to search box and giving data
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys("iPhone Xr")

    # submitting the form
    search_box.submit()
    time.sleep(4)  # giving some time to load page

    # selecting the product
    driver.find_element(By.XPATH, "//span[normalize-space()='Apple iPhone 13 (128GB) - Midnight']").click()
    time.sleep(4)

    # switching to the another tab as product page is opening in another url
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(4)

    # clicking to the Add to cart button
    driver.find_element(By.XPATH,"//div[@class='a-section a-spacing-none a-padding-none']//input[@id='add-to-cart-button']").click()
    time.sleep(5)

    # checkout button
    driver.get("https://www.amazon.in/gp/cart/view.html?ref_=nav_cart")
    # driver.find_element(By.XPATH,"//input[@name='proceedToRetailCheckout']").click()
    # time.sleep(3)

    # delete

    dropdown = driver.find_element(By.XPATH,"//span[@id='a-autoid-0-announce']")  # Replace "dropdown_id" with the ID of your dropdown
    dropdown.click()

    # Find the desired option within the dropdown and click on it
    option_to_select = driver.find_element(By.XPATH, "//a[@id='quantity_0']")  # Replace with your option text
    option_to_select.click()
    print("Item removed from the cart Successfully")


def test_update_address():
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)

    # Maximizing the window
    driver.maximize_window()

    # getting the Amazon url and navigating to amazon
    driver.get("https://www.amazon.in/b/ref=surl_fashion/?_encoding=UTF8&node=6648217031&pd_rd_w=sC81d&content-id=amzn1.sym.fd3d60f7-29ad-49a0-9806-0537521c536e&pf_rd_p=fd3d60f7-29ad-49a0-9806-0537521c536e&pf_rd_r=XYDTAHJ1XQ9B9N3G9MAM&pd_rd_wg=SW9W5&pd_rd_r=a6216d69-4dc6-42bd-9aa9-872eb0380028")

    # going to search box and giving data
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys("iPhone Xr")

    # submitting the form
    search_box.submit()
    time.sleep(4)  # giving some time to load page

    # selecting the product
    driver.find_element(By.XPATH, "//span[normalize-space()='Apple iPhone 13 (128GB) - Midnight']").click()
    time.sleep(4)

    # switching to the another tab as product page is opening in another url
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(4)

    # clicking to the Add to cart button
    driver.find_element(By.XPATH,
                        "//div[@class='a-section a-spacing-none a-padding-none']//input[@id='add-to-cart-button']").click()
    time.sleep(5)

    # checkout button
    driver.get("https://www.amazon.in/gp/cart/view.html?ref_=nav_cart")
    driver.find_element(By.XPATH,"//input[@name='proceedToRetailCheckout']").click()
    time.sleep(3)

    #login
    login_box=driver.find_element(By.XPATH,"//input[@id='ap_email']")
    login_box.send_keys("9113341622")
    login_box.submit()
    password_field=driver.find_element(By.XPATH,"//input[@id='ap_password']")
    password_field.send_keys("Mpesa@1396")
    password_field.submit()
    # navigate to the address page

    driver.find_element(By.XPATH, "//a[@id='add-new-address-popover-link']").click()

    # Set the new address details
    new_address = {
        "Full name (First and Last name)": "pappu kumar",
        "Mobile number": 9113341622,
        "Pincode": "122018",
        "Flat": "Apt 101",
        "Area":'Tikri',
        "Landmark":'Near GMD ground',
        "city": "Gurgaon",
        "state": "Haryana",
        "country": "India"
    }
    driver.find_element(By.XPATH,"//input[@id='address-ui-widgets-enterAddressFullName']").send_keys(new_address["Full name (First and Last name)"])
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id='address-ui-widgets-enterAddressPhoneNumber']").send_keys(new_address["Mobile number"])
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id='address-ui-widgets-enterAddressPostalCode']").send_keys(new_address["Pincode"])
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id='address-ui-widgets-enterAddressLine1']").send_keys(new_address["Flat"])
    time.sleep(2)
    driver.find_element(By.XPATH,"//input[@id='address-ui-widgets-enterAddressLine2']").send_keys(new_address["Area"])
    time.sleep(2)
    driver.find_element(By.XPATH,"//input[@id='address-ui-widgets-landmark']").send_keys(new_address["Landmark"])
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id='address-ui-widgets-enterAddressCity']").send_keys(new_address["city"])
    time.sleep(2)
    driver.find_element(By.XPATH,"//input[@aria-labelledby='address-ui-widgets-form-submit-button-announce']").click()
    print("Address changed successfully")

