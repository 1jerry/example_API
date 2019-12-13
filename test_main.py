from starlette.testclient import TestClient

import main

client = TestClient(main.app)

testjson = {
    "first_name": "bob",
    "last_name": "Peterson",
    "zip": 98665,
    "phone": 8005551212,
    "email": "bad@a.com"
}


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert type(response.content) == bytes


def test_read_me():
    response = client.get('/users/me')
    assert response.status_code == 200
    assert response.json() == main.fake_users_db[0]


def test_read_1():
    response = client.get('/users/1')
    assert response.status_code == 200
    assert response.json() == main.fake_users_db[0]


def test_read_4():
    response = client.get('/users/4')
    assert response.status_code == 404
    assert response.json() == dict()


def test_read_all():
    response = client.get('/users')
    assert response.status_code == 200
    res = response.json()
    assert type(res) == list
    assert len(res) == 3


def test_delete():
    response = client.delete('/users/1')
    assert response.status_code == 200
    assert response.json() == dict()


def test_create_item():
    response = client.post('/users/', json=testjson)
    assert response.status_code == 201
    resjson = response.json()
    sentkeys = testjson.keys()
    retkeys = set(resjson)
    newkeys = {'full_name', 'user_id'}
    partjson = {x: resjson[x] for x in sentkeys}
    assert partjson == testjson  # everything sent should exist
    assert retkeys.issuperset(newkeys)  # with two new elements


def test_read_all2():
    response = client.get('/users')
    assert response.status_code == 200
    res = response.json()
    assert type(res) == list
    assert len(res) == 3
