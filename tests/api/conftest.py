#import bcrypt
import pytest
from faker import Faker
from fastapi.testclient import TestClient
from sqlmodel import create_engine, select
from sqlmodel import Session, SQLModel

from A1Task import PACKAGE_ROOT
from A1Task.api import main

from A1Task.common import get_session, get_database_url


@pytest.fixture
def api_client() -> TestClient:
    test_env = PACKAGE_ROOT / ".env_test"
    engine = create_engine(get_database_url(env_path=test_env))
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        app = main.app
        app.dependency_overrides[get_session] = lambda: session

        client = TestClient(app)
        client.session = session
        yield client
    SQLModel.metadata.drop_all(engine)
