import requests


def new_post():
    body = {"name": "First object", "data": {"color": "white", "size": "big"}}
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


def put_a_post():
    post_id = new_post()
    body = {"name": "First object ", "data": {"color": "white 1", "size": "big 1"}}
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{post_id}',
        json=body,
        headers=headers
    ).json()
    print(response)
    clear(post_id)


def patch_a_post():
    post_id = new_post()
    body = {"name": "First object ", "data": {"color": "white 1"}}
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{post_id}',
        json=body,
        headers=headers
    ).json()
    print(response)
    clear(post_id)


def delete_a_post():
    post_id = new_post()
    response = clear(post_id)
    print(response.json())
