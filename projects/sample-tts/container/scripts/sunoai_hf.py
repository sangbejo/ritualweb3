import scipy
from transformers import AutoProcessor, AutoModelForTextToWaveform

model_name = "suno/bark"
processor = AutoProcessor.from_pretrained(model_name)
model = AutoModelForTextToWaveform.from_pretrained(model_name)

inputs = processor(
    text=[
        "Hello, my name is Suno. And, uh — and I like pizza. [laughs] But I also have other interests such as playing tic tac toe."
    ],
    return_tensors="pt",
)

print("generating")
speech_values = model.generate(**inputs, do_sample=True)
print("speech_values generated")

# from IPython.display import Audio
#
# sampling_rate = model.generation_config.sample_rate
# Audio(speech_values.cpu().numpy().squeeze(), rate=sampling_rate)


sampling_rate = model.generation_config.sample_rate
print("writing to file")
scipy.io.wavfile.write(
    "bark_out.wav", rate=sampling_rate, data=speech_values.cpu().numpy().squeeze()
)
print("done")
if __name__ == "__main__":
    pass
