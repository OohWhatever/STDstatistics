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
    <svg width="200" height="100" xmlns="http://www.w3.org/2000/svg">
        <rect width="100%" height="100%" fill="lightgrey" />
        <text x="10" y="30" font-size="20" fill="black">Username: {username}</text>
        <text x="10" y="60" font-size="20" fill="black">Position: {position}</text>
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
    return Response(svg_image, mimetype='image/svg+xml', headers={
        "Content-Disposition": f"attachment; filename=image{random_number}.svg",
        "Cache-Control": "no-cache, no-store, must-revalidate",
        "Pragma": "no-cache",
        "Expires": "0",
        "Cache-Control": "public, max-age=0"
    })
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
    app.run(debug=False,host='127.0.0.1',port=port_number)