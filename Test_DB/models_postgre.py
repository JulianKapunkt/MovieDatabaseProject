from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.sql import text


engine = create_engine("postgresql://postgres:yourPassword@localhost:5432/Users", echo = None)
meta = MetaData()


Users = Table(
    'users',meta,
    Column('username',String, primary_key=True),
    Column('clear_password',String),
    Column('email',String)
)

conn = engine.connect()
exp = Users.select()
#exp1 = text("INSERT INTO users (username,clear_password,email) values ('john','john123','john.wick@imdb.com');")

result = conn.execute(exp)

for row in result:
    print (row)

# conn.close()
# print (conn.closed)


# Insert Statement
# ins = Users.insert()
# print(ins)

# ins = Users.insert().values(username='alexa',clear_password='amazon')
# print (ins)

# # Execute Insert Statement
# result = conn.execute(ins)
row[0].username