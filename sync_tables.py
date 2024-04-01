
from sqlalchemy import create_engine

from app.config import settings
from app.routers.pet.models import Author
from app.utilities.mdb import Base


def create_tables():
    engine = create_engine(settings.sync_database_url)
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    print(settings.sync_database_url)
    create_tables()
