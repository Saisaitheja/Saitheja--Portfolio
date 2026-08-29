import os
import re
from pathlib import Path
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

EMAIL = "saitheja2002@gmail.com"
PHONE = "08143353332"

@app.route("/")
def home():
    return render_template("index.html")

@app.post("/contact")
def contact():
    data = request.get_json(silent=True) or {}
    name = str(data.get("name", "")).strip()
    email = str(data.get("email", "")).strip()
    message = str(data.get("message", "")).strip()

    if not name or not email or not message:
        return jsonify(ok=False, message="Please complete all fields."), 400
    if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
        return jsonify(ok=False, message="Please enter a valid email address."), 400

    # This demo form validates in the browser/server. It intentionally does not
    # send or store messages because no email service was supplied.
    return jsonify(ok=True, message=f"Thanks, {name}! Your message is ready to be sent to Saitheja.")

@app.errorhandler(404)
def not_found(_error):
    return render_template("404.html"), 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="127.0.0.1", port=port, debug=True)


