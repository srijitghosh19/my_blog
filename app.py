from flask import Flask, render_template
# flask - module having Flask(class)
'''html file is in template folder.To use in app,we're using render_template'''
app = Flask(__name__)


# we're importing class and creating its object
@app.route("/")  #route helps to establish path
def hello_world():
  return render_template('home.html')
  #home_page.html is name of template


if __name__ == '__main__':  #case when we run python app.py
  app.run(host='0.0.0.0', debug=True,port=8001)
'''if script is invoked using python command. we have created app but we don't want to run using flask run command, we're using with app.run()'''