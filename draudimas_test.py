from argparse import Action
from msilib.schema import ActionText
from selenium import webdriver
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from get_user_info import *   ## import my personal and car data /number/personal_code/car_years


driver = webdriver.Chrome('C:\\Users\\glera\\Desktop\\chromedriver.exe')
driver.get('https://www.edrauda.lt/')

wait = WebDriverWait(driver, 15)

time.sleep(2)
if driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"):
    cookies = driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection").click()


auto_insurance_field_loading = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Automobilio']")))
auto_insurance = driver.find_element(By.XPATH,"//div[text()='Automobilio']").click()

#fill auto number
auto_num_field_loading = wait.until(EC.visibility_of_element_located((By.NAME, "plate_n")))
auto_num_field = driver.find_element(By.NAME, "plate_n").send_keys(number)

checkbox = driver.find_element(By.XPATH, "//input[@id='chkContinue']/following-sibling::div")
checkbox.click()

# nepatinka jam sitas checkox. Kadangi užsideda checked klasė, tai mes vis tikrinam ar uzsidėjo ir jei ne, tai bandom.
while "checked" not in checkbox.get_attribute("class"):
    checkbox.click()
    time.sleep(0.1)

calculate_button = driver.find_element(By.XPATH, "//form[@class='frmIndex']/div[4]")
calculate_button_loading = wait.until(EC.element_to_be_clickable(calculate_button))
calculate_button.click()

#find confirm user personality field
personal_confirmation_field_loading = wait.until(EC.visibility_of_element_located((By.NAME, "pkodreg")))
personal_confirmation_field = driver.find_element(By.NAME, "pkodreg")
personal_confirmation_field.send_keys(personal_code)

#calculate (next)
next_button = driver.find_element(By.XPATH, "//div[@class='ctnContentDialogButtons text-center']/div")
next_button_loading = wait.until(EC.element_to_be_clickable(next_button))
next_button.click()
#find auto registration field

auto_year_field_loading = wait.until(EC.visibility_of_element_located((By.XPATH, "//select[@name='firstregtime']")))
auto_year_field = driver.find_element(By.XPATH, "//select[@name='firstregtime']")
#fill registration year
auto_year_field.send_keys(car_years)

next2_calculate = driver.find_element(By.XPATH, "//div[27]/div")
next2_calculate_loading = wait.until(EC.element_to_be_clickable(next2_calculate))

next2_calculate.click()
                                           
#select insurance period (months) / 12months
insurance_period = driver.find_element(By.XPATH,"//div[@id='tpvca_params_block']//div[text()='Vienas mokėjimas']").click()

#payment type (one payment or splitted)  / one payment
payment_type= driver.find_element(By.XPATH, "//*[@id='tpvca_params_block']//div[@class='edrauda-btn float-left selectionButton active edrauda-btn-blue']").click()

#one user checkbox  or  several car users  / one user
time.sleep(2)
auto_users = driver.find_element(By.XPATH, "//*[@id='user_private']//div[@data-for='other2_1']").click()


count = driver.find_element(By.XPATH, "//a[@id='big-recalc']")
count_loading= wait.until(EC.element_to_be_clickable(count))
count.click()

next = driver.find_element(By.XPATH, "//a[contains(text(),'PIRMYN')]")
nex_loading = wait.until(EC.element_to_be_clickable(next))
next.click()

driver.close()


            
               