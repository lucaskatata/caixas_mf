# %%
import pandas as pd
import streamlit as st

url = r"https://docs.google.com/spreadsheets/d/1pN3DWzUr39GHLESwwhOY3aj0A_ZJEbQxDBTibaO99Ko/export?format=csv&gid=0#gid=0"

df = pd.read_csv(url)

st.set_page_config(layout="wide")
st.title("Informações caixas")

# st.dataframe(df)

lista_sku = df["sku"].unique().tolist()
lista_sku = sorted(lista_sku)

col1, col2, col3 = st.columns(3)

sku_selecionado = col1.selectbox(label="Sku", options=lista_sku)

df_filtrado = df[df["sku"] == sku_selecionado]

df_filtrado = df_filtrado.drop(columns="sku")
df_filtrado = df_filtrado.set_index("caixa")


col3.dataframe(df_filtrado)

total = df_filtrado["quantidade"].sum()

col2.metric(value=total, label="Total")
