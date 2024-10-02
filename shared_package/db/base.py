"""
Módulo que contiene la clase base para modelos de base de datos.
"""

from datetime import datetime

from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.orm import DeclarativeBase, declared_attr
from sqlalchemy_easy_softdelete.mixin import generate_soft_delete_mixin_class


class SoftDeleteMixin(
    generate_soft_delete_mixin_class(
        # This table will be ignored by the hook
        # even if the table has the soft-delete column
        # ignored_tables=[IgnoredTable(table_schema="public", name="users"),]
        ### from sqlalchemy_easy_softdelete.hook import IgnoredTable
    )
):
    """
    Mixin para manejar la eliminación lógica de registros.
    https://pypi.org/project/sqlalchemy-easy-softdelete/
    > use session.query(Fruit).execution_options(include_deleted=True).all()
    to include deleted parameters
    """

    # type hint for autocomplete IDE support
    deleted_at: datetime


class Base(DeclarativeBase, SoftDeleteMixin):
    """
    Clase base para modelos de base de datos.

    Esta clase proporciona funcionalidad común para todos los modelos de la base de datos.
    """

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    __name__: str

    # to generate tablename from classname
    @declared_attr
    def __tablename__(self) -> str:
        return self.__name__.lower()

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime, nullable=True)
