import requests, json, os


def oauth_handler(token):
    url = os.getenv("OAUTH_PROVIDER", "http://localhost:8000/o/introspect/")

    payload=f'client_id=EuF0PvVdlG0CnrKUOaLA3OL4cci1YJUFmZKCvqwj&client_secret=CiDMsofQHa1ZjOIUM5pyZuJDbNIilCdCCpURFwr3NHuoCNGG3Rcg1si7Yjga6L6gGv2E4hiKoLzddWs7G85ZzHzcnPB4Jtjv9IiufEZqvSQuQ5fWan29BiVJmDnpgZf5&token={token}'
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    response_data = response.json()
    if response_data['active']:
        return True
    else:
        return False
    
