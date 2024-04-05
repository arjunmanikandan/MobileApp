import whisper
import json

def voice_text():

    model = whisper.load_model('small')

    result = model.transcribe(r"C:\Users\ADMIN\Videos\mobile_app\medical_summarization\recorded.wav",fp16=False)

    final_result = result["text"]

    print(result["text"])

    # Create a dictionary to store the result
    data = {"text": final_result}

    # Specify the filename for the JSON file
    filename = "text.json"

    # Write the data to the JSON file
    with open(filename, "w") as file:
        json.dump(data, file)

    print("transcribed successfully")
# voice_text()