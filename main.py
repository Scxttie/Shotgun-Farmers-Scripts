import psutil
import time
import subprocess
import threading

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
            # Run something after the executable is found
            # For example, you can run another script or function
            # replace `run_something()` with your desired action
            run_something()
            return
        else:
            # If executable is not found, start it
            print(f"Executable '{executable_name}' is not running. Starting...")
            subprocess.Popen([executable_name])
            # Wait for a few seconds before checking again
            time.sleep(5)

def run_something():
    print("Running something after the executable is found.")

def run_mitmproxy(executable_name):
    # Run mitmproxy on localhost:8080 with filtering
    subprocess.Popen(["mitmproxy", "-s", "proxy_script.py", "--listen-host", "127.0.0.1", "--listen-port", "8080", "--view-filter", f"~u {executable_name}"])

if __name__ == "__main__":
    # Replace 'Shotgun Farmers' with the name of your executable file displayed in the taskbar
    executable_name = 'Shotgun Farmers.exe'
    wait_for_executable(executable_name)
