from selenium import webdriver 
from datetime import datetime
import time 
# webdriver path set 
browser = webdriver.Chrome("chromedriver.exe") 

browser.maximize_window() 

browser.get('https://techmill.keka.com') 

time.sleep(3) 

username = "yourname@company.com"
password = "***********"



# username send 
a = browser.find_element_by_xpath("//input[@id ='email']") 
a.send_keys(username) 

# password send 
b = browser.find_element_by_xpath("//input[@id ='password']") 
b.send_keys(password) 

# submit button clicked 


browser.find_element_by_xpath("//*[@id='login-container-center']/div/div/form/div/div[4]/div/button[1]").click()


print('Login Successful') 
time.sleep(10)

currentTime = datetime.now()

print("Current time is ",currentTime.hour)

if currentTime.hour >= 9 and currentTime.hour < 10:
    #web clock-in
    print("let's get the day started and let's clock in")
    browser.find_element_by_xpath("/html/body/xhr-app-root/div/xhr-home/div/home-dashboard/div/div/div/div[1]/div[2]/div/div[2]/div[5]/home-attendance-clockin-widget/div/div[1]/div/div[1]/div/div[2]/div[1]/button").click()
    time.sleep(2)
    reasonbox = browser.find_element_by_xpath("/html/body/modal-container/div/div/xhr-confirm-dialog/div[2]/form/div/textarea")
    if(reasonbox):
        reasonbox.send_keys("wfh")
        browser.find_element_by_xpath("/html/body/modal-container/div/div/xhr-confirm-dialog/div[3]/button[2]").click()
    print("sucessfully clocked in")
    time.sleep(2)
    browser.close()
elif currentTime.hour >= 18 and currentTime.hour< 23:
    print("Now its time to clockout")

    
    browser.find_element_by_xpath("/html/body/xhr-app-root/div/xhr-home/div/home-dashboard/div/div/div/div[1]/div[2]/div/div[2]/div[5]/home-attendance-clockin-widget/div/div[1]/div/div[1]/div/div[2]/div[1]/button").click()
    time.sleep(2)
    browser.find_element_by_xpath("/html/body/xhr-app-root/div/xhr-home/div/home-dashboard/div/div/div/div[1]/div[2]/div/div[2]/div[5]/home-attendance-clockin-widget/div/div[1]/div/div[1]/div/div[2]/div/div[1]/button[1]").click()
    print("sucessfully clocked out")
    time.sleep(5)
    browser.close()

else:
    print("you are out of your mind")
