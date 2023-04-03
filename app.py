from flask import Flask
# flask - module having Flask(class)
app = Flask(__name__)
# we're importing class and creating its object
@app.route("/")  #route helps to establish path
def hello_world():
  return "Hello World!"
if __name__ == '__main__': #case when we run python app.py
  app.run(host='0.0.0.0',debug=True)
'''if script is invoked using python command. we have created app but we don't want to run using flask run command, we're using with app.run()'''