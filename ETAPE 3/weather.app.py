from flask import Flask
from flask import render_template
from flask import request

from askapi import ask_air, ask_weather

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    
    if request.method in ['POST']:
        
        city    = request.form['city']
        apikey  = request.form['apikey']
        
        airdata = ask_air(
                            city    = city,
                            apikey  = apikey
                        )
        weatherdata = ask_weather(
                            city    = city,
                            apikey  = apikey
                        )

        if "error" in weatherdata:
            print(weatherdata)
            data = {
            "air": airdata,
            "weather": {},
            }

        else:
            data = {
            "air": airdata,
            "weather": weatherdata,
            }
        return render_template('result.html',data=data,city=city)
    else:
        return render_template('home.html')



if __name__ == '__main__':
    app.run(debug=True)