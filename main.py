from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from collections import Counter


def get_video_urls():
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get("https://www.dailymotion.com/tseries2")
    time.sleep(5)  # Allow some time for the page to load

#     # Scroll and collect video URLs
#     video_urls = set()
#     scroll_pause_time = 2
#     max_scrolls = 50

#     for _ in range(max_scrolls):
#         videos = driver.find_elements(By.CSS_SELECTOR, 'a[data-xid]')
#         for video in videos:
#             video_urls.add(video.get_attribute('href'))
#             if len(video_urls) >= 500:
#                 break
#         if len(video_urls) >= 500:
#             break
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(scroll_pause_time)

#     driver.quit()
#     return list(video_urls)[:500]

# def extract_video_ids(video_urls):
#     video_ids = [url.split('/video/')[1] for url in video_urls if '/video/' in url]
#     return video_ids

# def most_frequent_char(video_ids):
#     all_chars = ''.join(video_ids)
#     char_counts = Counter(all_chars.lower())

#     most_common_char, count = min(char_counts.items(), key=lambda item: (-item[1], item[0]))
#     return most_common_char, count

# video_urls = get_video_urls()
# video_ids = extract_video_ids(video_urls)
# char, count = most_frequent_char(video_ids)
# print(f"{char}:{count}")