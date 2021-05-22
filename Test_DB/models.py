#from flask_sqlalchemy import SQLAlchemy as flask_Alchemy
import sqlalchemy


#db= flask_Alchemy()



# class users(db.Model):

#     username = db.Column(db.Integer(), primary_key= True)
#     name = db.Column(db.String())
#     year = db.Column(db.Date())


#     def __init__(self,name,year):
#         self.name = name
#         self.year = year

    # def __repr__(self):
    #     return f"{self.name} - {self.year}"

def select_data():
    engine= sqlalchemy.create_engine("postgresql://postgres:Sani43226117@localhost:5432/Users")
    connection = engine.connect()
    metadata = sqlalchemy.MetaData()
    user = sqlalchemy.Table('users', metadata,
                  sqlalchemy.Column('username',sqlalchemy.String, primary_key=True),
                  sqlalchemy.Column('clear_password',sqlalchemy.String),
                  sqlalchemy.Column('email',sqlalchemy.String),
                  autoload_with=engine)
    query= sqlalchemy.select(columns='*',from_obj=[user])
    sqlalchemy.JSON()
    result= connection.execute(query)
    resultset = result.fetchall()
    connection.close()

    
    return resultset
        


# d= select_data()
# print (d[0][2])