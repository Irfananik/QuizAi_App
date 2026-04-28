import streamlit as st

# Set page title and description
st.title("Note summary and quiz generator from images")
st.markdown("Upload maximal 5 and minimum 3 images to generate notes and quizzes.")
st.divider()

#sidebar
with st.sidebar:
    st.header("Control Panel")
    images = st.file_uploader("Upload your images here", 
    type=["jpg", "jpeg", "png"], 
    accept_multiple_files=True, key="image_uploader")

    if images:
        st.success(f"{len(images)} images uploaded successfully!")   