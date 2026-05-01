# TalentLens AI – Smart Hiring Intelligence

---

## Overview

---

TalentLens AI is an AI-powered application that analyzes a candidate’s resume against a job description to evaluate compatibility, identify skill gaps, and generate personalized interview questions along with actionable feedback. The system leverages Natural Language Processing and semantic similarity techniques to simulate intelligent hiring assistance.

## Features

---

* Resume and Job Description parsing from PDF files
* Skill extraction based on predefined technical keywords
* Semantic similarity scoring using transformer models
* Identification of missing and matching skills
* Automatic generation of interview questions
* Feedback system based on match score and skill gaps

## Tech Stack

---

* Python
* Streamlit
* Sentence Transformers
* PyMuPDF
* NumPy
* Torch

## Project Structure

---

talentlens-ai/
│
├── app.py
├── backend.py
├── skills.json
├── requirements.txt
├── README.md

## Installation

---

pip install -r requirements.txt

## Usage

---

streamlit run app.py

## How It Works

---

1. User uploads a resume and a job description in PDF format
2. The system extracts text from both documents
3. Skills are identified from each document
4. A similarity score is computed using a transformer model
5. Missing skills are detected
6. Interview questions are generated based on skill gaps
7. Feedback is provided to improve candidate readiness

## Output

---

* Match score between resume and job description
* List of detected skills in resume
* List of required skills from job description
* Missing skills
* Suggested improvements
* Generated interview questions

## Limitations

---

* Works best with text-based PDFs (not scanned images)
* Skill detection is based on predefined keywords
* Does not include real-time audio or video analysis

## Future Improvements

---

* Add speech-based confidence analysis
* Integrate facial emotion detection using computer vision
* Improve skill extraction using Named Entity Recognition
* Deploy as a web application using cloud platforms
* Add database support for storing user sessions

## Author

---

Developed as an AI-based project demonstrating applied machine learning, NLP, and full-stack integration for intelligent hiring systems.
### LIPSA PATTANAIK | ITER, SOA UNIVERSITY
