A simple Streamlit app that visualizes ECG data, detects R-peaks, and calculates estimated heart rate (BPM).

Biomedical Context

This application is designed for biomedical engineering students learning the fundamentals of ECG signal processing.
It provides an interactive way to explore ECG waveforms, detect R-peaks, and compute cardiac metrics without requiring advanced software or hardware.
The tool is educational, lightweight, and ideal for demonstrating core concepts like sampling rate, threshold detection, and heart-rate estimation.

Quick Start Instructions
Opening the Repository in GitHub Codespaces

Go to the repository link:
https://github.com/allendoescode/ECG_Viewer_App

Click the green Code button.

Select "Open with Codespaces" → New Codespace.

Wait for the environment to load.

Running the Application

Activate the virtual environment:

source .venv/bin/activate


Run the Streamlit app:

streamlit run app.py


A prompt will appear in Codespaces → click “Open in Browser.”

This launches the interactive ECG viewer.

Usage Guide

Step 1: Select ECG Source
In the sidebar, choose either:

Demo ECG (synthetic data), or

Upload CSV with time and ecg columns.

Step 2: Adjust Parameters
Modify sliders for:

Sampling Rate (Hz)

Minimum R–R interval (ms)

Demo Duration (if using synthetic ECG)

Step 3: View the Results
The app displays:

The ECG waveform

Automatically detected R-peaks (red dots)

Estimated heart rate (BPM)

Example Output:
(Insert your screenshot here)

Data Description (optional)
Data Source

Demo ECG: Generated programmatically using NumPy with simulated R-peaks and added noise.

Uploaded ECG: User-provided CSV file with two required columns:

time,ecg

Project Structure
ECG_Viewer_App/
│
├── app.py                # Main Streamlit application
├── README.md             # Documentation
├── .venv/                # Virtual environment
├── .devcontainer/        # Codespaces config
├── .vscode/              # Editor settings
└── .gitignore            # Files ignored by Git
