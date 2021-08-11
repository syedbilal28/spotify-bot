
from io import SEEK_CUR
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
import time

by, login_selector, cookies_selector = By.CSS_SELECTOR,"button._3f37264be67c8f40fa9f76449afdb4bd-scss", "button#onetrust-accept-btn-handler"
def open_and_click(actions,driver,delay,selector=None,xpath=None,**kwargs):
    if xpath:
        by=By.XPATH    
        sls = WebDriverWait(driver, delay).until(EC.presence_of_all_elements_located((by, xpath)))
    else:
        by=By.CSS_SELECTOR
        sls = WebDriverWait(driver, delay).until(EC.presence_of_all_elements_located((by, selector)))
    if sls:
        # get accept cookies button element and click
    
        
        # get buy button element, move to element and click
        if kwargs:
            sel_index=kwargs['choice']
            if selector:

                elem = driver.find_elements_by_css_selector(selector)[sel_index]
            else:
                elem = driver.find_elements_by_xpath(xpath)[sel_index]
        else:
            if selector:        
                elem = driver.find_elements_by_css_selector(selector)[0]
            else:
                elem = driver.find_elements_by_xpath(xpath)[0]
        
        if isinstance(elem, WebElement) and elem.is_displayed() and elem.is_enabled():
            try:
                actions.move_to_element(elem).click(elem).perform()
            except:
                elem.click()

def open_link(actions,driver,delay,selector=None,xpath=None,**kwargs):
    if xpath:
        by=By.XPATH    
        sls = WebDriverWait(driver, delay).until(EC.presence_of_all_elements_located((by, xpath)))
    else:
        by=By.CSS_SELECTOR
        sls = WebDriverWait(driver, delay).until(EC.presence_of_all_elements_located((by, selector)))
    if sls:
        # get accept cookies button element and click
    
        
        # get buy button element, move to element and click
        if kwargs:
            sel_index=kwargs['choice']
            if selector:

                elem = driver.find_elements_by_css_selector(selector)[sel_index]
            else:
                elem = driver.find_elements_by_xpath(xpath)[sel_index]
        else:
            if selector:        
                elem = driver.find_elements_by_css_selector(selector)[0]
            else:
                elem = driver.find_elements_by_xpath(xpath)[0]
        
        if isinstance(elem, WebElement) and elem.is_displayed() and elem.is_enabled():
            return elem
def open_and_input(actions,driver,delay,selector,input,*choice):
    
    sls = WebDriverWait(driver, delay).until(EC.presence_of_all_elements_located((by, selector)))
    if sls:
        # get accept cookies button element and click
    
        
        # get buy button element, move to element and click
        if choice:
            sel_index=choice[0]
            elem = driver.find_elements_by_css_selector(selector)[sel_index]
        else:
            elem = driver.find_elements_by_css_selector(selector)[0]
        
        if isinstance(elem, WebElement) and elem.is_displayed() and elem.is_enabled():
            elem.clear()
            elem.send_keys(input)
            if choice:
                if choice[1]:
                    print("pressing")
                    elem.send_keys(Keys.ENTER)
def find(actions,driver,delay,selector):
    try:
        sls = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((by, selector)))
    
        if sls:
            elem = driver.find_elements_by_css_selector(selector)
            return elem
    except:
        return None
    

def find_xpath(actions,driver,delay,xpath):
    sls = WebDriverWait(driver, delay).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
    if sls:
        elem = driver.find_elements_by_xpath(xpath)
        return elem

