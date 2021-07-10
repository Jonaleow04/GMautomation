from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time, schedule

#gm code
bm_code = 'julbmt5'
eng_code = 'par2bit5'
cn_code = 'hcsbct5'
phy_code = 'asrifzt5'
bio_code = 'shalbgt5'
sej_code = 'ruzsjt5a'
pm_code = 'mogpmt5'
mm_code = 'talmmt5'
am_code = 'cxq-uern-zrd'
pj_code = 'mzampjkt5'

#login credential
with open('Login Credential.txt', 'r') as file:
    login_credential = file.read().splitlines()

email = login_credential[0]
password = login_credential[1]

#login google account automation
def gLogin():
    # Login Page
    driver.get('https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')
    driver.refresh()
    # input Gmail
    print('Inputting Email...')
    driver.find_element_by_id("identifierId").send_keys(email) #email
    print('Done')
    driver.find_element_by_id("identifierNext").click()
    driver.implicitly_wait(10)

    # input Password
    print('Inputting Password...')
    driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password) #password
    driver.implicitly_wait(10)
    print('Done')
    driver.find_element_by_id("passwordNext").click()
    driver.implicitly_wait(10)
  
    # go to google home page
    driver.get('https://google.com/')
    driver.implicitly_wait(100)

#login meet automation
def login(gm_code):

    # go to google meet
    print('Loading Google Meet...')
    driver.get("https://meet.google.com/landing") 
    print('Done')
    time.sleep(2)
    print('Refreshing...')
    driver.refresh() #refresh to avoid error in loading page
    print('Done')

    #enter class code
    print('Inputting code...')
    driver.find_element_by_id("i3").send_keys(gm_code)
    press_enter = ActionChains(driver)
    press_enter.key_down(Keys.ENTER).key_up(Keys.ENTER).perform();
    print('Done')

    #turn off mic by ctrl + d
    time.sleep(10)
    print('Turning off mic...')
    turn_off_mic_action = ActionChains(driver)
    turn_off_mic_action.key_down(Keys.CONTROL).send_keys("d").key_up(Keys.CONTROL).perform();
    print('Done')

    #turn off cam by ctrl + e
    time.sleep(5)
    print('Turning off camera...')
    turn_off_camera_action = ActionChains(driver)
    turn_off_camera_action.key_down(Keys.CONTROL).send_keys("e").key_up(Keys.CONTROL).perform();
    print('Done')

    #Join class
    print('Joining meet...')
    join_button = WebDriverWait(driver, 36).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Join now')]")))
    driver.execute_script("arguments[0].click();", join_button)
    print('Done')

#create functions for each class with class code as schedule module .do(func()) does not taking in argument
def bm_class():
    login(bm_code)

def eng_class():
    login(eng_code)

def cn_class():
    login(cn_code)

def phy_class():
    login(phy_code)

def bio_class():
    login(bio_code)

def sej_class():
    login(sej_code)

def pm_class():
    login(pm_code)

def mm_class():
    login(mm_code)

def am_class():
    login(am_code)

def pj_class():
    login(pj_code)
  
# create chrome instamce
# Code to allow access for Microphone, Camera and notifications
# 0 is disable and 1 is allow.
opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
"profile.default_content_setting_values.media_stream_mic": 1, 
"profile.default_content_setting_values.media_stream_camera": 1,
"profile.default_content_setting_values.geolocation": 1, 
"profile.default_content_setting_values.notifications": 1 
})

#acess chromedriver (crhome for automation)
driver = webdriver.Chrome(options=opt, executable_path=r'C:\Users\jonat\Downloads\chromedriver_win32 (1)\chromedriver.exe')

#to login google account first
gLogin()

#loop that will keep the program running and execute the specific function according to the given time
if __name__ == "__main__":
    #monday class
    schedule.every().monday.at('07:30').do(bio_class)
    schedule.every().monday.at('09:02').do(bm_class)
    schedule.every().monday.at('12:30').do(phy_class)

    #tuesday class
    schedule.every().tuesday.at('08:00').do(pj_class)
    schedule.every().tuesday.at('10:30').do(am_class)
    schedule.every().tuesday.at('11:32').do(mm_class)

    #wednesday class
    schedule.every().wednesday.at('07:30').do(pm_class)
    schedule.every().wednesday.at('08:32').do(bm_class)
    schedule.every().wednesday.at('11:30').do(phy_class)
    schedule.every().wednesday.at('12:32').do(eng_class)

    #thursday class 
    schedule.every().thursday.at('07:30').do(bio_class)
    schedule.every().thursday.at('09:02').do(am_class)
    schedule.every().thursday.at('10:30').do(cn_class)
    schedule.every().thursday.at('11:32').do(pm_class)


    #friday class
    schedule.every().friday.at('07:30').do(sej_class)
    schedule.every().friday.at('08:32').do(eng_class)
    schedule.every().friday.at('10:30').do(mm_class)
    schedule.every().friday.at('11:32').do(cn_class)

    #run the program in the background
    while True:
        schedule.run_pending() #check if need to run anything
        time.sleep(10) #10 second interval

