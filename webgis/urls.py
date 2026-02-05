from django.contrib import admin
from django.urls import path
# Sửa dòng này: đổi ban_do thành map_view
from cuahang.views import map_view 

urlpatterns = [
    path('admin/', admin.site.urls),
    # Sửa dòng này: gọi hàm map_view
    path('', map_view, name='map_view'),
]