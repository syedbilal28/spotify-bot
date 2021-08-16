from io import SEEK_CUR
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from source import open_and_click,open_and_input
from AccountHandler import CreateAccounts,get_proxies
from selenium.webdriver.common.proxy import Proxy, ProxyType
import threading,os,zipfile,random
path_driver = "chromedriver.exe"
email="dummy6109@gmail.com"
password="inspirehot"
delay=15
new_email="dummy6133@gmail.com"
new_password="inspirehot"
# driver = webdriver.Chrome(path_driver)





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
            open_and_click(actions,driver,delay,selector=user_widget_selector)
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
            
            outfile.write(f"{new_email}:{new_password}\n")
            outfile.close()
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
thread_count=0
while True:
    if threading.activeCount() <= count:
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



















