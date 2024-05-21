from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    
    if request.method in ['POST']:

        
        city    = request.form['city']
        apikey  = request.form['apikey']
        
        data = []

        return render_template('result.html',data=data)

    else:

        return render_template('home.html')



if __name__ == '__main__':
    app.run(debug=True)