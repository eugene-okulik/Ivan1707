import pytest
import requests


@pytest.fixture(scope="session", autouse=True)
def session_messages():
    print("\nStart testing", flush=True)
    yield
    print("Testing completed", flush=True)


@pytest.fixture(autouse=True)
def test_messages():
    print("\nbefore test", flush=True)
    yield
    print("after test", flush=True)


def new_post(name="First object", data=None):
    if data is None:
        data = {"color": "white", "size": "big"}
    body = {"name": name, "data": data}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    )
    return response.json()['id']


def clear(post_id):
    url = f'http://objapi.course.qa-practice.com/object/{post_id}'
    response = requests.delete(url)
    return response


def get_object(obj_id):
    url = f'http://objapi.course.qa-practice.com/object/{obj_id}'
    response = requests.get(url)
    return response


@pytest.fixture
def obj_fixture():
    obj_id = new_post("Default", {"color": "grey", "size": "medium"})
    yield obj_id
    clear(obj_id)


@pytest.mark.critical
@pytest.mark.parametrize("name, data", [
    ("First object", {"color": "white", "size": "big"}),
    ("Second object", {"color": "black", "size": "small"}),
    ("Third object", {"color": "red", "size": "medium"})
])
def test_create_object(name, data):
    obj_id = new_post(name, data)
    resp = get_object(obj_id)
    assert resp.status_code == 200
    obj = resp.json()
    assert obj['name'] == name
    assert obj['data'] == data
    clear(obj_id)


@pytest.mark.medium
def test_get_object_by_id(obj_fixture):
    obj_id = obj_fixture
    resp = get_object(obj_id)
    assert resp.status_code == 200
    assert resp.json()['id'] == obj_id


def test_update_object_put(obj_fixture):
    obj_id = obj_fixture
    headers = {'Content-Type': 'application/json'}
    new_body = {"name": "Updated PUT", "data": {"color": "blue", "size": "huge"}}
    resp = requests.put(
        f'http://objapi.course.qa-practice.com/object/{obj_id}',
        json=new_body,
        headers=headers
    )
    assert resp.status_code == 200
    updated = resp.json()
    assert updated['name'] == "Updated PUT"
    assert updated['data']['color'] == "blue"
    assert updated['data']['size'] == "huge"


def test_update_object_patch(obj_fixture):
    obj_id = obj_fixture
    headers = {'Content-Type': 'application/json'}
    patch_body = {"data": {"color": "yellow"}}
    resp = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{obj_id}',
        json=patch_body,
        headers=headers
    )
    assert resp.status_code == 200
    updated = resp.json()
    if 'data' in updated and 'color' in updated['data']:
        assert updated['data']['color'] == "yellow"
    else:
        get_resp = get_object(obj_id)
        assert get_resp.status_code == 200
        assert get_resp.json()['data']['color'] == "yellow"


def test_delete_object():
    obj_id = new_post("ToDelete", {"color": "purple", "size": "tiny"})
    del_resp = clear(obj_id)
    assert del_resp.status_code == 200
    get_resp = get_object(obj_id)
    assert get_resp.status_code == 404
