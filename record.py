import speech_recognition as sr
# Import the speech_recognition library:

# Define the main() function:
def main():

# Create a recognizer object from the Recognizer class:
    r = sr.Recognizer()

# Use a context manager to access the microphone as a source:
    #It will free up the space after recording
    with sr.Microphone() as source:

        # Adjust for ambient noise to improve audio quality:
        r.adjust_for_ambient_noise(source)

        print("Please say something")

        # Use the listen() method to capture audio from the microphone:
        audio = r.listen(source)

        print("Recognizing Now .... ")

# Open a file named "recorded.wav" in binary write mode:
        # write audio
        with open("recorded.wav", "wb") as f:
            f.write(audio.get_wav_data())
            print("Audio file saved")
# When you call audio.get_wav_data(), it returns the raw audio data 
# in the form of a byte string.
# This byte string represents the audio data in WAV format, which is a 
# standard format for storing digital audio.

# You can then write this byte string to a file using binary write mode ("wb") to 
# save the recorded audio as a WAV file, as demonstrated in the provided code snippet.
            
# if __name__ == "__main__":
#     main()
