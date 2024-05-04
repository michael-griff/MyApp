from app.app import lambda_handler

# Here is where the testing takes place...
def test_lambda_handler():
    assert lambda_handler(None,None) != None
    