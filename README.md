# 🛰️ Bhuvan NDVI Analyzer - ISRO Project

Live Demo: (Deploy on Streamlit Cloud - Free)

**What it does:**
Analyzes satellite imagery from ISRO Bhuvan / NASA Landsat to map vegetation health using NDVI.

**Tech:** Python, Rasterio, OpenCV, Streamlit

**Features:**
- Upload Landsat TIFF (Band 4 Red + Band 5 NIR)
- Calculates NDVI = (NIR - Red)/(NIR + Red)
- Vegetation health map, flood detection, cloud masking
- Stats: Vegetation %, Barren %, Mean NDVI

**How to get data:**
1. ISRO Bhuvan: bhuvan.nrsc.gov.in -> Download LISS-III data
2. NASA: earthexplorer.usgs.gov -> Landsat 8/9 -> Bands 4,5

**For ISRO VSSC:**
This replicates work done at SAC Ahmedabad - Remote Sensing Applications.

**Run locally:**
pip install -r requirements.txt
streamlit run app.py
