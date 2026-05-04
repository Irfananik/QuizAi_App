# QuizAi_App

Note summary and quiz generator from images — a small Streamlit app that extracts notes from uploaded images, generates audio, and produces quizzes using the Gemini API.

**Live demo:** https://imagetoquiz.streamlit.app/ 

**Features**

- Upload up to 3 images.
- Auto-generate concise notes (Markdown) from images.
- Convert generated notes to audio (TTS).
- Generate quizzes (multiple-choice) with selectable difficulty.
- Simple API error handling and status messages in the UI.

**Quick start**

1. Clone the repo and open the project folder.
2. Create and activate a Python virtual environment (optional but recommended):

```bash
python -m venv quizai_env
quizai_env\Scripts\activate    # Windows PowerShell
```

3. Install requirements:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root with your Gemini API key:

```dotenv
# .env
GEMINI_API_KEY="YOUR_API_KEY_HERE"
```

5. Run the app:

```bash
streamlit run app.py
```

**Notes & troubleshooting**

- The app requires a valid Gemini API key and appropriate quota. If you see quota or rate-limit errors (HTTP 429), either wait, enable billing on your Google Cloud project, or use a different API key.
- `.env` is ignored by default; do not commit secrets.
- If the quiz generation fails but notes/audio work, check API responses and ensure the model specified in `api_call.py` is available to your account.

**Files of interest**

- `app.py` — Streamlit UI and main application flow.
- `api_call.py` — Gemini API wrappers for notes, audio, and quiz generation.
- `error_handle.py` — small helper to display API errors in the UI.

If you'd like, I can add a `README` badge or an example `.env.example` file next.
