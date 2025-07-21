                                🧠 Streamlit Project  
                     📄 AI Research Agent using Groq + LangChain

📌 Project Overview

Welcome to my AI Research Agent! This web app allows you to input any research topic and automatically generates a research plan, gathers relevant insights, summarizes the findings, and exports everything as a downloadable PDF.

It’s powered by **Groq’s blazing-fast LLaMA3-70B model**, enhanced by LangChain tools, and wrapped in an interactive **Streamlit** interface — perfect for students, researchers, and curious minds!


🚀 How I Built & Ran the App (Step-by-Step):

Here’s the exact process I followed to bring this research assistant to life 👇

1️⃣ Created a project folder: `ai_research_agent`

2️⃣ Inside the folder, added a `src/` directory for the app code

3️⃣ Added the following key Python files:

- `main.py`: Streamlit frontend
- `agent_nodes.py`: LLM logic for planning, searching, and summarizing
- `agent_tools.py`: LangChain tools for reading PDFs and simulating web search

4️⃣ Created a `.env` file for API key storage:

GROQ_API_KEY=your_actual_groq_api_key_here

5️⃣ Created a `requirements.txt` file with these libraries:

langgraph==0.3.12
langchain-community==0.0.18
langchain==0.0.247
openai
duckduckgo-search
arxiv
python-dotenv
PyMuPDF
fpdf
streamlit


6️⃣ Installed all required packages via terminal:

pip install -r requirements.txt

7️⃣ Launched the app using Streamlit:

streamlit run src/main.py

8️⃣ Opened the app in my browser:

🌍 http://localhost:8501 (or the Streamlit URL provided)

---

🔁 GitHub Upload Steps

(Here’s how I published the project to GitHub 💻)

1️⃣ Created a new repository on GitHub

2️⃣ Opened terminal inside the local folder

3️⃣ Initialized Git:

git init

4️⃣ Added all files:

git add .

5️⃣ Committed with a message:

git commit -m "Add AI Research Agent with Groq"

6️⃣ Linked local repo to GitHub:

git remote add origin https://github.com/your-username/your-repo-name.git

7️⃣ Pushed the code:

git push -u origin main

📝 Replace `your-username` and `your-repo-name` with your actual GitHub details.


📁 Project Folder Structure

📦 ai_research_agent  
┣ 📁 .idea → IDE settings (safe to ignore in `.gitignore`)  
┣ 📁 src  
┃ ┣ 📄 main.py → Streamlit UI and PDF export logic  
┃ ┣ 📄 agent_nodes.py → LLM-powered research planner, searcher, summarizer  
┃ ┣ 📄 agent_tools.py → Tools for simulated search and PDF reading  
┃ ┗ 📄 utils.py → (Utility functions if needed)  
┣ 📁 venv → Virtual environment (not tracked)  
┣ 📄 .env → Stores your Groq API key  
┣ 📄 requirements.txt → All Python dependencies  
┣ 📄 README.md → You’re reading it!  
┗ 📄 LICENSE → MIT License


💡 What the App Can Do

✔ Accepts any research topic from the user  
✔ Generates a multi-step research plan using LLaMA3  
✔ Extracts bullet-point insights via simulated search  
✔ Summarizes findings and scores confidence  
✔ Exports all content as a PDF report  
✔ Clean UI built in Streamlit for instant use  

✨ Tech Stack Used

**Streamlit** — interactive front-end  
**Groq API (LLaMA3-70B)** — LLM for reasoning and writing  
**LangChain** — framework for chaining tools  
**Python-dotenv** — for environment variables  
**ReportLab** — to export research as PDF  
**PyPDF2** — read document inputs (if extended)


👩‍💻 Created By

**Ushmitha Annapaneni**

Feel free to ⭐ star or fork the project if you find it useful!

📄 License

**MIT License** — Free to use, modify, and share!
