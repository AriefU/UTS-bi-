import pandas as pd

df = pd.read_excel("product_data_with_native_chart.xlsx", sheet_name="Data Produk", header=0)
print(df.columns.tolist())
