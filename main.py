import re

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
driver = webdriver.Chrome('C:/Users/yasuo/Desktop/ne/chromedriver.exe')

#open the webpage

driver.get(
        "https://www.linkedin.com/search/results/companies/?keywords=publishing%20books&origin=SWITCH_SEARCH_VERTICAL&page=6&sid=xpt")
not_now = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "تسجيل الدخول")]'))).click()
username = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='session_key']")))
password = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='session_password']")))

    # enter username and password
username.clear()
username.send_keys("username")
password.clear()
password.send_keys("password")

button = WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
gg=[]
hh = driver.find_elements_by_xpath('//a[@class="app-aware-link"]')
for h in hh:

    nn = h.get_attribute('href')
    if nn not in gg:
        gg.append(nn)
for g in gg:
    driver.get(g)
    emails=[]
    try:
        webs = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[class='ember-view org-top-card-primary-actions__action']")))
        kk = webs.get_attribute('href')
        driver.get(kk)
        doc = driver.page_source
        ems = re.findall(r'[\w\.-]+@[\w\.-]+', doc)
        if len(ems)!=0:
            for em in ems:
                bb = em.split('@')
                if em not in emails:
                    if bb[1].endswith('png') or bb[1].endswith('jpg') or bb[1].endswith('1') or bb[1].endswith(
                                    '2') or \
                        bb[1].endswith('0') or bb[1].endswith('3') or bb[1].endswith('4') or bb[1].endswith(
                                '5') or \
                        bb[1].endswith('6') or bb[1].endswith('7') or bb[1].endswith('8') or bb[1].endswith(
                                '9') or len(em) < 6:
                        continue
                    else:
                        emails.append(em)
                else:
                    continue
        else:
            if kk.endswith('/'):
                driver.get(kk+'contact')
            else:
                driver.get(kk+'/contact')

            for em in ems:
                bb = em.split('@')
                if em not in emails:
                    if bb[1].endswith('png') or bb[1].endswith('jpg') or bb[1].endswith('1') or bb[1].endswith(
                                    '2') or \
                        bb[1].endswith('0') or bb[1].endswith('3') or bb[1].endswith('4') or bb[1].endswith(
                                '5') or \
                        bb[1].endswith('6') or bb[1].endswith('7') or bb[1].endswith('8') or bb[1].endswith(
                                '9') or len(em) < 6:
                        continue
                    else:
                        emails.append(em)
                else:
                    continue
        for e in emails:
            print(e)
        emails = []
        print('*'*50)
    except:
        print('no web site there')



