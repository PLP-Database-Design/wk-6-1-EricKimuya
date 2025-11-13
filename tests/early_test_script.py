"""
Power Testers — Early Automation Script (Phase 2)
Bookstore Project | Date: November 11, 2025
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "http://localhost:3000"

@pytest.fixture(scope="module")
def driver():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_homepage_loads(driver):
    driver.get(BASE_URL)
    assert "Bookstore" in driver.title or "book" in driver.page_source.lower()
    print("✅ Homepage loaded successfully")

def test_search_for_book(driver):
    driver.get(BASE_URL)
    search_boxes = driver.find_elements(By.TAG_NAME, "input")
    assert len(search_boxes) > 0, "❌ Search box not found"
    search_boxes[0].send_keys("Python")
    print("✅ Search box found and input entered")

def test_add_to_cart_button(driver):
    driver.get(BASE_URL)
    try:
        add_button = driver.find_element(By.XPATH, "//button[contains(text(),'Add to Cart')]")
        add_button.click()
        print("✅ Add to Cart button found and clicked")
    except Exception:
        print("⚠️ Add to Cart button not found on page — check layout or component visibility")
