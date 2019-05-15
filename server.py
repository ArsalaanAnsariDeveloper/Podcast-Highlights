from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
from pydub import AudioSegment
app = Flask(__name__)


data = []

fullPodcasts =  {"Startup Podcast Episode 1": "https://s3.amazonaws.com/ui-podcast-bucket/startupEpisode1.mp3", "Startup Podcast Episode 2": "https://s3.amazonaws.com/ui-podcast-bucket/startupEpisode2.mp3", "This American Life Episode 1": "https://s3.amazonaws.com/ui-podcast-bucket/talEpisode1.mp3", "This American Life Episode 2": "https://s3.amazonaws.com/ui-podcast-bucket/talEpisode2.mp3"}





@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name) 

@app.route('/people')
def people(name=None):
    return render_template('people.html', data=data)  

@app.route('/cut')
def cut():
    return render_template('example-2.html')
    
@app.route('/f_episodes')
def f_episodes():
    global fullPodcasts
    return jsonify(data = fullPodcasts)


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


@app.route('/upload_podcast', methods=['POST'])
def upload_podcast():

    global data 
    json_data = request.form 
    print(json_data)
    data.append(json_data)


    return jsonify(data = data)


@app.route('/get_podcast', methods=['GET'])
def get_podcast():

    global data

    if(len(data) >0 ):
        return jsonify(data = data[-1])
    else:
        return jsonify(data = "")



if __name__ == '__main__':
   app.run(debug = True)




