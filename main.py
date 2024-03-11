import psutil
import time
import subprocess
import threading
import mitmproxy.http

authorization_header = None

def is_process_running(process_name):
    for process in psutil.process_iter():
        try:
            if process.name() == process_name:
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def wait_for_executable(executable_name):
    while True:
        if is_process_running(executable_name):
            print(f"Executable '{executable_name}' is already running.")
            # Run mitmproxy in a separate thread
            mitm_thread = threading.Thread(target=run_mitmproxy, args=(executable_name,))
            mitm_thread.start()
            return
        else:
            print(f"Executable '{executable_name}' is not running. Starting...")
            subprocess.Popen([executable_name])
            time.sleep(5)

def run_mitmproxy(executable_name):
    subprocess.Popen(["mitmproxy", "-s", "proxy_script.py", "--listen-host", "127.0.0.1", "--listen-port", "8080", "--view-filter", f"~u {executable_name}"])

# proxy_script.py
def save_authorization_header(authorization_header):
    with open("Authorization.txt", "w") as file:
        file.write(authorization_header)

def request(flow: mitmproxy.http.HTTPFlow):
    global authorization_header
    if "X-Authorization" in flow.request.headers:
        authorization_header = flow.request.headers.get("X-Authorization")
        print("Authorization header found:", authorization_header)
        save_authorization_header(authorization_header)

def response(flow: mitmproxy.http.HTTPFlow):
    pass

if __name__ == "__main__":
    executable_name = 'Shotgun Farmers.exe'
    wait_for_executable(executable_name)
