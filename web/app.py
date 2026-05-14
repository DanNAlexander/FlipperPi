# FlipperPi — This is a DIY Flipper Zero-style multi-tool running on Raspberry Pi Zero 2.
# Copyright (C) 2026 Danton Alexander
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License along with this program.  If not, see <https://www.gnu.org/licenses/>.


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

