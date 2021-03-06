from sqlalchemy import Column, ForeignKey, Integer, String, Date, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Reading(Base):
    __tablename__ = 'values'
    id = Column(Integer, primary_key = True)
    dev_id = Column(String(16), ForeignKey('devices.id'))
    value = Column(Integer)
    date = Column(DateTime, default=datetime.datetime.utcnow)

class Devices(Base):
    __tablename__ = 'devices'
    id = Column(String(16), primary_key = True)
    sensor_type = Column(String(16))

engine = create_engine('mysql+mysqldb://root:example@db:3306/sensario')

Base.metadata.create_all(engine)
