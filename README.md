# 🌱 PlantSaathi — Plant Care Assistant

PlantSaathi is a beginner-friendly plant-care web app built with Python and Streamlit. Users can select a plant, report visible symptoms, view general care suggestions, upload a photo for reference, and save checks to a session journal.

## Features
- Plant photo upload and preview
- Symptom-based care assessment
- Care guides for common plants
- Session-based plant journal
- Simple interface suitable for a student project

## Important scope note
This version is a **working educational prototype**. It does not classify diseases from image pixels and does not include trained model weights. Photo upload is for visual reference only; care suggestions are based on the symptom selected by the user. Do not describe this version as a trained image-recognition model.

## Requirements
- Python 3.10–3.12 recommended
- Internet connection for initial package installation

## Run locally
1. Download or clone this repository.
2. Open a terminal in the project folder.
3. (Optional) Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
4. Activate on Windows:
   ```bash
   .venv\\Scripts\\activate
   ```
   On macOS/Linux:
   ```bash
   source .venv/bin/activate
   ```
5. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt --timeout 120 --retries 10
   ```
6. Start the app:
   ```bash
   python -m streamlit run app.py
   ```
7. Open the local URL shown in the terminal, usually `http://localhost:8501`.

## Suggested future improvements
- Add a properly trained and evaluated plant image classifier.
- Store journals in a database with user consent.
- Add multilingual guidance and text-to-speech.
- Evaluate recommendations with a horticulture expert.
- Test with real-world phone photos.

## Project details
- **Project name:** PlantSaathi
- **Category:** Plant care / agriculture technology
- **Stack:** Python, Streamlit, Pillow
- **Purpose:** Demonstrate an accessible plant-care assistant prototype for a college PBL submission.

## Disclaimer
Plant care recommendations are general information only. They may not identify the true cause of a plant's symptoms. Check the specific plant's needs and seek qualified horticulture advice when necessary.
