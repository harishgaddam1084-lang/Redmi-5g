from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
	return "Hello. Are you able to see this text "
@app.route("/admin")
def admin():
	return "This is admin page"

if __name__ == "__main__":
	app.run(host = "0.0.0.0",port = 5000,debug = True)