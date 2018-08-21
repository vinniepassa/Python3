from selenium import webdriver

driver = webdriver.Chrome()

url_1 = 'https://babel.hathitrust.org/cgi/imgsrv/image?id=uc1.b4373047;seq='
url_2 = ';width=850'

for i in range(1, 217):
    i = str(i)
    driver.get(url_1+i+url_2)
    filename = i+'.png'
    driver.save_screenshot(filename)
