from flask import Flask, render_template, request, redirect, url_for
import subprocess
import os

app = Flask(__name__)
PIN_CODE = "1234"

SCRIPTS = {
    "hid": "../hid_keyboard.py",
    "rf": "../cc1101_send.py",
    "nfc": "../nfc_reader.py",
    "usb": "../usb_storage_toggle.py"
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        pin = request.form.get("pin")
        action = request.form.get("action")

        if pin != PIN_CODE:
            return render_template("index.html", message="Invalid PIN")

        script = SCRIPTS.get(action)
        if script and os.path.exists(script):
            subprocess.Popen(["python3", script])
            return render_template("index.html", message=f"{action.upper()} started")

        return render_template("index.html", message="Unknown action")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

