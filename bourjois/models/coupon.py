# coding:UTF-8

from .database import Base
from .base_class import InitUpdate
from sqlalchemy import Column, String, Integer, ForeignKey, FLOAT
from sqlalchemy.dialects.mysql import DOUBLE

COUPON = 'coupon'

class Coupon(Base, InitUpdate):
    '''用户'''
    __tablename__ = COUPON
    id = Column(Integer, primary_key=True)
    openid = Column(String(200), nullable=True)
    type = Column(String(10), nullable=True)
    name = Column(String(200), nullable=True)
    value = Column(String(10), nullable=True)