import random
from faker import Faker
from fastapi.testclient import TestClient

fake = Faker()


def test_post_user_empty_request(api_client: TestClient):
    response = api_client.get("/users")
    assert response.status_code == 200


def test_add_new_user(api_client: TestClient):
    # Generate random values for the request payload
    gender = random.choice(["Male", "Female", "Other"])
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    username = fake.user_name()
    password = fake.password()
    birthday = fake.date_of_birth(minimum_age=18, maximum_age=80).strftime("%Y-%m-%d")
    nationality = fake.country()
    cell = fake.phone_number()
    location_street = fake.street_name()
    location_street_number = fake.building_number()
    location_city = fake.city()
    location_state = fake.state()
    location_country = fake.country()
    location_postcode = fake.postcode()

    valid_request = {
        "gender": gender,
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "username": username,
        "password": password,
        "birthday": birthday,
        "nationality": nationality,
        "cell": cell,
        "location_street": location_street,
        "location_street_number": location_street_number,
        "location_city": location_city,
        "location_state": location_state,
        "location_country": location_country,
        "location_postcode": location_postcode,
    }

    response = api_client.post("/users", json=valid_request)
    assert response.status_code == 201
    # Add additional assertions or validation if required
    # assert response.json() == expected_response


    # session = api_client.session
    # statement = select(Users)
    # user = session.exec(statement).one()
    #
    # assert user.username == valid_request["username"]
    # assert user.email == valid_request["email"]
    # assert user.first_name == valid_request["first_name"]
    # assert user.last_name == valid_request["last_name"]

#
# @pytest.mark.parametrize("key",
#                          ["username", "first_name", "last_name", "email", "password"])
# def test_add_new_user_with_missing_value(key, api_client: TestClient):
#     invalid_request = {
#         "username": fake.name(),
#         "first_name": fake.name(),
#         "last_name": fake.name(),
#         "email": fake.email(),
#         "password": FAKE_PASSWORD_LENGTH_8
#     }
#     del invalid_request[key]
#
#     response = api_client.post("/users", json=invalid_request)
#     assert response.status_code == 422
#
#
# @mock_ses
# def test_add_new_user_if_username_already_exists(api_client: TestClient):
#     valid_request = {
#         "username": "marija",
#         "email": fake.email(),
#         "first_name": fake.name(),
#         "last_name": fake.name(),
#         "password": FAKE_PASSWORD_LENGTH_8
#     }
#
#     conn = boto3.client("ses", region_name=common.get_settings().REGION_NAME)
#     conn.verify_email_identity(EmailAddress=common.get_settings().SENDER_EMAIL)
#
#     response = api_client.post("/users", json=valid_request)
#     assert response.status_code == 201
#
#     invalid_request_with_same_username = {
#         "username": "marija",
#         "email": fake.email(),
#         "first_name": fake.name(),
#         "last_name": fake.name(),
#         "date_of_birth": fake.date(),
#         "password": FAKE_PASSWORD_LENGTH_8
#     }
#     invalid_response = api_client.post("/users", json=invalid_request_with_same_username)
#     assert invalid_response.status_code == 400
#
#
# @pytest.mark.parametrize("user_name",
#                          ["\t", "\n", "", " "])
# def test_create_new_user_with_invalid_username(user_name, api_client: TestClient):
#     invalid_request = {
#         "username": user_name,
#         "first_name": fake.name(),
#         "last_name": fake.name(),
#         "email": fake.email(),
#         "password": FAKE_PASSWORD_LENGTH_8
#     }
#
#     response = api_client.post("/users", json=invalid_request)
#     assert response.status_code == 422
#
#
# @pytest.mark.parametrize("email", ["marko.email.com", "markoemail@", "marko@.", "@.com "])
# def test_create_new_user_with_invalid_email(email, api_client: TestClient):
#     invalid_request = {
#         "username": fake.name(),
#         "first_name": fake.name(),
#         "last_name": fake.name(),
#         "email": email,
#         "password": FAKE_PASSWORD_LENGTH_8
#     }
#
#     response = api_client.post("/users", json=invalid_request)
#     assert response.status_code == 422
#
#
# @pytest.mark.parametrize("first_name",
#                          ["\t", "\n", "", " "])
# def test_add_user_incorrect_first_name_len(first_name, api_client: TestClient):
#     valid_request = {
#         "username": fake.name(),
#         "first_name": first_name,
#         "last_name": fake.name(),
#         "email": fake.email(),
#         "password": FAKE_PASSWORD_LENGTH_8
#     }
#
#     response = api_client.post("/users", json=valid_request)
#     assert response.status_code == 422
#
#
# @pytest.mark.parametrize("last_name",
#                          ["\t", "\n", "", " "])
# def test_check_user_incorrect_last_name(last_name, api_client: TestClient):
#     valid_request = {
#         "username": fake.name(),
#         "first_name": fake.name(),
#         "last_name": last_name,
#         "email": fake.email(),
#         "password": FAKE_PASSWORD_LENGTH_8
#     }
#
#     response = api_client.post("/users", json=valid_request)
#     assert response.status_code == 422
#
#
# @pytest.mark.parametrize("password_len", range(8))
# def test_add_user_with_incorrect_password_len(password_len, api_client: TestClient):
#     valid_request = {
#         "user_name": fake.name(),
#         "first_name": fake.name(),
#         "last_name": fake.name(),
#         "email": fake.email(),
#         "password": "a" * password_len
#     }
#
#     response = api_client.post("/users", json=valid_request)
#     assert response.status_code == 422
#
#
# # TESTS FOR LOGIN USER
# @mock_ses
# def test_login_user_with_valid_values(api_client: TestClient):
#     username = fake.name()
#     password = fake.password()
#     valid_request = {
#         "username": username,
#         "first_name": fake.name(),
#         "last_name": fake.name(),
#         "email": fake.email(),
#         "password": password}
#
#     conn = boto3.client("ses", region_name=common.get_settings().REGION_NAME)
#     conn.verify_email_identity(EmailAddress=common.get_settings().SENDER_EMAIL)
#
#     response = api_client.post("/users", json=valid_request)
#     assert response.status_code == 201
#     login_user_request = {
#         "username": username,
#         "password": password
#
#     }
#     response = api_client.post("/me/account", data=login_user_request)
#     assert response.status_code == 200
#
#
# @mock_ses
# def test_add_single_user_and_login_with_invalid_password(api_client: TestClient):
#     username = fake.name()
#     user_creation_request = {
#         "username": username,
#         "first_name": fake.name(),
#         "last_name": fake.name(),
#         "email": fake.email(),
#         "password": FAKE_PASSWORD_LENGTH_8
#     }
#     conn = boto3.client("ses", region_name=common.get_settings().REGION_NAME)
#     conn.verify_email_identity(EmailAddress=common.get_settings().SENDER_EMAIL)
#
#     response = api_client.post("/users", json=user_creation_request)
#     assert response.status_code == 201
#
#     login_user_request = {
#         "username": username,
#         "password": fake.password()
#
#     }
#     response = api_client.post("/me/account", data=login_user_request)
#     assert response.status_code == 403
#
#
# @mock_ses
# def test_add_single_user_and_login_with_invalid_username(api_client: TestClient):
#     password = FAKE_PASSWORD_LENGTH_8
#     user_creation_request = {
#         "username": fake.name(),
#         "first_name": fake.name(),
#         "last_name": fake.name(),
#         "email": fake.email(),
#         "password": password
#     }
#     conn = boto3.client("ses", region_name=common.get_settings().REGION_NAME)
#     conn.verify_email_identity(EmailAddress=common.get_settings().SENDER_EMAIL)
#     api_client.post("/users", json=user_creation_request)
#
#     login_user_request = {
#         "username": fake.name(),
#         "password": password
#     }
#     response = api_client.post("/me/account", data=login_user_request)
#     assert response.status_code == 403
#     assert response.json()["detail"] == "Invalid username/password."
#
#
# # TESTS FOR GETTING MY ACCOUNT #
#
# def test_get_details_of_own_account_user_not_authenticated(api_client: TestClient):
#     response = api_client.get("/me/account")
#     assert response.status_code == 401
#
#
# def test_get_details_of_own_account(authenticated_api_client: TestClient):
#     response = authenticated_api_client.get("/me/account")
#     assert response.status_code == 200
#
#
# # TESTS FOR GET USER BY ID #
#
# def test_get_user_by_id_if_current_user_not_authenticated(api_client: TestClient):
#     session = api_client.session
#
#     create_user = CreateUser(username=fake.name(),
#                              first_name=fake.name(),
#                              last_name=fake.name(),
#                              email=fake.email(),
#                              password=FAKE_PASSWORD_LENGTH_8)
#
#     add_new_user_in_db(user=create_user, db=session)
#
#     statement = select(Users).where(Users.email == create_user.email)
#     user = session.exec(statement).one()
#     user_id = user.user_id
#
#     response = api_client.get(f"/users/{user_id}", params=dict(user))
#     assert response.status_code == 401
#
#
# def test_get_user_by_id_if_current_user_not_admin(authenticated_api_client):
#     session = authenticated_api_client.session
#
#     create_user = CreateUser(username=fake.name(),
#                              first_name=fake.name(),
#                              last_name=fake.name(),
#                              email=fake.email(),
#                              password=FAKE_PASSWORD_LENGTH_8)
#
#     add_new_user_in_db(user=create_user, db=session)
#
#     statement = select(Users).where(Users.email == create_user.email)
#     user = session.exec(statement).one()
#     user_id = user.user_id
#
#     response = authenticated_api_client.get(f"/users/{user_id}", params=dict(user))
#     assert response.status_code == 403
#
#
# def test_get_user_by_id_if_current_user_admin(admin_api_client: TestClient):
#     session = admin_api_client.session
#
#     create_user = CreateUser(username=fake.name(),
#                              first_name=fake.name(),
#                              last_name=fake.name(),
#                              email=fake.email(),
#                              password=FAKE_PASSWORD_LENGTH_8)
#
#     add_new_user_in_db(user=create_user, db=session)
#
#     statement = select(Users).where(Users.email == create_user.email)
#     user = session.exec(statement).one()
#     user_id = user.user_id
#
#     response = admin_api_client.get(f"/users/{user_id}", params=dict(user))
#     assert response.status_code == 200
#
#
# def test_get_user_by_id_invalid_id(admin_api_client: TestClient):
#     response = admin_api_client.get("/users/0")
#     assert response.status_code == 404
#
#
# # TESTS FOR USER UPDATE #
#
# def test_update_my_account_user_without_credentials(api_client: TestClient):
#     response = api_client.put("/me/account")
#     assert response.status_code == 401
#
#
# def test_update_my_account_with_valid_values_and_check_data(authenticated_api_client: TestClient):
#     valid_request = {
#         "username": " ggg",
#         "last_name": fake.name(),
#         "date_of_birth": fake.date(),
#     }
#     response = authenticated_api_client.put("/me/account", json=valid_request)
#     assert response.status_code == 200
#
#     session = authenticated_api_client.session
#     statement = select(Users).where(Users.username == valid_request["username"])
#     user = session.exec(statement).one()
#
#     assert user.username == valid_request["username"]
#     assert user.last_name == valid_request["last_name"]
#
#
# @pytest.mark.parametrize("user_name",
#                          ["\t", "\n", "", " "])
# def test_update_my_account_with_invalid_username(user_name, authenticated_api_client: TestClient):
#     invalid_request = {
#         "username": user_name,
#     }
#
#     response = authenticated_api_client.put("/me/account", json=invalid_request)
#     assert response.status_code == 422
#
#
# @mock_ses
# def test_update_my_account_username_already_in_use(authenticated_api_client: TestClient):
#     username = fake.name()
#     valid_request = {
#         "username": username,
#         "email": fake.email(),
#         "first_name": fake.name(),
#         "last_name": fake.name(),
#         "password": FAKE_PASSWORD_LENGTH_8
#     }
#     conn = boto3.client("ses", region_name=common.get_settings().REGION_NAME)
#     conn.verify_email_identity(EmailAddress=common.get_settings().SENDER_EMAIL)
#
#     response = authenticated_api_client.post("/users", json=valid_request)
#     assert response.status_code == 201
#
#     invalid_request_with_same_username = {
#         "username": username,
#         "first_name": fake.name(),
#         "last_name": fake.name(),
#     }
#     invalid_response = authenticated_api_client.put("/me/account", json=invalid_request_with_same_username)
#     assert invalid_response.status_code == 400
#
#
# @pytest.mark.parametrize("first_name",
#                          ["\t", "\n", "", " "])
# def test_update_my_account_with_invalid_first_name_len(first_name, authenticated_api_client: TestClient):
#     valid_request = {
#         "first_name": first_name,
#     }
#
#     response = authenticated_api_client.put("/me/account", json=valid_request)
#     assert response.status_code == 422
#
#
# @pytest.mark.parametrize("last_name",
#                          ["\t", "\n", "", " "])
# def test_update_my_account_with_incorrect_last_name(last_name, authenticated_api_client: TestClient):
#     valid_request = {
#         "last_name": last_name,
#     }
#
#     response = authenticated_api_client.put("/me/account", json=valid_request)
#     assert response.status_code == 422
#
#
# # TESTS FOR GETTING ALL USERS #
#
# def test_get_all_users_if_current_user_not_authenticated(api_client: TestClient):
#     response = api_client.get("/users")
#     assert response.status_code == 401
#
#
# def test_get_all_users_if_current_user_is_not_admin(authenticated_api_client):
#     response = authenticated_api_client.get("/users")
#     assert response.status_code == 403
#
#
# def test_get_all_users_if_current_user_is_admin(admin_api_client: TestClient):
#     response = admin_api_client.get("/users")
#     assert response.status_code == 200
#
#
# @mock_ses
# def test_add_more_users_and_get_list_of_users(admin_api_client: TestClient):
#     for i in range(4):
#         valid_request = {
#             "username": fake.name(),
#             "first_name": fake.name(),
#             "last_name": fake.name(),
#             "email": fake.email(),
#             "password": FAKE_PASSWORD_LENGTH_8
#
#         }
#         conn = boto3.client("ses", region_name=common.get_settings().REGION_NAME)
#         conn.verify_email_identity(EmailAddress=common.get_settings().SENDER_EMAIL)
#         admin_api_client.post("/users", json=valid_request)
#
#     response = admin_api_client.get("/users")
#     assert response.status_code == 200
#     assert len(response.json()) == 5
#
#
# def test_get_list_of_one_user(admin_api_client: TestClient):
#     response = admin_api_client.get("/users")
#     assert response.status_code == 200
#     assert len(response.json()) == 1
#
#
# # TESTS FOR SENDING FRIEND REQUEST #
# @mock_ses
# def test_friend_request_valid_form(authenticated_api_client: TestClient):
#     session = authenticated_api_client.session
#     create_user = {
#         "username": fake.name(),
#         "email": fake.email(),
#         "first_name": fake.name(),
#         "last_name": fake.name(),
#         "password": FAKE_PASSWORD_LENGTH_8
#     }
#     conn = boto3.client("ses", region_name=common.get_settings().REGION_NAME)
#     conn.verify_email_identity(EmailAddress=common.get_settings().SENDER_EMAIL)
#
#     authenticated_api_client.post("/users", json=create_user)
#
#     statement = select(Users).where(Users.email == create_user["email"])
#     user = session.exec(statement).one()
#     recipient_id = user.user_id
#
#     request_details = BaseFriendRequest(recipient_id=recipient_id, message="Let's be friends.")
#
#     response = authenticated_api_client.post("/friend_request", data=request_details.json())
#     assert response.status_code == 201
#
#
# def test_send_friend_request_to_non_existent_user(authenticated_api_client: TestClient):
#     request_details = BaseFriendRequest(recipient_id=2, message="Let's be friends.")
#
#     response = authenticated_api_client.post("/friend_request", data=request_details.json())
#     assert response.status_code == 400
#
#
# def test_friend_request_if_current_user_not_authenticated(api_client: TestClient):
#     request_details = BaseFriendRequest(recipient_id=2, message="Let's be friends.")
#
#     response = api_client.post("/friend_request", data=request_details.json())
#     assert response.status_code == 401
#
#
# @mock_ses
# def test_send_friend_request_two_times_to_same_user(authenticated_api_client: TestClient):
#     session = authenticated_api_client.session
#     create_user = {
#         "username": fake.name(),
#         "email": fake.email(),
#         "first_name": fake.name(),
#         "last_name": fake.name(),
#         "date_of_birth": fake.date(),
#         "password": FAKE_PASSWORD_LENGTH_8
#     }
#     conn = boto3.client("ses", region_name=common.get_settings().REGION_NAME)
#     conn.verify_email_identity(EmailAddress=common.get_settings().SENDER_EMAIL)
#
#     authenticated_api_client.post("/users", json=create_user)
#
#     statement = select(Users).where(Users.email == create_user["email"])
#     user = session.exec(statement).one()
#     recipient_id = user.user_id
#
#     request_details = BaseFriendRequest(recipient_id=recipient_id, message="Let's be friends.")
#
#     response = authenticated_api_client.post("/friend_request", data=request_details.json())
#     assert response.status_code == 201
#
#     response = authenticated_api_client.post("/friend_request", data=request_details.json())
#     assert response.status_code == 400
#
#
# # TESTS FOR GETTING PENDING FRIEND REQUESTS #
# def test_get_friend_request_if_current_user_not_authenticated(api_client: TestClient):
#     response = api_client.get("/me/friend_requests")
#     assert response.status_code == 401
#
#
# def test_get_empty_list_of_friend_requests(authenticated_api_client: TestClient):
#     response = authenticated_api_client.get("/me/friend_requests")
#     assert response.status_code == 200
#     assert len(response.json()) == 0
#
#
# @mock_ses
# def test_get_list_of_one_friend_requests(authenticated_api_client: TestClient):
#     session = authenticated_api_client.session
#     create_user = {
#         "username": fake.name(),
#         "email": fake.email(),
#         "first_name": fake.name(),
#         "last_name": fake.name(),
#         "date_of_birth": fake.date(),
#         "password": FAKE_PASSWORD_LENGTH_8
#     }
#     conn = boto3.client("ses", region_name=common.get_settings().REGION_NAME)
#     conn.verify_email_identity(EmailAddress=common.get_settings().SENDER_EMAIL)
#
#     authenticated_api_client.post("/users", json=create_user)
#     statement = select(Users).where(Users.email == create_user["email"])
#     user = session.exec(statement).one()
#     sender_id = user.user_id
#     recipient_id = authenticated_api_client.user_id
#
#     friend_request = FriendRequests(sender_id=sender_id,
#                                     recipient_id=recipient_id,
#                                     message="Let's be friends.")
#     session.add(friend_request)
#     session.commit()
#
#     response = authenticated_api_client.get("/me/friend_requests")
#     assert response.status_code == 200
#     assert len(response.json()) == 1
#
#
# @mock_ses
# def test_get_list_of_few_friend_requests(authenticated_api_client: TestClient):
#     session = authenticated_api_client.session
#     recipient_id = authenticated_api_client.user_id
#     for i in range(4):
#         create_user = {
#             "username": fake.name(),
#             "email": fake.email(),
#             "first_name": fake.name(),
#             "last_name": fake.name(),
#             "password": FAKE_PASSWORD_LENGTH_8
#         }
#         conn = boto3.client("ses", region_name=common.get_settings().REGION_NAME)
#         conn.verify_email_identity(EmailAddress=common.get_settings().SENDER_EMAIL)
#
#         authenticated_api_client.post("/users", json=create_user)
#         statement = select(Users).where(Users.email == create_user["email"])
#         user = session.exec(statement).one()
#         sender_id = user.user_id
#
#         friend_request = FriendRequests(sender_id=sender_id,
#                                         recipient_id=recipient_id,
#                                         message="Let's be friends.")
#         session.add(friend_request)
#         session.commit()
#
#     response = authenticated_api_client.get("/me/friend_requests")
#     assert response.status_code == 200
#     assert len(response.json()) == 4
#
#
# def test_send_friend_request_to_yourself(authenticated_api_client: TestClient):
#     recipient_id = authenticated_api_client.user_id
#     request_details = BaseFriendRequest(recipient_id=recipient_id, message="Let's be friends.")
#     response = authenticated_api_client.post("/friend_request", data=request_details.json())
#     assert response.status_code == 400
#
#
# # TESTS FOR RESPONSE ON FRIEND REQUEST #
# @mock_ses
# def test_response_on_friend_request_rejected(authenticated_api_client: TestClient):
#     session = authenticated_api_client.session
#     create_user = {
#         "username": fake.name(),
#         "email": fake.email(),
#         "first_name": fake.name(),
#         "last_name": fake.name(),
#         "date_of_birth": fake.date(),
#         "password": FAKE_PASSWORD_LENGTH_8
#     }
#     conn = boto3.client("ses", region_name=common.get_settings().REGION_NAME)
#     conn.verify_email_identity(EmailAddress=common.get_settings().SENDER_EMAIL)
#
#     authenticated_api_client.post("/users", json=create_user)
#     statement = select(Users).where(Users.email == create_user["email"])
#     user = session.exec(statement).one()
#     sender_id = user.user_id
#     recipient_id = authenticated_api_client.user_id
#
#     friend_request = FriendRequests(sender_id=sender_id,
#                                     recipient_id=recipient_id,
#                                     message="Let's be friends.")
#     session.add(friend_request)
#     session.commit()
#
#     request_response = ResponseOnFriendRequest(sender_id=sender_id,
#                                                reaction_on_request=False)
#
#     response = authenticated_api_client.put("/me/friend_requests", data=request_response.json())
#     assert response.status_code == 200
#
#     statement = select(FriendRequests)
#     friend_request = session.exec(statement).one()
#
#     assert friend_request.request_status == "rejected"
#
#
# @mock_ses
# def test_response_on_friend_request_accepted(authenticated_api_client: TestClient):
#     session = authenticated_api_client.session
#     create_user = {
#         "username": fake.name(),
#         "email": fake.email(),
#         "first_name": fake.name(),
#         "last_name": fake.name(),
#         "date_of_birth": fake.date(),
#         "password": FAKE_PASSWORD_LENGTH_8
#     }
#     conn = boto3.client("ses", region_name=common.get_settings().REGION_NAME)
#     conn.verify_email_identity(EmailAddress=common.get_settings().SENDER_EMAIL)
#
#     authenticated_api_client.post("/users", json=create_user)
#     statement = select(Users).where(Users.email == create_user["email"])
#     user = session.exec(statement).one()
#     sender_id = user.user_id
#     recipient_id = authenticated_api_client.user_id
#
#     friend_request = FriendRequests(sender_id=sender_id,
#                                     recipient_id=recipient_id,
#                                     message="Let's be friends.")
#     session.add(friend_request)
#     session.commit()
#
#     request_response = ResponseOnFriendRequest(sender_id=sender_id,
#                                                reaction_on_request=True)
#
#     response = authenticated_api_client.put("/me/friend_requests", data=request_response.json())
#     assert response.status_code == 200
#
#     statement = select(FriendRequests)
#     friend_request = session.exec(statement).one()
#
#     assert friend_request.request_status == "accepted"
#
#
# def test_response_on_invalid_friend_request(authenticated_api_client: TestClient):
#     response_info = ResponseOnFriendRequest(sender_id=5, reaction_on_request=True)
#     response = authenticated_api_client.put(f"/me/friend_requests", data=response_info.json())
#     assert response.status_code == 204
#
#
# # TESTS FOR USER SEARCH#
# def test_search_user_if_current_user_is_not_authenticated(api_client):
#     response = api_client.get("/me/search_user")
#     assert response.status_code == 401
#
#
# @mock_ses
# def test_add_new_user_and_search_username_is_in_database(authenticated_api_client):
#     valid_request = {
#         "username": "marko",
#         "first_name": fake.name(),
#         "last_name": fake.name(),
#         "date_of_birth": fake.date(),
#         "email": fake.email(),
#         "password": FAKE_PASSWORD_LENGTH_8
#
#     }
#     conn = boto3.client("ses", region_name=common.get_settings().REGION_NAME)
#     conn.verify_email_identity(EmailAddress=common.get_settings().SENDER_EMAIL)
#     authenticated_api_client.post("/users", json=valid_request)
#
#     valid_request1 = {
#         "search_username": "marko",
#     }
#
#     response = authenticated_api_client.get("/me/search_user", params=valid_request1)
#     assert response.status_code == 200
#     assert response.json()["username"] == "marko"
#
#
# @mock_ses
# def test_add_new_user_and_search_wrong_username(authenticated_api_client):
#     valid_request = {
#         "username": "marija",
#         "first_name": fake.name(),
#         "last_name": fake.name(),
#         "date_of_birth": fake.date(),
#         "email": fake.email(),
#         "password": FAKE_PASSWORD_LENGTH_8
#
#     }
#     conn = boto3.client("ses", region_name=common.get_settings().REGION_NAME)
#     conn.verify_email_identity(EmailAddress=common.get_settings().SENDER_EMAIL)
#     authenticated_api_client.post("/users", json=valid_request)
#
#     valid_request1 = {
#         "search_username": "marko",
#     }
#
#     response = authenticated_api_client.get("/me/search_user", params=valid_request1)
#     assert response.status_code == status.HTTP_404_NOT_FOUND
#
#
# # TESTS FOR RECOMMENDATION #
#
# def test_get_recommendation_if_current_user_not_authenticated(api_client: TestClient):
#     response = api_client.get("/me/recommendation")
#     assert response.status_code == 401
#
#
# @mock_ses
# def test_get_valid_recommendation(authenticated_api_client: TestClient):
#     for i in range(5):
#         valid_request = {
#             "username": fake.name(),
#             "first_name": fake.name(),
#             "last_name": fake.name(),
#             "date_of_birth": fake.date(),
#             "email": fake.email(),
#             "password": FAKE_PASSWORD_LENGTH_8
#
#         }
#         conn = boto3.client("ses", region_name=common.get_settings().REGION_NAME)
#         conn.verify_email_identity(EmailAddress=common.get_settings().SENDER_EMAIL)
#         authenticated_api_client.post("/users", json=valid_request)
#     response = authenticated_api_client.get("/me/recommendation")
#     assert response.status_code == 200
#
#
# def test_user_without_recommendation(authenticated_api_client: TestClient):
#     response = authenticated_api_client.get("/me/recommendation")
#     assert response.json() == "No recommendation at the moment."
#
#
# # TESTS FOR SENDING EMAIL REGISTRATION #
# @mock_ses
# def test_user_registration_and_sanding_verification_mail(api_client: TestClient):
#     valid_request = {
#         "username": fake.name(),
#         "first_name": fake.name(),
#         "last_name": fake.name(),
#         "date_of_birth": fake.date(),
#         "email": fake.email(),
#         "password": FAKE_PASSWORD_LENGTH_8
#     }
#
#     conn = boto3.client("ses", region_name=common.get_settings().REGION_NAME)
#     conn.verify_email_identity(EmailAddress=common.get_settings().SENDER_EMAIL)
#
#     response = api_client.post("/users", json=valid_request)
#     assert response.status_code == 201
#
#     send_quota = conn.get_send_quota()
#     sent_count = int(send_quota["SentLast24Hours"])
#     assert sent_count == 2  # Todo: Determine why this is 2 now despite single TO
#
#
# # TESTS FOR PASSWORD RECOVERY #
# def test_send_mail_for_reset_password_user_does_not_exist(api_client: TestClient):
#     info = {"user_email": fake.email()}
#     # because of protection user will be got successfully message
#     # even if he doesn't exist
#     response = api_client.post("/me/forgot_password", json=info)
#     assert response.status_code == 404
#     assert response.json()["detail"] == "Email sent successfully."
#
#
# def test_send_email_for_reset_password_valid_values(not_authenticated_api_client: TestClient, monkeypatch):
#     user = not_authenticated_api_client.user_data
#     user_email = {"user_email": user["email"]}
#     mock = MagicMock()
#     mock.return_value = {"message": "Email sent successfully."}
#     monkeypatch.setattr(
#         "cute_be.api_functions."
#         "user_functions.send_email_for_password_recovery",
#         mock,
#     )
#     response = not_authenticated_api_client.post("/me/forgot_password", json=user_email)
#     assert response.json()["message"] == "Email sent successfully."
#     mock.assert_called()
#
#
# @mock_ses
# def test_user_resets_password_valid_values(not_authenticated_api_client: TestClient):
#     payload = {"email": not_authenticated_api_client.user_data["email"]}
#     token = generate_token(data=payload, purpose=TokenPurpose.PASSWORD, expires=1)
#
#     new_password = {"token": token, "new_password": fake.password()}
#
#     response = not_authenticated_api_client.put("/me/forgot_password", json=new_password)
#     assert response.status_code == 200
#
#
# # TEST FOR REPORT USER #
# @mock_ses
# def test_report_user_valid_value(authenticated_api_client):
#     session = authenticated_api_client.session
#     create_account = {
#         "username": fake.name(),
#         "email": fake.email(),
#         "first_name": fake.name(),
#         "last_name": fake.name(),
#         "date_of_birth": fake.date(),
#         "password": FAKE_PASSWORD_LENGTH_8
#     }
#     conn = boto3.client("ses", region_name=common.get_settings().REGION_NAME)
#     conn.verify_email_identity(EmailAddress=common.get_settings().SENDER_EMAIL)
#
#     response = authenticated_api_client.post("/users", json=create_account)
#     assert response.status_code == 201
#
#     statement = select(Users).where(Users.username == create_account["username"])
#     user = session.exec(statement).one()
#     reported_user_id = user.user_id
#
#     valid_request1 = {
#         "reported_user_id": reported_user_id,
#         "reported_message": fake.paragraph(),
#         "report_category": "hate speech"
#     }
#     response = authenticated_api_client.post("/report", json=valid_request1)
#     assert response.status_code == 201
#
#
# def test_report_user_invalid_reported_user_id(authenticated_api_client):
#     valid_request1 = {
#         "reported_user_id": 0,
#         "reported_message": fake.paragraph(),
#         "report_category": "other"
#     }
#     response = authenticated_api_client.post("/report", json=valid_request1)
#     assert response.status_code == 400
#
#
# @mock_ses
# def test_report_user_with_invalid_report_message_length(authenticated_api_client):
#     session = authenticated_api_client.session
#     create_account = {
#         "username": fake.name(),
#         "email": fake.email(),
#         "first_name": fake.name(),
#         "last_name": fake.name(),
#         "date_of_birth": fake.date(),
#         "password": FAKE_PASSWORD_LENGTH_8
#     }
#     conn = boto3.client("ses", region_name=common.get_settings().REGION_NAME)
#     conn.verify_email_identity(EmailAddress=common.get_settings().SENDER_EMAIL)
#
#     response = authenticated_api_client.post("/users", json=create_account)
#     assert response.status_code == 201
#
#     statement = select(Users).where(Users.username == create_account["username"])
#     user = session.exec(statement).one()
#     reported_user_id = user.user_id
#
#     valid_request1 = {
#         "reported_user_id": reported_user_id,
#         "reported_message": "a" * 3,
#         "report_category": "other"
#     }
#     response = authenticated_api_client.post("/report", json=valid_request1)
#     assert response.status_code == 422
#
#
# def test_report_user_no_values(authenticated_api_client):
#     response = authenticated_api_client.post("/report")
#     assert response.status_code == 422
#
#
# def test_report_user_if_current_user_is_not_authenticated(api_client: TestClient):
#     response = api_client.post("/report")
#     assert response.status_code == 401
#
#
# @mock_ses
# def test_report_user_add_invalid_report_category(authenticated_api_client):
#     session = authenticated_api_client.session
#     create_account = {
#         "username": fake.name(),
#         "email": fake.email(),
#         "first_name": fake.name(),
#         "last_name": fake.name(),
#         "date_of_birth": fake.date(),
#         "password": FAKE_PASSWORD_LENGTH_8
#     }
#     conn = boto3.client("ses", region_name=common.get_settings().REGION_NAME)
#     conn.verify_email_identity(EmailAddress=common.get_settings().SENDER_EMAIL)
#
#     response = authenticated_api_client.post("/users", json=create_account)
#     assert response.status_code == 201
#
#     statement = select(Users).where(Users.username == create_account["username"])
#     user = session.exec(statement).one()
#     reported_user_id = user.user_id
#
#     valid_request1 = {
#         "reported_user_id": reported_user_id,
#         "reported_message": fake.paragraph(),
#         "report_category": "aaaaaaaaaaa"
#     }
#     response1 = authenticated_api_client.post("/report", json=valid_request1)
#     assert response1.status_code == 422
#
#
# @mock_ses
# def test_report_user_without_reported_message(authenticated_api_client):
#     session = authenticated_api_client.session
#     create_account = {
#         "username": fake.name(),
#         "email": fake.email(),
#         "first_name": fake.name(),
#         "last_name": fake.name(),
#         "date_of_birth": fake.date(),
#         "password": FAKE_PASSWORD_LENGTH_8
#     }
#     conn = boto3.client("ses", region_name=common.get_settings().REGION_NAME)
#     conn.verify_email_identity(EmailAddress=common.get_settings().SENDER_EMAIL)
#
#     response = authenticated_api_client.post("/users", json=create_account)
#     assert response.status_code == 201
#
#     statement = select(Users).where(Users.username == create_account["username"])
#     user = session.exec(statement).one()
#     reported_user_id = user.user_id
#
#     valid_request1 = {
#         "reported_user_id": reported_user_id,
#         "report_category": "hate speech"
#     }
#     response = authenticated_api_client.post("/report", json=valid_request1)
#     assert response.status_code == 422
#
#
# # TESTS FOR GETTING ALL REPORTS
# @mock_ses
# def test_report_one_user_and_admin_gets_one_report(admin_api_client):
#     session = admin_api_client.session
#     create_account = {
#         "username": fake.name(),
#         "email": fake.email(),
#         "first_name": fake.name(),
#         "last_name": fake.name(),
#         "date_of_birth": fake.date(),
#         "password": FAKE_PASSWORD_LENGTH_8
#     }
#     conn = boto3.client("ses", region_name=common.get_settings().REGION_NAME)
#     conn.verify_email_identity(EmailAddress=common.get_settings().SENDER_EMAIL)
#
#     response = admin_api_client.post("/users", json=create_account)
#     assert response.status_code == 201
#
#     statement = select(Users).where(Users.username == create_account["username"])
#     user = session.exec(statement).one()
#     reported_user_id = user.user_id
#
#     valid_request1 = {
#         "reported_user_id": reported_user_id,
#         "reported_message": fake.paragraph(),
#         "report_category": "bulling and harassment"
#     }
#     response1 = admin_api_client.post("/report", json=valid_request1)
#     assert response1.status_code == 201
#
#     response2 = admin_api_client.get("/reports")
#     assert response2.status_code == 200
#     assert len(response2.json()) == 1
#
#
# def test_get_empty_list_of_reports_if_current_user_is_admin(admin_api_client: TestClient):
#     response = admin_api_client.get("/reports")
#     assert response.status_code == 200
#     assert response.json() == []
#
#
# def test_get_reports_if_current_user_is_authenticated_but_not_admin(authenticated_api_client):
#     response = authenticated_api_client.get("/reports")
#     assert response.status_code == 403
#
#
# def test_get_reports_if_current_user_is_not_authenticated(api_client):
#     response = api_client.get("/reports")
#     assert response.status_code == 401
#
#
# def test_get_report_category_url_and_return_all_report_categories(api_client):
#     response = api_client.get("/report-category")
#     assert response.status_code == 200
#     assert response.json() == ['spam', 'hate speech', 'bulling and harassment', 'other']
#
#
# # TESTS FOR CHECKING IF ACCOUNT IS COMPLETED #
# @mock_ses
# def test_create_uncompleted_account_and_fill_empty_fields(authenticated_api_client):
#     session = authenticated_api_client.session
#     create_account = {
#         "username": fake.name(),
#         "first_name": fake.name(),
#         "last_name": fake.name(),
#         "email": fake.email(),
#         "password": FAKE_PASSWORD_LENGTH_8,
#     }
#     conn = boto3.client("ses", region_name=common.get_settings().REGION_NAME)
#     conn.verify_email_identity(EmailAddress=common.get_settings().SENDER_EMAIL)
#
#     authenticated_api_client.post("/users", json=create_account)
#
#     statement = select(Users).where(Users.username == create_account["username"])
#     user = session.exec(statement).one()
#
#     rest_fields = UpdateUser(username=create_account["username"],
#                              first_name=create_account["first_name"],
#                              last_name=create_account["last_name"],
#                              pronounce="he",
#                              date_of_birth=fake.date(),
#                              introduction_field=fake.sentence(),
#                              preferred_language=Languages.DEUTSCH.value,
#                              image_url=fake.image_url())
#
#     result = fill_empty_fields(edit_data=rest_fields, db=session, user=user)
#     assert result["message"] == "Account is completed."
#
#
# @mock_ses
# def test_check_if_auth_api_client_have_completed_account(authenticated_api_client):
#     session = authenticated_api_client.session
#     create_account = {
#         "username": fake.name(),
#         "first_name": fake.name(),
#         "last_name": fake.name(),
#         "email": fake.email(),
#         "password": FAKE_PASSWORD_LENGTH_8,
#     }
#
#     conn = boto3.client("ses", region_name=common.get_settings().REGION_NAME)
#     conn.verify_email_identity(EmailAddress=common.get_settings().SENDER_EMAIL)
#
#     authenticated_api_client.post("/users", json=create_account)
#
#     statement = select(Users).where(Users.username == create_account["username"])
#     user = session.exec(statement).one()
#
#     rest_fields = UpdateUser(username=create_account["username"],
#                              first_name=create_account["first_name"],
#                              last_name=create_account["last_name"],
#                              pronounce=None,
#                              date_of_birth=fake.date(),
#                              introduction_field=fake.sentence(),
#                              preferred_language=Languages.DEUTSCH.value,
#                              image_url=fake.image_url())
#
#     result = fill_empty_fields(edit_data=rest_fields, db=session, user=user)
#     assert result["message"] == "Please complete your account."
#
#
# # TEST FOR GET ALL FRIENDS#
# def test_get_friends_if_current_user_not_authenticated(api_client: TestClient):
#     response = api_client.get("/me/friends")
#     assert response.status_code == 401
#
#
# def test_get_user_friends_if_user_doesnt_have_friends(authenticated_api_client: TestClient):
#     response = authenticated_api_client.get("/me/friends")
#     assert response.status_code == 200
#     assert len(response.json()) == 0
#
#
# @mock_ses
# def test_add_friend_and_get_friend(authenticated_api_client: TestClient):
#     session = authenticated_api_client.session
#     valid_request = {
#         "username": "zika",
#         "email": fake.email(),
#         "first_name": fake.name(),
#         "last_name": fake.name(),
#         "password": FAKE_PASSWORD_LENGTH_8,
#
#     }
#
#     conn = boto3.client("ses", region_name=common.get_settings().REGION_NAME)
#     conn.verify_email_identity(EmailAddress=common.get_settings().SENDER_EMAIL)
#
#     authenticated_api_client.post("/users", json=valid_request)
#     recipient_id = authenticated_api_client.user_id
#
#     friend_request = FriendRequests(sender_id=2,
#                                     recipient_id=recipient_id,
#                                     message="Let's be friends.")
#     session.add(friend_request)
#     session.commit()
#
#     request_response = ResponseOnFriendRequest(sender_id=2,
#                                                reaction_on_request=True)
#
#     response = authenticated_api_client.put("/me/friend_requests", data=request_response.json())
#     assert response.status_code == 200
#
#     statement = select(FriendRequests)
#     friend_request = session.exec(statement).one()
#
#     assert friend_request.request_status == "accepted"
#
#     response1 = authenticated_api_client.get("/me/friends")
#     assert response1.status_code == 200
#     assert len(response1.json()) == 1
#     assert response1.json()[0]['username'] == "zika"
#
#
# @mock_ses
# def test_add_8_friends_and_get_8_friends(authenticated_api_client: TestClient):
#     session = authenticated_api_client.session
#     recipient_id = authenticated_api_client.user_id
#     for i in range(8):
#         valid_request = {
#             "username": fake.name(),
#             "first_name": fake.name(),
#             "last_name": fake.name(),
#             "email": fake.email(),
#             "password": FAKE_PASSWORD_LENGTH_8
#         }
#
#         conn = boto3.client("ses", region_name=common.get_settings().REGION_NAME)
#         conn.verify_email_identity(EmailAddress=common.get_settings().SENDER_EMAIL)
#
#         authenticated_api_client.post("/users", json=valid_request)
#         sender_id = i + 1
#
#         friend_request = FriendRequests(sender_id=sender_id,
#                                         recipient_id=recipient_id,
#                                         message="Let's be friends.")
#         session.add(friend_request)
#         session.commit()
#
#         request_response = ResponseOnFriendRequest(sender_id=sender_id,
#                                                    reaction_on_request=True)
#
#         response = authenticated_api_client.put("/me/friend_requests", data=request_response.json())
#         assert response.status_code == 200
#
#     response = authenticated_api_client.get("/me/friends")
#     assert response.status_code == 200
#     assert len(response.json()) == 8
