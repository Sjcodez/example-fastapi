from fastapi.testclient import TestClient
import pytest
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base 
from app.main import app
from app.config import settings
from app.database import get_db
from sqlalchemy import create_engine
from app.database import Base, engine
from alembic import command



Base.metadata.create_all(bind=engine)

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'

engine = create_engine(SQLALCHEMY_DATABASE_URL) 

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


client = TestClient(app)

@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine) 
    db = TestingSessionLocal()
    try: 
        yield db
    finally:
        db.close()

@pytest.fixture()
def client(session):
    def overide_get_db():
        try: 
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = overide_get_db
    yield TestClient(app)