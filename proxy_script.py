import sys
import requests
import mitmproxy.http
import time
import psutil

authorization_header = None

def request(flow: mitmproxy.http.HTTPFlow):
    global authorization_header
    if "X-Authorization" in flow.request.headers:
        authorization_header = flow.request.headers.get("X-Authorization")
        print("Authorization header found:", authorization_header)

def response(flow: mitmproxy.http.HTTPFlow):
    global authorization_header
    if authorization_header is not None:
        print("Triggering request...")
        # Once authorization header is found, trigger the specific request
        if flow.request.pretty_url == "https://77ee.playfabapi.com/Client/UpdateUserData":
            url = "https://77ee.playfabapi.com/Client/UpdateUserData"

            querystring = {"sdk": "UnitySDK-2.94.200901"}

            payload = {
                "CustomTags": None,
                "Data": {
                    "level": "100",
                    "prestige": "0",
                    "exp": "144",
                    "None": "366",
                    "wintertokens": "50000",
                    "season3_Level": "100",
                    "season2_Level": "100",
                    "season1_Level": "100"
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
                "X-Authorization": authorization_header,
                "Accept-Encoding": "GZIP",
                "X-Unity-Version": "2019.4.0f1",
                "Content-Length": "136"
            }

            response = requests.request("POST", url, json=payload, headers=headers, verify=False)

            print(response.text)

            print("Game is now closing. Once you re-open the game, you should be level 100.")
            time.sleep(5)
            terminate_process("Shotgun Farmers.exe")
            raise KeyboardInterrupt

def terminate_process(process_name):
    for proc in psutil.process_iter():
        if proc.name() == process_name:
            proc.terminate()
            print(f"Process {process_name} terminated.")
