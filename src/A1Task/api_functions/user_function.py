import pycountry
import requests
from datetime import datetime
from sqlmodel import Session, select
from A1Task.api.models import User, CreateUser
from A1Task.common import engine
from fastapi import HTTPException
from sqlalchemy.exc import NoResultFound, IntegrityError
from starlette import status


def get_country_full_name(abbreviation):
    try:
        return pycountry.countries.get(alpha_2=abbreviation).name
    except AttributeError:
        return abbreviation


def get_clean_user_data():
    url = "https://randomuser.me/api/"
    for _ in range(3):
        response = requests.get(url)
        data = response.json()
        result = data["results"][0]
        user = User()
        user.gender = result.get("gender")
        user.first_name = result["name"].get("first")
        user.last_name = result["name"].get("last")
        user.email = result.get("email")
        user.username = result["login"].get("username")
        user.password = result["login"].get("password")
        user.birthday = datetime.strptime(result["dob"].get("date"), "%Y-%m-%dT%H:%M:%S.%fZ").date()
        user.nationality = get_country_full_name(result.get("nat"))
        user.cell = result.get("cell")
        user.location_street = result["location"]["street"].get("name")
        user.location_street_number = result["location"]["street"].get("number")
        user.location_city = result["location"].get("city")
        user.location_state = result["location"].get("state")
        user.location_country = result["location"].get("country")
        user.location_postcode = str(result["location"].get("postcode"))
        print(user)
        yield user


with Session(engine) as session:
    for user in get_clean_user_data():
        session.add(user)
        session.commit()


def get_all_users_from_db(db: Session, ) -> list[User]:
    statement = select(User).order_by(User.id)
    users = db.exec(statement).all()
    return [User.parse_obj(user) for user in users]


def get_user_by_id_from_db(
        user_id: int,
        db: Session,
) -> User:
    statement = select(User).where(User.id == user_id)
    try:
        user: User = db.exec(statement).one()
    except NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")
    return User.parse_obj(user)


def add_new_user_in_db(user: CreateUser, db: Session) -> dict:
    new_user = User(gender= user.gender,
    first_name= user.first_name,
    last_name= user.last_name,
    email= user.email,
    username= user.username,
    password= user.password,
    birthday= user.birthday,
    nationality= user.nationality,
    cell= user.cell,
    location_street= user.location_street,
    location_street_number= user.location_street_number,
    location_city= user.location_city,
    location_state= user.location_state,
    location_country= user.location_country,
    location_postcode= user.location_postcode)

    try:
        db.add(new_user)
        db.commit()
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=e.orig.diag.message_detail)

    return {"message": "User added to the database."}


def update_user_in_db(user_id: int, user: User, db: Session) -> dict:
    existing_user = db.query(User).filter(User.id == user_id).first()

    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")

    for field, value in user.dict(exclude_unset=True).items():
        setattr(existing_user, field, value)

    try:
        db.commit()
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=e.orig.diag.message_detail)

    return {"message": "User updated successfully"}


def delete_user_from_db(user_id: int, db: Session) -> dict:
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()

    return {"message": "User deleted successfully"}


if __name__ == "__main__":
    get_clean_user_data()
