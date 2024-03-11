# Shotgun-Farmers-Scripts
Installation Process
---------------------------
pip install psutil \
pip install time \
pip install subprocess \
pip install threading \
pip install mitmproxy \
pip install os \
pip install requests
------------------------

Javascript Code to execute whenever you have your authorization.
--------------------------------------------------------------
```js
const data = JSON.stringify({
  "CustomTags": null,
  "Data": {
    "level": "100",
    "exp": "144",
    "None": "366"
  },
  "KeysToRemove": null,
  "Permission": null,
  "AuthenticationContext": null
});

const xhr = new XMLHttpRequest();
xhr.withCredentials = true;

xhr.addEventListener("readystatechange", function () {
  if (this.readyState === this.DONE) {
    console.log(this.responseText);
  }
});

xhr.open("POST", "https://77ee.playfabapi.com/Client/UpdateUserData?sdk=UnitySDK-2.94.200901");
xhr.setRequestHeader("Content-Type", "application/json");
xhr.setRequestHeader("Host", "77ee.playfabapi.com");
xhr.setRequestHeader("User-Agent", "UnityPlayer/2019.4.0f1 (UnityWebRequest/1.0, libcurl/7.52.0-DEV)");
xhr.setRequestHeader("Accept", "*/*");
xhr.setRequestHeader("X-ReportErrorAsSuccess", "true");
xhr.setRequestHeader("X-PlayFabSDK", "UnitySDK-2.94.200901");
xhr.setRequestHeader("X-Authorization", "7E08813F1157A9C5-C0ED76AE2BCCDC6C-6BB72E5CCA8CBE12-77EE-8DC4076D3589F1B-udW6zNUAFA9XTNl9+xSdOIi01MZBhcwaKak6IAuJqhw=");
xhr.setRequestHeader("Accept-Encoding", "GZIP");
xhr.setRequestHeader("X-Unity-Version", "2019.4.0f1");
xhr.setRequestHeader("Content-Length", "136");

xhr.send(data);```
