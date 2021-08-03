from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from pyvirtualdisplay import Display

display = Display(visible=0, size=(1024, 768))
display.start()

testid = 'a'
testpass ='aa'

with open('./config.txt','r') as f:
    testid = f.readline().rstrip('\n')
    testpass = f.readline().rstrip('\n')

options = Options();
options.add_argument("--disable-dev-shm-usage")
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome('/home/test/chromedriver', chrome_options=options)
URL='https://point.happylth.com/web/kddi/home'
URL2='https://hc-point-user.happylth.com/HealthPointFront/Team/Team'
URL3='https://point.happylth.com/web/kddi/login?p_p_id=58&p_p_lifecycle=0&_58_redirect=%2Fweb%2Fkddi%2Fhome'

driver.get(URL3)
sleep(1)

id = driver.find_element_by_id("_58_auth-id")
id.send_keys(testid)
password = driver.find_element_by_id("_58_auth-pass")
password.send_keys(testpass)

sleep(1)

driver.find_element_by_class_name('btn.btn-medium.btn-green.btn-normal-padding').click()

sleep(1)

driver.find_element_by_class_name('_bohccampaign_WAR_BOHCCampaignportlet_campaignBannerLink').click()
handle_array = driver.window_handles
driver.switch_to.window(handle_array[-1])

sleep(5)

driver.save_screenshot('screenshot.png')

sleep(5)

driver.close()
driver.quit()
