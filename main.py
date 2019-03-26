from datetime import datetime
import os
import datetime

from flask import Flask, render_template, request, redirect, url_for, session
from passlib.hash import pbkdf2_sha256

from model import Task, User

app = Flask(__name__)


@app.route('/all')
def all_tasks():
    return render_template('all.jinja2', tasks=Task.select())


@app.route('/create', methods=['GET', 'POST'])
def create_task():

    if request.method == 'POST':
        task = str(request.form['task_name'])

        new_task = Task(name=task)
        new_task.save()
        return render_template('all.jinja2', tasks=Task.select())

    return render_template('create.jinja2')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
