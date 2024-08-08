import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar os dados
dados = pd.read_excel("vendas.xlsx")  # Certifique-se de que o arquivo esteja no mesmo diretório ou forneça o caminho correto

# Título da aplicação
st.title("Gráficos Interativos de Faturamento")

# Criação do histograma
grafico = px.histogram(dados, x="loja",
                       y="preco",
                       color="forma_pagamento",
                       text_auto=True,
                       title="Faturamento por loja")

# Exibição do gráfico no Streamlit
st.plotly_chart(grafico)
