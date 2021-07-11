from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time, schedule, json

#login credential and gm code
with open('config.json') as file:
    data = json.load(file)

#login google account automation
def gLogin():
    # Login Page
    driver.get('https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')
    driver.refresh()

    # input Gmail
    print('Inputting Email...')
    driver.find_element_by_id("identifierId").send_keys(data['email']) #email
    print('Done')
    driver.find_element_by_id("identifierNext").click()
    driver.implicitly_wait(10)

    # input Password
    print('Inputting Password...')
    driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(data['password']) #password
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
    time.sleep(30) #wait for page to load correctly
    print('Turning off mic...')
    turn_off_mic_action = ActionChains(driver)
    turn_off_mic_action.key_down(Keys.CONTROL).send_keys("d").key_up(Keys.CONTROL).perform();
    print('Done')

    #turn off cam by ctrl + e
    time.sleep(10)
    print('Turning off camera...')
    turn_off_camera_action = ActionChains(driver)
    turn_off_camera_action.key_down(Keys.CONTROL).send_keys("e").key_up(Keys.CONTROL).perform();
    print('Done')

    #Join class
    print('Joining meet...')
    join_button = WebDriverWait(driver, 36).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Join now')]")))
    driver.execute_script("arguments[0].click();", join_button)
    print('Done')
  
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
    schedule.every().monday.at('07:30').do(login, data['bio_code'])
    schedule.every().monday.at('09:02').do(login, data['bm_code'])
    schedule.every().monday.at('12:30').do(login, data['phy_code'])

    #tuesday class
    schedule.every().tuesday.at('08:00').do(login, data['pj_code'])
    schedule.every().tuesday.at('10:30').do(login, data['am_code'])
    schedule.every().tuesday.at('11:32').do(login, data['mm_code'])

    #wednesday class
    schedule.every().wednesday.at('07:30').do(login, data['pm_code'])
    schedule.every().wednesday.at('08:32').do(login, data['bm_code'])
    schedule.every().wednesday.at('11:30').do(login, data['phy_code'])
    schedule.every().wednesday.at('12:32').do(login, data['eng_code'])

    #thursday class 
    schedule.every().thursday.at('07:30').do(login, data['bio_code'])
    schedule.every().thursday.at('09:02').do(login, data['am_code'])
    schedule.every().thursday.at('10:30').do(login, data['cn_code'])
    schedule.every().thursday.at('11:32').do(login, data['pm_code'])

    #friday class
    schedule.every().friday.at('07:30').do(login, data['sej_code'])
    schedule.every().friday.at('08:32').do(login, data['eng_code'])
    schedule.every().friday.at('10:30').do(login, data['mm_code'])
    schedule.every().friday.at('11:32').do(login, data['cn_code'])

    #run the program in the background
    while True:
        schedule.run_pending() #check if need to run anything
        time.sleep(10) #10 second interval
