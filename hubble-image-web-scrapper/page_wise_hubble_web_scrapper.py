import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import time


# url = "https://www.rocketstem.org/2015/04/23/the-top-100-images-of-the-universe-captured-by-the-hubble-space-telescope/?gad_source=1&gad_campaignid=294050895&gbraid=0AAAAADh7MOlb4kE3rHBR7YSDoEVP0ZUvs&gclid=Cj0KCQjwnIDUBhDrARIsAJDGwStnYBm0Rhgh85v-W8Ln3ARFzZ2xZsFosZL0PaNbqwbXSAzCzKETe28aApGtEALw_wcB"

headers= {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
"AppleWebKit/537.36 (KHTML, Like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

# print("Fetching data fromt the URL...")
# response = requests.get(url, headers=headers)

for page_no in range(1,4):
    if page_no == 1:
        url = "https://www.rocketstem.org/2015/04/23/the-top-100-images-of-the-universe-captured-by-the-hubble-space-telescope/"
        print("Fetching data fromt the URL...")

        response = requests.get(url, headers=headers)

        print(response.status_code)
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

                folder_name = f"hubble_images/{page_no}_page"
                os.makedirs(folder_name, exist_ok=True)

                for index, img_url in enumerate(img_urls):
                    img_data = requests.get(img_url).content

                    with open(f"hubble_images/{page_no}_page/image-{index}.jpg","wb") as f:
                        f.write(img_data)




    else:
        url = f"https://www.rocketstem.org/2015/04/23/the-top-100-images-of-the-universe-captured-by-the-hubble-space-telescope/{page_no}/"
        print("Fetching data fromt the URL...")
        time.sleep(1)
        response = requests.get(url, headers=headers)

        print(response.status_code)
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

                folder_name = f"hubble_images/{page_no}_page"
                os.makedirs(folder_name, exist_ok=True)

                for index, img_url in enumerate(img_urls):
                    img_data = requests.get(img_url).content

                    with open(f"hubble_images/{page_no}_page/image-{index}.jpg","wb") as f:
                        f.write(img_data)
        time.sleep(1)

print("Yayy, one project done, curiosity get's you to the places you never dreamt of, Proud of you SarthakM, sxrthk17")



# How to start from where you haves topped
