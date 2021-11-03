from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from core.conf import settings

from db.session import engine 
from db.base_class import Base 
from db.models.users import User
from db.models.jobs import Job



def create_tables(): 
	Base.metadata.create_all(bind=engine)


# working as a decorator, to fire create_app when start_application is fired
def start_application():
	app = FastAPI(title=settings.PROJECT_TITLE,version=settings.PROJECT_VERSION)

	create_tables()      
	return app

app = start_application()

@app.get("/")
def hello_api():
    return {"detail": "hello world"}


@app.post("/")
def hello_post():
	return {"detail": "this is a post"}


