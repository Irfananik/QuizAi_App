import streamlit as st


def show_api_error(error_message):
	"""Show a simple API error message in Streamlit."""
	if error_message:
		st.error("API not working")
