#!/usr/bin/env python
from flask import Flask, request, render_template, flash
from flask_script import Manager
#import ev3dev.ev3 as ev3
import time


app = Flask(__name__)
manager = Manager(app)

#leftmotor = ev3.LargeMotor('outA')
#rightmotor = ev3.LargeMotor('outD')

moves = 0

@app.route('/' , methods=["GET", "POST"])
def move():
    moves = []
    loop = True
    while loop == True:
        if request.method == 'POST':
            if request.form['submit'] == 'leftForward':
                moves.append("lf")
                print(moves)
                print"leftForward"
                return render_template('index.html')
            elif request.form['submit'] == 'rightForward':
                moves.append("rf")
                print(moves)
                print"rightForward"
                return render_template('index.html')
            elif request.form['submit'] == 'leftBack':
                moves.append("lb")
                print(moves)
                print"leftBack"
                return render_template('index.html')
            elif request.form['submit'] == 'rightBack':
                moves.append("rb")
                print(moves)
                print"rightBack"
                return render_template('index.html')
            else:
                return render_template('index.html')
        elif request.method == 'GET':
            return render_template('index.html')


@app.route('/register' , methods=["GET", "POST"])
def register():
    return render_template('register.html')


@app.route('/test' , methods=["GET", "POST"])
def test():
    return render_template('test.html')

if __name__ == '__main__':
    manager.run()
    app.run(debug=True)
