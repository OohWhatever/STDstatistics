
from flask import Flask, request, Response
import requests
import random

app = Flask(__name__)

STANDOFF_API_URL = "https://api.standoff365.com/api/scoring-mgr/scoring/total?page_number=1&pagesize=10&search={username}&sort=cyberrange_asc"

def fetch_user_data(username):
    response = requests.get(STANDOFF_API_URL.format(username=username))
    response.raise_for_status()
    data = response.json()
    return data['items'][0] if data['items'] else None

def generate_svg(username, position):
    svg_template = f'''
    <svg xmlns="http://www.w3.org/2000/svg" width="470" height="200">
   <style type="text/css">@import url('https://fonts.googleapis.com/css?family=Lato|Open+Sans|Oswald|Raleway|Roboto|Indie+Flower|Gamja+Flower');</style>
  <rect x="0" y="0" width="470" height="200" rx="20" ry="20" fill="#080820" />
    <text x="50%" y="30%" dominant-baseline="middle" text-anchor="middle" fill="white" font-size="35" font-weight="bold">
    STANDOFF365 RATING
  </text>
  <text x="50%" y="60%" dominant-baseline="middle" text-anchor="middle" fill="white" fill="white" font-size="18"  font-weight="bold" >
    Username: {username}
  </text>
  <text x="50%" y="80%" dominant-baseline="middle" text-anchor="middle" fill="white" font-size="18" font-weight="bold" >
    Rating: {position}
  </text>
</svg>
    '''
    return svg_template
@app.route('/', methods=['GET'])
def mainasd():
    return("Please use /generate-svg?username=Your_Username")
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
    position = user_data['position']
    
    svg_image = generate_svg(username, position)
    return Response(svg_image, mimetype='image/svg+xml')
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
