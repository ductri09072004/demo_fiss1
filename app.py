from flask import Flask, jsonify
from data.mock_data import get_system_info, get_user_profile, get_health_status, get_products_data, get_orders_data

app = Flask(__name__)

@app.route('/api/base')
def hello():
    """API endpoint trả về thông tin hệ thống"""
    return jsonify(get_system_info())

@app.route('/api/user')
def api_hello():
    """API endpoint trả về thông tin người dùng"""
    return jsonify(get_user_profile())

@app.route('/api/health')
def health_check():
    """API endpoint kiểm tra trạng thái server"""
    return jsonify(get_health_status())

@app.route('/api/products')
def get_products():
    """API endpoint trả về danh sách sản phẩm"""
    return jsonify(get_products_data())

@app.route('/api/orders')
def get_orders():
    """API endpoint trả về danh sách đơn hàng"""
    return jsonify(get_orders_data())


if __name__ == '__main__':
    print("🚀 Starting Demo FISS API...")
    print("📍 Available endpoints:")
    print("   - GET /api/base (system information)")
    print("   - GET /api/user (user profile)")
    print("   - GET /api/health (system health check)")
    print("   - GET /api/products (products list)")
    print("   - GET /api/orders (orders list)")
    print("🌐 Server running at: http://localhost:5001")
    app.run(debug=True, host='0.0.0.0', port=5001)
