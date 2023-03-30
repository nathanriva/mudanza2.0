#importamos los modulos para la que sera la coneccion entre el backend y la base de datos
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#importamos modulo para molde de tabla
from sqlalchemy.ext.declarative import declarative_base
#importamos modulos para definir la tabla
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean

#creamos la coneccion
engine = create_engine("postgresql://nathan:123@mypsqlcont:5432/mudanza")
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
    