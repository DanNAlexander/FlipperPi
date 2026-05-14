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

# Flask web UI
from flask import Flask
app = Flask(__name__)
@app.route('/')
def home(): return 'FlipperPi Web'
