import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = "https://77ee.playfabapi.com/Client/UpdateUserData"

querystring = {"sdk":"UnitySDK-2.94.200901"}

payload = {
    "CustomTags": None,
    "Data": {
        "level": "100",
        "exp": "144",
        "None": "366"
    },
    "KeysToRemove": None,
    "Permission": None,
    "AuthenticationContext": None
}
headers = {
    "Content-Type": "application/json",
    "Host": "77ee.playfabapi.com",
    "User-Agent": "UnityPlayer/2019.4.0f1 (UnityWebRequest/1.0, libcurl/7.52.0-DEV)",
    "Accept": "*/*",
    "X-ReportErrorAsSuccess": "true",
    "X-PlayFabSDK": "UnitySDK-2.94.200901",
    "X-Authorization": "PASTE YOUR AUTHORIZATION YOU GOT FROM THE SCRIPT HERE",
    "Accept-Encoding": "GZIP",
    "X-Unity-Version": "2019.4.0f1",
    "Content-Length": "136"
}

response = requests.request("POST", url, json=payload, headers=headers, verify=False)

print(response.text)
