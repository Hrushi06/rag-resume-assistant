RAG Resume Assistant

This project is a Prompt Engineering + Retrieval-Augmented Generation (RAG) based AI assistant 
that answers questions using resume data. The system uses resume content as context and 
generates grounded responses while reducing hallucinations.

--------------------------------------------------
Features
--------------------------------------------------
- Retrieval-Augmented Generation (RAG)
- Prompt Engineering
- Resume-based Question Answering
- Hallucination Control ("I don't know" fallback)
- Context Injection
- CLI Chat Interface
- Streamlit UI

--------------------------------------------------
Project Structure
--------------------------------------------------
rag-resume-assistant/
│-- app.py
│-- ui.py
│-- resume.txt
│-- requirements.txt
│-- README.txt
│-- .env (not uploaded)

--------------------------------------------------
Step 1 — Clone Repository
--------------------------------------------------
git clone https://github.com/your-username/rag-resume-assistant.git
cd rag-resume-assistant

--------------------------------------------------
Step 2 — Create Virtual Environment
--------------------------------------------------
Windows:
python -m venv venv
venv\Scripts\activate

Mac/Linux:
python3 -m venv venv
source venv/bin/activate

--------------------------------------------------
Step 3 — Install Dependencies
--------------------------------------------------
pip install -r requirements.txt

--------------------------------------------------
Step 4 — Add API Key
--------------------------------------------------
Create .env file in root folder

OPENROUTER_API_KEY=your_api_key_here

--------------------------------------------------
Step 5 — Add Resume Data
--------------------------------------------------
Edit resume.txt

Example:

Name: Hrushikesh Bharat Kharade

Skills: Python, AWS, Machine Learning

Projects:
Secure Image Retrieval using Deep Learning
Two Wheeler Health Monitoring System

--------------------------------------------------
Step 6 — Run CLI Version
--------------------------------------------------
python app.py

Example:
Ask: what are my skills?

--------------------------------------------------
Step 7 — Run UI Version
--------------------------------------------------
streamlit run ui.py

--------------------------------------------------
Example Questions
--------------------------------------------------
- What are my skills?
- What projects have I done?
- Summarize my resume
- Suggest roles for me
- What is my salary?

--------------------------------------------------
Tech Stack
--------------------------------------------------
Python
Prompt Engineering
Retrieval-Augmented Generation (RAG)
Streamlit
LLM API
dotenv
requests

--------------------------------------------------
How It Works
--------------------------------------------------
1. Loads resume as knowledge base
2. Injects context into prompt
3. Sends prompt to LLM
4. Generates grounded response
5. Displays answer

--------------------------------------------------
Author
--------------------------------------------------
Hrushikesh Bharat Kharade
Prompt Engineering | Generative AI | Machine Learning
