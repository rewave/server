#!/usr/bin/python

from peewee import *
import datetime, time


db = SqliteDatabase("templates.db")

class BaseModel(Model):
	class Meta:
		database = db

class Pattern(BaseModel):
	name = CharField()
	threshold_lower = FloatField(default=0)
	key_code = IntegerField()
	st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
	created_at = DateTimeField(formats=["%Y-%m-%d %H:%M:%S"], default=st)

class MotionLog(BaseModel):
	pattern = ForeignKeyField(Pattern)
	timestamp = FloatField()
	ax = FloatField(default="0.0")
	ay = FloatField(default="0.0")
	az = FloatField(default="0.0")
	gx = FloatField(default="0.0")
	gy = FloatField(default="0.0")
	gz = FloatField(default="0.0")
	st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
	created_at = DateTimeField(formats=["%Y-%m-%d %H:%M:%S"], default=st)

def up():
	if not Pattern.table_exists() :	Pattern.create_table()
	if not MotionLog.table_exists() : MotionLog.create_table()

def main():
	up()

if __name__ == '__main__':
	main()