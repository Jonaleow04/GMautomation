# Chrome GMautomation

## General Information
- This Python program will open up Chrome and log into your scheduled Google Meet with camera and mic turned off.
- The web automation is made using the selenium module with ChromeDriver and the scheduling is made using the schedule module
- An idea popped up in my head when entering my school's class, that is 'What if I can automate all these entering the code process'. Thus, Chrome GMautomation was born.

> WARNING: Note that this program must be used according to one's resonsibility. In no way do I or any contributors of this project encourage students to use this as a way to not sit in front of the desk during class. This project was made with the pure intention of personal

## Setup
1. Install [Python](https://www.python.org/downloads/) 3.4 or above
2. Install the following Python modules: selenium, schedule, time
```bash
python -m pip install selenium
python -m pip install schedule
python -m pip install time

```
3. Install [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

## Usage
- Clone the repository first
- Open up the Login Credential.txt file
- Replace the first line with your Gmail used for logging into the Google Meet
- Then replace the second line with your Gmail's password
- Now open up the Python file
- From line 11 to 20, is the variable used to store the Google Meet's code, you may need to rename the variable it according to your references and replace the code
```python
#gm code
bm_code = '#code' 
eng_code = '#code'
cn_code = '#code'
phy_code = '#code'
bio_code = '#code'
sej_code = '#code'
pm_code = '#code'
mm_code = '#code'
am_code = '#code'
pj_code = '#code'
```
- From line 93 to 121, is the function for each respective classes, the function inside of it contains the code variable of line 11 to 20 as argument.
```python
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
```
- From line 148 to 175, is the scheduling of Google Meets, you will need to repolace it with the time your meeting starts
```python
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
```
