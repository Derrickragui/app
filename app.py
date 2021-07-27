from flask import Flask #import Flask from flask folder
app = Flask(__name__)#creating an instance

@app.route('/')#create our routes end point
def index():
   return 'Hello World'

if __name__ == '__main__':
   app.run()