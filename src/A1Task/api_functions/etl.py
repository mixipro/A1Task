import pycountry
import requests
from datetime import datetime
from sqlmodel import Session
from A1Task.api.models import User
from A1Task.common import engine


def get_country_full_name(abbreviation):
    try:
        return pycountry.countries.get(alpha_2=abbreviation).name
    except AttributeError:
        return abbreviation


def get_clean_user_data():
    url = "https://randomuser.me/api/"
    for _ in range(100):
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
        user.birthday = datetime.strptime(
            result["dob"].get("date"), "%Y-%m-%dT%H:%M:%S.%fZ"
        ).date()
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


if __name__ == "__main__":
    get_clean_user_data()
