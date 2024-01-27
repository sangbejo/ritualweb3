import os
from typing import Any, Optional

from ml.utils.service_models import InfernetInput
from ml.workflows.inference.tts_inference_workflow import TTSInferenceWorkflow
from quart import Quart, request

workflow = TTSInferenceWorkflow(
    output_path="/root/audio",
)


def create_app() -> Quart:
    # setup workflow
    # check if ~/.cache/suno/bark_v0 is empty
    homedir = os.path.expanduser("~")
    cachedir = f"{homedir}/.cache/suno/bark_v0"
    cache_items = os.listdir(cachedir)
    print(f"cache dir: {cachedir}")
    print(f"cache items: {cache_items}")
    if len(cache_items) == 0:
        workflow.setup()
    else:
        print("items already downloaded")

    app = Quart(__name__)

    @app.route("/")
    async def index() -> str:
        return "TTS service!"

    @app.route("/service_output", methods=["POST"])
    async def inference() -> dict[str, Any]:
        data: Optional[dict[str, Any]] = await request.get_json()
        input: InfernetInput = InfernetInput(**data)
        print("inference input", input)
        inference_input = input.data
        if input.source == 0:
            bytearray = bytes.fromhex(inference_input)
            prompt = bytearray.decode("utf-8")
        else:
            prompt = inference_input.get("prompt")
        return workflow.do_inference({"text": prompt})

    return app


if __name__ == "__main__":
    # app = create_app()
    # app.run(port=3000)
    # tts_inference_workflow = TTSInferenceWorkflow()
    # tts_inference_workflow.setup()
    workflow.do_inference({"text": "Hello, my name is arshan how are you?"})
