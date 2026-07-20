import os
from sqlmodel import create_engine, Session

base_dir = os.path.dirname(os.path.abspath(__file__))
db_url = f"sqlite:///{os.path.join(base_dir, 'bangusbuhai.db')}"

engine = create_engine(db_url, connect_args={"check_same_thread": False})

def get_session():
    with Session(engine) as session:
        yield session

