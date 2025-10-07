from flask import Flask, jsonify
from data.mock_data import get_system_info, get_user_profile, get_health_status, get_products_data, get_orders_data
import time
import random

app = Flask(__name__)

# Metrics variables
request_count = 0
response_times = []

@app.route('/api/base')
def hello():
    """API endpoint trả về thông tin hệ thống"""
    global request_count, response_times
    start_time = time.time()
    request_count += 1
    result = jsonify(get_system_info())
    response_times.append(time.time() - start_time)
    # Keep only last 100 response times to prevent memory leak
    if len(response_times) > 100:
        response_times.pop(0)
    return result

@app.route('/api/user')
def api_hello():
    """API endpoint trả về thông tin người dùng"""
    global request_count, response_times
    start_time = time.time()
    request_count += 1
    result = jsonify(get_user_profile())
    response_times.append(time.time() - start_time)
    # Keep only last 100 response times to prevent memory leak
    if len(response_times) > 100:
        response_times.pop(0)
    return result

@app.route('/api/health')
def health_check():
    """API endpoint kiểm tra trạng thái server"""
    global request_count, response_times
    start_time = time.time()
    request_count += 1
    result = jsonify(get_health_status())
    response_times.append(time.time() - start_time)
    # Keep only last 100 response times to prevent memory leak
    if len(response_times) > 100:
        response_times.pop(0)
    return result

@app.route('/api/products')
def get_products():
    """API endpoint trả về danh sách sản phẩm"""
    global request_count, response_times
    start_time = time.time()
    request_count += 1
    result = jsonify(get_products_data())
    response_times.append(time.time() - start_time)
    # Keep only last 100 response times to prevent memory leak
    if len(response_times) > 100:
        response_times.pop(0)
    return result

@app.route('/api/orders')
def get_orders():
    """API endpoint trả về danh sách đơn hàng"""
    global request_count, response_times
    start_time = time.time()
    request_count += 1
    result = jsonify(get_orders_data())
    response_times.append(time.time() - start_time)
    # Keep only last 100 response times to prevent memory leak
    if len(response_times) > 100:
        response_times.pop(0)
    return result

@app.route('/metrics')
def metrics():
    """Prometheus metrics endpoint"""
    global request_count, response_times
    
    # Simulate some metrics
    avg_response_time = sum(response_times[-10:]) / len(response_times[-10:]) if response_times else 0
    
    metrics_text = f"""# HELP demo_fiss_requests_total Total number of requests
# TYPE demo_fiss_requests_total counter
demo_fiss_requests_total {request_count}

# HELP demo_fiss_response_time_seconds Average response time
# TYPE demo_fiss_response_time_seconds gauge
demo_fiss_response_time_seconds {avg_response_time:.3f}

# HELP demo_fiss_active_connections Current active connections
# TYPE demo_fiss_active_connections gauge
demo_fiss_active_connections {random.randint(1, 10)}

# HELP demo_fiss_memory_usage_bytes Memory usage in bytes
# TYPE demo_fiss_memory_usage_bytes gauge
demo_fiss_memory_usage_bytes {random.randint(50000000, 100000000)}
"""
    return metrics_text, 200, {'Content-Type': 'text/plain'}


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
