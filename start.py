
from os import environ
from flask import *
app = Flask(__name__)

def buss(fro,to):
	x=int(fro)-int(to)
	if x<0:
		x=-x
	return x
	
	
@app.route("/", methods=['GET', 'POST'])
def home():
	return render_template('mainregisteration.html')

@app.route("/mov.html", methods=['GET', 'POST'])
def movie():
	if request.method=="POST":
		mtheatre=request.form['mtheatre']
		mname=request.form['mname']
		seats=request.form['seats']
		seats=str(int(seats)*100)
		return render_template('movbill.html',b2name=mtheatre, bname=mname, price=seats)
	return render_template('mov.html')

@app.route("/rail.html", methods=['GET', 'POST'])
def rail():
	if request.method=="POST":
		n=request.form['RS']
		if n=='1':
			RS="Trivandrum Railway Station"
		if n=='2':
			RS="Ernakulam Jnt Railway Station"
		if n=='3':
			RS="Calicut Railway Station"
		if n=='4':
			RS="Kannur Railway Station"
		price=str(40+int(n)*10)
		t=request.form['t']
		return render_template('irctc.html',bname=RS, price=price)
	return render_template('rail.html')

@app.route("/flightt.html", methods=['GET', 'POST'])
def flight():
	if request.method=="POST":
		airport=request.form['Apt']
		airline=request.form['air12']
		oneround=request.form['myRadio']
		seats=request.form['seats']
		seats=str(int(seats)*int(oneround)*1500)
		return render_template('flightbill.html',bname=airline, b2name=airport, price=seats)
	return render_template('flightt.html')

@app.route("/bus/save", methods=['GET', 'POST'])
def bus():
	if request.method == 'POST':
		busname=request.form['name1']
		fro=request.form['name12']
		to=request.form['name123']
		d=buss(fro,to)
		return render_template('KSRTC.html',price=d,bname=busname)
	return render_template('/bus.html')

def runappserver():
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '1234'))
    except ValueError:
        PORT = 1234
    app.run(HOST, PORT,debug=True)
@app.route('/pay.html')
def pay_page():
	return render_template('/pay.html')

if __name__ == '__main__':
	runappserver()
