"""
from pydantic_settings import BaseSettings, SettingsConfigDict 

class Settings(BaseSettings): 
# إعدادات التطبيق الأساسية 
 
    APP_NAME: str = "mini-rag" 
    APP_VERSION: str = "0.1.0" 
# إعدادات رفع الملفات للأمان 
 
    FILE_ALLOWED_TYPES: list = ["application/pdf", "text/plain"] 
    FILE_MAX_SIZE: int = 10 * 1024 * 1024 
    
# 10 ميجابايت كحد أقصى للملف 
 
    FILE_DEFAULT_CHUNK_SIZE: int = 512 * 1024 
    # 512 كيلوبايت لكل جزء عند القراءة 

    #  تحديد ملف المتغيرات البيئية 
    model_config = SettingsConfigDict(
            env_file=".env",
            extra="ignore",
            env_ignore_empty=True)  
# دالة مجردة للوصول للإعدادات 
 
def get_settings():
    return Settings()

"""

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    APP_NAME: str
    APP_VERSION: str
    OPENAI_API_KEY: str

    FILE_ALLOWED_TYPES: list
    FILE_MAX_SIZE: int
    FILE_DEFAULT_CHUNK_SIZE: int

    class Config:
        env_file = ".env"

def get_settings():
    return Settings()