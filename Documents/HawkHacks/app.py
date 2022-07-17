#Authentication header
# curl --request GET \
#   --url https://api.assemblyai.com/v2/ \
#   --header 'authorization: YOUR-API-TOKEN'

import requests
from flask import Flask, render_template, request

app = Flask(__name__)

auth_key = 'a30b0d235ea04ce5946b07f391afd504'

@app.route('/', methods = ['POST', 'GET'])
def get_transcript():
    return render_template('index.html')
    
@app.route('/HawkHacks/templates/text.html?_ijt=ru8pe5a0phkec4omd1je5nf7ob&_ij_reload', methods = ['GET', 'POST'])
def get_text():
    return render_template('text.html')

