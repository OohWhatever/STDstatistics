
from flask import Flask, request, Response
from flask import render_template
from svg_routes import generate_svg
from svg_routes import generatebb_svg
import requests
import random

app = Flask(__name__)

#Ссылки на апи стендофа
STANDOFF_API_URL = "https://api.standoff365.com/api/scoring-mgr/scoring/total/{username}"
STANDOFFBB_API_URL = "https://api.standoff365.com/api/bug-bounty/metrics/user/{username}"

# Здесь мы вытягиваем из апишек информацию о нашем профиле
def fetch_user_data(username):
    response = requests.get(STANDOFF_API_URL.format(username=username))
    response.raise_for_status()
    data = response.json()
    return data if data else None

def fetch_user_bbdata(username):
    response = requests.get(STANDOFFBB_API_URL.format(username=username))
    response.raise_for_status()
    data = response.json()
    print(data)
    return data if data else None

# Путь до хелп 
@app.route('/help', methods=['GET'])
def mainasd():
    return("Please use /generate-svg?username=Your_Username or /generatebb-svg?username=Your_Username")
# Путь в корень
@app.route('/')
def hello():
  return render_template('home.html')

# Путь до свгшки по главной статистике
@app.route('/generate-svg', methods=['GET'])
def generate_svg_endpoint():
    username = request.args.get('username')
    if not username:
        return "Username parameter is required", 400
    
    user_data = fetch_user_data(username)
    if not user_data:
        return "User not found", 404
    
    random_number = random.randint(1, 100000000)
    position = user_data['position']
    crPosition = user_data['crPosition']
    bbPosition = user_data['bbPosition']
    username = user_data['username']
    total = user_data['total']
    bbTotal = user_data['bbTotal']
    crTotal = user_data['crTotal']
    bbReportsCount = user_data['bbReportsCount']
    crReportsCount = user_data['crReportsCount']
    crVulnerability = user_data['crVulnerability']
    crBusinessRisk = user_data['crBusinessRisk']


    svg_image = generate_svg(position, crPosition, bbPosition, username, total,bbTotal ,crTotal ,bbReportsCount ,crReportsCount ,crVulnerability ,crBusinessRisk)
    return Response(svg_image, mimetype='image/svg+xml')

# Путь до свгшки по статистике багбаунти
@app.route('/generatebb-svg', methods=['GET'])
def generatebb_svg_endpoint():
    username = request.args.get('username')
    if not username:
        return "Username parameter is required", 400
    
    user_databb = fetch_user_bbdata(username)
    print(user_databb)
    if not user_databb:
        return "User not found", 404

    user_databb_other = fetch_user_data(username)
    print(user_databb_other)
    if not user_databb_other:
        return "User not found", 404


    
    random_number = random.randint(1, 100000000)
    bbPosition = user_databb_other['bbPosition']
    signal = user_databb['signal']
    impact = user_databb['impact']
    reportsTotal = user_databb['reportsTotal']
    reportsFinished = user_databb['reportsFinished']
    reportsInProgress = user_databb['reportsInProgress']
    reportsAccepted = user_databb['reportsAccepted']
    reportsInformational = user_databb['reportsInformational']
    reportsDuplicate = user_databb['reportsDuplicate']
    reportsOutOfScope = user_databb['reportsOutOfScope']
    reportsRejected = user_databb['reportsRejected']
    reportsAbuse = user_databb['reportsAbuse']



    bbsvg_image = generatebb_svg(username, bbPosition, signal, impact,reportsTotal,reportsFinished,reportsInProgress,reportsAccepted,reportsInformational,reportsDuplicate,reportsOutOfScope,reportsRejected,reportsAbuse)
    return Response(bbsvg_image, mimetype='image/svg+xml')



# Попытки очищать кэш, вроде как не работает но пускай пока побудет здесь
@app.after_request
def add_header(r):

    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r
port_number = 80
if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0',port=port_number)
