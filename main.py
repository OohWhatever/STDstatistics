
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

def generate_svg(username, position, crVulnerability, bbTotal, crBusinessRisk):
    svg_template = f'''
   <svg xmlns="http://www.w3.org/2000/svg" width="470" height="180">
  <rect x="0" y="0" width="470" height="165" rx="20" ry="20" fill="url(#MyGradient)" />

    <text x="30" y="40" fill="white" font-size="25" font-weight="bold" font-family="Arial">
    STANDOFF365 metrics
  </text>
    
  <text x="30" y="80" fill="white" font-size="13" font-weight="bold" font-family="Arial">
    Username: </text>
   <text x="110" y="80" fill="#00ff33" font-size="13" font-weight="bold" font-family="Arial">
    {username}</text>
  <text x="75%" y="80" dominant-baseline="middle" text-anchor="middle" fill="white" font-size="17" font-weight="bold" font-family="Arial">
    CYBERRANGE RATING </text>
   <text x="75%" y="67%" dominant-baseline="middle" text-anchor="middle" fill="#ff0000" font-size="70" font-weight="bold" font-family="Arial">
    {position}</text>
  <text x="30" y="102" fill="white" font-size="13" font-weight="bold" font-family="Arial">
    Vuln score: </text>
   <text x="110" y="102" fill="#00ff33" font-size="13" font-weight="bold" font-family="Arial">
    {crVulnerability}</text>
   <text x="30" y="125" fill="white" font-size="13" font-weight="bold" font-family="Arial">
    Buisness Risc score: </text>
   <text x="170" y="125" fill="#00ff33" font-size="13" font-weight="bold" font-family="Arial">
    {crBusinessRisk}</text>
<defs>
        <linearGradient id="MyGradient">
          <stop offset="5%" stop-color="#660033" />
          <stop offset="95%" stop-color="#0e1231" />
        </linearGradient>
      </defs>
</svg>
    '''
    return svg_template


def generatebb_svg(username, bbPosition, bbReportsCount):
    bbsvg_template = f'''
   <svg xmlns="http://www.w3.org/2000/svg" width="300" height="70" fill="none">
    <rect width="220" height="20" y="48" x="10" rx="10" fill="url(#grad)" stroke="#FFFFFF" stroke-width="2"  />
  <defs>
    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color: #4f0014; stop-opacity: 1" />
      <stop offset="100%" style="stop-color: #252850; stop-opacity: 1" />
    </linearGradient>
  </defs>
  <polygon points="10,0 120,0 190,50 10,50" fill="#470736" rx="10" />
  <rect width="300" height="35" y="15" rx="10" fill="url(#grad)" stroke="#FFFFFF" stroke-width="2"  />
  <text x="10" y="38" fill="#f5f5f5" font-size="20" font-weight="bold" font-family="Arial">
    BugBounty Rating:</text>
   <text x="215" y="41" fill="#88f000" font-size="28" font-weight="bold" font-family="Arial">
    {bbPosition}</text>
    <text x="25" y="10" fill="#dbdbdb" font-size="11" font-weight="bold" font-family="Arial">
    STANDOFF365</text>
   <text x="25" y="63" fill="#dbdbdb" font-size="11" font-weight="bold" font-family="Arial">
    BugBounty report count:  </text>
 <text x="220" y="63" text-anchor="end" fill="#00ffa6" font-size="13" font-weight="bold" font-family="Arial">
  {bbReportsCount}
</text>
</svg>

    '''
    return bbsvg_template



@app.route('/', methods=['GET'])
def mainasd():
    return("Please use /generate-svg?username=Your_Username or /generatebb-svg?username=Your_Username")



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
    
    svg_image = generate_svg(username, position, crVulnerability, bbTotal, crBusinessRisk)
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
