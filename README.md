# ECG Viewer & Heart Rate Calculator


A Streamlit application that visualizes ECG signals, detects R-peaks, and computes an estimated heart rate (BPM).

## Biomedical Context

This app is intended for biomedical engineering students and learners who are studying ECG signal processing.  
It provides an interactive way to explore ECG waveforms, understand how R-peaks are detected, and see how heart rate is calculated from the R–R intervals.  
The tool is educational only and is not intended for clinical diagnosis.

## Quick Start Instructions

### Opening the Repository in GitHub Codespaces

1. Go to the repository:  
   https://github.com/allendoescode/ECG_Viewer_App
2. Click the green **Code** button.
3. Select **“Open with Codespaces”** (or create a new Codespace on `main`).
4. Wait for the Codespace to finish loading.

### Running the Application

1. In the Codespaces terminal, activate the virtual environment:

       source .venv/bin/activate

2. Run the Streamlit app:

       streamlit run app.py

3. When Codespaces shows a notification that the app is running on port 8501, click **“Open in Browser”** to view the ECG Viewer.

## Usage Guide

- **Step 1: Select ECG Source**  
  Use the sidebar on the left to choose between:
  - **Demo ECG**: uses a synthetic ECG signal generated in the app.  
  - **Upload CSV**: allows you to upload your own ECG data as a CSV file with `time` and `ecg` columns.

- **Step 2: Adjust Parameters**  
  Still in the sidebar, set:
  - **Sampling Rate (Hz)** – the sampling frequency of the ECG signal.  
  - **Minimum R–R Distance (ms)** – the minimum allowed distance between detected R-peaks.  
  - **Demo Duration (seconds)** – length of the synthetic ECG when using the demo mode.

- **Step 3: View Results**  
  After selecting the source and parameters, the main panel shows:
  - The **ECG Signal** plot.  
  - Red markers indicating **detected R-peaks**.  
  - A **Heart Rate Result** section displaying the estimated BPM.

You can capture a screenshot of this view (demo ECG selected, R-peaks shown, and BPM displayed) for documentation in your report.

## Data Description (optional)

### Data Source

- **Demo ECG**  
  The demo signal is generated programmatically using NumPy. It consists of Gaussian noise with simulated R-peaks added at regular intervals to mimic a simplified ECG.

- **Uploaded ECG**  
  Users can upload a CSV file with at least the following columns:

      time,ecg

  - `time` – time in seconds.  
  - `ecg` – ECG amplitude at each time point.  

If the required columns are missing, the app displays an error message instead of plotting.

## Project Structure

A high-level view of the project files:

- `app.py` – main Streamlit application that loads data, detects R-peaks, plots the ECG, and calculates heart rate.  
- `README.md` – this documentation file describing the project, usage, and structure.  
- `.venv/` – virtual environment directory used in Codespaces (not tracked by Git).  
- `.devcontainer/` – configuration files for the GitHub Codespaces development container.  
- `.vscode/` – editor settings for Visual Studio Code / Codespaces.  
- `.gitignore` – specifies files and folders that should not be tracked by Git (e.g., `.venv`, temporary files).

