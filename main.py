import streamlit as st
import pickle as pkl

st.title('Previsão do Oscar!')

proba_model = pkl.load(open('./ensemble_proba_model.pkl', 'rb'))