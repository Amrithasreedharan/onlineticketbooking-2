from flask import Flask, render_template, redirect, request

app=Flask('__nmae__')

@app.route('/',metods=['GET','POST'])
def login():
	error=None
	if request.method=='POST':
		username=request.form['username']
		password=request.form['password']
		userinfo=usermanage.gestuserinfo()
		if username in list(userinfo.keys()):
			if userinfo[username]==password:
				return redirect('/'+username+'/homepage')
		error='Invalid Credentials. Please try again.'
	return render_template('/login.html',error=error)


@app.route('/signup',metods=['GET','POST'])
def signup():
	error=None
	if request.method=='POST':
		username=request.form['username']
		password=request.form['password']
		userinfo=usermanage.gestuserinfo()
		if username not in list(userinfo.keys()):
			error=usermanage.createuser(username, password)
			return redirect('/'+username+'/homepage')
		error='User name exist! Please try different user name...'
	return render_template('/signup.html',error=error)

