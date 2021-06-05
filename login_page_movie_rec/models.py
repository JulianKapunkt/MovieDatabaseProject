from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.exc import MultipleResultsFound
from sqlalchemy.sql import text
from sqlalchemy.orm.exc import NoResultFound



engine = create_engine("postgresql://postgres:Sani43226117@localhost:5432/Users", echo = None)
meta = MetaData()


Users = Table(
    'users',meta,
    Column('username',String, primary_key=True),
    Column('clear_password',String),
    Column('email',String)
)


#exp1 = text("INSERT INTO users (username,clear_password,email) values ('john','john123','john.wick@imdb.com');")



# Insert Statement
# ins = Users.insert()
# print(ins)

# ins = Users.insert().values(username='alexa',clear_password='amazon')
# print (ins)

# # Execute Insert Statement
# result = conn.execute(ins)

def select_user(email, password):
    conn = engine.connect()
    select_query = Users.select().where(Users.c.email==email)
    conn.close()
    try:
        result= conn.execute(select_query).one_or_none()
        if result and str(password) == result.clear_password:
            return "Login Successfull, welcome %s"%(result.username)
        else:
            return "The email or password is not correct!"
    except MultipleResultsFound:
        return "There are more than one user with this email ! Alert the administrator !"




