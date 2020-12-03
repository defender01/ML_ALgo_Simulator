#!flask/bin/python
from GradientDescent import gradientDescent as gdClass
from LineFitting import Visualization as linearVis
from PolynomialFitting import Visualization as polyVis
import pyrebase
import csv
from flask import Flask, request
from flask import render_template

app = Flask(__name__)

config = {
    "apiKey": "AIzaSyCUW8TF3Rc_aC_FdVJqt4mqKRM-sJj2mjE",
    "authDomain": "mlalgosimulator.firebaseapp.com",
    "databaseURL": "https://mlalgosimulator.firebaseio.com",
    "projectId": "mlalgosimulator",
    "storageBucket": "mlalgosimulator.appspot.com",
    "messagingSenderId": "717217949100"
}

firebase = pyrebase.initialize_app(config)


# @app.route('/')
# def output():
# 	# serve index template
# 	return render_template('test.html', name='Joe')

# endpotints
@app.route("/")
def hello():
    return "Welcome to Python Flask!"


@app.route('/loginPage')
def signUp():
    return render_template('loginPage.html')


@app.route("/takeInput", methods=["POST"])
def takeInput():
    print("reached destination python program")
    values = request.form['firstname'].split('*')
    uid = request.form['uid']
    print('uid = ' + uid)
    callingState = request.form['callingState']
    print('callingState =' + callingState)

    # Get a reference to the auth service
    auth = firebase.auth()

    # Get a reference to the database service
    database = firebase.database()
    database.child("gradientDescent").child(uid).child("iteration").set("111")

    # empty the csv file
    writeCsv = open("input.csv", "w")
    writer = csv.writer(writeCsv)
    writer.writerow("")
    writeCsv.close()

    # appending data in csv file
    writeCsv = open("input.csv", "a")
    writer = csv.writer(writeCsv)
    for i in range(0, len(values)):
        temp = values[i].split(',')
        print(temp)
        writer.writerow(temp)
    writeCsv.close()

    error = "no error occured"
    return render_template('loginPage.html', error=error)
    # return jsonify({'output': 'EXCELLENT'})


@app.route("/linearRegression", methods=["POST"])
def linearRegression():
    print("reached linearRegression python program")
    values = request.form['firstname'].split('*')
    uid = request.form['uid']
    print('uid = ' + uid)
    callingState = request.form['callingState']
    print('callingState =' + callingState)


    # empty the csv file
    writeCsv = open("D:\webDevelopment\Ml_Algo_Simulator\LineFitting\data.csv", "w")
    writer = csv.writer(writeCsv)
    writer.writerow("")
    writeCsv.close()

    # appending data in csv file
    writeCsv = open("D:\webDevelopment\Ml_Algo_Simulator\LineFitting\data.csv", "a")
    writer = csv.writer(writeCsv)
    for i in range(0, len(values)):
        temp = values[i].split(',')
        print(temp)
        writer.writerow(temp)
    writeCsv.close()

    lf = linearVis.Visualization()
    lf.call_simulation()

    error = "no error occured"
    return render_template('loginPage.html', error=error)
    # return jsonify({'output': 'EXCELLENT'})

@app.route("/polynomialRegression", methods=["POST"])
def polynomialRegression():
    print("reached polynomialRegression python program")
    values = request.form['firstname'].split('*')
    uid = request.form['uid']
    print('uid = ' + uid)
    callingState = request.form['callingState']
    print('callingState =' + callingState)


    # empty the csv file
    writeCsv = open("D:\webDevelopment\Ml_Algo_Simulator\PolynomialFitting\data.csv", "w")
    writer = csv.writer(writeCsv)
    writer.writerow("")
    writeCsv.close()

    # appending data in csv file
    writeCsv = open("D:\webDevelopment\Ml_Algo_Simulator\PolynomialFitting\data.csv", "a")
    writer = csv.writer(writeCsv)
    for i in range(0, len(values)):
        temp = values[i].split(',')
        print(temp)
        writer.writerow(temp)
    writeCsv.close()

    pf = polyVis.Visualization()
    pf.call_simulation()

    error = "no error occured"
    return render_template('loginPage.html', error=error)
    # return jsonify({'output': 'EXCELLENT'})




@app.route("/gradientDescent", methods=["POST"])
def gradientDescent():
    print("reached destination python program")
    # values = request.form['firstname'].split('*')
    uid = request.form['uid']
    print('uid = ' + uid)
    callingState = request.form['callingState']
    print('callingState =' + callingState)
    alpha = float(request.form['alpha'])
    print('alpha=',alpha)
    startX = float(request.form['startX'])
    print('startX=',startX)
    gd = gdClass.gradientDescent()
    no_of_iterations = gd.call_simulation(startX,alpha)
    print("iteration no= ",no_of_iterations)

    # Get a reference to the auth service
    auth = firebase.auth()

    # Get a reference to the database service
    database = firebase.database()
    database.child("gradientDescent").child(uid).child("iteration").set(no_of_iterations)

    error = "no error occured"
    return render_template('loginPage.html', error=error)
    # return jsonify({'output': 'EXCELLENT'})


if __name__ == '__main__':
    # run!
    app.run(debug=True)
# If you wish to view your scripts on a different computer on the same network, change app.run() to:
# app.run("0.0.0.0", "5010")
