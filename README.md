# Image Processing and Style Transfer App

A modern Python application that combines Streamlit frontend with FastAPI backend for interactive image processing and style transfer.

## Features

- Upload images through a user-friendly interface
- Apply various image filters and style transfers
- Real-time preview of processed images
- Download processed images
- Modern API backend with FastAPI
- Interactive frontend with Streamlit

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Start the FastAPI backend:
   ```bash
   python backend/main.py
   ```
   The API will be available at http://localhost:8000

2. In a new terminal, start the Streamlit frontend:
   ```bash
   streamlit run frontend/app.py
   ```
   The web interface will open automatically in your browser

## Project Structure

- `backend/` - FastAPI server code
  - `main.py` - Main FastAPI application
  - `processors/` - Image processing modules
- `frontend/` - Streamlit interface
  - `app.py` - Main Streamlit application
- `requirements.txt` - Project dependencies
