from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException

user = ""
user_password = ""

driver = webdriver.Firefox()

#  Open site
driver.get("http://geoportal.pgi.gov.pl/sopo-web/zad/tasklist")

# Login
username = driver.find_element_by_name("ssousername")
username.send_keys(user)

password = driver.find_element_by_name("password")
password.send_keys(user_password)

OK_button = driver.find_element_by_xpath('/html[1]/body[1]/center[1]/form[1]/table[1]/tbody[1]/tr[3]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/input[1]')
OK_button.click()

# Wait for page
WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'xf-40')))

# Select page
select_page = Select(driver.find_element_by_xpath("//select[@id='xf-40']"))

select_page.select_by_visible_text("10")
driver.find_element_by_xpath("//a[@id='xf-46']").click()

# Loop between landslides start here
for i in range(1, 26):

    # Go to inside landslide page
    time.sleep(3)
    WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.ID, 'xf-105·1')))

    try:
        new_card = driver.find_element_by_xpath("//a[@id='xf-105·" + str(i) + "']")
    except NoSuchElementException:
        break

    new_card.click()

    # Select cards
    WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.ID, 'xf-42')))
    bookmarks = driver.find_element_by_xpath("//select[@id='xf-42']")
    options = bookmarks.find_elements_by_tag_name('option')
    time.sleep(3)

    # Select number of card to edit
    options[16].click()

    # Work but not good have loop
    # for opt in bookmarks.find_elements_by_tag_name('option'):
    #     if '15' in opt.text:
    #         option = opt
    # option.click()

    # Insert text about issues
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'xf-49')))
    issues_text = driver.find_element_by_xpath("//textarea[@id='xf-49']")
    time.sleep(1)
    issues_text.click()
    issues_text.send_keys(Keys.CONTROL, "a")
    issues_text.send_keys(Keys.DELETE)
    issues_text.send_keys("Na chwile obecną osuwisko nie wymaga zabezpieczenia.")

    # Go ahead
    driver.find_element_by_xpath("//a[@id='xf-60']").click()

    # Fill author card
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'xf-62')))
    issues_text = driver.find_element_by_xpath("//textarea[@id='xf-62']")
    time.sleep(1)
    issues_text.click()
    issues_text.send_keys(Keys.CONTROL, "a")
    issues_text.send_keys(Keys.DELETE)
    issues_text.send_keys("Andrzej Michalski")

    # Fill geological qualifications
    geol_qual = driver.find_element_by_xpath("//input[@id='xf-66$xforms-input-1']")
    geol_qual.click()
    geol_qual.send_keys(Keys.CONTROL, "a")
    geol_qual.send_keys(Keys.DELETE)
    geol_qual.send_keys("8/202")

    # Select institution
    initution_select = driver.find_element_by_xpath("//select[@id='xf-82']")
    institutions = initution_select.find_elements_by_tag_name('option')
    time.sleep(1)
    institutions[16].click()

    # Write date
    date_field = driver.find_element_by_xpath("//input[@id='xf-105$xforms-input-1']")
    date_field.click()
    date_field.send_keys(Keys.CONTROL, "a")
    date_field.send_keys(Keys.DELETE)
    date_field.send_keys("2016-10-18")

    # Exit card
    exit_link = driver.find_element_by_xpath("//a[@id='xf-31']").click()

    # Wait for loading
    time.sleep(10)