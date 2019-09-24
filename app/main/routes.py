from flask import render_template, redirect
from app.main import bp
from app.main.forms import EventForm


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    form = EventForm()
    if form.validate_on_submit():
        employees = form.employees_count.data
        salary = form.average_salary.data/(21*8)
        time = form.event_duration.data
        count = int(employees*salary/time)
        return render_template('index.html', cost=count)
    return render_template('index.html', form=form)
