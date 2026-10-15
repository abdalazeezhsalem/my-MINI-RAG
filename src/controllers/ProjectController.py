"""
import os 
from controllers.BaseController import BaseController 

class ProjectController(BaseController): 
    def __init__(self):
         super().__init__()
         self.project_dir = None

    def get_project_path(self, project_id: str):
        
        # تحديد مسار مجلد المشروع بناءً على ID
        project_dir = os.path.join(self.files_dir, project_id)

        # إنشاء المجلد إذا لم يكن موجوداً
        if not os.path.exists(project_dir):
            os.makedirs(project_dir)


        return project_dir

"""

from .BaseController import BaseController
from fastapi import UploadFile
from models import ResponseSignal
import os

class ProjectController(BaseController):
    
    def __init__(self):
        super().__init__()

    def get_project_path(self, project_id: str):
        project_dir = os.path.join(
            self.files_dir,
            project_id
        )

        if not os.path.exists(project_dir):
            os.makedirs(project_dir)

        return project_dir

    