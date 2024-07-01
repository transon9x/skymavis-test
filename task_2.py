import os
import requests
from flask import Flask, jsonify
from dotenv import dotenv_values


app = Flask(__name__)

env_vars = dotenv_values(".env")

INFURA_URL = env_vars.get("INFURA_URL")
ANKR_URL = env_vars.get('ANKR_URL')

def get_block_number(url):
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_blockNumber",
        "params": [],
        "id": 1
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    result = response.json()
    return int(result["result"], 16)

@app.route('/metrics', methods=['GET'])
def metrics():
    try:
        infura_block_number = get_block_number(INFURA_URL)
        ankr_block_number = get_block_number(ANKR_URL)
        block_diff = infura_block_number - ankr_block_number
        
        if block_diff < 5:
            status = "success"
        else:
            status = "fail"
        
        data = {
            "infura_block_number": infura_block_number,
            "ankr_block_number": ankr_block_number,
            "block_diff": block_diff,
            "status": status
        }
    except Exception as e:
        data = {
            "error": str(e)
        }
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
