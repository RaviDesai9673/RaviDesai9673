'''
This is an automation code of a customer registering an account, selecting and comparing products
and finally purchasing them using his credit card and lastly logging out of an demo E-commerce website: nopcommerce
Kindly specify your chrome webdriver location details in the Service class to run the code(line 14)
'''
# import functions
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Launching the webdriver and
obj = Service()
# ops = webdriver.ChromeOptions()
# ops.headless = True
driver = webdriver.Chrome(service=obj)  # , options=ops)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
driver.implicitly_wait(10)

# Registering an account
driver.find_element(By.XPATH, "//a[@class='ico-register']").click()
driver.find_element(By.ID, "gender-male").click()
time.sleep(2)
driver.find_element(By.NAME, "FirstName").send_keys("Steven")
driver.find_element(By.XPATH, "//input[@id='LastName']").send_keys("Mathew")
(d, m, y) = (20, 2, 2000)
day = Select(driver.find_element(By.XPATH,
                                 "/html/body/div[6]/div[3]/div/div/div/div[2]/form/div[1]/div[2]/div[4]/div/select[1]"))
day.select_by_visible_text('23')
month = Select(driver.find_element(By.XPATH,
                                   "/html/body/div[6]/div[3]/div/div/div/div[2]/form/div[1]/div[2]/div[4]/div/select[2]"))
month.select_by_visible_text('February')
year = Select(driver.find_element(By.XPATH,
                                  "/html/body/div[6]/div[3]/div/div/div/div[2]/form/div[1]/div[2]/div[4]/div/select[3]"))
year.select_by_visible_text('1998')
time.sleep(5)
driver.find_element(By.XPATH, "//input[@id='Email']").send_keys("StevenMathew@gmail.com")
driver.find_element(By.XPATH, "//input[@id='Company']").send_keys("XYZ")
driver.find_element(By.XPATH, "//input[@id='Newsletter']").submit()

driver.find_element(By.XPATH, "//input[@id='Password']").send_keys("ste123")
driver.find_element(By.XPATH, "//input[@id='ConfirmPassword']").send_keys("ste123")
time.sleep(2)
driver.find_element(By.XPATH, "//button[@id='register-button']").click()

# Comparing and selecting one phone
driver.find_element(By.XPATH, "//ul[@class='top-menu notmobile']//a[normalize-space()='Electronics']").click()
driver.find_element(By.XPATH, "//li[@class='inactive']//a[normalize-space()='Cell phones']").click()
driver.find_element(By.XPATH,
                    "//h2[@class='product-title']//a[contains(text(),'HTC One M8 Android L 5.0 Lollipop')]").click()
driver.find_element(By.XPATH,
                    "//div[@class='compare-products']//button[@type='button'][normalize-space()='Add to compare list']").click()
time.sleep(2)
driver.back()
driver.find_element(By.XPATH, "//h2[@class='product-title']//a[contains(text(),'Nokia Lumia 1020')]").click()
driver.find_element(By.XPATH,
                    "//div[@class='compare-products']//button[@type='button'][normalize-space()='Add to compare list']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[normalize-space()='Compare products list']").click()
driver.find_element(By.XPATH,
                    "//tr[@class='product-name']//a[contains(text(),'HTC One M8 Android L 5.0 Lollipop')]").click()

# Selecting the quantity and adding to cart
quantity = driver.find_element(By.XPATH, "//input[@id='product_enteredQuantity_18']")
quantity.clear()
quantity.send_keys(2)
time.sleep(2)
driver.find_element(By.XPATH, "//button[@id='add-to-cart-button-18']").click()
driver.find_element(By.XPATH, "//span[@class='cart-label']").click()

# adding gift wrap and proceeding to checkout
wrap = Select(driver.find_element(By.XPATH, "//select[@id='checkout_attribute_1']"))
wrap.select_by_visible_text("Yes [+$10.00]")
driver.find_element(By.XPATH, "//input[@id='termsofservice']").click()
driver.find_element(By.XPATH, "//button[@id='checkout']").click()

# Billing address
country = Select(driver.find_element(By.XPATH, "//select[@id='BillingNewAddress_CountryId']"))
country.select_by_visible_text("India")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='BillingNewAddress_City']").send_keys("Pune")
driver.find_element(By.XPATH, "//input[@id='BillingNewAddress_Address1']").send_keys("47th Cross 3rd Main")
driver.find_element(By.XPATH, "//input[@id='BillingNewAddress_ZipPostalCode']").send_keys('818001')
driver.find_element(By.XPATH, "//input[@id='BillingNewAddress_PhoneNumber']").send_keys("123456789")
driver.find_element(By.XPATH, "//button[@onclick='Billing.save()']").click()

# Shipping method
driver.find_element(By.XPATH, "//button[@class='button-1 shipping-method-next-step-button']").click()

# payment method

driver.find_element(By.XPATH,"//input[@id='paymentmethod_1']").click()
driver.find_element(By.XPATH, "//button[@class='button-1 payment-method-next-step-button']").click()

# payment info
card = Select(driver.find_element(By.XPATH, "//select[@id='CreditCardType']"))
card.select_by_visible_text("Discover")
driver.find_element(By.XPATH, "//input[@id='CardholderName']").send_keys("John Jacobs")
driver.find_element(By.XPATH, "//input[@id='CardNumber']").send_keys("6011984972794241")
date = Select(driver.find_element(By.XPATH, "//select[@id='ExpireMonth']"))
date.select_by_visible_text("07")
yea = Select(driver.find_element(By.XPATH, "//select[@id='ExpireYear']"))
yea.select_by_visible_text("2026")
driver.find_element(By.XPATH, "//input[@id='CardCode']").send_keys("284")
driver.find_element(By.XPATH, "//button[@class='button-1 payment-info-next-step-button']").click()

# confirm order
driver.find_element(By.XPATH, "//button[normalize-space()='Confirm']").click()

# viewing order details
driver.find_element(By.XPATH, "//a[normalize-space()='Click here for order details.']").click()

#logging out
driver.find_element(By.XPATH, "//a[@class='ico-logout']").click()
print("TEST PASSED")
driver.close()
