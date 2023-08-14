from flask import Flask, render_template, request, url_for, flash, redirect
from forms import CourseForm, columns
from pprint import pprint
import os

app = Flask(__name__)
secret_key = os.getenv('SECRET_KEY')
app.config['SECRET_KEY'] = secret_key

courses_list = [{
	'title': 'Python 101',
	'description': 'Learn Python basics',
	'price': 34,
	'available': True,
	'level': 'Beginner'
}]

in_data = {key: None for key in columns}

@app.route('/', methods=('GET', 'POST'))
def index():
	form = CourseForm()
	if form.validate_on_submit():
		print(form._fields)
		in_data['area'] 					= float(form.area.data)
		in_data['canopy_moisture'] 			= float(form.canopy_moisture.data)
		in_data['run_max_mem_rss_bytes'] 	= float(form.run_max_mem_rss_bytes.data)
		in_data['sim_time'] 				= float(form.sim_time.data)
		in_data['steps_fire'] 				= float(form.steps_fire.data)
		in_data['surface_moisture'] 		= float(form.surface_moisture.data)
		in_data['timestep'] 				= float(form.timestep.data)
		in_data['wind_direction'] 			= float(form.wind_direction.data)
		in_data['wind_speed'] 				= float(form.wind_speed.data)
		return redirect(url_for('courses'))
	print("errors" ,form.errors)
	return render_template('index.html', form=form)

@app.route('/courses/')
def courses():
	return render_template('courses.html', in_data=in_data.items())
