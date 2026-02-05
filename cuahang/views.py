from django.shortcuts import render
from django.core.serializers import serialize
from .models import CuaHang
# Import các thư viện GIS để xử lý khoảng cách
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance

def map_view(request):
    # 1. Lấy tham số từ người dùng (nếu có)
    # Mặc định lấy tọa độ trung tâm TP.HCM nếu user không nhập
    user_lat = request.GET.get('lat', 10.776) 
    user_lon = request.GET.get('lon', 106.700)
    ban_kinh = request.GET.get('dist', None) # Khoảng cách muốn tìm (km)

    # Tạo điểm vị trí người dùng (để làm tâm tính toán)
    user_location = Point(float(user_lon), float(user_lat), srid=4326)

    # 2. Bắt đầu truy vấn dữ liệu
    # annotate(distance=...): Tính thêm trường 'distance' cho mỗi cửa hàng
    shops = CuaHang.objects.annotate(
        distance=Distance('vi_tri', user_location)
    )

    # 3. TOOL XỬ LÝ: Nếu người dùng nhập bán kính -> Lọc
    if ban_kinh:
        # Lọc những quán có khoảng cách nhỏ hơn hoặc bằng bán kính nhập vào
        # Dùng 'm' vì Distance trả về mét, nên nhân 1000
        shops = shops.filter(distance__lte=float(ban_kinh) * 1000)

    # Sắp xếp từ gần đến xa
    shops = shops.order_by('distance')

    # 4. Chuyển dữ liệu sang JSON để vẽ lên bản đồ
    data_json = serialize('geojson', shops, geometry_field='vi_tri', fields=('ten_quan', 'dia_chi', 'ban_kinh'))

    return render(request, 'map.html', {
        'data_json': data_json,
        'user_lat': user_lat,
        'user_lon': user_lon
    })