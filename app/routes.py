from app import app
from flask import render_template,request,redirect,jsonify
import nlpsql
import app.models as User,sqlite3


@app.route('/')
@app.route('/index')
def index():
	return render_template("nlpsearch.html");
#nlp input
@app.route('/',methods=['POST','GET'])
def nlp():
	textInput = request.form['search']
	search = nlpsql.queryGenerator(textInput)
	if 'query' in request.form:
		return search
	elif 'submit' in request.form:
		con=sqlite3.connect('app.db') 
		cur = con.cursor()
		query = cur.execute(search)
		data = query.fetchall()
		dataList =[]
		for d in data:
			temp=str(d)
			dataList.append(temp[2:len(temp)-2])
		if(dataList==[]):
			return 'No Search Result'

		return render_template('result.html',result=dataList)
