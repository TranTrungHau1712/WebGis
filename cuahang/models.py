from django.contrib.gis.db import models

class CuaHang(models.Model):
    ten_quan = models.CharField(max_length=100, verbose_name="Tên Quán")
    dia_chi = models.CharField(max_length=200, verbose_name="Địa chỉ")
    vi_tri = models.PointField(srid=4326, verbose_name="Vị trí") # Chứa tọa độ GPS
    ban_kinh = models.FloatField(default=5.0, verbose_name="Bán kính ship (km)")

    def __str__(self):
        return self.ten_quan