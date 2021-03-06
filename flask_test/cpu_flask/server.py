"""
Main module of the server file
"""

from flask import jsonify
import connexion


# Create the application instance
app = connexion.App(__name__, specification_dir="./")

# Read the yaml file to configure the endpoints
app.add_api("cpu.yaml")

# create a URL route in our application for "/"
@app.route("/")
def home():
    msg = {"msg": "Welcome home. Available tags: /cpu"}
    return jsonify(msg)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
