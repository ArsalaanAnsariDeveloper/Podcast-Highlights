from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)


current_id = 2
data = [
    {
        "id": 1,
        "name": "michael scott"
    },
    {
        "id": 2,
        "name": "jim halpert"
    },
]





@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name) 

@app.route('/people')
def people(name=None):
    return render_template('people.html', data=data)  
    


@app.route('/add_name', methods=['GET', 'POST'])
def add_name():
    global data 
    global current_id 

    json_data = request.get_json()   
    name = json_data["name"] 
    
    # add new entry to array with 
    # a new id and the name the user sent in JSON
    current_id += 1
    new_id = current_id 
    new_name_entry = {
        "name": name,
        "id":  current_id
    }
    data.append(new_name_entry)

    #send back the WHOLE array of data, so the client can redisplay it
    return jsonify(data = data)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
 

@app.route('/podcast', methods=['GET'])
def podcast():
    return render_template('podcast.html')

@app.route('/upload', methods=['GET'])
def upload():
    return render_template('upload.html')
    





if __name__ == '__main__':
   app.run(debug = True)



