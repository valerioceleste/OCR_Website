import whisper

def speech2text(audio_file,model_selection):
	model = whisper.load_model(model)
	text = model.transcribe("../Audio2Text/audiofiles/Silvia.m4a",fp16=False)
return text