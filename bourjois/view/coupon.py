# coding:UTF-8
from flask import request, render_template
from flask import request, render_template, redirect, url_for
from bourjois.services.coupon_service import *
from bourjois.services.times_service import *

def to_home():
    return render_template('home.html')


def to_send():
    return render_template('test4.html')

def to_getCoupon():
    return render_template('test5.html')

def to_share():
    return render_template('share.html')

def get_total_times():
    t = get_times()
    return render_template('/total.html',
                           t=t)