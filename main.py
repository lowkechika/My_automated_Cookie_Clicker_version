from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.maximize_window()

driver.get('https://orteil.dashnet.org/cookieclicker//')

# cookie consent pop-up
consent = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]/p')
consent.click()

# choose language. English by default
lang = driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]')
lang.click()

# the store. I create a dict for later
store = driver.find_elements(By.XPATH, '/html[1]/body[1]/div[3]/div[5]/div[1]/div')

store_dict = {}
n = 0
for item in store:
    new_item = item.text.replace("Time machine", "Time_machine")
    latest_item = new_item.replace("Alchemy lab", "Alchemy_lab").split()
    if len(latest_item) > 1:
        prices = int(latest_item[2].replace(",", ""))
        product = latest_item[0]
        store_dict[n] = {
            'product_name': product,
            'cost': prices,
        }
        n += 1
our_data = store_dict

# here lies the cookie master
cookie = driver.find_element(By.XPATH, '//*[@id="bigCookie"]')

new_count = 0
store = driver.find_elements(By.XPATH, '/html/body/div[2]/div[2]/div[19]/div[3]/div[6]/div')
cursor = driver.find_element(By.XPATH, "//div[@id='product0']")
granny = driver.find_element(By.XPATH, "//div[@id='product1']")
farm = driver.find_element(By.XPATH, "//div[@id='product2']")

# zi loop. more below. so things don't make sense , ie locked printing... it kind of does though
timer = 0
while True:
    cursor = driver.find_element(By.XPATH, '//*[@id="product0"]')
    current_cookies = driver.find_element(By.XPATH, '//*[@id="cookies"]')
    cookies_count = int(current_cookies.text.split()[0].replace(",", ""))
    cookie.click()
    timer += 1
    product_list = []
    for x in store[1:5]:
        product = x.text.split()
        product_list.append(product)

        if '???' in product:
            print("locked")

    print(f"Number of cookies: {cookies_count}")
    cursor_cost = int(product_list[0][1].replace(",", ""))
    granny_cost = int(product_list[1][1].replace(",", ""))
    if len(product_list) > 5:
        farm_cost = int(product_list[2][1].replace(",", ""))
        next_1 = int(product_list[3][1].replace(",", ""))
        next_2 = int(product_list[4][1].replace(",", ""))
        if farm_cost <= cookies_count < 2000:
            farm.click()

    if cursor_cost <= cookies_count < 100:
        cursor.click()
    elif granny_cost <= cookies_count < 1100:
        granny.click()

# Make sure you open in full screen or else you'll have click problems. Trust me. It took me a while to figure
# this out
# the algorithm isn't finished yet. Feel free to twerk it as much as you want.

############################# HAVE FUN! #########################################
