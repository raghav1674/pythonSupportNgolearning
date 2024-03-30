from fastapi import FastAPI
from models.models import engine,User,create_db_and_tables,Session,select

# sqlalchemy - ORM library 
create_db_and_tables()


app = FastAPI()

@app.get("/")
async def index():
    return "Hello World"


@app.get("/users/")
def read_heroes():
    session = Session(engine)
    users = session.exec(select(User)).all()
    session.close()
    return users