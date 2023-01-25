import hashlib
import os
import shutil
from pathlib import Path

from fastapi import FastAPI, Request, UploadFile, status, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse


app = FastAPI()
app.mount("/files", StaticFiles(directory="files"), name="files")
templates = Jinja2Templates(directory="views")

file_dir = Path(os.getcwd() + "/files")


@app.get('/')
def index(req: Request):
    ctx = {
        "request": req,
    }
    files = get_user_files(file_dir)
    ctx["files"] = files

    return templates.TemplateResponse("index.html", ctx)

@app.post('/')
def post_file(request: Request, file: UploadFile):
    with open(file_dir / file.filename, "wb+") as f:
        shutil.copyfileobj(file.file, f)
        file.file.close()
    return RedirectResponse(request.url_for("index"), status_code=status.HTTP_303_SEE_OTHER)

@app.post('/delete')
def delete_file(req: Request, delete: list[str] = Form(False), delete_all: bool = Form(False)):
    to_delete = []

    if delete_all:
        to_delete = get_user_files(file_dir)
    elif delete:
        to_delete = delete

    for f in to_delete:
        os.unlink(file_dir / f)

    return RedirectResponse(req.url_for("index"), status_code=status.HTTP_303_SEE_OTHER)

def get_user_files(dr: str)->list:
    files = []
    for f in os.scandir(dr):
        if f.is_file():
            files.append(f.name)

    return files
