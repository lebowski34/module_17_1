from app.backend.db import engine
from app.models import user, task

if __name__ == "__main__":
    from app.backend.db import Base
    Base.metadata.create_all(bind=engine)
    print("Таблицы успешно созданы!")
