# Import required Selenium libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time

# ================================
# Launch Chrome Browser
# ================================
driver = webdriver.Chrome()
driver.maximize_window()    # Maximize browser window

driver.implicitly_wait(30)  # Implicit wait (Same as your Java code - 20 seconds)

driver.get("https://dev.octopussaas.com/auth") # Open application URL


# ================================
# ========== LOGIN ==============
# ================================

# Enter Email
driver.find_element(By.ID, "login-email").send_keys("henry@test.com")

# Enter Password
driver.find_element(By.ID, "login-password").send_keys("Nayan123!@")

# Click Login button
driver.find_element(By.XPATH, "//button[text()='Log In']").click()

print("====== login done ======")


# ================================
# ===== ADD NEW GENERATOR  ======
# ================================

# Click on Add New
driver.find_element(By.XPATH, "//h6[text()='Add New']").click()
time.sleep(2)

# Select Generator option
driver.find_element(By.XPATH, "//li[text()='Generator']").click()

# Enter Generator Name
driver.find_element(By.XPATH,"//input[@type='text' and @placeholder='Enter generator name']").send_keys("Nisha N.B")

# Enter Internal Account Number
driver.find_element(By.XPATH,
                    "//input[@type='text' and @placeholder='Enter internal account number']").send_keys(
    "321963741852")

# Submit Generator form
driver.find_element(By.XPATH, "//button[@type='submit']").submit()
time.sleep(2)


# ===================================
# =====FILL BILLING INFORMATION =====
# ===================================

# Select Industry
driver.find_element(By.XPATH, "//input[@placeholder='Select Industry Type']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//span[text()='Urgent Care Clinics']").click()
time.sleep(2)

# Enter Street Address
driver.find_element(By.XPATH,
                    "//input[@id='serviceAddress-street' and @type='text']").send_keys("Mahisbathan Salt lake sector V")

time.sleep(2)
# Enter City
driver.find_element(By.XPATH,
                    "//input[@placeholder='City' and @id='serviceAddress-city']").send_keys("kolkata")
time.sleep(2)
# Select State
driver.find_element(By.XPATH,
                    "//input[@placeholder='Select State' and @id='serviceAddress-state']").click()
driver.find_element(By.XPATH, "//span[text()='IN']").click()
time.sleep(2)


# Enter ZIP Code
driver.find_element(By.XPATH,
                    "//input[@placeholder='ZIP Code' and @id='serviceAddress-zipCode']").send_keys("700102")


# Enter Email
time.sleep(2)
driver.find_element(By.XPATH,
                    "//input[@placeholder='Email Address' and @id='serviceAddress-email']").send_keys( "nisha@gmail.com")

# Enter Phone Number
time.sleep(2)
driver.find_element(By.XPATH,
                    "//input[@id='serviceAddress-phone' and @placeholder='(123) 456-7890']").send_keys("8597124181")

time.sleep(2)

# Copy to Billing Address
driver.find_element(By.XPATH,
                    "//button[@type='button' and @class='enabled:hover:text-primary']").click()
time.sleep(2)


# ================================
# ===== LATITUDE & LONGITUDE ====
# ================================

# Click Edit Position On Map
driver.find_element(By.XPATH, "//button[text()='Edit Position On Map']").click()

time.sleep(2)

# Enter Latitude
latitude = driver.find_element(By.XPATH, "(//input[@type='number'])[1]")
latitude.send_keys("22.57")

time.sleep(2)
# Enter Longitude
longitude = driver.find_element(By.XPATH, "(//input[@type='number'])[2]")
longitude.send_keys("88.27")

time.sleep(2)
# Verify Latitude field is displayed
if latitude.is_displayed():
    print("====== latitude verified successfully ======")

time.sleep(2)
# Verify Longitude field is displayed
if longitude.is_displayed():
    print("====== longitude verified successfully ======")

time.sleep(2)
# Click Update Address
driver.find_element(By.XPATH, "//button[text()='Update Address']").click()


# ================================
# ===== SERVICE HOURS ===========
# ================================

# Select Monday Opening Time
driver.find_element(By.XPATH,
                    "//input[@placeholder='Monday Opening Time']").click()
driver.find_element(By.XPATH, "//span[text()='10:00 AM']").click()

# Select Monday Lunch Start Time
driver.find_element(By.XPATH,
                    "//input[@placeholder='Monday Lunch Start Time']").click()
driver.find_element(By.XPATH, "//span[text()='1:00 PM']").click()

# Select Monday Lunch End Time
driver.find_element(By.XPATH,
                    "//input[@placeholder='Monday Lunch End Time']").click()
driver.find_element(By.XPATH, "//span[text()='2:00 PM']").click()

# Select Monday Closing Time
driver.find_element(By.XPATH,
                    "//input[@placeholder='Monday Closing Time']").click()
driver.find_element(By.XPATH, "//span[text()='5:00 PM']").click()

# -------Copy Monday timings--------

driver.find_element(By.XPATH,
                    "(//span[@class='w-1/4 flex items-center justify-center'])[1]").click()

# Paste timings to other days
driver.find_element(By.XPATH,
                    "(//span[@class='w-1/4 flex items-center justify-center'])[2]").click()
driver.find_element(By.XPATH,
                    "(//span[@class='w-1/4 flex items-center justify-center'])[3]").click()
driver.find_element(By.XPATH,
                    "(//span[@class='w-1/4 flex items-center justify-center'])[4]").click()
driver.find_element(By.XPATH,
                    "(//span[@class='w-1/4 flex items-center justify-center'])[5]").click()

# Close Saturday & Sunday
driver.find_element(By.XPATH,
                    "(//div[contains(@class,'cursor-pointer min-w-[26px]')])[6]").click()
driver.find_element(By.XPATH,
                    "(//div[contains(@class,'cursor-pointer min-w-[26px]')])[7]").click()


# Click 3 dots menu
driver.find_element(By.XPATH, "//button[text()='...']").click()

print("generator created")

# ================================
# ===== ROUTE ASSIGNMENT ========
# ================================

# Click Route Assignment
driver.find_element(By.XPATH, "//button[text()='Route Assignment']").click()

# Use ActionChains
actions = ActionChains(driver)
button = driver.find_element(By.XPATH,
                             "(//button[text()='Go Back to Generator Profile'])[1]")
actions.click(button).perform()

time.sleep(2)

# Select first checkbox
driver.find_element(By.XPATH,
                    "(//div[contains(@class,'cursor-pointer min-w-[26px] min-h-[26px] border-2')])[1]").click()
time.sleep(3)

# Confirm Yes
driver.find_element(By.XPATH, "//button[text()='Yes']").click()



# Open 3 dots again
time.sleep(15)
driver.find_element(By.XPATH, "//button[text()='...']").click()


# Click Route Assignment again
time.sleep(10)
driver.find_element(By.XPATH, "//button[text()='Route Assignment']").click()


# Click Add a Service
time.sleep(10)
driver.find_element(By.XPATH, "//span[text()='Add a Service']").click()


# ================================
# ===== ADD SERVICE DETAILS =====
# ================================


# Select Route
time.sleep(15)
driver.find_element(By.ID, "route").click()

time.sleep(15)
# Click the route option from dropdown
driver.find_element(By.XPATH, "//div[text()='Nisha route']").click()
time.sleep(15)

# Select Service Type
driver.find_element(By.XPATH, "//button[@id='service-input-0']").click()
driver.find_element(By.XPATH, "//div[text()='Medical Waste']").click()
time.sleep(2)


# Select Date from Calendar
driver.find_element(By.XPATH,
                    "//div[@class='react-datepicker__input-container']").click()
driver.find_element(By.XPATH, "//div[text()='28']").click()


# Select Service Frequency
driver.find_element(By.XPATH,
                    "//span[text()='Service Frequency']").click()

# Select "Multiple Times Weekly (MTW)"
driver.find_element(By.XPATH, "//div[text()='Multiple Times Weekly (MTW)']").click()
time.sleep(2)

# ---- Click Select Weekdays dropdown ----
driver.find_element(By.XPATH, "//span[text()='Select Weekdays']").click()
time.sleep(15)

check1 = driver.find_element(By.XPATH, "(//input[@class='mr-2'])[4]")
actions.move_to_element(check1).click().perform()
check2 = driver.find_element(By.XPATH, "(//input[@class='mr-2'])[5]")
actions.move_to_element(check2).click().perform()
check3 = driver.find_element(By.XPATH, "(//input[@class='mr-2'])[6]")
actions.move_to_element(check3).click().perform()
check4 = driver.find_element(By.XPATH, "(//input[@class='mr-2'])[7]")
actions.move_to_element(check4).click().perform()

# Choose a specific date
time.sleep(10)
driver.find_element(By.TAG_NAME, "body").click()
time.sleep(2)

# Now click the date field
driver.find_element(By.XPATH, "//div[contains(@class,'bg-inputBg rounded-full h-9 text-cardTextGray')]").click()

#driver.find_element(By.XPATH, "//div[contains(@class,'bg-inputBg rounded-full h-9 text-cardTextGray')]").click()

time.sleep(10)
driver.find_element(By.XPATH, "//div[@aria-label='Choose Saturday, February 21st, 2026']").click()
time.sleep(10)
# Select Service Type
driver.find_element(By.XPATH, "//button[@id='service-input-0']").click()
driver.find_element(By.XPATH, "//div[text()='Medical Waste']").click()
time.sleep(3)

# Set Scope of Work (SOW)
driver.find_element(By.XPATH, "(//span[text()='Scope Of Work (SOW)'])[2]").click()
driver.find_element(By.XPATH, "(//input[@type='checkbox' and @class='mr-2'])[4]").click()
driver.find_element(By.XPATH, "(//input[@type='checkbox' and @class='mr-2'])[5]").click()

# Remove extra items if needed
# Close any open dropdown first
driver.find_element(By.TAG_NAME, "body").click()
time.sleep(1)

for i in range(4):
    try:
        remove_btn = driver.find_element(
            By.XPATH,
            "(//button[contains(@class,'absolute right-2 top-1')])[1]"
        )

        # Scroll into view
        driver.execute_script("arguments[0].scrollIntoView(true);", remove_btn)
        time.sleep(1)

        # Use JavaScript click (prevents intercept error)
        driver.execute_script("arguments[0].click();", remove_btn)
        time.sleep(1)

    except:
        break

# Add service to route
driver.find_element(By.XPATH, "//button[text()='Add to Route']").click()
print("Successfull 4")
time.sleep(2)

# -----------------------
# Price Book
# -----------------------

from selenium.webdriver.common.keys import Keys

# Open Price Book
time.sleep(20)
driver.find_element(By.XPATH, "//button[text()='...']").click()
time.sleep(10)

# -----------------------
# Price Book Section
# -----------------------

# Click on Price Book link
# Find all links in the dropdown
dropdown_links = driver.find_elements(By.XPATH, "//div[@role='menu']//a")

# Loop through links and click Price Book
for link in dropdown_links:
    if "Price Book" in link.text:
        link.click()
        print("Price Book clicked")
        break

time.sleep(20)
# Click the toggle button
#driver.find_element(By.XPATH, "//button[@class='bg-[#898989] z-0 relative flex items-center h-7 w-[49px] rounded-full transition-colors focus:outline-none cursor-pointer']").click()

# Click the toggle button (more robust XPath)
toggle_button = driver.find_element(
    By.XPATH, "//button[contains(@class,'rounded-full') and contains(@class,'cursor-pointer')]"
)
toggle_button.click()
print("Price Book toggle clicked successfully")

time.sleep(10)
# Click Yes to confirm
driver.find_element(By.XPATH, "//button[contains(@class,'btn-primary') and text()='Yes']").click()

# Wait for 3 seconds
time.sleep(10)

# Update SP1 price
SP1 = driver.find_element(By.XPATH, "(//input[@class='bg-transparent text-sm text-gray-700 w-full pl-1 outline-none '])[265]")
SP1.click()
SP1.send_keys(Keys.CONTROL + "a")
SP1.send_keys(Keys.DELETE)
SP1.send_keys("13.35")

# Update SP2 price
SP2 = driver.find_element(By.XPATH, "(//input[@class='bg-transparent text-sm text-gray-700 w-full pl-1 outline-none '])[268]")
SP2.click()
SP2.send_keys(Keys.CONTROL + "a")
SP2.send_keys(Keys.DELETE)
SP2.send_keys("17.35")

print("Successful 5")
time.sleep(2)

# -----------------------
# Logout Section
# -----------------------

# Click profile image
driver.find_element(By.XPATH, "//img[@class='rounded-full w-full h-full object-cover']").click()

# Click Logout
driver.find_element(By.XPATH, "//button[text()='Logout']").click()

print("Successful 6")
time.sleep(2)

# Close browser
driver.quit()