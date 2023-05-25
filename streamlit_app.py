import streamlit as st
from  PIL import Image, ImageEnhance

st.header('Image Colorization using cycle gan :)')

col1, col2 = st.columns( [0.5, 0.5])
uploaded_file = st.file_uploader("From here you can upload files from your computer:",type=['jpg','png','jpeg'])
def uploadingIMG():
    if uploaded_file is not None:
    # To read file as bytes:
        image = Image.open(uploaded_file)
        
        with col1:
            st.markdown('<p style="text-align: center;">Before</p>',unsafe_allow_html=True)
            st.image(image,width=300)  

    with col2:
            st.markdown('<p style="text-align: center;">After</p>',unsafe_allow_html=True)

uploaded_file = st.file_uploader("From here you can upload files from your computer:",type='jpg')
camera_picture = st.camera_input("You can tkae photos using your computers camera")
uploadingIMG(uploaded_file)
uploadingIMG(camera_picture)





