# 🛰️ Bhuvan NDVI Analyzer - ISRO SAC Project

🚀 **Live App:** https://ananya0-alt-bhuvan-ndvi-analyzer-app-tfmcvc.streamlit.app
📁 **For ISRO VSSC Internship Application 2026**

### Overview
Developed a satellite image processing tool to calculate NDVI (Normalized Difference Vegetation Index) from ISRO Bhuvan & NASA Landsat data. This replicates vegetation health monitoring work done at ISRO SAC, Ahmedabad.

**NDVI Formula:** `NDVI = (NIR - Red) / (NIR + Red)`
- Range -1 to +1
- Green: Dense vegetation (>0.3)
- Brown: Barren land / Built-up (0.1 to 0.3)
- Blue: Water (<0)

### Data Source Used
- ISRO Bhuvan: bhuvan.nrsc.gov.in
- NASA Landsat: earthexplorer.usgs.gov (Band 4=Red, Band 5=NIR)
- Test Location: Kovalam, Trivandrum (8.3986 N, 76.9746 E) - DOP: 07-01-2025

### Features
- Upload Bhuvan / Landsat TIFF or JPG/PNG
- Two modes: Demo Mode (RGB proxy) & Real Mode (Red + NIR bands)
- Generates NDVI Map + Stats (Mean NDVI, Vegetation %, Barren %)
- Built with Python, Rasterio, OpenCV, Streamlit

### Results (Kovalam Coast)
- Mean NDVI: 0.148
- Vegetation: 6.6%
- Classification: Sparse Vegetation / Urban - matches coastal settlement reality

### Tech Stack
Python, Rasterio, NumPy, OpenCV, Matplotlib, Streamlit

### Built By
Ananya - BTech Student, Kochi
Built for ISRO VSSC Internship

### How to Run Locally
### Live Result
![Kovalam NDVI Result](https://... upload your screenshot to GitHub)

Kovalam, Trivandrum (8.3986N, 76.9746E) - Mean NDVI 0.148, Sparse Vegetation/Urban
