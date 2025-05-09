import requests
from bs4 import BeautifulSoup
import csv
import datetime

def collect_data():
    print("Chọn tỉnh/thành phố:")
    print("1: Ha Noi")
    print("2: Ho Chi Minh")
    print("3: Da Nang")
    province_choice = int(input("Nhập số tương ứng: "))

    print("Chọn loại nhà đất:")
    print("1: Nha")
    print("2: Can Ho Chung Cu")
    print("3: Dat")
    property_choice = int(input("Nhập số tương ứng: "))

    province_map = {
        1: {"code": "1", "name": "ha-noi"},
        2: {"code": "2", "name": "ho-chi-minh"},
        3: {"code": "3", "name": "da-nang"}
    }

    property_map = {
        1: "nha-dat",
        2: "can-ho-chung-cu",
        3: "dat-tho-cu-dat-o"
    }

    province = province_map.get(province_choice, {"code": "1", "name": "ha-noi"})
    property_type = property_map.get(property_choice, "nha-dat")

    today = datetime.datetime.now().strftime("%Y-%m-%d")
    filename = f"alonhadat_{province['name']}_{property_type}_{today}.csv"

    data = []
    page = 1

    while True:
        if page == 1:
            url = f"https://alonhadat.com.vn/nha-dat/can-ban/{property_type}/{province['code']}/{province['name']}.html"
        else:
            url = f"https://alonhadat.com.vn/nha-dat/can-ban/{property_type}/{province['code']}/{province['name']}/trang--{page}.html"

        print(f"Đang thu thập dữ liệu từ trang {page}: {url}")

        try:
            response = requests.get(url, timeout=10)
            if response.status_code != 200:
                print(f"Lỗi: không thể truy cập {url}")
                break

            soup = BeautifulSoup(response.text, 'html.parser')
            listings = soup.select('div.ct_title')

            if not listings:
                print("Không có bài viết trên trang này.")
                break

            for listing in listings:
                title = listing.get_text(strip=True)
                description = listing.find_next('div', class_='ct_desc')
                address = listing.find_next('div', class_='ct_location')
                area = listing.find_next('div', class_='ct_area')
                price = listing.find_next('div', class_='ct_price')

                description_text = description.get_text(strip=True) if description else ""
                address_text = address.get_text(strip=True) if address else ""
                area_text = area.get_text(strip=True) if area else ""
                price_text = price.get_text(strip=True) if price else ""

                data.append([title, description_text, address_text, area_text, price_text])

            page += 1

        except requests.exceptions.RequestException as e:
            print(f"Đã xảy ra lỗi khi gửi yêu cầu: {e}")
            break

    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Tiêu đề", "Mô tả", "Địa chỉ", "Diện tích", "Giá"])
        writer.writerows(data)

    print(f"Dữ liệu đã được lưu vào file {filename}")

collect_data()
    