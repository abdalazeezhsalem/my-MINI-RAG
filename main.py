from fastapi import FastAPI

# إنشاء أوبجكت تطبيق FastAPI
app = FastAPI()

# تعريف Route من نوع GET على المسار /welcome
@app.get("/welcome")
def welcome():
    return {"message": "Hello World"}

