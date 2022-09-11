#!/usr/bin/python3
"""Defines a City Model and inherits from SQLAlchemy Base and links
   to the MySQL table `cities`
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Represents a city for a MySQL database
    __tablename__ (str): The name of the MySQL table to store states
    id (sqlalchemy.Integer): The City's id
    name (sqlalchemy.String): The City's name
    state_id (sqlalchemy.Integer): The City's state_id
    """

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
