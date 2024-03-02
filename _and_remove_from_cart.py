from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.wait import WebDriverWait

def test_Add_to_cart_and_remove_from_cart():
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
    # driver.find_element(By.XPATH("(//input[@aria-labelledby='attach-sidesheet-checkout-button-announce'])[1]")).click()

    #navigating to the cart
    driver.get("https://www.amazon.in/ref=nav_logo")
    driver.find_element(By.XPATH,"//span[@id='nav-cart-count']").click()
    time.sleep(5)

    #deleting the item
    driver.find_element(By.NAME,"submit.delete.856d6574-42bc-4322-9cd8-55011a11b60").click()