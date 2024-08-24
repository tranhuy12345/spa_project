import firebase_admin
from firebase_admin import credentials, storage

# Đường dẫn đến tệp JSON mà bạn đã tải xuống
cred = credentials.Certificate(r"C:\Users\ADMIN\Downloads\spaproject-d0368-firebase-adminsdk-wwlpp-be78206f11.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'spaproject-d0368.appspot.com'
})

bucket = storage.bucket()


# Hàm tải ảnh lên Firebase Storage
def upload_image_to_firebase(file):
    # Tạo một tên tệp duy nhất
    blob = bucket.blob(f'images/{file.name}')
    
    # Tải lên tệp
    blob.upload_from_file(file)
    
    # Đặt quyền công khai cho tệp nếu muốn
    blob.make_public()
    
    # Lấy URL công khai của tệp
    return blob.public_url
