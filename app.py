from flask import Flask, render_template, request, url_for, flash, redirect
from forms import CourseForm, columns
from pprint import pprint
import os
import numpy as np
import sklearn
import pickle
import humanize
from datetime import timedelta

app = Flask(__name__)
secret_key = os.getenv('SECRET_KEY')
app.config['SECRET_KEY'] = secret_key


form_data = {key: None for key in columns}
pred_data = None

CATEGORIES = [1934, 3305, 10956, 25866]
CATEGORY_CONVERSION = ['0-32 min', '33-55 min', '56 min-3hr','3-7 hrs']

def print_categories():
    global CATEGORIES
    for i in range(len(CATEGORIES)):
        print(f"{convert(CATEGORIES[i])}   \t{i}")

def convert(seconds):
	return humanize.naturaldelta(timedelta(seconds=seconds))


@app.route('/', methods=('GET', 'POST'))
def index():
	global pred_data, form_data
	form = CourseForm()
	if form.validate_on_submit():
		print(form._fields)
		form_data['sim_time'] 				= float(form.sim_time.data)
		form_data['surface_moisture'] 		= float(form.surface_moisture.data)
		form_data['timestep'] 				= float(form.timestep.data)
		form_data['wind_direction'] 		= float(form.wind_direction.data)
		form_data['wind_speed'] 			= float(form.wind_speed.data)
		form_data['canopy_moisture'] 		= float(form.canopy_moisture.data)
		form_data['run_max_mem_rss_bytes'] 	= float(form.run_max_mem_rss_bytes.data)
		form_data['area'] 					= float(form.area.data)
		form_data['steps_fire'] 			= float(form.steps_fire.data)
		pred_data = np.array(list(form_data.values()))
		return redirect(url_for('prediction'))
	print("errors" ,form.errors)
	return render_template('index.html', form=form)

# RENAME
@app.route('/prediction/')
def prediction():
	with open('models.pkl','rb') as file:
		models = pickle.load(file)
		print(models)
	print("======PREDICTION======")
	k = 'GradientBoosting'
	prediction = models[k].predict([pred_data])[0]
	print(prediction)
	print(CATEGORIES[prediction])
	prediction_str = CATEGORY_CONVERSION[prediction]
	return render_template('prediction.html', form_data=form_data.items(), prediction_str=prediction_str)
