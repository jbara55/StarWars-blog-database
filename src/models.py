import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class Personajes(Base):
    __tablename__ = 'Personajes'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    uid = Column(Integer, primary_key=True)
    height = Column(Integer)
    mass = Column(Integer)
    gender = Column(String)
    name = Column(String(50))
    homeworld = Column(String(50), ForeignKey('Planet.name'))
 
class Planet(Base):
    __tablename__ = 'Planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    diameter =  Column(Integer)
    poulation = Column(Integer)
    climate = Column(String)
    name = Column(String)
    relacionPersonaje= relationship("Personajes")
    
class Planet_vehicle(Base):
    __tablename__ = 'Planet_vehicle'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    idPlanet = Column(Integer,primary_key=True)
    manufacturaV = Column(String)
    

class Personaje_Vehiculo(Base):
    __tablename__ = 'Personaje_Vehiculo'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    piloto_uid = Column(Integer, primary_key=True)
    uid_name = Column(String)
  

class ListaFavoritos(Base):
    __tablename__ = 'ListaFavoritos'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    mail_usuario = Column(String)
    favoritoPersonaje = Column(Integer)
    favoritoPlaneta = Column(Integer)
    favoritoVehiculo = Column(String)
    
class Vehicles(Base):
    __tablename__ = 'Vehicles'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    name = Column(String,primary_key=True)
    model = Column(String)
    vehicle_class = Column(String)
    lenght = Column(Float)
    manufactura = Column(String)
   

class Usuario(Base):
    __tablename__ = 'Usuario'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    nombre = Column(String, primary_key=True)
    mail = Column(String)
    Password = Column(String)
    
    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
