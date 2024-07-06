# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 23:37:07 2024

@author: Administrator
"""

from flask import Flask
from functools import partial
 
app = Flask(__name__)
 
# 定义一个预设了 URL 规则的偏函数
admin_route = partial(app.route, '/admin')
 
@admin_route()
def admin_users():
    return "Admin users page"
 
# @admin_route('/settings')
# def admin_settings():
#     return "Admin settings page"
 
if __name__ == '__main__':
    app.run()