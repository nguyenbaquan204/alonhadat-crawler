# Dự Án Thu Thập Dữ Liệu Bất Động Sản

## Mô Tả
Dự án này sử dụng Python và thư viện BeautifulSoup để thu thập thông tin về nhà đất từ trang web [alonhadat.com.vn](https://alonhadat.com.vn). Dữ liệu thu thập bao gồm các thông tin về các loại nhà đất (nhà, căn hộ chung cư, đất) tại các tỉnh/thành phố mà người dùng lựa chọn. Dữ liệu thu thập bao gồm:

- Tiêu đề
- Mô tả
- Địa chỉ
- Diện tích
- Giá

Thông tin này sẽ được lưu vào file CSV để tiện cho việc xử lý và phân tích.

## Các Tính Năng
- **Chọn Tỉnh/Thành Phố**: Hỗ trợ chọn từ các tỉnh/thành phố như Hà Nội, Hồ Chí Minh, và Đà Nẵng.
- **Chọn Loại Nhà Đất**: Có thể chọn loại nhà đất bao gồm Nhà, Căn hộ chung cư, và Đất.
- **Thu Thập Dữ Liệu**: Thu thập dữ liệu từ các trang kết quả tìm kiếm của website.
- **Lưu Dữ Liệu**: Kết quả thu thập được sẽ được lưu vào một file CSV với thông tin chi tiết.

## Cài Đặt
Để sử dụng dự án này, bạn cần có Python và một số thư viện phụ thuộc.

### Cài Đặt Python
1. Cài đặt Python từ trang chủ [https://www.python.org/downloads/](https://www.python.org/downloads/).
2. Sau khi cài đặt Python, mở terminal (hoặc command prompt) và kiểm tra lại phiên bản Python với lệnh:
   ```bash
   python --version

### Cách Sử Dụng


Mở terminal hoặc command prompt và điều hướng đến thư mục chứa file Python.

1. Chạy script 

python alonhadat.py
2. Khi chương trình chạy, bạn sẽ được yêu cầu nhập số tương ứng với tỉnh/thành phố mà bạn muốn thu thập dữ liệu. Chọn từ một trong ba lựa chọn: Hà Nội, Hồ Chí Minh, Đà Nẵng.

Chọn loại nhà đất:

Sau đó, bạn sẽ được yêu cầu chọn loại nhà đất: Nhà, Căn hộ chung cư, hoặc Đất.

3. Thu Thập Dữ Liệu:

Chương trình sẽ tự động thu thập dữ liệu từ các trang kết quả và lưu vào một file CSV. File này sẽ có tên dạng alonhadat_{province}_{property_type}_{today}.csv, ví dụ alonhadat_ha-noi_nha-dat_2025-05-09.csv.

4. Kiểm tra kết quả:

Sau khi chương trình hoàn thành, bạn có thể mở file CSV để kiểm tra dữ liệu đã thu thập.

### Tạo project GitHub ở chế độ Public
Bước 1: Truy cập GitHub
Vào trang: https://github.com
Đăng nhập hoặc tạo tài khoản nếu chưa có.

Bước 2: Tạo repository mới
Nhấn nút New repository hoặc vào https://github.com/new

Nhập:

Repository name: alonhadat-crawler 

Description: Thu thập dữ liệu bất động sản từ alonhadat.com.vn

Public: ✅ chọn chế độ Public

Bỏ chọn "Initialize this repository with a README"

Nhấn Create repository


###  Khởi tạo Git & đẩy lên GitHub
chạy từng lệnh ở dưới


# lưu ý  cd path/to/thu-muc-cua-ban

git init
git remote add origin https://github.com/<ten-ban>/<ten-repo>.git
git add .
git commit -m "Initial commit"
git push -u origin master




