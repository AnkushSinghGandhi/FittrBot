from selenium import webdriver
from selenium.webdriver import ActionChains
import pyautogui
import time

driver = webdriver.Chrome()

driver.get("https://www.fittr.com/dashboard/home/social/all")

email = input("Enter email to sign in : ")

#password = input("Enter password")
#profile = input("Enter profile link")

# add post
add_post = driver.find_element_by_css_selector(".addpost_btn")
add_post.click()
time.sleep(2)

# recipie button
recipe = driver.find_element_by_xpath('/html/body/div[3]/div[3]/div[2]/main/div[1]/div[1]/div/nav/div[3]/div/div/div/div[2]/span[3]')
recipe.click()
time.sleep(1)
#pyautogui.click(472, 290)

# image upload
imageupload = driver.find_element_by_xpath("//input[@type='file']")
imageupload.send_keys("/home/ankush/Downloads/download.jpeg")

# recipe name
recipename = driver.find_elements_by_id("outlined-dense")[0]
recipename.send_keys("Egg Salad")

# recipe type
recipetype = driver.find_elements_by_id("mui-component-select-recipe_type")[0]
recipetype.click()
time.sleep(1)
pyautogui.click(598, 788)
time.sleep(1)

# region
#region = driver.find_elements_by_xpath('/html/body/div[3]/div[3]/div[2]/main/div[1]/div[1]/div/nav/div[3]/div/div/div/div[3]/div/form/div[4]/div[1]/div/div/div/div')[0]
#region.click()
pyautogui.click(293, 850)
time.sleep(1)
pyautogui.click(284, 811)

# time
timet = driver.find_element_by_xpath('/html/body/div[3]/div[3]/div[2]/main/div[1]/div[1]/div/nav/div[3]/div/div/div/div[3]/div/form/div[4]/div[2]/div/div/div/div/div/input')
time.sleep(1)
timet.send_keys("0012")

# protien
protien = driver.find_elements_by_id("outlined-dense")[1]
protien.send_keys("13")

# carbs
carbs = driver.find_elements_by_id("outlined-dense")[2]
carbs.send_keys("10")

# fats
fats = driver.find_elements_by_id("outlined-dense")[3]
fats.send_keys("7")

# ingredients
ingredients = driver.find_elements_by_id("outlined-dense")[4]
ingredients.send_keys("eggs, dill, chives, celery and onion in creamy garlic mayo")

# directions
directions = driver.find_elements_by_id("outlined-dense")[5]
directions.send_keys("1) Hard boil eggs on the stovetop or in the instant pot and cool. Once cooled, cut into desired pieces (we like ours chunky) 2) Finely cube the celery and red onion (sweet onion may be substituted for red onion)")

# post
post = driver.find_element_by_xpath('//*[@id="post-wrapper-sidebar"]/div/div/div[3]/div/form/div[7]/button')
time.sleep(4)
post.click()


