import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

output_dir = Path(r"C:\Users\Asus\.gemini\antigravity\scratch\AI-Assistant-for-data-Analyst\screenshots")

options = Options()
options.add_argument("--headless=new")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--window-size=1366,880")

driver = webdriver.Chrome(options=options)
driver.get("http://localhost:8503")
time.sleep(3)

# 1. Click "Remove Duplicates" to show cleaning alert
buttons = driver.find_elements(By.TAG_NAME, "button")
for btn in buttons:
    if "Remove Duplicates" in btn.text:
        btn.click()
        break
time.sleep(2)
driver.save_screenshot(str(output_dir / "screenshot_cleaning_action.png"))

# 2. Type "Show correlation heatmap" into chat input
inputs = driver.find_elements(By.TAG_NAME, "input")
for inp in inputs:
    placeholder = inp.get_attribute("placeholder") or ""
    if "E.g." in placeholder or "Ask" in placeholder or "summary" in placeholder:
        inp.send_keys("Show correlation heatmap")
        inp.send_keys(Keys.ENTER)
        break
time.sleep(3)

# Scroll down to capture the newly generated heatmap
driver.execute_script("window.scrollTo(0, 900);")
time.sleep(1)
driver.save_screenshot(str(output_dir / "screenshot_correlation_heatmap.png"))

driver.quit()
print("Interactive cleaning and correlation heatmap screenshots captured!")

