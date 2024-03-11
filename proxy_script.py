import mitmproxy.http

authorization_header = None

def request(flow: mitmproxy.http.HTTPFlow):
    global authorization_header
    if "X-Authorization" in flow.request.headers:
        authorization_header = flow.request.headers.get("X-Authorization")
        print("Authorization header found:", authorization_header)
        with open("Authorization.txt", "w") as file:
            file.write(authorization_header)

def response(flow: mitmproxy.http.HTTPFlow):
    pass
