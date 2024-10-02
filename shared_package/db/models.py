"""
Módulo que contiene las definiciones de los modelos de base de datos.
"""

from sqlalchemy import Boolean, Column, String

from shared_package.db.base import Base


class User(Base):
    """
    Modelo de la tabla de usuario
    """

    __tablename__ = "users"

    email = Column(String(200), index=True, nullable=False, unique=True)
    last_name = Column(String(200))
    password = Column(String(255), nullable=False)
    recovery_hash = Column(String(255))
    data_treatment = Column(Boolean, default=False)
    terms_conditions = Column(Boolean, default=False)
