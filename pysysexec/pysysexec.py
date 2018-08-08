#!/usr/bin/env python
from flask import Flask, request, Response, redirect, url_for, abort, render_template, flash
from flask_bootstrap import Bootstrap
import subprocess

app = Flask(__name__)

@app.route('/')
def greet():
    return render_template('index.html')

@app.route('/cmd', methods=['POST'])
def do_cmd():
    proc = subprocess.Popen(
                                [request.form['command']],
                                shell=True,
                                stdout=subprocess.PIPE
                                ).stdout.read()

    return Response(proc, mimetype='text/html')
    flash('Command executed')
    
if __name__ == "__main__":
    Bootstrap(app)
    # Once development is finished
    # app.run(host='0.0.0.0')
    app.secret_key = 'supersecret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    # Remove this for production
    app.debug = True
    app.run()
