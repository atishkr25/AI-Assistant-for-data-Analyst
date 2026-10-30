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

targets = [
    ("screenshot_1_overview.png", "http://localhost:8503/?view=overview"),
    ("screenshot_2_cleaning.png", "http://localhost:8503/?view=cleaning"),
    ("screenshot_3_salary_chart.png", "http://localhost:8503/?view=salary_chart"),
    ("screenshot_4_stats.png", "http://localhost:8503/?view=stats"),
    ("screenshot_5_correlation.png", "http://localhost:8503/?view=correlation"),
    ("screenshot_6_scatter.png", "http://localhost:8503/?view=scatter"),
]

print("Starting distinct screenshot capture for AI-Assistant-for-data-Analyst...")

for filename, url in targets:
    driver.get(url)
    time.sleep(3.5)  # Wait for Streamlit, tables, and Seaborn charts to render
    save_path = output_dir / filename
    driver.save_screenshot(str(save_path))
    print(f"Captured {filename}: {save_path.stat().st_size:,} bytes")

driver.quit()
print("All 6 distinct screenshots captured successfully!")
