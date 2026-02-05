"""
Django settings for webgis project.
Cấu hình chuẩn: PostgreSQL 18 + PostGIS + Windows
"""

import os
from pathlib import Path

# =========================================================
import os
from pathlib import Path

# =========================================================
# 1. CẤU HÌNH GDAL + PROJ (FIX LỖI OGR FAILURE)
# =========================================================

# Thư mục gốc cài đặt PostgreSQL
PG_DIR = r"C:\Program Files\PostgreSQL\18"

# 1. Đường dẫn thư viện (DLL)
GDAL_LIBRARY_PATH = os.path.join(PG_DIR, r"bin\libgdal-35.dll")
GEOS_LIBRARY_PATH = os.path.join(PG_DIR, r"bin\libgeos_c.dll")

# 2. Thêm bin vào PATH (để Windows tìm thấy các file phụ thuộc)
os.environ['PATH'] = os.path.join(PG_DIR, "bin") + ";" + os.environ.get('PATH', '')

# 3. Cấu hình GDAL_DATA (Từ điển GDAL)
# Kiểm tra xem folder gdal-data nằm ở đâu (thường là ở gốc hoặc trong share)
gdal_data_path = os.path.join(PG_DIR, "gdal-data")
if not os.path.exists(gdal_data_path):
    # Nếu không thấy ở gốc, thử tìm trong share
    gdal_data_path = os.path.join(PG_DIR, r"share\gdal")

os.environ['GDAL_DATA'] = gdal_data_path

# 4. Cấu hình PROJ_LIB (Quan trọng nhất để fix lỗi OGR Failure)
# Bạn hãy SỬA SỐ '3.4' dưới đây thành phiên bản bạn thấy ở Bước 1 (ví dụ 3.5, 3.6)
# Đường dẫn này phải trỏ tới thư mục chứa file 'proj.db'
PROJ_LIB_PATH = os.path.join(PG_DIR, r"share\contrib\postgis-3.6\proj") 

if os.path.exists(PROJ_LIB_PATH):
    os.environ['PROJ_LIB'] = PROJ_LIB_PATH
else:
    print(f"CẢNH BÁO: Không tìm thấy thư mục PROJ tại {PROJ_LIB_PATH}")
    print("Hãy kiểm tra lại đường dẫn C:/Program Files/PostgreSQL/18/share/contrib/")

# 5. Add DLL Directory (Bắt buộc cho Python trên Windows)
if os.name == 'nt':
    try:
        os.add_dll_directory(os.path.join(PG_DIR, "bin"))
    except Exception:
        pass

# =========================================================
# ... (Giữ nguyên phần còn lại của file settings.py)

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-key-nay-duoc-tao-tu-dong-cho-ban'

DEBUG = True

ALLOWED_HOSTS = []


# =========================================================
# 3. KHAI BÁO ỨNG DỤNG (INSTALLED_APPS)
# =========================================================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # --- APP BẢN ĐỒ ---
    'django.contrib.gis',

    # --- APP CỦA BẠN ---
    'cuahang',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# --- QUAN TRỌNG: PHẢI LÀ 'webgis.urls' VÌ THƯ MỤC TÊN LÀ webgis ---
ROOT_URLCONF = 'webgis.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# --- QUAN TRỌNG: PHẢI LÀ 'webgis.wsgi.application' ---
WSGI_APPLICATION = 'webgis.wsgi.application'


# =========================================================
# 4. CẤU HÌNH DATABASE
# =========================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        
        # Tên database chuẩn (chuỗi ký tự)
        'NAME': 'gis_store', 
        
        'USER': 'postgres',
        'PASSWORD': '1',     # Mật khẩu bạn cung cấp
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# =========================================================
# 5. CÁC CẤU HÌNH KHÁC
# =========================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'