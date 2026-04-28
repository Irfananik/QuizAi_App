import streamlit as st

# Set page title and description
st.title("Note summary and quiz generator from images")
st.markdown("Upload 3 images to generate notes and quizzes.")
st.divider()

#sidebar
with st.sidebar:
    st.header("Control Panel")
    #images uploader
    images = st.file_uploader("Upload your images here", 
    type=["jpg", "jpeg", "png"], 
    accept_multiple_files=True, key="image_uploader")

    if images:
        if len(images) > 3:
            st.error("Please upload only 3 images.")
        else:
            st.subheader("Uploaded Images")
            col = st.columns(len(images))
            for i,img in enumerate(images):
                with col[i]:
                    st.image(img)