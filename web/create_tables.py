#! -*- coding: utf-8 -*-

from app.dbs import db

db.drop_all()
db.create_all()

