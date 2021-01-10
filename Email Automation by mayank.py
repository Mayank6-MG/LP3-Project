from selenium import webdriver
from time import sleep
driver = webdriver.Chrome("C:\\Users\\MAYANK\\Downloads\\New folder (2)\\chromedriver_win32\\chromedriver.exe")
driver.get("http://www.google.com")
sleep(10)
#-----------Clicking on the Signin button
element = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/div[2]/div[2]/div/a")
element.click()

#----------Filling id in the vacant block
user=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
user.click()
user.send_keys('itvii50@rgcer.edu.in')
btn=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]")
btn.click()

#---------taking sleep
sleep(5)

#---------------filing password
user1=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
user1.click()
user1.send_keys('PAss@1999')

#----------Clicking on login button
btn1=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]")
btn1.click()

sleep(5)

gm=driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/div[1]/div[1]/a")
gm.click()

sleep(20)

#no=driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[1]/div[4]/div[1]/div/div[3]/div/div/div[2]/span[2]/span[2]")
#no.click()

customize=driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div")
customize.click()


to=driver.find_element_by_xpath("/html/body/div[20]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/form/div[1]/table/tbody/tr[1]/td[2]/div/div/textarea")
to.click()
to.send_keys('itvii50@rgcer.edu.in')
#to.click()

sleep(3)

sub=driver.find_element_by_xpath("/html/body/div[20]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/form/div[3]/div/input")
sub.click()
sub.send_keys('New Offer from Learninstudy.com')

sleep(3)

text=driver.find_element_by_xpath("/html/body/div[20]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[1]/td/div/div[1]/div[2]/div[1]/div/table/tbody/tr/td[2]/div[2]/div")
text.click()
text.send_keys("Hello.....")

sleep(3)

submi=driver.find_element_by_xpath("/html/body/div[20]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/div/div[4]/table/tbody/tr/td[1]/div/div[2]/div[1]")
submi.click()
#/html/body/div[20]/div/div/div/div[1]/div[3]/div[1]/div[1]/div/div/div/div[3]/div/div/div[4]/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/div/div[4]/table/tbody/tr/td[1]/div/div[2]/div[1]
#element.send_keys("toys")
#element.submit()


#driver.close()