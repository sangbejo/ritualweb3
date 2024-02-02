import json
import os
from typing import Any, cast

import requests
from flask import Flask, request  # type: ignore

# read api key from env
api_key = os.environ["OPENAI_API_KEY"]


def query_chatgpt(
    prompt: str, model: str = "gpt-3.5-turbo-0613", api_key: str = api_key
) -> Any:
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
        raise Exception(f"error: {response.text}")


def create_app() -> Flask:
    app = Flask(__name__)

    @app.route("/")
    def index():  # type: ignore
        return "GPT 3 service!"

    @app.route("/service_output", methods=["POST"])
    def inference():  # type: ignore
        input: dict[str, Any] = cast(dict[str, Any], request.json)
        print("input is", json.dumps(input, indent=2))
        if input.get("source") == 0:
            encoded: str = input["data"]
            bytearray = bytes.fromhex(encoded)
            prompt = bytearray.decode("utf-8")
        else:
            prompt = input["data"]["prompt"]
        response = query_chatgpt(prompt, api_key=api_key)
        return {"output": response["choices"][0]["message"]["content"]}

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(port=3000)
