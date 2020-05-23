import pytest
import handler

def test_handler():
    event = {
        "httpMethod": "POST",
        "path": "/cp/sharelatlong",
        "body": '{"hello":"1"}'
    }
    result = handler.hello(event, None)
    assert result == {
        "statusCode": 200,
        "body": '{"message": "Hello World!!"}'
    }

