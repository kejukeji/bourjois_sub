# coding:UTF-8

from bourjois.models.coupon import Coupon
from bourjois.models.database import db

def save(coupon):
    db.add(coupon)
    db.commit()

def find_by_id(id):
    return Coupon.query.filter(Coupon.id == id).first()

def update(coupon):
    b = find_by_id(coupon.id)
    b.update(name = coupon.name,value = coupon.value)
    db.commit()

def find_by_openId(open_id):
    coupon= Coupon.query.filter(Coupon.openid == open_id).all()
    return coupon