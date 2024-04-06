import streamlit as st
import assemblyai as aai
import toml



api_key = st.secrets["API_KEY"]

aai.settings.api_key = api_key
transcriber = aai.Transcriber()

# Function to transcribe audio from URL
def transcribe_audio(audio_url):
    transcript = transcriber.transcribe(audio_url)
    return transcript.text

# Streamlit UI
def main():
    st.title("Audio Transcription App")

    # User input for audio URL
    audio_url = st.text_input("Enter the URL of the audio file:")

    # Transcribe button
    if st.button("Transcribe"):
        if audio_url:
            st.write("Transcribing... 🎙️")
            try:
                transcription = transcribe_audio(audio_url)
                st.write("Transcription:")
                st.write(transcription)
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("Please enter the URL of the audio file.")

if __name__ == "__main__":
    main()
