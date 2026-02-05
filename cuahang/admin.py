from django.contrib import admin
# Đổi OSMGeoAdmin thành GISModelAdmin (class mới)
from django.contrib.gis.admin import GISModelAdmin 
from .models import CuaHang

@admin.register(CuaHang)
class CuaHangAdmin(GISModelAdmin): # Sửa chỗ này luôn
    list_display = ('ten_quan', 'dia_chi', 'ban_kinh')