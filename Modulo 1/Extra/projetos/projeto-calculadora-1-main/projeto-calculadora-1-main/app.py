import streamlit as st
import calculadora as calc

st.title("calculadora 🧮")

numero1 = st.number_input("digite o primeiro numero: ",step=0.1,value=None)
numero2 = st.number_input("digite o segundo numero: ",step=0.1,value=None)
operacao = st.selectbox("selecione a operação", ["+", "-", "*", "/"] ) 

if st.button("calcular"):
    resultado = calc.calcular(numero1, numero2, operacao)
    st.toast(f"o resultado e:{resultado} ", duration=10,icon="✅")