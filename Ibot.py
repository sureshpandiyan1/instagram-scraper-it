import time
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from auth import user, passwd

userid = user
passwd =  passwd


d = DesiredCapabilities.CHROME
d['loggingPrefs'] = { 'performance':'ALL' }
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_experimental_option('w3c', False)
driver = webdriver.Chrome(desired_capabilities=d, options=chrome_options)


driver.get("https://www.instagram.com/")
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input").send_keys(userid)
driver.find_element(By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input").send_keys(passwd)
driver.find_element(By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button").click()

time.sleep(10)
s = driver.get_log("performance")
s = str(s).split(',')
with open('session.txt','w') as kz:
    for m in s:
        if 'sessionid' in m:
            m = m.split('Secure')
            p = str(m).split('=')
            print(p,file=kz)

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
