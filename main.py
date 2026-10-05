from typing import Annotated, Optional

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlmodel import Session, select

from models import User, engine, create_tables

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_tables()


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


class UserForm(BaseModel):
    name: str
    age: Optional[int] = None


@app.post("/user/create", summary="User Create")
def user_create(form: UserForm, session: SessionDep):
    user = User(**form.model_dump())
    session.add(user)
    session.commit()
    session.refresh(user)
    return {"message": "User yaratildi!", "data": user}


@app.get("/user/list", summary="User List")
def user_list(session: SessionDep):
    users = session.exec(select(User)).all()
    return users


@app.get("/user/detail/{user_id}", summary="User Detail")
def user_detail(user_id: int, session: SessionDep):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User topilmadi")
    return user


@app.delete("/user/{user_id}/delete", summary="User Delete")
def user_delete(user_id: int, session: SessionDep):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User topilmadi")
    session.delete(user)
    session.commit()
    return {"message": "User o'chirildi!"}