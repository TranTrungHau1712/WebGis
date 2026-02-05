from django.shortcuts import render
from django.core.serializers import serialize
from .models import CuaHang

def ban_do(request):
    # 1. Lấy toàn bộ cửa hàng từ Database
    cac_cua_hang = CuaHang.objects.all()
    
    # 2. Chuyển dữ liệu sang dạng GeoJSON (để bản đồ hiểu được)
    #    Chúng ta chỉ lấy các trường cần thiết để nhẹ web
    data_json = serialize('geojson', cac_cua_hang, geometry_field='vi_tri', fields=('ten_quan', 'dia_chi', 'ban_kinh'))
    
    # 3. Đẩy dữ liệu sang file HTML
    return render(request, 'map.html', {'data_json': data_json})