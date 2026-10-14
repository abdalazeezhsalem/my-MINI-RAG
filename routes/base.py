import os 
from fastapi import APIRouter 
# إنشاء راوتر فرعي مع تحديد بادئة المسار والتاجات الخاصة بالتوثيق 

base_router = APIRouter(prefix="/api/v1", tags=["api_v1"]) 

# استخدام async def لتحسين أداء السيرفر 
@base_router.get("/") 
async def welcome(): 
    app_name = os.getenv("APP_NAME") 
    app_version = os.getenv("APP_VERSION") 
    
    return { 
        "app_name": app_name, 
        "app_version": app_version 
        }