import os.path
from selenium import webdriver



class login():

    def __init__(self):
        self.is_logined = False
        self.driver = None
        
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('headless')
        self.options.add_argument('window-size=1920x1080')
        self.options.add_argument("disable-gpu")

    def execute_login_process(self):
        user_id = input('ID: ')
        user_pw = input('PW: ')
        print('Hold on a sec...')
        self.driver = webdriver.Chrome(os.path.abspath('chromedriver'), chrome_options=self.options) #The location of your chromedriver is changable.
        self.driver.implicitly_wait(5)                                                                  #Make sure the location is correct.
        


        self.driver.get('https://nid.naver.com/nidlogin.login')
        self.driver.find_element_by_name('id').send_keys(user_id)
        self.driver.find_element_by_name('pw').send_keys(user_pw)
        print('processing...')
        self.driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()



        try:
            self.driver.find_element_by_id('err_common')
        except:
            self.is_logined = True
            try:
                self.driver.find_element_by_xpath('//*[@id="phone_value"]')
            except:
                pass
            else:
                print('It seems that you are trying to login in a foreign country.\nWe need your telephone number to verifiy your identification')
                tel_num = input('Telephone number: ')
                print('Hold on a sec...')
                self.driver.find_element_by_xpath('//*[@id="phone_value"]').send_keys(tel_num)
                self.driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/span/input').click()
                print('processing...')
                try:
                    self.driver.find_element_by_id('error_common')
                except:
                    pass
                else:
                    print('Failed to verify')
                    self.is_logined = False
        else:
            self.is_logined = False

    if self.is_logined:
        print("Succeeded to login!")
    else:
        print("Failed to login")
        
        return self.is_logined

    def close_login_session(self): #You have to call this function after calling execute_login_process
        if self.driver != None:
            self.driver.quit()
            return True
        else:
            return False

# if __name__ == '__main__':
#     n = login()
#     r = n.execute_login_process()
#     if r:
#         print('login successfully')

#     a = n.close_login_session()
#     if a:
#         print('succesfully closed the session')
#     else:
#         print('the session is not open')