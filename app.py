from io import SEEK_CUR
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from source import open_and_click,open_and_input,find,open_link,find_xpath
from AccountHandler import CreateAccounts,get_proxies
from selenium.webdriver.common.proxy import Proxy, ProxyType
import threading,os,zipfile,random,time,bs4
path_driver = "chromedriver.exe"
email="dummy6109@gmail.com"
password="inspirehot"
delay=15
new_email="dummy6133@gmail.com"
new_password="inspirehot"
# driver = webdriver.Chrome(path_driver)

# Email bot variables
infile=open("email.txt","r")
content=infile.read()
infile.close()
content=content.split(":")
gmail_email=content[0]
gmail_password=content[1]
delay=100
path_driver = "chromedriver.exe"
gmail_input_selector="input.whsOnd"
password_selector="input.whsOnd"
more_selector="div.ajR"
by, login_selector, cookies_selector = By.CSS_SELECTOR,"button._3f37264be67c8f40fa9f76449afdb4bd-scss", "button#onetrust-accept-btn-handler"
unread_emails_selector="tr.zE"
confirm_emails_div_selector="div.gs"
confirm_xpath='/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/table/tr/td[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div[3]/div[3]/div[1]/div/table/tbody/tr/td/div/table[4]/tbody/tr[2]/td[2]/table/tbody/tr/td/div/a'
confirm_email_xpath="//*[contains(text(), 'CONFIRM EMAIL')]|//*[contains(text(), 'BEKRÄFTA E-POSTADRESS')]|//*[contains(text(), 'CONFIRMAR CORREO ELECTRÓNICO')]|//*[contains(text(), '確認電子郵件')]"




# login_button=driver.find_element_by_xpath("//*[@data-testid='login-button']")
by, login_selector, cookies_selector = By.CSS_SELECTOR,"button.Hy_P64B8lNKgp3N7Qz4Z", "button#onetrust-accept-btn-handler"
email_input_selector="input#login-username"
password_input_selector="input#login-password"
login_button_selector="button#login-button"
user_widget_selector="button.PnXH8Hvc4os3tFpc10_z"
account_button_selector="button._qjkLyY1fy0hwCfzDZP7"
edit_profile_selector="a.CTA__root--3drmT"
email_change_selector="input#email"
edit_password_selector="input#password"
account_button_selector_edit="button.svelte-kdyqkb"
logout_button_selector="a.mh-subtle"

save_profile_button_selector="button.ButtonLegacy__ButtonLegacyInner-o653de-0"
# driver.maximize_window()
# actions = ActionChains(driver)

accounts=CreateAccounts("created_accountstest.txt","tochangetest.txt")
count=4 
new_accounts=[]
proxies=get_proxies()

def login(actions,driver,delay):
    driver.get(r'https://accounts.google.com/signin/v2/identifier?continue='+'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1'+'&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
    open_and_input(actions,driver,delay,gmail_input_selector,gmail_email,0,True)
    time.sleep(10)
    open_and_input(actions,driver,delay,password_selector,gmail_password,0,True)

def get_unread_emails(actions,driver,delay):
    unread_emails= find(actions,driver,delay,unread_emails_selector)
    selected_emails=[]
    for j,i in enumerate(unread_emails):
        innerhtml=i.get_attribute("innerHTML")
        soup = bs4.BeautifulSoup(innerhtml,"html.parser")
        tds=soup.find_all("td")
        subject=tds[3].find("span",{"class":"zF"})
        desc=tds[4].find("span",{"class":"bqe"})
        if "Spotify" in subject:
            
            selected_emails.append(i)
    return selected_emails

def change_email(driver,actions):
    

    l= len(accounts)
    for j in range(l):
        try:
            driver.get("https://open.spotify.com")
            email=accounts[0].current_account.email
            password=accounts[0].current_account.password
            new_email=accounts[0].change_account.email
            new_password=accounts[0].current_account.password

            open_and_click(actions,driver,delay,selector=login_selector,choice=0)
            open_and_input(actions,driver,delay,email_input_selector,email)
            open_and_input(actions,driver,0,password_input_selector,password,0,True)
            open_and_click(actions,driver,50,selector=user_widget_selector)
            open_and_click(actions,driver,delay,selector=account_button_selector)
            driver.close()
            driver.switch_to_window(driver.window_handles[-1])
            print(driver.current_url)
            sliced=driver.current_url.split("/")
            new_url=sliced[0]+"//"+sliced[2]+"/"+sliced[3]+"/"+sliced[4]+"/"+"profile/"
            driver.get(new_url)
            open_and_input(actions,driver,delay,email_change_selector,new_email)
            open_and_input(actions,driver,delay,edit_password_selector,new_password,0,True)
            open_and_click(actions,driver,delay,selector=account_button_selector_edit)
            open_and_click(actions,driver,delay,selector=logout_button_selector)
            accounts.pop(0)
            outfile=open("new_accounts.txt","a")
            
            outfile.write(new_email+":"+new_password)
            outfile.close()
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
                        more_button=find(actions,driver,10,more_selector)

                        if more_button:
                            print("found more button")
                            open_and_click(actions,driver,delay,more_selector)
                        confirm_email_div=find(actions,driver,15,confirm_emails_div_selector)
                        print(f"confirm buttons {confirm_email_div}")
                        l=len(confirm_email_div)
                        for z in range(l):
                            # print(confirm_email_div[z].tag_name,confirm_email_div[z].get_attribute("innerHTML"))
                            confirm_email_div[z].click()
                        # multiple_conf_buttons=find_xpath(actions,driver,10,confirm_email_xpath)
                        # print(f"found emails {multiple_conf_buttons}")
                        

                        
                        # if multiple_conf_buttons:

                        #     print("found confirm")
                        #     for button in multiple_conf_buttons: 
                        #         # print(button.tag_name)
                        #         if button.tag_name =="td":
                        #             try:
                        #                 button.click()                        
                                        
                        #                 print('clicked confirm')
                        #                 time.sleep(2)
                        #                 driver.switch_to_window(driver.window_handles[-1])
                        #                 driver.close()
                        #                 driver.switch_to_window(driver.window_handles[0])
                        #                 print("switching")
                                        
                        #                 # driver.get("https://mail.google.com")
                                        
                        #                 print("going back")
                                        
                        #                 time.sleep(5)        
                                        
                        #                 # print("switching windows")
                                    
                        #                 # driver.get("https://mail.google.com")
                        #             except:    
                        #             # print("going back except")
                        #                 driver.refresh()
                        #             # time.sleep(5)
                        #     driver.back()
                

            
            driver.quit()
            
        except:
            driver.get("https://www.spotify.com/pk-en/logout/")
            driver.switch_to_window(driver.window_handles[-1])
            accounts.pop(0)

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
len_proxies=len(proxies)-1
thread_count=int(input("Enter the number of threads: "))

while True:
    if threading.activeCount() <= thread_count:
        num=random.randint(0,len_proxies)
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
        driver = webdriver.Chrome("chromedriver.exe",options=chrome_options)
        actions = ActionChains(driver)
        browserThread=threading.Thread(target=change_email,args=(driver,actions))
        browserThread.start()



















