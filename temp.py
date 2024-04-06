import streamlit as st
import assemblyai as aai
import toml



api_key = st.secrets["API_KEY"]
aai.settings.api_key=api_key


transcriber = aai.Transcriber()

def transcribe_and_summarize(audio_url, prompt):
    # Transcribe audio
    transcript = transcriber.transcribe(audio_url)
    
    # Generate summary
    result = transcript.lemur.task(prompt)
    summary = result.response
    
    return transcript.text, summary

# Streamlit UI
def main():
    st.title("Audio Transcription and Summarization App")

    # User input for audio URL and prompt
    audio_url = st.text_input("Enter the URL of the audio file:")
    prompt = st.text_input("Enter the prompt for summary:")
    
    # Transcribe and summarize button
    if st.button("Transcribe and Summarize"):
        if audio_url and prompt:
            st.write("Transcribing and summarizing... 🎙️📝")
            try:
                transcription, summary = transcribe_and_summarize(audio_url, prompt)
                st.write("Transcription:")
                st.write(transcription)
                st.write("Summary:")
                st.write(summary)
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("Please enter the URL of the audio file and the prompt.")

if __name__ == "__main__":
    main()
