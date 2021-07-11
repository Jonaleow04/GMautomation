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
```python
yourname@gmail.com
yourpassword
```
- Now open up gmautomation.py
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
- From line 117 to 144, is the scheduling of Google Meets, you will need to replace it with the time your meeting starts
```python
    #monday class
    schedule.every().monday.at('07:30').do(login, bio_code)
    schedule.every().monday.at('09:02').do(login, bm_code)
    schedule.every().monday.at('12:30').do(login, phy_code)
```
- You may run the program itself on an idle, or else you may run the program according to the following steps
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
