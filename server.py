#!/usr/bin/env python3
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

@app.route('/api/chat', methods=['POST', 'OPTIONS'])
def chat():
    if request.method == 'OPTIONS':
        return '', 200
    
    try:
        print(f"Content-Type: {request.content_type}")
        print(f"Raw data: {request.data}")
        
        data = request.get_json(force=True)
        print(f"Parsed JSON: {data}")
        
        api_key = data.get('apiKey') if data else None
        message = data.get('message') if data else None
        
        print(f"API Key: {api_key[:10] if api_key else 'None'}...")
        print(f"Message: {message}")
        
        if not data:
            print("No JSON data received")
            return jsonify({'error': 'No JSON data received'}), 400
            
        if not api_key:
            print("Missing API key")
            return jsonify({'error': 'Missing apiKey'}), 400
            
        if not message:
            print("Missing message")
            return jsonify({'error': 'Missing message'}), 400
        
        print("Sending to Mistral AI API...")
        print(f"Authorization header: Bearer {api_key[:20] if api_key else 'None'}...")
        
        response = requests.post(
            'https://api.mistral.ai/v1/chat/completions',
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {api_key}'
            },
            json={
                'model': 'mistral-tiny',
                'messages': [
                    {'role': 'user', 'content': message}
                ],
                'max_tokens': 1024
            },
            timeout=30
        )
        
        print(f"Mistral AI API response: {response.status_code}")
        print(f"Mistral AI response body: {response.text}")
        
        if response.status_code == 401:
            return jsonify({'error': 'Invalid Mistral AI API key. Check your key at console.mistral.ai'}), 401
        
        if response.status_code == 200:
            result = response.json()
            # Transform Mistral response to match Anthropic format
            return jsonify({
                'content': [{'text': result['choices'][0]['message']['content']}]
            }), 200
        else:
            result = response.json() if response.text else {}
            return jsonify({'error': result.get('message', result.get('error', 'Mistral AI API error'))}), response.status_code
    
    except Exception as e:
        print(f"Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("Starting SUPER-H OS API Server on http://localhost:3000")
    print("Make sure you have Flask installed: pip install flask requests")
    app.run(debug=False, port=3000, host='localhost')
