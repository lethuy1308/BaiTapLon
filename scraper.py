from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from bs4 import BeautifulSoup
import requests
from uuid import uuid4


def tao_driver():
    return webdriver.Chrome()

def lay_links_trong_trang(driver, so_trang):
    driver.get(f"https://vnexpress.net/cong-nghe/ai-p{so_trang}")
    time.sleep(2)
    links = driver.find_elements(By.CSS_SELECTOR, ".title-news a")
    return [link.get_attribute("href") for link in links]

def lay_hinh_anh(soup):
    hinh = soup.find('div', class_='fig-picture')
    if not hinh:
        return "Không có hình ảnh"
    return hinh.get('data-src') or hinh.find('img')['src'] if hinh.find('img') else "Không có hình ảnh"

def lay_thong_tin_bai_viet(url):
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.content, 'html.parser')

        tieu_de = soup.find('h1', class_='title-detail')
        tom_tat = soup.find('p', class_='description')
        noi_dung = soup.find('article', class_='fck_detail')

        return [
            tieu_de.text.strip() if tieu_de else "Không có tiêu đề",
            tom_tat.text.strip() if tom_tat else "",
            noi_dung.get_text(strip=True) if noi_dung else "",
            lay_hinh_anh(soup)
        ]
    except Exception as e:
        print(f"Lỗi: {url} - {e}")
        return ["Lỗi", "", "", ""]

def luu_excel(data):
    df = pd.DataFrame(data, columns=["Tiêu đề", "Tóm tắt", "Nội dung", "Hình ảnh"])
    df.to_excel(f"vnexpress_ai_{uuid4()}.xlsx", index=False)
