from typing import Any

from flask import Flask, request

import os
import json
import requests

# read api key from env
api_key = os.environ.get("OPENAI_API_KEY")


def query_chatgpt(prompt, model="gpt-3.5-turbo-0613", api_key=api_key):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    data = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    }

    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers=headers,
        data=json.dumps(data),
    )

    if response.status_code == 200:
        return response.json()
    else:
        return response.text


def create_app() -> Flask:
    app = Flask(__name__)

    @app.route("/")
    def index() -> str:
        return "Hello world service!"

    @app.route("/service_output", methods=["POST"])
    def inference() -> dict[str, Any]:
        input = request.json
        prompt = input.get("prompt")
        response = query_chatgpt(prompt, api_key=api_key)
        return {"output": response["choices"][0]["message"]["content"]}

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(port=3000)
