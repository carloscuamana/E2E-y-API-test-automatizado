from itertools import product
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
def test_agregar_y_comprar_2_produtos ():
    driver.get("https://www.demoblaze.com/")
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="tbodyid"]/div[1]/div/div/h4/a'))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a'))).click()
    wait.until(EC.alert_is_present()).accept()
    time.sleep(5)
    driver.get("https://www.demoblaze.com/")
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="tbodyid"]/div[9]/div/div/h4/a'))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a'))).click()
    time.sleep(5)
    wait.until(EC.alert_is_present()).accept()
    wait.until(EC.presence_of_element_located((By.ID, "cartur"))).click()
    time.sleep(30)
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-wrapper"]/div/div[2]/button'))).click()
    time.sleep(5)
    driver.find_element(By.ID, "name").send_keys("jhon")
    driver.find_element(By.ID, "country").send_keys("USA")
    driver.find_element(By.ID, "city").send_keys("NY")
    driver.find_element(By.ID, "card").send_keys("12345")
    driver.find_element(By.ID, "month").send_keys("12")
    driver.find_element(By.ID, "year").send_keys("2025")
    driver.find_element(By.XPATH, '//*[@id="orderModal"]/div/div/div[3]/button[2]').click()
    assert (By.XPATH, '/html/body/div[10]/div[7]/div/button')
    print("prueba exitosa")
    driver.quit()
