import streamlit as st
from  PIL import Image, ImageEnhance

st.header('Image Colorization using cycle gan :)')

uploaded_file = st.file_uploader("Choose a file",type=['jpg','png','jpeg'])
if uploaded_file is not None:
    # To read file as bytes:
    image = Image.open(uploaded_file)
    col1, col2 = st.columns( [0.5, 0.5])
    with col1:
        st.markdown('<p style="text-align: center;">Before</p>',unsafe_allow_html=True)
        st.image(image,width=300)  

    with col2:
        st.markdown('<p style="text-align: center;">After</p>',unsafe_allow_html=True)

