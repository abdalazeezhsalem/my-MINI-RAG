"""
import aiofiles 
from fastapi import APIRouter, UploadFile, File, status 
from fastapi.responses import JSONResponse 
from controllers.DataController import DataController 
from models.enums.ResponseEnums import ResponseSignal 

data_router = APIRouter(prefix="/api/v1/data", tags=["api_v1", "data"]) 

@data_router.post("/upload/{project_id}") 
async def upload_file(project_id: str, file: UploadFile = File(...)):
    data_controller = DataController() 
     # 1\. التحقق من نوع وحجم الملف 
     
    is_valid, response_signal = data_controller.validate_uploaded_file(file=file) 
    if not is_valid:
          return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST, 
                content={"signal": response_signal} ) 
     
     # 2\. توليد المسار والاسم الفريد للملف داخل مجلد المشروع 
     
    file_path, file_name = data_controller.generate_unique_filepath( 
          orig_file_name=file.filename, 
          project_id=project_id ) 
     
# 3\. قراءة الملف وتقطيعه لكُتل (Chunks) وحفظه على القرص بشكل غير تزامني 

    try: 
         async with aiofiles.open(file_path, "wb") as f: 
             while chunk := await data_controller.app_settings.FILE_DEFAULT_CHUNK_SIZE: 
                 await f.write(chunk) 
         return JSONResponse( 
             status_code=status.HTTP_200_OK, 
             content={ 
                 "signal": ResponseSignal.FILE_UPLOAD_SUCCESS.value, 
                 "file_name": file_name 
             } 
         ) 
    except Exception as e: 
        return JSONResponse( 
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            content={"signal": ResponseSignal.FILE_UPLOAD_FAILED.value} 
        )"""


from fastapi import FastAPI, APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
import os
from helpers.config import get_settings, Settings
from controllers import DataController, ProjectController
import aiofiles
from models import ResponseSignal
import logging

logger = logging.getLogger('uvicorn.error')

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"],
)

@data_router.post("/upload/{project_id}")
async def upload_data(project_id: str, file: UploadFile,
                      app_settings: Settings = Depends(get_settings)):
        
    
    # validate the file properties
    data_controller = DataController()

    is_valid, result_signal = data_controller.validate_uploaded_file(file=file)

    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal": result_signal
            }
        )

    project_dir_path = ProjectController().get_project_path(project_id=project_id)
    file_path, file_id = data_controller.generate_unique_filepath(
        orig_file_name=file.filename,
        project_id=project_id
    )

    try:
        async with aiofiles.open(file_path, "wb") as f:
            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
                await f.write(chunk)
    except Exception as e:

        logger.error(f"Error while uploading file: {e}")

        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal": ResponseSignal.FILE_UPLOAD_FAILED.value
            }
        )

    return JSONResponse(
            content={
                "signal": ResponseSignal.FILE_UPLOAD_SUCCESS.value,
                "file_id": file_id
            }
        )