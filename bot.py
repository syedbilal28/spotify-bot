
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from source import open_and_input,find,open_and_click,find_xpath
import time,bs4
class EmailBot:
    def __init__(self,email,password):
        self.email=email
        self.password=password
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.actions = ActionChains(self.driver)
        self.delay=30
        self.email_input_selector="input.whsOnd"
        self.password_selector="input.whsOnd"
        self.unread_emails_selector="tr.zE"
        self.more_selector="div.ajR"
        self.confirm_emails_div_selector="div.gs"
        self.current_email_confirmation_button_counter=0
        self.confirm_email_button_xpath="//*[contains(text(), 'CONFIRM EMAIL')]|//*[contains(text(), 'BEKRÄFTA E-POSTADRESS')]|//*[contains(text(), 'CONFIRMAR CORREO ELECTRÓNICO')]|//*[contains(text(), '確認電子郵件')]"
        # self.mark_as_unread_box_xpath="//*[contains(text(), 'Mark as unread')]"
        self.mark_as_unread_box_xpath="//div[//*[contains(text(), 'Mark as unread')]]"


    def login(self):
        self.driver.get(r'https://accounts.google.com/signin/v2/identifier?continue='+'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1'+'&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
        open_and_input(self.actions,self.driver,self.delay,self.email_input_selector,self.email,0,True)
        time.sleep(10)
        open_and_input(self.actions,self.driver,self.delay,self.password_selector,self.password,0,True)
        
    
    def get_unread_emails(self):
        unread_emails= find(self.actions,self.driver,self.delay,self.unread_emails_selector)
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
    def click_unread_email(self):
        unread_emails=self.get_unread_emails()
        first_unread_email=unread_emails.pop(0)
        self.current_active_unread_email=first_unread_email
        first_unread_email.click()

    def click_more_button(self):
        more_buttons=find(self.actions,self.driver,10,self.more_selector)
        print(f"more buttons {more_buttons}")
        if more_buttons:
            print("found more button")
            open_and_click(self.actions,self.driver,self.delay,self.more_selector)

    def click_all_email_boxes(self):
        confirm_email_div=find(self.actions,self.driver,15,self.confirm_emails_div_selector)
        print(f"confirm buttons {confirm_email_div}")
        l=len(confirm_email_div)
        for i in range(l):
            # print(confirm_email_div[z].tag_name,confirm_email_div[z].get_attribute("innerHTML"))
            confirm_email_div[i].click()

    def click_confirm_email(self):
        confirm_email_buttons=find_xpath(self.actions,self.driver,10,self.confirm_email_button_xpath)
        print(f"found emails {confirm_email_buttons}")
        l=len(confirm_email_buttons)
        if confirm_email_buttons:
            print("found confirm")
            for i in range(self.current_email_confirmation_button_counter,l): 
                # print(button.tag_name)
                button=confirm_email_buttons[i]
                self.current_email_confirmation_button_counter=i
                if button.tag_name =="td":
                    try:
                        button.click()
                        time.sleep(10)
                        self.driver.switch_to_window(self.driver.window_handles[-1])
                        
                        page_html=self.driver.page_source
                        soup = bs4.BeautifulSoup(page_html,"html.parser")
                        body=soup.find("body").text

                        if "Too Many Requests" in body:
                            self.driver.switch_to_window(self.driver.window_handles[0])
                            self.mark_email_as_unread()    
                            # self.driver.quit()
                            break
                        # self.driver.close()
                        self.driver.switch_to_window(self.driver.window_handles[0])
                    except Exception as e:
                        print(f"Exception occured: {e}")
                        pass
            self.current_email_confirmation_button_counter=0

    def mark_email_as_unread(self):
        self.driver.back()
        time.sleep(10)
        target=self.current_active_unread_email
        
        
        self.actions.move_to_element(target).perform()
        
        self.actions.context_click(target).perform()
        time.sleep(10)
        mark_as_unread_button=find_xpath(self.actions,self.driver,10,self.mark_as_unread_box_xpath)
        print(mark_as_unread_button)
        mark_as_unread_button[0].click()


    # def confirm_email_change(self):
        # self.click_unread_email()
        # self.click_more_button()
        # self.click_all_email_boxes()
        # self.click_confirm_email()

    def test_for_unread(self):
        unread_emails=self.get_unread_emails()
        target=unread_emails[0]
        target.click()
        time.sleep(10)
        # self.driver.switch_to_window(self.driver.window_handles[0])
        
        self.current_active_unread_email=target
        self.mark_email_as_unread()



if __name__ == "__main__":
    email="bigbloggerdeluxe@gmail.com"
    password="Testkit1"
    email_bot=EmailBot(email,password)
    email_bot.login()
    # email_bot.confirm_email_change()
    email_bot.test_for_unread()