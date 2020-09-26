# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
import logging
import requests
import json

"""
基于 daovoice 定义自定义回复
"""

with open('/opt/daovoice_config.json', 'r') as f:
    config = json.load(f)

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)


@app.route('/send', methods=['POST'])
def main():
    req = request.json
    logging.info('msg: {}'.format(req))
    conversation_id = req.get('data').get('conversation_parts')[0].get('conversation_id')
    reply(conversation_id, '么么哒')
    return jsonify({'status': 'success'})


def reply(conversation_id, content):
    requests.post(
        'https://api.daovoice.io/v1/conversations/{}/reply'.format(conversation_id),
        json={
            "admin": {
                "admin_id": config.get('admin_id')
            },
            "message_type": "comment",
            "body": content
        },
        headers={
            'Authorization': 'token ' + config.get('token')
        }
    )


def get_admin_id():
    response = requests.get(
        'https://api.daovoice.io/v1/admins',
        headers={
            'Authorization': 'token ' + config.get('token')
        }
    )
    print(response.json())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8801, debug=True)
