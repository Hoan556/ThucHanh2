import requests

# Thông tin cần thiết
access_token = 'EAAqZBV7L3iLMBO0BN8TbTX7TiQgm2tfWDtb1LkCSfQHZBa4yRhxjPHPQ8GVe7INB9D37sfWrkevIHwm9RZBL781AKs43ioD539Mcu3zghVC2tEIdvXHC1iHFnMSDt1hZBmH9bpoHdSJzlKtl2eudULAsAVEbMaGySCFuYR5aZC2D8TKGI93RUxkYhbgjY6s5BKWHNMA6pHsqsr431Wx74gafm'  # Thay bằng access token của bạn
page_id = '655557894302354'            # Thay bằng ID của trang bạn quản lý
message = 'Đây là bài viết tự động từ Python của Hoanchivas 🚀'  # Nội dung bài đăng

# URL API của Facebook để đăng bài
url = f'https://graph.facebook.com/{page_id}/feed'

# Dữ liệu gửi đi
payload = {
    'message': message,
    'access_token': access_token
}

# Gửi yêu cầu POST đến Facebook Graph API
response = requests.post(url, data=payload)

# Xử lý kết quả
if response.status_code == 200:
    print("✅ Đăng bài thành công!")
    print("ID bài viết:", response.json().get('id'))
else:
    print("❌ Lỗi khi đăng bài:")
    print(response.status_code)
    print(response.text)