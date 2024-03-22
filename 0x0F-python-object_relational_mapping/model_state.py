#!/usr/bin/python3
"""Using orm."""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

x = MetaData()
Base = declarative_base(metadata=x)


class State(Base):
    """Inherted from Base."""

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
