import streamlit as st
import rasterio
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

st.set_page_config(page_title="Bhuvan NDVI Analyzer | ISRO Project", layout="wide")
st.title("🛰️ Bhuvan NDVI Analyzer - ISRO SAC Project")
st.markdown("**Upload Landsat / Bhuvan TIFF to calculate Vegetation Health (NDVI)**")

st.sidebar.header("How it works")
st.sidebar.markdown("""
**NDVI = (NIR - Red) / (NIR + Red)**
- Range: -1 to +1
- Green: Dense vegetation
- Brown: Barren land / Builtup
- Blue: Water

**Data Source:**
- ISRO Bhuvan: bhuvan.nrsc.gov.in
- NASA Landsat: earthexplorer.usgs.gov (Band 4=Red, Band 5=NIR)
""")

uploaded = st.file_uploader("Upload Satellite Image (TIFF with Red & NIR bands) OR 2 separate bands", type=['tif','tiff'])

# For demo - allow single RGB image to simulate
mode = st.radio("Select Mode:", ["Demo Mode (Use sample RGB as Red/NIR)", "Real Mode (Upload 2 bands - Red & NIR)"])

if mode == "Demo Mode (Use sample RGB as Red/NIR)":
    demo_file = st.file_uploader("Upload any satellite JPG/PNG for demo", type=['jpg','png','jpeg'])
    if demo_file:
        img = np.array(Image.open(demo_file))
        if len(img.shape) == 3:
            red = img[:,:,0].astype(float)
            nir = img[:,:,1].astype(float) # using green as NIR for demo
        else:
            red = img.astype(float)
            nir = img.astype(float) * 1.2
        
        ndvi = (nir - red) / (nir + red + 1e-10)
        ndvi = np.clip(ndvi, -1, 1)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader("Original")
            st.image(img, use_column_width=True)
        with col2:
            st.subheader("NDVI Map")
            fig, ax = plt.subplots()
            im = ax.imshow(ndvi, cmap='RdYlGn', vmin=-1, vmax=1)
            ax.axis('off')
            plt.colorbar(im, ax=ax, label='NDVI')
            st.pyplot(fig)
        with col3:
            st.subheader("Stats")
            st.metric("Mean NDVI", f"{np.mean(ndvi):.3f}")
            st.metric("Vegetation %", f"{np.sum(ndvi > 0.3)/ndvi.size*100:.1f}%")
            st.metric("Barren %", f"{np.sum(ndvi < 0.1)/ndvi.size*100:.1f}%")
            
            # Flood / Cloud detection simple
            st.write("**Analysis:**")
            if np.mean(ndvi) > 0.3:
                st.success("🌿 Healthy Vegetation / No Flood")
            elif np.mean(ndvi) < 0:
                st.error("🌊 Possible Waterlogged / Flood")
            else:
                st.warning("🏜️ Sparse Vegetation / Urban")

if mode == "Real Mode (Upload 2 bands - Red & NIR)":
    red_file = st.file_uploader("Upload RED Band (Band 4)", type=['tif','tiff'], key='red')
    nir_file = st.file_uploader("Upload NIR Band (Band 5)", type=['tif','tiff'], key='nir')
    if red_file and nir_file:
        with rasterio.open(red_file) as src:
            red = src.read(1).astype(float)
        with rasterio.open(nir_file) as src:
            nir = src.read(1).astype(float)
        
        ndvi = (nir - red) / (nir + red + 1e-10)
        
        fig, ax = plt.subplots()
        im = ax.imshow(ndvi, cmap='RdYlGn', vmin=-1, vmax=1)
        ax.axis('off')
        plt.colorbar(im)
        st.pyplot(fig)
        st.success("NDVI Calculated Successfully - This is what SAC Ahmedabad does!")

st.markdown("---")
st.markdown("**Built for ISRO VSSC Internship | Tech: Python, Rasterio, Streamlit | By Ananya0-alt**")
