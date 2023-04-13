#importamos los modulos para la que sera la coneccion entre el backend y la base de datos
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#importamos modulo para molde de tabla
from sqlalchemy.ext.declarative import declarative_base
#importamos modulos para definir la tabla
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
#importamos los modulos para dotenv
import os 
from dotenv import load_dotenv

#establecemos las variables para el engine, esto debe incluirse en el mismo string de este mas adelante
USER_DB=os.getenv('USER_DB')
PSSWRD_DB=os.getenv('PSSWRD_DB')
CONT_DB=os.getenv('CONT_DB')
PORT_DB=os.getenv('PORT_DB')
NAME_DB=os.getenv('NAME_DB')

#creamos la coneccion
engine = create_engine(f"postgresql://{USER_DB}:{PSSWRD_DB}@{CONT_DB}:{PORT_DB}/{NAME_DB}")
Session = sessionmaker(engine)
session = Session()

#creamos el molde y la tabla
base = declarative_base()


class ARTTABLE(base):
    __tablename__ = 'tablearticulos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))

class BUYTABLE(base):
    __tablename__ = 'tablecompras'
    id_compra = Column(Integer, primary_key=True)
    id_art = Column(Integer, ForeignKey(ARTTABLE.id))
    cant = Column(Integer)
    in_stock = Column(Boolean)
    