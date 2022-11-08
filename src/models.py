import os
import sys
import datetime
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Person(Base):

    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    user_name = Column(String(250), nullable=False)
    email = Column(String(250) nullable=False)
    password = Column(String(250), nullable=False)
    create_account = Column(DateTime, default=datetime.datetime.utcnow)
    birth_year = Column(String(250), nullable=False)
    profile_photo = Column(String(250))

class Followers(Base):

    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    person_id_to = Column(Integer, ForeignKey('person.id'))
    person_id_from  = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

class Posts(Base):

    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

class Multimedia(Base):

    __tablename__ = 'multimedia'
    id = Column(Integer, primary_key=True)
    image_url = Column(String(250), nullable=False)
    video_url = Column(String(250), nullable=False)
    posts_id = Column(Integer, ForeignKey('posts.id'))
    posts = relationship(Posts)

class Comments(Base):

    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    text = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    posts_id = Column(Integer, ForeignKey('posts.id'))
    person = relationship(Person)
    posts = relationship(Posts)

    def to_dict(self):
        return {}
        
render_er(Base, 'diagram.png')