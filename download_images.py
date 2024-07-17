import os
import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

def fetch_images(url, target_folder):
    # 確保目標資料夾存在
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # 獲取網頁內容
    response = requests.get(url)
    response.raise_for_status()  # 確保網頁正確響應
    soup = BeautifulSoup(response.text, 'html.parser')# 解析 HTML

    # 尋找所有圖片標籤
    images = soup.find_all('img')

    # 下載每個圖片
    for img in images:
        # 使用 img 標籤中的 'zoomfile' 屬性作為圖片來源
        img_url = img.get('zoomfile')
        if img_url:
            try:
                img_data = requests.get(img_url).content
                img_name = os.path.basename(img_url)
                img_path = os.path.join(target_folder, img_name)
                with open(img_path, 'wb') as file:
                    file.write(img_data)
                print(f"Saved {img_name}")
            except Exception as e:
                print(f"Error downloading {img_url}: {e}")

url = 'url'  # 目標網站 URL
target_folder = '/Users/yenhung/Downloads/'  # 本地保存目標資料夾

fetch_images(url, target_folder)
