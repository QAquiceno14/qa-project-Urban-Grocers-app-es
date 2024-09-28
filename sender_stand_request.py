import requests
import configuration
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


auth_token_user = post_new_user(data.user_body).json()['authToken']


def post_new_client_kit(body):
    auth_token = auth_token_user
    headers_with_auth = data.headers.copy()
    headers_with_auth["Authorization"] = f'Bearer {auth_token}'
    response = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=body,
                         headers=headers_with_auth)
    return response



