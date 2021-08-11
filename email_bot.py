from io import SEEK_CUR
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
import time,bs4
from source import open_and_click, open_and_input,find,open_link,find_xpath
email="bigbloggerdeluxe@gmail.com"
password="Testkit1"
delay=100
path_driver = "chromedriver.exe"
email_input_selector="input.whsOnd"
password_selector="input.whsOnd"
more_selector="div.ajR"
by, login_selector, cookies_selector = By.CSS_SELECTOR,"button._3f37264be67c8f40fa9f76449afdb4bd-scss", "button#onetrust-accept-btn-handler"
unread_emails_selector="tr.zE"
confirm_emails_div_selector="div.gs"
confirm_xpath='/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/table/tr/td[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div[3]/div[3]/div[1]/div/table/tbody/tr/td/div/table[4]/tbody/tr[2]/td[2]/table/tbody/tr/td/div/a'
confirm_email_xpath="//*[contains(text(), 'CONFIRM EMAIL')]"
driver = webdriver.Chrome(path_driver)

driver.maximize_window()
actions = ActionChains(driver)
driver.get(r'https://accounts.google.com/signin/v2/identifier?continue='+'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1'+'&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
open_and_input(actions,driver,delay,email_input_selector,email,0,True)
time.sleep(10)
open_and_input(actions,driver,delay,password_selector,password,0,True)

unread_emails= find(actions,driver,delay,unread_emails_selector)
selected_emails=[]
for j,i in enumerate(unread_emails):
    innerhtml=i.get_attribute("innerHTML")
    soup = bs4.BeautifulSoup(innerhtml,"html.parser")
    tds=soup.find_all("td")
    subject=tds[3].find("span",{"class":"zF"})
    desc=tds[4].find("span",{"class":"bqe"})
    if "Spotify" in subject and "Confirm your new email address" in desc:
        
        selected_emails.append(i)
for k in range(len(selected_emails)):

    unread_emails= find(actions,driver,delay,unread_emails_selector)
    print("got unread emails")
    
    for j,i in enumerate(unread_emails):
        time.sleep(2)
        innerhtml=i.get_attribute("innerHTML")
        soup = bs4.BeautifulSoup(innerhtml,"html.parser")
        tds=soup.find_all("td")
        subject=tds[3].find("span",{"class":"zF"})
        desc=tds[4].find("span",{"class":"bqe"})
        if "Spotify" in subject and "Confirm your new email address" in desc:
            print("found")
            i.click()
            print("clicked")
    # print(selected_emails[i].get_attribute("class"))
    # open_and_click(actions,driver,delay,selector=selected_emails[i].get_attribute("class").split(" ")[1],choice=0)
    
            more_button=find(actions,driver,10,more_selector)

            if more_button:
                print("found more button")
                open_and_click(actions,driver,delay,more_selector)
            
            # try:
            confirm_email_div=find(actions,driver,delay,confirm_emails_div_selector)
            l=len(confirm_email_div)
            for i in range(l):
                confirm_email_div[i].click()
            
            multiple_conf_buttons=find_xpath(actions,driver,delay,confirm_email_xpath)
            print(f"found emails {multiple_conf_buttons}")
            

            confirm_button=find_xpath(actions,driver,delay,confirm_xpath)
            if confirm_button:
                print("found confirm")
                try:
                    time.sleep(3)
                    open_and_click(actions,driver,10,xpath=confirm_xpath)
                    print('clicked confirm')
                    time.sleep(2)
                    driver.switch_to_window(driver.window_handles[0])
                    print("switching")
                    # driver.get("https://mail.google.com")
                    driver.back()
                    print("going back")
                    
                    time.sleep(5)        
                    
                    # print("switching windows")
                except:
                    # driver.get("https://mail.google.com")
                    driver.back()
                    print("going back except")
                    driver.refresh()
                    time.sleep(5)
        else:
            pass

# driver.quit()
    
    # driver.back()
    
    
    # except:

    #     driver.back()
    # test=open_link(actions,driver,delay,selector=unread_emails_selector,choice=i)
    # innerhtml=test.get_attribute("innerHTML")
    # if "Spotify" in innerhtml:
    #     ###for testing code
    #     test=find(actions,driver,delay,unread_emails_selector)
    #     for j in test:
    #         print(f'on link {j.get_attribute("innerHTML")}')
    #     open_and_click(actions,driver,delay,selector=unread_emails_selector,choice=i)

    #     time.sleep(3)
    #     more_button=find(actions,driver,delay,more_selector)
    #     if more_button:
    #         open_and_click(actions,driver,delay,more_selector)
        # try:
        #     open_and_click(actions,driver,delay,xpath=confirm_xpath)

        #     driver.switch_to_window(driver.window_handles[0])
        #     driver.back()
        # except:

        #     driver.back()
        # time.sleep(5)
    






