from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, scoped_session, sessionmaker
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String, Text, DateTime
from sqlalchemy_utils import database_exists, create_database

db_engine = create_engine(f'sqlite:///cars_park.db')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=db_engine))
Base = declarative_base()
Base.query = db_session.query_property()

if not database_exists(db_engine.url):
    create_database(db_engine.url)


class Driver(Base):
    __tablename__ = 'drivers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(80), nullable=False)
    last_name = Column(String(80), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow, default=datetime.utcnow)
    vehicles = relationship('Vehicle', backref='driver', lazy=True)

    def __str__(self):
        return f'{self.first_name}: {self.last_name}'


class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    driver_id = Column(Integer, ForeignKey('drivers.id'), nullable=True, default=0)
    make = Column(String(100), nullable=False)
    model = Column(String(100), nullable=False)
    plate_number = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow, default=datetime.utcnow)

    def __str__(self):
        return f'{self.plate_number}: {self.make}: {self.model}'


def init_db():
    Base.metadata.create_all(bind=db_engine)


init_db()
