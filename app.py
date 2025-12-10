import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
#   ECG Utility Functions
# ---------------------------

def generate_demo_ecg(duration_s=10, fs=250):
    """Generate a synthetic ECG-like signal with simple peaks."""
    t = np.linspace(0, duration_s, duration_s * fs)
    signal = 0.05 * np.random.randn(len(t))  # noise
    
    # Create R-peaks every ~0.83s (HR ~72 BPM)
    rr_interval = 0.83
    for beat in np.arange(0, duration_s, rr_interval):
        idx = (np.abs(t - beat)).argmin()
        if 1 < idx < len(t) - 2:
            signal[idx] += 1.0
            signal[idx-1] += 0.4
            signal[idx+1] += 0.4
    return t, signal


def detect_r_peaks(ecg, fs, threshold_factor=0.5, min_distance_ms=300):
    """Very simple threshold-based R-peak detection."""
    ecg = np.array(ecg)
    threshold = np.mean(ecg) + threshold_factor * np.std(ecg)
    min_samples = int((min_distance_ms / 1000) * fs)

    peaks = []
    last_peak = -min_samples

    for i in range(1, len(ecg) - 1):
        if i - last_peak < min_samples:
            continue
        if ecg[i] > threshold and ecg[i] > ecg[i - 1] and ecg[i] > ecg[i + 1]:
            peaks.append(i)
            last_peak = i

    return np.array(peaks)


def compute_hr(peaks_idx, fs, duration_s):
    """Compute BPM from detected R-peaks."""
    if len(peaks_idx) < 2:
        return None
    beats = len(peaks_idx)
    hr = 60 * beats / duration_s
    return hr


# ---------------------------
#     Streamlit Interface
# ---------------------------

st.title("ECG Viewer & Heart Rate Calculator")

st.write("""
This interactive app allows you to **visualize ECG data**, detect **R-peaks**,  
and calculate **Heart Rate (BPM)**.  
Use the sidebar to choose demo data or upload your own CSV.
""")

# Sidebar options
st.sidebar.header("ECG Settings")

data_source = st.sidebar.radio("Select ECG Source:", ["Demo ECG", "Upload CSV"])

fs = st.sidebar.number_input("Sampling Rate (Hz):", value=250, min_value=50, max_value=2000)

min_distance_ms = st.sidebar.slider("Minimum R-R Distance (ms):", 200, 1000, 300)

# ---------------------------
# Load ECG Data
# ---------------------------

if data_source == "Demo ECG":
    duration_s = st.sidebar.slider("Demo Duration (seconds):", 5, 20, 10)
    t, ecg = generate_demo_ecg(duration_s, fs)
else:
    uploaded_file = st.sidebar.file_uploader("Upload CSV (must contain 'time' and 'ecg' columns):", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        if "time" in df.columns and "ecg" in df.columns:
            t = df["time"].values
            ecg = df["ecg"].values
        else:
            st.error("CSV must contain 'time' and 'ecg' columns.")
            t, ecg = None, None
    else:
        t, ecg = None, None

# ---------------------------
# Process and Display Results
# ---------------------------

if t is not None and ecg is not None:
    duration_s = t[-1] - t[0]
    
    # Detect peaks
    peaks = detect_r_peaks(ecg, fs, threshold_factor=0.5, min_distance_ms=min_distance_ms)
    hr = compute_hr(peaks, fs, duration_s)

    # Plot ECG
    st.subheader("ECG Signal")
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(t, ecg, label="ECG")
    if len(peaks) > 0:
        ax.plot(t[peaks], ecg[peaks], "ro", label="R-peaks")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Amplitude")
    ax.legend()
    st.pyplot(fig)

    # Heart Rate Output
    st.subheader("Heart Rate Result")
    if hr is not None:
        st.metric("Estimated Heart Rate (BPM)", f"{hr:.1f}")
    else:
        st.warning("Not enough peaks detected to compute HR.")

else:
    st.info("Upload a CSV or select Demo ECG to begin.")
