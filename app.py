#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st
import pandas as pd

file_path = r"C:\Users\user\Desktop\Python\data\03.アプリ\sales.xlsx"

df = pd.read_excel(file_path, sheet_name="Sales")
df["Date"] = pd.to_datetime(df["Date"])

store = st.selectbox("店舗選択", sorted(df["Store"].dropna().unique()))

filtered = df[df["Store"] == store].copy()

daily_sales = (
    filtered.groupby("Date", as_index=False)["SalesAmount"]
    .sum()
    .sort_values("Date")
    .set_index("Date")
)

st.title("店舗別売上推移")
st.metric("売上合計", f"{filtered['SalesAmount'].sum():,}円")
st.metric("客数", f"{filtered['CustomerID'].nunique():,}人")
st.metric(
    "客単価",
    f"{(filtered['SalesAmount'].sum() / filtered['CustomerID'].nunique()):,.0f}円"
    if filtered["CustomerID"].nunique() > 0 else "0円"
)

st.line_chart(daily_sales)


# In[ ]:




