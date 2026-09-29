import streamlit as st
import pymupdf
import ollama
from gtts import gTTS
from streamlit_mic_recorder import speech_to_text
import io

# Page configuration
st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="📚",
    layout="wide"
)

st.title("📚 AI Study Assistant")
st.write("Upload your study material PDF and use AI to understand it easily.")

# Upload PDF
uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type=["pdf"]
)

if uploaded_file is not None:

    # Extract text from PDF
    pdf_document = pymupdf.open(
        stream=uploaded_file.read(),
        filetype="pdf"
    )

    pdf_text = ""

    for page in pdf_document:
        pdf_text += page.get_text()

    if pdf_text.strip():

        st.success("PDF uploaded and text extracted successfully!")

        with st.expander("View extracted PDF text"):
            st.text_area(
                "PDF Content",
                pdf_text,
                height=250
            )

        # Limit text sent to the AI model
        study_material = pdf_text[:12000]

        # Short Summary
        st.subheader("📝 Short Summary")

        if st.button("Generate Short Summary"):
            with st.spinner("Gemma is generating a short summary..."):
                try:
                    response = ollama.chat(
                        model="gemma3:1b",
                        messages=[
                            {
                                "role": "user",
                                "content": (
                                    "Summarize this study material briefly "
                                    "using simple language and important points:\n\n"
                                    + study_material
                                )
                            }
                        ]
                    )

                    short_summary = response["message"]["content"]
                    st.session_state["short_summary"] = short_summary

                except Exception as e:
                    st.error(f"Error generating summary: {e}")

        if "short_summary" in st.session_state:
            st.write(st.session_state["short_summary"])

        # Detailed Summary
        st.subheader("📖 Detailed Summary")

        if st.button("Generate Detailed Summary"):
            with st.spinner("Gemma is generating a detailed summary..."):
                try:
                    response = ollama.chat(
                        model="gemma3:1b",
                        messages=[
                            {
                                "role": "user",
                                "content": (
                                    "Create a detailed summary of this study material. "
                                    "Use headings, explain important concepts in simple "
                                    "language, and include key points:\n\n"
                                    + study_material
                                )
                            }
                        ]
                    )

                    detailed_summary = response["message"]["content"]
                    st.session_state["detailed_summary"] = detailed_summary

                except Exception as e:
                    st.error(f"Error generating detailed summary: {e}")

        if "detailed_summary" in st.session_state:
            st.write(st.session_state["detailed_summary"])

        # Ask Questions
        st.subheader("❓ Ask Questions from Your PDF")

        st.write("You can type your question or use the microphone.")

        spoken_question = speech_to_text(
            language="en",
            start_prompt="🎤 Start Speaking",
            stop_prompt="⏹️ Stop Recording",
            key="speech_to_text"
        )

        question = st.text_input(
            "Enter your question about the uploaded PDF",
            value=spoken_question or "",
            key="question_input"
        )

        if st.button("Get Answer"):

            if question.strip():

                with st.spinner("Gemma is finding the answer..."):
                    try:
                        response = ollama.chat(
                            model="gemma3:1b",
                            messages=[
                                {
                                    "role": "user",
                                    "content": (
                                        "Answer the question using only the study "
                                        "material provided below. If the answer is "
                                        "not available in the material, clearly say so. "
                                        "Explain in simple language.\n\n"
                                        "Study material:\n"
                                        + study_material
                                        + "\n\nQuestion: "
                                        + question
                                    )
                                }
                            ]
                        )

                        st.subheader("Answer")
                        st.write(response["message"]["content"])

                    except Exception as e:
                        st.error(f"Error generating answer: {e}")

            else:
                st.warning("Please enter a question.")

        # Text-to-Speech
        st.subheader("🔊 Listen to Your Summary")

        summary_choice = st.selectbox(
            "Choose a summary to listen to",
            ["Short Summary", "Detailed Summary"]
        )

        if st.button("Generate Audio"):

            if summary_choice == "Short Summary":
                selected_summary = st.session_state.get(
                    "short_summary", ""
                )
            else:
                selected_summary = st.session_state.get(
                    "detailed_summary", ""
                )

            if selected_summary:

                with st.spinner("Generating audio..."):
                    try:
                        audio = gTTS(
                            text=selected_summary,
                            lang="en"
                        )

                        audio_buffer = io.BytesIO()
                        audio.write_to_fp(audio_buffer)
                        audio_buffer.seek(0)

                        st.success("Audio generated successfully!")

                        st.audio(
                            audio_buffer,
                            format="audio/mp3"
                        )

                    except Exception as e:
                        st.error(f"Error generating audio: {e}")

            else:
                st.warning(
                    "Please generate the selected summary first."
                )

    else:
        st.warning("No readable text was found in this PDF.")

else:
    st.info("Please upload a PDF file to get started.")