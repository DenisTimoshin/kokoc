
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



options = webdriver.ChromeOptions()

# Опции браузера

options.add_argument(" --window-size=1920,1080")
#options.add_argument("--headless")




# Создание экземпляра веб-драйвера

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 30, poll_frequency=1)


# Переход на веб-страницу

driver.get("https://kokoc.tech/")

#ФОС header

btn__name = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/nav[1]/div/div[2]/div/button').click()

input__name = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div/form/div/div[1]/input').send_keys("auto-test")

input__email = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div/form/div/div[2]/input').send_keys("auto@test.test")

for i in range(10):
    input__phone = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div/form/div/div[3]/input').send_keys(9)

btn = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div/form/button')
wait.until(EC.element_to_be_clickable(btn)).click()


appearance_of_the_component = (By.XPATH, '/html/body/div[2]/div/div/div/div/div/h4')
wait.until(EC.visibility_of_element_located(appearance_of_the_component))

driver.refresh()

print("ФОС header")

#ФОС hero
btn__name = driver.find_element(By.XPATH, '/html/body/div/div/section[1]/div/div/button[1]').click()

input__name = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div/form/div/div[1]/input').send_keys("auto-test")

input__email = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div/form/div/div[2]/input').send_keys("auto@test.test")

for i in range(10):
    input__phone = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div/form/div/div[3]/input').send_keys(9)

btn = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div/form/button')
wait.until(EC.element_to_be_clickable(btn)).click()

appearance_of_the_component = (By.XPATH, '/html/body/div[2]/div/div/div/div/div/h4')
wait.until(EC.visibility_of_element_located(appearance_of_the_component))

driver.refresh()

print("ФОС hero")

#ФОС

input__name = driver.find_element(By.XPATH, '/html/body/div/div/section[11]/div/div[2]/form/div[1]/input').send_keys("auto-test")

input__email = driver.find_element(By.XPATH, '/html/body/div/div/section[11]/div/div[2]/form/div[2]/input').send_keys("auto@test.test")

for i in range(10):
    input__phone = driver.find_element(By.XPATH, '/html/body/div/div/section[11]/div/div[2]/form/div[3]/input').send_keys(9)

btn = driver.find_element(By.XPATH, '/html/body/div/div/section[11]/div/div[2]/form/button')
wait.until(EC.element_to_be_clickable(btn)).click()

appearance_of_the_component = (By.XPATH, '/html/body/div[2]/div/div/div/div/div/h4')
wait.until(EC.visibility_of_element_located(appearance_of_the_component))

driver.refresh()

print("ФОС")

#ФОС Футер

input__email = driver.find_element(By.XPATH, '/html/body/div/div/footer/div/div[1]/form/div/input').send_keys("auto@test.test")

btn = driver.find_element(By.XPATH, '/html/body/div/div/footer/div/div[1]/form/button').click()

print("ФОС Футер")
print("Успех!")