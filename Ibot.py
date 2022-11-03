import time
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from auth import user, passwd

userid = user
passwd =  passwd


d = DesiredCapabilities.CHROME
d['goog:loggingPrefs'] = { 'performance':'ALL' }
 # to open the chromebrowser 
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_experimental_option('w3c', True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(desired_capabilities=d, options=chrome_options)



driver.get("https://www.instagram.com/")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "div._ab32:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)").send_keys(userid)
driver.find_element(By.CSS_SELECTOR, "div._ab32:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)").send_keys(passwd)
driver.find_element(By.CSS_SELECTOR, "div._abak:nth-child(3)").click()

time.sleep(10)
s = driver.get_log("performance")
s = str(s).split(',')
with open('session.txt','w') as kz:
    for m in s:
        if 'sessionid' in m:
            m = m.split('Secure')
            p = str(m).split('=')
            print(p,file=kz)
            print(p)

pz = []
with open('session.txt','r') as l:
    for mz in l:
        mz = mz.split(']')
        pz.append(mz)

for sm in pz[7:10]:
    sm = str(sm).split(',')
    if '%' in sm[4]:
        imp = sm[4]
        sz = imp[3:]
        (f,s) = str(sz).split(';')
        print(f)
