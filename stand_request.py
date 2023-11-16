import requests, configuration

def post_new(body, headers, end_path):
    return requests.post(configuration.BASE_URL_SERVICE + end_path,
                         json=body,
                         headers=headers)

def get_new(headers, end_path):
    return requests.get(configuration.BASE_URL_SERVICE + end_path,
                         headers=headers)