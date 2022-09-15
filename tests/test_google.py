from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from seleyasha.conditions import element, click_on_element, type_to_element, number_of_elements

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

wait = WebDriverWait(driver, timeout=2)

driver.get('https://ecosia.org')

# type_to_element('[name=q]', value='selene yashaka' + Keys.ENTER)
wait.until(type_to_element('[name=q]', value='selene yashaka' + Keys.ENTER))

# element('[data-test-id=mainline-result-web]):nth-of-type(1) a').click()
wait.until(element('[data-test-id=mainline-result-web]):nth-of-type(1) a')).click()

# click_on_element('[data-test-id=mainline-result-web]):nth-of-type(1) a')
wait.until(click_on_element('[data-test-id=mainline-result-web]):nth-of-type(1) a'))

# number_of_pulls = len(driver.find_elements(By.CSS_SELECTOR, '[id^=issue_]:not([id$=_link])'))
# assert number_of_pulls == 4

# assert_that(number_of_elements('[id^=issue_]:not([id$=_link])', value=4))
wait.until(number_of_elements('[id^=issue_]:not([id$=_link])', value=4))

driver.quit()

