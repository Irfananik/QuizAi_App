import streamlit as st
from api_call import generate_notes, generate_audio, generate_quiz
from error_handle import show_api_error
from PIL import Image
import io

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

    pil_images = []
    for img in images:
        image = Image.open(io.BytesIO(img.read()))
        pil_images.append(image)

    if images:
        if len(images) > 3:
            st.error("Please upload only 3 images.")
        else:
            st.subheader("Uploaded Images")
            col = st.columns(len(images))
            for i,img in enumerate(images):
                with col[i]:
                    st.image(img)
    #dificulties
    st.markdown(
        """
        <style>
        div[data-baseweb="select"] {
            cursor: pointer;
        }
        div[data-baseweb="select"] * {
            cursor: pointer;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    selected_Option = st.selectbox(
        "Select quiz difficulty",
        ["Easy", "Medium", "Hard"],
        index = None,
        )
    if selected_Option:
        st.markdown(f"You selected: **{selected_Option}**")
    # else:
    #     st.error("Please select a difficulty level.")

    #button to generate notes and quizzes
    pressed = st.button(
        "Click the button to generate notes and quizzes", 
        type="primary", 
        key="generate_button"
        )

# Main content area
if pressed:
    if not images:
        st.error("Please upload 3 images to generate notes and quizzes.")
    # elif len(images) != 3:
    #     st.error("Please upload exactly 3 images.")
    elif not selected_Option:
        st.error("Please select a difficulty level.")
    # else:
    #     st.success("Generating notes and quizzes...")
    if images and selected_Option:
        
        #note container
        with st.container(border= True):
            st.subheader("Generated Notes")
            # st.markdown(f"Here are the notes generated from the uploaded images with **{selected_Option} difficulty.**")
            with st.spinner("Generating notes..."):
                try:
                    notes_response = generate_notes([img.name for img in images])
                    st.markdown(notes_response)
                except Exception as exc:
                    show_api_error(exc)
                    st.stop()
        
        #audio container
        with st.container(border= True):
            st.subheader("Generated Audio")
            # Placeholder for generated audio
        with st.spinner("Generating audio..."):
            audio_text = notes_response.replace("\n", " ")
            audio_text = audio_text.replace("#", "")
            audio_text = audio_text.replace("*", "")
            audio_text = audio_text.replace("-", "")
            audio_text = audio_text.replace("**", "")
            audio_text = audio_text.replace("_", "")
            audio_response = generate_audio(audio_text)
            st.audio(audio_response, format="audio/wav")

        #quiz container
        with st.container(border= True):
            st.subheader("Generated Quiz")
            st.markdown(f"Here is the quiz generated from the notes with **{selected_Option} difficulty.**")
            # Placeholder for generated quiz
            with st.spinner("Generating quiz..."):
                try:
                    quiz_response = generate_quiz(notes_response, selected_Option)
                    st.markdown(quiz_response)
                except Exception as exc:
                    show_api_error(exc)