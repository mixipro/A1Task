from fastapi import APIRouter, Depends, status
from A1Task.api.models import User, CreateUser
from sqlmodel import Session

from A1Task.api_functions.user_function import get_all_users_from_db, get_user_by_id_from_db, \
    add_new_user_in_db, update_user_in_db, delete_user_from_db
from A1Task.common import get_session

app = APIRouter()


@app.get("/users", status_code=status.HTTP_200_OK, tags=["User"])
def get_users(db: Session = Depends(get_session)
              ) -> list[User]:
    return get_all_users_from_db(db=db)


# Response model?
@app.get("/user/{user_id}", status_code=status.HTTP_200_OK, response_model=User, tags=["User"])
def get_user_info(user_id: int,
                  db: Session = Depends(get_session)) -> User:
    return get_user_by_id_from_db(user_id=user_id, db=db)


@app.post("/user", status_code=status.HTTP_201_CREATED, tags=["User"])
def add_user(user: CreateUser,
             db: Session = Depends(get_session)):
    return add_new_user_in_db(user=user, db=db)


@app.put("/user/{user_id}", status_code=status.HTTP_200_OK, tags=["User"])
def update_user(user_id: int, user: User,
                db: Session = Depends(get_session)):
    return update_user_in_db(user_id=user_id, user=user, db=db)


@app.delete("/user/{user_id}", status_code=status.HTTP_200_OK, tags=["User"])
def delete_user(user_id: int,
                db: Session = Depends(get_session)):
    return delete_user_from_db(user_id=user_id, db=db)
