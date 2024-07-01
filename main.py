
from flask import Flask, request, Response
from flask import render_template
from svg_routes import generate_svg
from svg_routes import generatebb_svg
import requests
import random

app = Flask(__name__)

STANDOFF_API_URL = "https://api.standoff365.com/api/scoring-mgr/scoring/total/{username}"

def fetch_user_data(username):
    response = requests.get(STANDOFF_API_URL.format(username=username))
    response.raise_for_status()
    data = response.json()
    return data if data else None






@app.route('/help', methods=['GET'])
def mainasd():
    return("Please use /generate-svg?username=Your_Username or /generatebb-svg?username=Your_Username")

@app.route('/')
def hello():
  return render_template('home.html')

@app.route('/generate-svg', methods=['GET'])
def generate_svg_endpoint():
    username = request.args.get('username')
    if not username:
        return "Username parameter is required", 400
    
    user_data = fetch_user_data(username)
    if not user_data:
        return "User not found", 404
    
    random_number = random.randint(1, 100000000)
    username = user_data['username']
    position = user_data['crPosition']
    crVulnerability = user_data['crVulnerability']
    bbTotal = user_data['bbTotal']
    crBusinessRisk = user_data['crBusinessRisk']
    bbReportsCount = user_data['bbReportsCount']
    
    svg_image = generate_svg(username, position, crVulnerability, crBusinessRisk)
    return Response(svg_image, mimetype='image/svg+xml')





@app.route('/generatebb-svg', methods=['GET'])
def generatebb_svg_endpoint():
    username = request.args.get('username')
    if not username:
        return "Username parameter is required", 400
    
    user_data = fetch_user_data(username)
    if not user_data:
        return "User not found", 404
    
    random_number = random.randint(1, 100000000)
    username = user_data['username']
    bbPosition = user_data['bbPosition']
    bbTotal = user_data['bbTotal']
    bbReportsCount = user_data['bbReportsCount']
    
    bbsvg_image = generatebb_svg(username, bbPosition, bbReportsCount)
    return Response(bbsvg_image, mimetype='image/svg+xml')




@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r
port_number = 80
if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0',port=port_number)
