
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
  <rect x="0" y="0" width="470" height="200" rx="20" ry="20" fill="#080820" />
<svg x="223" y="130" fill="white" version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" 
	 width="20px" height="20px" viewBox="0 0 31.891 31.891"
	 xml:space="preserve">
<g>
	<path d="M28.096,7.828c-2.101,0-3.804,1.702-3.804,3.801c0,0.252,0.025,0.499,0.074,0.738l-4.806,4.328
		c-0.407-0.149-0.85-0.231-1.312-0.231c-0.176,0-0.35,0.012-0.52,0.032l-2.726-3.641c0.131-0.385,0.201-0.798,0.201-1.227
		c0-2.1-1.702-3.801-3.8-3.801c-2.098,0-3.8,1.702-3.8,3.801c0,0.485,0.089,0.948,0.256,1.375l-3.128,3.572
		c-0.299-0.074-0.609-0.113-0.93-0.113C1.703,16.462,0,18.163,0,20.263c0,2.101,1.703,3.801,3.801,3.801
		c2.1,0,3.802-1.7,3.802-3.801c0-0.319-0.04-0.629-0.114-0.926l3.446-3.936c0.153,0.019,0.31,0.029,0.468,0.029
		c0.213,0,0.421-0.018,0.623-0.051l2.66,3.551c-0.156,0.414-0.24,0.863-0.24,1.332c0,2.101,1.702,3.801,3.799,3.801
		c2.101,0,3.802-1.7,3.802-3.801c0-0.184-0.013-0.362-0.037-0.539l4.955-4.462c0.354,0.11,0.731,0.169,1.125,0.169
		c2.098,0,3.801-1.702,3.801-3.801C31.895,9.53,30.193,7.828,28.096,7.828z"/>
</g>
</svg>

<svg x="108" y="108" width="20px" height="20px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M3 21C3 21.5523 3.44772 22 4 22C4.55228 22 5 21.5523 5 21H3ZM11.8584 15.0608C12.4051 15.139 12.9117 14.7592 12.9899 14.2125C13.0681 13.6658 12.6883 13.1592 12.1416 13.081L11.8584 15.0608ZM17.29 17.2929C16.8994 17.6834 16.8994 18.3166 17.29 18.7071C17.6805 19.0976 18.3137 19.0976 18.7042 18.7071L17.29 17.2929ZM15.0916 14.7507C14.954 15.2856 15.2759 15.8308 15.8108 15.9684C16.3457 16.1061 16.8908 15.7841 17.0285 15.2493L15.0916 14.7507ZM17.9971 20C17.4448 20 16.9971 20.4477 16.9971 21C16.9971 21.5523 17.4448 22 17.9971 22V20ZM18.0071 22C18.5594 22 19.0071 21.5523 19.0071 21C19.0071 20.4477 18.5594 20 18.0071 20V22ZM14 7C14 8.65685 12.6569 10 11 10V12C13.7614 12 16 9.76142 16 7H14ZM11 10C9.34315 10 8 8.65685 8 7H6C6 9.76142 8.23858 12 11 12V10ZM8 7C8 5.34315 9.34315 4 11 4V2C8.23858 2 6 4.23858 6 7H8ZM11 4C12.6569 4 14 5.34315 14 7H16C16 4.23858 13.7614 2 11 2V4ZM5 21C5 17.6863 7.68629 15 11 15V13C6.58172 13 3 16.5817 3 21H5ZM11 15C11.292 15 11.5786 15.0208 11.8584 15.0608L12.1416 13.081C11.7682 13.0276 11.387 13 11 13V15ZM18.997 15.5C18.997 15.6732 18.9516 15.8053 18.6776 16.0697C18.5239 16.218 18.3429 16.3653 18.0919 16.574C17.8536 16.7723 17.5741 17.0087 17.29 17.2929L18.7042 18.7071C18.92 18.4913 19.1405 18.3033 19.3709 18.1116C19.5887 17.9305 19.8452 17.7223 20.0665 17.5087C20.5426 17.0493 20.997 16.4314 20.997 15.5H18.997ZM17.997 14.5C18.5493 14.5 18.997 14.9477 18.997 15.5H20.997C20.997 13.8431 19.6539 12.5 17.997 12.5V14.5ZM17.0285 15.2493C17.1396 14.8177 17.5325 14.5 17.997 14.5V12.5C16.5978 12.5 15.4246 13.457 15.0916 14.7507L17.0285 15.2493ZM17.9971 22H18.0071V20H17.9971V22Z" fill="white"/>
</svg>
    <text x="50%" y="30%" dominant-baseline="middle" text-anchor="middle" fill="white" font-size="35" font-weight="bold">
    STANDOFF365 RATING
  </text>
  <text x="50%" y="60%" dominant-baseline="middle" text-anchor="middle" fill="white" font-size="18" font-weight="bold">
    Username: {username}</text>
  <text x="50%" y="80%" dominant-baseline="middle" text-anchor="middle" fill="white" font-size="18" font-weight="bold">
    Rating: {position}</text>
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
