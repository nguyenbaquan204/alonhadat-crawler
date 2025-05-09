import requests
from bs4 import BeautifulSoup
from danhsach import cities
import csv
import datetime

def collect_data():
    # In danh sách tỉnh/thành phố
    print("Chọn tỉnh/thành phố:")
    for i, city in enumerate(cities, 1):
        print(f"{i}: {city['name'].replace('-', ' ').title()}")

    try:
        province_choice = int(input("Nhập số tương ứng: "))
        if province_choice < 1 or province_choice > len(cities):
            print(" Lựa chọn không hợp lệ.")
            return
    except ValueError:
        print(" Vui lòng nhập một số hợp lệ.")
        return

    # In danh sách loại nhà đất
    property_map = {
        1: "nha-dat",
        2: "can-ho-chung-cu",
        3: "dat-tho-cu-dat-o"
    }

    print("\nChọn loại nhà đất:")
    print("1: Nhà")
    print("2: Căn Hộ Chung Cư")
    print("3: Đất")

    try:
        property_choice = int(input("Nhập số tương ứng: "))
        if property_choice not in property_map:
            print(" Lựa chọn không hợp lệ.")
            return
    except ValueError:
        print(" Vui lòng nhập một số hợp lệ.")
        return

    province = cities[province_choice - 1]
    property_type = property_map[property_choice]

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
                print(f"⚠️ Không thể truy cập {url}")
                break

            soup = BeautifulSoup(response.text, 'html.parser')
            listings = soup.select('div.ct_title')

            if not listings:
                print("✅ Không còn dữ liệu trên trang này.")
                break

            for listing in listings:
                title = listing.get_text(strip=True)
                description = listing.find_next('div', class_='ct_desc')
                address = listing.find_next('div', class_='ct_location')
                area = listing.find_next('div', class_='ct_area')
                price = listing.find_next('div', class_='ct_price')

                data.append([
                    title,
                    description.get_text(strip=True) if description else "",
                    address.get_text(strip=True) if address else "",
                    area.get_text(strip=True) if area else "",
                    price.get_text(strip=True) if price else ""
                ])

            page += 1

        except requests.exceptions.RequestException as e:
            print(f"❌ Lỗi khi gửi yêu cầu: {e}")
            break

    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Tiêu đề", "Mô tả", "Địa chỉ", "Diện tích", "Giá"])
        writer.writerows(data)

    print(f"\n✅ Dữ liệu đã được lưu vào file: {filename}")

# Gọi hàm chính
collect_data()
