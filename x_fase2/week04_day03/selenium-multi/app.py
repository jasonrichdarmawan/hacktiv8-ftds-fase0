from flask import Flask, request, Response
from util.webdriverutil import get_or_load_driver, get_comments

app = Flask(__name__)

@app.route('/get_comments')
def api_get_comments():
    args = request.args
    
    symbol = args.get("symbol")
    if symbol == None: return "", 400
    
    start_from = args.get("start_from")
    try: start_from = int(start_from)
    except (TypeError, ValueError): return "", 400
    
    end_at = args.get("end_at")
    try: end_at = int(end_at)
    except (TypeError, ValueError): return "", 400
    
    driver = get_or_load_driver(symbol=symbol)
    
    comments = get_comments(driver, end_at=end_at)[start_from:end_at]
    
    return Response(response=comments.to_json(orient="records"), mimetype='application/json')