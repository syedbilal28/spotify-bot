from io import SEEK_CUR
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from source import open_and_click,open_and_input
from AccountHandler import CreateAccounts
path_driver = "chromedriver.exe"
email="dummy6109@gmail.com"
password="inspirehot"
delay=15
new_email="dummy6133@gmail.com"
new_password="inspirehot"
driver = webdriver.Chrome(path_driver)





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
driver.maximize_window()
actions = ActionChains(driver)
accounts=CreateAccounts("created_accountstest.txt","tochangetest.txt")
for account in accounts:
    try:
        driver.get("https://open.spotify.com")
        email=account.current_account.email
        password=account.current_account.password
        new_email=account.change_account.email
        new_password=account.current_account.password

        open_and_click(actions,driver,delay,selector=login_selector,choice=0)
        open_and_input(actions,driver,delay,email_input_selector,email)
        open_and_input(actions,driver,0,password_input_selector,password,0,True)
        open_and_click(actions,driver,delay,selector=user_widget_selector)
        open_and_click(actions,driver,delay,selector=account_button_selector)
        driver.switch_to_window(driver.window_handles[-1])
        print(driver.current_url)
        sliced=driver.current_url.split("/")
        new_url=sliced[0]+"//"+sliced[2]+"/"+sliced[3]+"/"+sliced[4]+"/"+"profile/"
        driver.get(new_url)
        open_and_input(actions,driver,delay,email_change_selector,new_email)
        open_and_input(actions,driver,delay,edit_password_selector,new_password,0,True)
        open_and_click(actions,driver,delay,selector=account_button_selector_edit)
        open_and_click(actions,driver,delay,selector=logout_button_selector)
    except:
        driver.get("https://www.spotify.com/pk-en/logout/")
        driver.switch_to_window(driver.window_handles[-1])
        
















