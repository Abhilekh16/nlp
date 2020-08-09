from app import db

class User(db.Model):
	
	id = db.Column(db.Integer, primary_key=True,index=True)
	season = db.Column(db.Integer, index=True)
	city = db.Column(db.Text,index=True)
	date = db.Column(db.Text,index=True)
	team1 = db.Column(db.String(50),index=True)
	team2 = db.Column(db.String(50),index=True)
	toss_winner = db.Column(db.String(50),index=True)
	toss_decision = db.Column(db.String(20),index=True)
	result = db.Column(db.String(20),index=True)
	winner = db.Column(db.String(50),index=True)
	win_by_runs = db.Column(db.Integer, index=True)
	win_by_wickets = db.Column(db.Integer, index=True)
	player_of_match = db.Column(db.String(50),index=True)
	venue = db.Column(db.String(50),index=True)

def init_db():
    db.create_all()

