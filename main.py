from fastapi import Depends, FastAPI,Response,status,HTTPException
from typing import Optional
from modules.instagram import user_finder,local_get_comments,validate_commenters
from requests import Session
from database import engine,get_db
import models,schema


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def root():
    return {"message":"hello world"}


@app.get("/sqlalchemy")
async def test_database(db:Session=Depends(get_db)):
    return {"status":"success"}

@app.get("/usersample")
async def get_usrers(db:Session=Depends(get_db)):
    users = db.query(models.MustBeActive).all()
    return(users)

@app.post("/usersample")
async def create_user(user:schema.UserCreate,db:Session=Depends(get_db)):
    new_user = models.MustBeActive(username=user.username)
    db.add(new_user)
    db.commit()
    return(new_user)

@app.patch("/usersample/{id}")
async def edit_user(id:int,user:schema.UserCreate,db:Session=Depends(get_db)):
    queried_user = db.query(models.MustBeActive).filter(models.MustBeActive.id == id)
    edited_user = queried_user.first()
    if edit_user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with the id of {id} not found")
    queried_user.update({"username":user.username},synchronize_session=False)
    db.commit()
    return({"data":"successful"})

@app.get("/noncommenters")
async def get_usrers(limit:int,filter:str,db:Session=Depends(get_db)):
    USER = filter
    usernames = db.query(models.MustBeActive.username).all()
    commenters_dict = local_get_comments(USER,limit)
    userslist=user_finder(usernames)
    uncommenters = validate_commenters(userslist, commenters_dict)
    return({"data":uncommenters})

@app.get("/commenters")
async def get_usrers(limit:int,filter:str,db:Session=Depends(get_db)):
    USER = filter
    commenters_dict = local_get_comments(USER,limit)
    return({"data":commenters_dict})

