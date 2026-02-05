from django.contrib import admin
from django.urls import path
from cuahang.views import ban_do  # Import hàm ban_do vừa viết

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Đường dẫn trang chủ (trống) sẽ trỏ vào bản đồ
    path('', ban_do, name='trang_chu'),
]