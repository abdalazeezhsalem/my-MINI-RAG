"""
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv(".env")


# 2\. استيراد الراوتر بعد تحميل المتغيرات 
from routes.base import base_router
from routes.data import data_router

# إنشاء أوبجكت تطبيق FastAPI
app = FastAPI()

# 3\. تضمين الراوتر الفرعي داخل التطبيق الرئيسي 
app.include_router(base_router)
app.include_router(data_router)

"""



from fastapi import FastAPI
from routes import base, data

app = FastAPI()

app.include_router(base.base_router)
app.include_router(data.data_router)