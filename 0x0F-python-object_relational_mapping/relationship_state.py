#!/usr/bin/python3
"""Defines a State Model and inherits from SQLAlchemy Base and links
   to the MySQL table `states`
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City

Base = declarative_base()


class State(Base):
    """Represents a state for a MySQL database

    __tablename__ (str): The name of the MySQL table to store states
    id (sqlalchemy.Integer): The State's id
    name (sqlalchemy.String): The State's name
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")