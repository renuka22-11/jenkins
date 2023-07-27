from flask import Flask

app = Flask (__name__)

@app.route('/', methods=["GET"])


def get_version():
    return f"Current version: {current_version}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
