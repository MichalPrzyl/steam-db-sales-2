from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


options = Options()
options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                        #   options=options)
driver = webdriver.Chrome(options=options)

url = 'https://steamdb.info/sales/'
driver.get(url)

select_box_id = 'dt-length-0'
select_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, select_box_id))
)

select = Select(select_box)
select.select_by_visible_text("5K")
print(f"select_box: {select_box}")


# links = driver.find_elements("xpath", "//a[@href]")
# # for link in links:
#     # print(link)
#     # print(100*'-')
# skip_inner_htmls = [
#     "<img",
#     "<svg"
# ]
# for link in links:
#     # Skip hrefs with images
#     if any([skip in link.get_attribute("innerHTML") for skip in skip_inner_htmls]):
#         continue

#     print(f"{link.get_attribute('innerHTML')}")

#     if " Price" in link.get_attribute("innerHTML"):
#         print(f"Found Price in link")
#         link.click()
#         break