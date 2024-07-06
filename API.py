from flask import Flask, request, jsonify
import json
from Caesar_Cipher.Caesar_Cipher import get_cipher

# 1) app
app = Flask(__name__)


# 2) Route
@app.route("/", methods=['GET'])
def cipher():
    
    message  = request.args.get('message')    # use default value repalce ''
    # to ignore all errors or wrong result >> standardized the format of encrypt
    encrypt  = request.args.get('encrypt','true').lower()=='true'    # use default value repalce 'True'
    key  = request.args.get('key', None)          # use default value repalce 'None'

    key = json.loads(key)
    try:
        result = get_cipher(string=message, key=key, encrypt=encrypt)
        return result

    except TypeError as e:
        return "error", e    

# 3) run
if __name__ =="__main__":  
    # app.run(debug = False)
    app.debug = True
    app.run()