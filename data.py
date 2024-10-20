from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Weather(Base):
    __tablename__ = 'weather'
    id = Column(Integer, primary_key=True)
    city = Column(String)
    temp = Column(Float)
    feels_like = Column(Float)
    main = Column(String)
    dt = Column(Integer)

engine = create_engine('sqlite:///weather.db')
Base.metadata.create_all(engine)
