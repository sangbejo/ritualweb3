from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from IPython.display import Audio


def main():
    # download and load all models
    preload_models()

    # generate audio from text
    text_prompt = """
        thought about it more, if i had to pick a point in time this cycle 
        where credit finally starts flowing again, this will be one of the first dominoes. 
        go back 5 years in time in the space and the credemption flows always beget borrow demand which begets 
        the {celsius, blockfi, etc.}s of the world to source. im sure there's a new guard of 3ac/etc.
         style basis funds starting up as this is painted against a dovish backdrop this year
             """
    audio_array = generate_audio(text_prompt)

    # save audio to disk
    write_wav("bark_generation.wav", SAMPLE_RATE, audio_array)

    # play text in notebook
    Audio(audio_array, rate=SAMPLE_RATE)


if __name__ == "__main__":
    main()
