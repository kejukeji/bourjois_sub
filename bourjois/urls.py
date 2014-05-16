# coding: UTF-8
from flask.ext.admin import Admin
from flask.ext import restful
from bourjois.view.coupon import *
from bourjois.restfuls.countTime import *

from . import app

app.add_url_rule('/home','to_home',to_home,methods=('GET','POST'))
app.add_url_rule('/send','to_send',to_send,methods=('GET','POST'))
app.add_url_rule('/getCoupon','to_getCoupon',to_getCoupon,methods=('GET','POST'))
app.add_url_rule('/to_share','to_share',to_share,methods=('GET','POST'))
app.add_url_rule('/total','get_total_times',get_total_times,methods=('GET','POST'))

# 接口定义
api = restful.Api(app)
api.add_resource(ViewTimes,'/viewTimes')
api.add_resource(ClickTimes,'/clickTimes')