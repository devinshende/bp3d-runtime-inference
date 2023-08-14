from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,
					 RadioField, DecimalField)
from wtforms.validators import InputRequired, Length

columns = [
	'sim_time',
	'surface_moisture',
	'timestep',
	'wind_direction',
	'wind_speed',
	'canopy_moisture',
	'run_max_mem_rss_bytes',
	'area',
	'steps_fire'
]

class CourseForm(FlaskForm):

	sim_time 				= IntegerField('sim_time',validators=[InputRequired()], default=1200)
	surface_moisture 		= DecimalField('surface_moisture',validators=[InputRequired()], default=10.2)
	timestep 				= IntegerField('timestep',validators=[InputRequired()],default=4)
	wind_direction			= IntegerField('wind_direction',validators=[InputRequired()],default=40)
	wind_speed 				= IntegerField('wind_speed',validators=[InputRequired()],default=20)
	canopy_moisture			= IntegerField('canopy_moisture',validators=[InputRequired()],default=1)
	run_max_mem_rss_bytes	= IntegerField('run_max_mem_rss_bytes',validators=[InputRequired()],default=24)
	area 					= IntegerField('area',validators=[InputRequired()],default=400)
	steps_fire				= IntegerField('steps_fire',validators=[InputRequired()],default=100)

	# title = StringField('Title', validators=[InputRequired(), Length(min=10, max=100)])
	
	# description = TextAreaField('Course Description', 
	# 	validators=[InputRequired(), Length(max=200)])

	# price = IntegerField('Price', validators=[InputRequired()])
	
	# level = RadioField('Level', choices=['Beginner', 'Intermediate', 'Advanced'],
	# 	validators=[InputRequired()])



