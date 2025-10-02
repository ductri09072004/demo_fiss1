from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    """API endpoint trả về dữ liệu hello"""
    return jsonify({
        "message": "Hello World! Đây là server 2",
        "status": "success 2",
        "data": "Xin chào từ Python API 2!"
    })

@app.route('/api/hello')
def api_hello():
    """API endpoint chuyên dụng cho hello"""
    return jsonify({
        "message": "Hello from API!",
        "status": "success",
        "timestamp": "2024-01-01T00:00:00Z"
    })

@app.route('/health')
def health_check():
    """API endpoint kiểm tra trạng thái server"""
    return jsonify({
        "status": "healthy",
        "service": "Python Test API"
    })

if __name__ == '__main__':
    print("🚀 Starting Python Test API...")
    print("📍 Available endpoints:")
    print("   - GET / (hello world)")
    print("   - GET /api/hello (hello API)")
    print("   - GET /health (health check)")
    print("🌐 Server running at: http://localhost:5001")
    app.run(debug=True, host='0.0.0.0', port=5001)
