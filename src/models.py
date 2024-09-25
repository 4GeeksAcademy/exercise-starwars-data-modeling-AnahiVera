import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime, Table, func
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False, unique=True)
    fullname = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    favorites = relationship("Favorite", back_populates="users")


class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name =  Column(String(100), nullable=False)
    description=description = Column(Text)
    favorites = relationship("Favorite", back_populates="characters")
    

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name =  Column(String(100), nullable=False)
    description=description = Column(Text)
    climate = Column(String(100))
    population = Column(Integer)
    favorites = relationship("Favorite", back_populates="planets")

class Favorite(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    character_id = Column(Integer, ForeignKey('characters.id'), nullable=True)
    planet_id = Column(Integer, ForeignKey('planets.id'), nullable=True)
    user = relationship("User", back_populates ="favorites")
    character = relationship("Character", back_populates ="favorites")
    planet = relationship("Planet", back_populates ="favorites")

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
