from app.core.database import engine
from app.models.base import Base

# важно: регистрируем все модели
from app.models import *


def init_db():
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Done.")


if __name__ == "__main__":
    init_db()
