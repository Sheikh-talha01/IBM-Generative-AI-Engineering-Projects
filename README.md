# Image Captioning with GenAI

This project uses the Salesforce BLIP (Bootstrapping Language-Image Pre-training) model to generate descriptive captions for images. It features a user-friendly web interface built with Gradio and can be easily containerized using Docker.

## Features
- **AI-Powered Captioning**: Uses `Salesforce/blip-image-captioning-base`.
- **Web Interface**: Simple and intuitive UI built with Gradio.
- **Docker Support**: Ready to be deployed as a container.

## Installation

### Prerequisites
- Python 3.9+
- Pip

### Setup
1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd Image-Captioning-with-GenAI
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python demo.py
   ```

## Docker Usage

1. Build the Docker image:
   ```bash
   docker build -t image-captioning .
   ```

2. Run the container:
   ```bash
   docker run -p 7860:7860 image-captioning
   ```
   Access the app at `http://localhost:7860`.

## Project Structure
- `demo.py`: Main application script with Gradio interface.
- `requirements.txt`: Python dependencies.
- `Dockerfile`: Container configuration.
- `Image-Captioning-with-GenAI/main.py`: Core logic script.
