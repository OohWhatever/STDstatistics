from flask import Flask, request, Response
import requests

app = Flask(__name__)

STANDOFF_API_URL = "https://api.standoff365.com/api/scoring-mgr/scoring/total?page_number=1&pagesize=10&search={username}&sort=cyberrange_asc"

def fetch_user_data(username):
    response = requests.get(STANDOFF_API_URL.format(username=username))
    response.raise_for_status()
    data = response.json()
    return data['items'][0] if data['items'] else None

def generate_svg(username, cr_position):
    svg_template = f'''
    <svg width="200" height="100" xmlns="http://www.w3.org/2000/svg">
        <rect width="100%" height="100%" fill="lightgrey" />
        <text x="10" y="30" font-size="20" fill="black">Username: {username}</text>
        <text x="10" y="60" font-size="20" fill="black">CR Position: {cr_position}</text>
    </svg>
    '''
    return svg_template

@app.route('/generate-svg', methods=['GET'])
def generate_svg_endpoint():
    username = request.args.get('username')
    if not username:
        return "Username parameter is required", 400
    
    user_data = fetch_user_data(username)
    if not user_data:
        return "User not found", 404
    
    username = user_data['username']
    cr_position = user_data['crPosition']
    
    svg_image = generate_svg(username, cr_position)
    return Response(svg_image, mimetype='image/svg+xml', headers={
        "Content-Disposition": "attachment; filename=image.svg"
    })

if __name__ == '__main__':
    app.run(debug=True)