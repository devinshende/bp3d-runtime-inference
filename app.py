from flask import Flask, render_template, request, url_for, flash, redirect
from forms import CourseForm
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


@app.route('/', methods=('GET', 'POST'))
def index():
    form = CourseForm()
    if form.validate_on_submit():
        print(form)
        print(form.sim_time.data)
        # courses_list.append({'title': form.sim_time.data,
        #                      'description': form.surface_moisture.data,
        #                      'price': form.wind_direction.data,
        #                      'available': form.area.data,
        #                      'level': form.steps_fire.data
        #                      })
        # print(courses_list)
        return redirect(url_for('courses'))
    print("errors" ,form.errors)
    return render_template('index.html', form=form)

@app.route('/courses/')
def courses():
    return render_template('courses.html', courses_list=courses_list)
