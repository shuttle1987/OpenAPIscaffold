"""This file contains the development server for running the API

NOTE: This is NOT a production ready server"""
from {{cookiecutter.project_slug}}.app import create_app
from {{cookiecutter.project_slug}}.settings import DevConfig

app = create_app(DevConfig)

@app.route('/')
def index():
    return """The API explorer tool can be found at <a href="/ui/">/ui/</a>, this is the best place to explore the API."""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

