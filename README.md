# AI Study Assistant

## Project Description
AI Study Assistant is a Python-based application that helps students understand study materials using Artificial Intelligence.

Users can upload PDF study materials, generate summaries, ask questions, and listen to summaries.

## Technologies Used
- Python
- Streamlit
- Ollama
- Gemma 3 1B
- PyMuPDF
- gTTS
- SpeechRecognition UI using Streamlit Mic Recorder

## Features
1. Upload PDF files.
2. Extract text from PDF files.
3. Generate short summaries.
4. Generate detailed summaries.
5. Ask questions based on uploaded PDF content.
6. Use a microphone to speak questions.
7. Convert summaries into audio.

## Installation

Install the required Python packages:

```bash

pip install -r requirements.txt
```

## Demo Video

[Watch the AI Study Assistant demo](https://drive.google.com/file/d/1g1d4iNtPK8mwN2BRVaBvQhF2zTaXdW8h/view?usp=sharing)

## Problem Statement

Students spend a lot of time reading study materials in PDF format. This application helps students understand PDF content through summaries, question answering and voice features.

## Objectives

- To extract text from PDF files.
- To generate short and detailed summaries.
- To answer questions based on PDF content.
- To support voice input.
- To convert summaries into audio.

## Application Architecture

1. User uploads a PDF through Streamlit.
2. PyMuPDF extracts text from the PDF.
3. Ollama with Gemma 3 1B generates summaries and answers.
4. Streamlit displays the results.
5. Speech input converts voice questions into text.
6. gTTS converts summaries into audio.

## Environment Setup

- Install Python.
- Install Ollama.
- Download the Gemma 3 1B model using `ollama pull gemma3:1b`.
- Install the required Python packages using the requirements.txt file.

No API key is required because this project uses local Ollama.

## How to Run

1. Open the project folder in the terminal.
2. Make sure Ollama is running.
3. Run:

```bash
py -m streamlit run app.py
```
## Screenshots

Screenshots of the AI Study Assistant application will be added here.

## Future Enhancements

- Generate MCQs from PDF content.
- Create flashcards.
- Support multiple PDF uploads.
- Add multilingual support.
