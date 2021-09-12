from AccountHandler import get_proxies
from io import SEEK_CUR
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
import time,bs4,random
import os,zipfile,threading
from source import open_and_click, open_and_input,find,open_link,find_xpath

infile=open("email.txt","r")
content=infile.read()
infile.close()
content=content.split(":")
email=content[0]
password=content[1]
delay=100
path_driver = "chromedriver.exe"
email_input_selector="input.whsOnd"
password_selector="input.whsOnd"
more_selector="div.ajR"
by, login_selector, cookies_selector = By.CSS_SELECTOR,"button._3f37264be67c8f40fa9f76449afdb4bd-scss", "button#onetrust-accept-btn-handler"
unread_emails_selector="tr.zE"
confirm_emails_div_selector="div.gs"
confirm_xpath='/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/table/tr/td[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div[3]/div[3]/div[1]/div/table/tbody/tr/td/div/table[4]/tbody/tr[2]/td[2]/table/tbody/tr/td/div/a'
confirm_email_xpath="//*[contains(text(), 'CONFIRM EMAIL')]|//*[contains(text(), 'BEKRÄFTA E-POSTADRESS')]|//*[contains(text(), 'CONFIRMAR CORREO ELECTRÓNICO')]|//*[contains(text(), '確認電子郵件')]"


# driver = webdriver.Chrome(path_driver)

# driver.maximize_window()
# actions = ActionChains(driver)
def login(actions,driver,delay):
    driver.get(r'https://accounts.google.com/signin/v2/identifier?continue='+'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1'+'&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
    open_and_input(actions,driver,delay,email_input_selector,email,0,True)
    time.sleep(10)
    open_and_input(actions,driver,delay,password_selector,password,0,True)

def get_unread_emails(actions,driver,delay):
    unread_emails= find(actions,driver,delay,unread_emails_selector)
    selected_emails=[]
    if unread_emails is not None:
        for j,i in enumerate(unread_emails):
            innerhtml=i.get_attribute("innerHTML")
            soup = bs4.BeautifulSoup(innerhtml,"html.parser")
            tds=soup.find_all("td")
            subject=tds[3].find("span",{"class":"zF"})
            desc=tds[4].find("span",{"class":"bqe"})
            if "Spotify" in subject:
                
                selected_emails.append(i)
        return selected_emails
    return None
def click_confirm(driver,actions):
    login(actions,driver,delay)
    selected_emails=get_unread_emails(actions,driver,delay)
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
            print(f"subject {subject}")
            if "Spotify" in subject:
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
                confirm_email_div=find(actions,driver,15,confirm_emails_div_selector)
                print(f"confirm buttons {confirm_email_div}")
                l=len(confirm_email_div)
                for z in range(l):
                    # print(confirm_email_div[z].tag_name,confirm_email_div[z].get_attribute("innerHTML"))
                    confirm_email_div[z].click()
                
                multiple_conf_buttons=find_xpath(actions,driver,10,confirm_email_xpath)
                print(f"found emails {multiple_conf_buttons}")
                

                
                if multiple_conf_buttons:

                    print("found confirm")
                    for confirm_count,button in enumerate(multiple_conf_buttons): 
                        # print(button.tag_name)
                        if button.tag_name =="td":
                            try:
                                button.click()                        
                                
                                print(f'clicked confirm, button number {confirm_count}')
                                time.sleep(10)
                                driver.switch_to_window(driver.window_handles[-1])
                                driver.close()
                                driver.switch_to_window(driver.window_handles[0])
                                print("switching")
                                
                                # driver.get("https://mail.google.com")
                                
                                print("going back")
                                
                                time.sleep(5)        
                                
                                # print("switching windows")
                            
                                # driver.get("https://mail.google.com")
                            except:    
                            # print("going back except")
                                driver.quit()
                            # time.sleep(5)
                        else:
                            pass
                    driver.quit()
            else:
                pass

def get_chromedriver(use_proxy=False, user_agent=None):
    path = os.path.dirname(os.path.abspath(__file__))
    chrome_options = webdriver.ChromeOptions()
    if use_proxy:
        pluginfile = 'proxy_auth_plugin.zip'

        with zipfile.ZipFile(pluginfile, 'w') as zp:
            zp.writestr("manifest.json", manifest_json)
            zp.writestr("background.js", background_js)
        chrome_options.add_extension(pluginfile)
    if user_agent:
        chrome_options.add_argument('--user-agent=%s' % user_agent)
    driver = webdriver.Chrome(
        path_driver,
        chrome_options=chrome_options)
    return driver
count=1
proxies=get_proxies()
l =len(proxies)
while True:
    if threading.activeCount() <= count:
        num=random.randint(0,l-1)
        PROXY_HOST = proxies[num][0]  # rotating proxy or host
        PROXY_PORT = proxies[num][1] # port
        
        manifest_json = """
        {
            "version": "1.0.0",
            "manifest_version": 2,
            "name": "Chrome Proxy",
            "permissions": [
                "proxy",
                "tabs",
                "unlimitedStorage",
                "storage",
                "<all_urls>",
                "webRequest",
                "webRequestBlocking"
            ],
            "background": {
                "scripts": ["background.js"]
            },
            "minimum_chrome_version":"22.0.0"
        }
        """

        background_js = """
        var config = {
                mode: "fixed_servers",
                rules: {
                singleProxy: {
                    scheme: "http",
                    host: "%s",
                    port: parseInt(%s)
                },
                bypassList: ["localhost"]
                }
            };

        chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

        function callbackFn(details) {
            return {
                
            };
        }

        chrome.webRequest.onAuthRequired.addListener(
                    callbackFn,
                    {urls: ["<all_urls>"]},
                    ['blocking']
        );
        """ % (PROXY_HOST, PROXY_PORT)
        PROXY = f"{PROXY_HOST}:{PROXY_PORT}" # IP:PORT or HOST:PORT
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=%s' % PROXY)
        driver = webdriver.Chrome("chromedriver.exe")
        
        actions = ActionChains(driver)
        print(PROXY_HOST,PROXY_PORT)
        try:
            browserThread=threading.Thread(target=click_confirm,args=(driver,actions))
            browserThread.start()
        except:
            pass



