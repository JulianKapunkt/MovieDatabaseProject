from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as ss


db= SQLAlchemy()



class MovieModel(db.Model):
    __tablename__ = "movies"

    id = db.Column(db.Integer(), primary_key= True)
    name = db.Column(db.String())
    year = db.Column(db.Date())


    def __init__(self,name,year):
        self.name = name
        self.year = year

    # def __repr__(self):
    #     return f"{self.name} - {self.year}"

def select_data():
    engine= ss.create_engine("postgresql://postgres:Sani43226117@localhost:5432/movie_rating")
    connection = engine.connect()
    metadata = ss.MetaData()
    movies = ss.Table('movies', metadata,
                  ss.Column('id',ss.BIGINT, primary_key=True),
                  ss.Column('name',ss.String),
                  ss.Column('year',ss.String),
                  autoload_with=engine)
    query= ss.select(columns='*',from_obj=[movies])
    result= connection.execute(query)
    resultset = result.fetchall()

    
    return resultset
        