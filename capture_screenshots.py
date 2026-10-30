import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

output_dir = Path(r"C:\Users\Asus\.gemini\antigravity\scratch\AI-Assistant-for-data-Analyst\screenshots")
output_dir.mkdir(parents=True, exist_ok=True)

options = Options()
options.add_argument("--headless=new")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1366,880")

driver = webdriver.Chrome(options=options)

print("Navigating to http://localhost:8503...")
driver.get("http://localhost:8503")
time.sleep(5)  # Wait for Streamlit and Seaborn chart to render

# 1. Capture Full Overview & Metrics
save_p1 = output_dir / "screenshot_1_overview.png"
driver.save_screenshot(str(save_p1))
print(f"Captured screenshot_1_overview.png: {save_p1.stat().st_size:,} bytes")

# 2. Scroll down to show the Chat & Seaborn Chart
driver.execute_script("window.scrollTo(0, 480);")
time.sleep(2)
save_p2 = output_dir / "screenshot_2_chat_chart.png"
driver.save_screenshot(str(save_p2))
print(f"Captured screenshot_2_chat_chart.png: {save_p2.stat().st_size:,} bytes")

# 3. Scroll down further to show full chart and input
driver.execute_script("window.scrollTo(0, 750);")
time.sleep(2)
save_p3 = output_dir / "screenshot_3_full_chart.png"
driver.save_screenshot(str(save_p3))
print(f"Captured screenshot_3_full_chart.png: {save_p3.stat().st_size:,} bytes")

# 4. Scroll to top with sidebar focused
driver.execute_script("window.scrollTo(0, 0);")
time.sleep(1)
save_p4 = output_dir / "screenshot_4_data_hub.png"
driver.save_screenshot(str(save_p4))
print(f"Captured screenshot_4_data_hub.png: {save_p4.stat().st_size:,} bytes")

driver.quit()
print("All screenshots successfully captured!")

