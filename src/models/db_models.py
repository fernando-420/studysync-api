from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from src.database.connection import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    carrera = Column(String, nullable=False)
    semestre = Column(Integer, nullable=False)
    creado_en = Column(DateTime, default=datetime.utcnow)

    sesiones = relationship("Sesion", back_populates="organizador")


class Sesion(Base):
    __tablename__ = "sesiones"

    id = Column(Integer, primary_key=True, index=True)
    materia = Column(String, nullable=False)
    fecha = Column(String, nullable=False)
    hora = Column(String, nullable=False)
    organizador_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    creado_en = Column(DateTime, default=datetime.utcnow)

    organizador = relationship("Usuario", back_populates="sesiones")