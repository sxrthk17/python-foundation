import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os


url = "https://www.rocketstem.org/2015/04/23/the-top-100-images-of-the-universe-captured-by-the-hubble-space-telescope/?gad_source=1&gad_campaignid=294050895&gbraid=0AAAAADh7MOlb4kE3rHBR7YSDoEVP0ZUvs&gclid=Cj0KCQjwnIDUBhDrARIsAJDGwStnYBm0Rhgh85v-W8Ln3ARFzZ2xZsFosZL0PaNbqwbXSAzCzKETe28aApGtEALw_wcB"

headers= {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
"AppleWebKit/537.36 (KHTML, Like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

print("Fetching data fromt the URL...")
response = requests.get(url, headers=headers)

print(response.status_code)

## Step 2: Parsing the HTML and Finding Image tags
soup = BeautifulSoup(response.text,"html.parser")
img_tags = soup.find_all("img", class_="size-full")
print("Number of image tags found:", len(img_tags))

img_urls = []
for img in img_tags:
    extracted_url = img.get("data-orig-file") or img.get("src")

    if extracted_url:
        full_url = urljoin(url, extracted_url)
        img_urls.append(full_url)

print(img_urls[0])

folder_name = "hubble_images"
os.makedirs(folder_name, exist_ok=True)
nested_folder = "hubble_images/1_page"
os.makedirs(nested_folder, exist_ok=True)

for index, img_url in enumerate(img_urls):
    img_data = requests.get(img_url).content

    with open(f"hubble_images/1_page/image-{index}.jpg","wb") as f:
        f.write(img_data)

