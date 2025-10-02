def main(context):
    return {
        "status": 200,
        "body": {
            "message": "Hello World! Đây là Fission function từ Python_test2",
            "status": "success",
            "service": "python-test2",
        },
        "headers": {"Content-Type": "application/json"},
    }

