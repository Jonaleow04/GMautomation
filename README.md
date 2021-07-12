# Chrome GMautomation
# Table of Contents
1. [General Information](#general-information)
2. [Setup](#setup)
3. [Usage](#usage)
4. [References](#references)
5. [Improvements](#improvements)

## General Information
- This Python program will open up Chrome and log into your scheduled Google Meet with camera and mic turned off.
- The web automation is made using the selenium module with ChromeDriver and the scheduling is made using the schedule module
- An idea popped up in my head when entering my school's online class, that is 'What if I can automate all these entering the code process'. Thus, Chrome GMautomation was born.

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
- Open up the config.json file
- Replace the data with your own data
```json
{
    "email": " ",
    "password": " ",
    "bm_code": " ",
    "eng_code": " ",
    "cn_code": " ",
    "phy_code": " ",
    "bio_code": " ",
    "sej_code": " ",
    "pm_code": " ",
    "mm_code": " ",
    "am_code": " ",
    "pj_code": " "
}
```
- Now open up gmautomation.py
- From line 104 to 108, you will need to replace the data with your own data
```python
#scheduling
monday_class = [('07:30', 'bio_code'), ('09:00', 'bm_code'), ('12:30', 'phy_code')]
tuesday_class = [('08:00', 'pj_code'), ('10:30', 'am_code'), ('11:30', 'mm_code')] 
wednesday_class = [('07:30', 'pm_code'), ('08:30', 'bm_code'), ('11:30', 'phy_code'), ('12:30', 'eng_code')]
thursday_class = [('07:30', 'bio_code'), ('09:00', 'am_code'), ('10:30', 'cn_code'), ('11:30', 'pm_code')]
friday_class = [('07:30', 'sej_code'), ('08:30', 'eng_code'), ('10:30', 'mm_code'), ('11:30', 'pm_code')]
```
- Go to line 95 and input the path of your chromedriver.exe
```python
driver = webdriver.Chrome(options=opt, executable_path=r'#your chromedriver.exe path')
```
- You may run the program itself on an IDE, or else you may run the program according to the following steps
- Open up command prompt and direct it to the Python program's path
- Type the following and press enter
```bash
python gmautomation.py
```


## References
- https://selenium-python.readthedocs.io
- https://schedule.readthedocs.io/en/stable/


## Improvements
### Update 1:
- Got rid of separate function for each class and improved the scheduling code as suggested by u/17291 on reddit
- Migrated data to config.json file as suggested by u/mikerahk on reddit

### Update 2:
- Reduced the syntax noises by implementing the mapping concept for the scheduling section as suggested by u/ElevenPhonons on reddit
