# Automated Microring Resonator (MRR) Wafer Map Analysis

This project provides a Python-based automation tool for evaluating the performance of Microring Resonators (MRR) in silicon photonics. It processes experimental or simulated data to determine if specific designs meet quality benchmarks for Q-factor and Free Spectral Range (FSR).

## Overview
Designing photonics circuits requires finding the optimal "Goldilocks zone" between the **Ring Radius** and the **Coupling Gap**. This script automates that search by:
1. Calculating the **Quality Factor (Q)** using: 
   $$Q = \frac{\lambda_{res}}{FWHM}$$
2. Evaluating the **Free Spectral Range (FSR)** against design specifications.
3. Visualizing the "Pass/Fail" status of every design on a heatmap for rapid wafer-map inspection.

## Key Features
- **Automated Calculations:** Converts raw FWHM and resonance data into performance metrics.
- **Dynamic Heatmapping:** Uses `Seaborn` to visualize the parameter space.
- **Pass/Fail Overlay:** Automatically marks designs that meet specifications with a star (*) for easy identification.
- **Cross-Platform Compatibility:** Uses relative pathing to ensure the code runs on any machine.

## Project Structure
- `MRR.py`: The main analysis script.
- `mrr_for_test.csv`: Sample dataset containing radius, gap, and FSR measurements.
- `requirements.txt`: List of necessary Python libraries.

## How to Run
1. Clone this repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

## Example
If everything is done correctly you should get something that looks like this:
<img width="1504" height="1153" alt="Automate Wafer Map" src="https://github.com/user-attachments/assets/1a6f9d82-3583-4992-928e-2c0f6bc1309f" />

## Credit
I got this project from Kraggle.com where someone uploaded the csv that I have in this repository. 
Link to the Kraggle: https://www.kaggle.com/datasets/assylkhannurgali/mrr-parameters
