import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Visualisasi GMV Produk", layout="wide")
st.title("📊 Visualisasi GMV per Kanal - Top 5 Produk")

@st.cache_data
def load_data():
    file_path = "product_data_with_native_chart.xlsx"
    df = pd.read_excel(file_path, sheet_name="Data Produk", header=0)
    df = df[1:]  # Drop duplicate header row
    cols = [
        "GMV", "GMV dari Shop Tab", "GMV dari LIVE", 
        "GMV dari video", "GMV dari kartu produk"
    ]
    for col in cols:
        df[col] = pd.to_numeric(
            df[col].astype(str)
                  .str.replace("Rp", "", regex=False)
                  .str.replace(".", "", regex=False)
                  .str.replace(",", ".", regex=False),
            errors="coerce"
        )
    return df

df = load_data()

if "Produk" not in df.columns:
    st.error("Kolom 'Produk' tidak ditemukan. Cek header file Excel-nya.")
else:
    top_5 = df.sort_values(by="GMV", ascending=False).head(5)
    fig, ax = plt.subplots(figsize=(12, 6))
    channels = ["GMV dari Shop Tab", "GMV dari LIVE", "GMV dari video", "GMV dari kartu produk"]
    for channel in channels:
        ax.plot(top_5["Produk"], top_5[channel], marker="o", label=channel)

    ax.set_title("GMV per Kanal untuk Top 5 Produk", fontsize=16)
    ax.set_ylabel("GMV (dalam Rupiah)")
    ax.set_xlabel("Nama Produk")
    ax.tick_params(axis='x', rotation=45)
    ax.legend()
    st.pyplot(fig)

st.markdown("Sumber data: Sheet 'Data Produk' dari file Excel.")
