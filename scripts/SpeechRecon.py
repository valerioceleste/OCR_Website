import whisper

def speech2text(audio_file, model_quality, language):
    model = whisper.load_model(model_quality)
    text = model.transcribe(audio_file, fp16=False)
    return text