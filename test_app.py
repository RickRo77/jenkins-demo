# from app import app

# def test_home():
#     client = app.test_client()
#     res = client.get("/")
#     assert res.status_code == 200
#     assert res.json["message"] == "Python CI/CD Demo API is running!"

# def test_greet():
#     client = app.test_client()
#     res = client.get("/hello/Ricky")
#     assert res.status_code == 200
#     assert res.json["greeting"] == "Hello, Ricky!"


from app import app

def test_home():
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200
    assert res.json["message"] == "Python Calculator API is running!"

def test_add():
    client = app.test_client()
    res = client.get("/add?a=5&b=3")
    assert res.status_code == 200
    assert res.json["result"] == 8

def test_subtract():
    client = app.test_client()
    res = client.get("/subtract?a=10&b=4")
    assert res.status_code == 200
    assert res.json["result"] == 6

def test_multiply():
    client = app.test_client()
    res = client.get("/multiply?a=6&b=7")
    assert res.status_code == 200
    assert res.json["result"] == 42

def test_divide():
    client = app.test_client()
    res = client.get("/divide?a=20&b=5")
    assert res.status_code == 200
    assert res.json["result"] == 4

def test_divide_by_zero():
    client = app.test_client()
    res = client.get("/divide?a=10&b=0")
    assert res.status_code == 400
    assert res.json["error"] == "Division by zero"
