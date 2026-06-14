<div align="center">

# 🎯 AI Interview Prep Coach

### Your personal AI-powered interview coach — runs 100% locally on your machine

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Ollama](https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.com/)
[![Mistral](https://img.shields.io/badge/Mistral_AI-F7931E?style=for-the-badge&logo=mistral&logoColor=white)](https://mistral.ai/)
[![License: MIT](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)

<br/>

> 💡 **Ace your next interview** — practice technical, behavioral, and role-specific questions with an AI coach that guides you using proven frameworks like the **STAR method**, live code examples, and expert tips.  
> No API keys. No internet. Just you and your AI coach.

<br/>

![Demo Banner](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square) ![PRs](https://img.shields.io/badge/PRs-Welcome-blue?style=flat-square)

</div>

---

## 📌 What is this?

**AI Interview Prep Coach** is a simple, lightweight Streamlit web app powered by **Ollama** and **Mistral** that runs entirely on your local machine. You tell it your target job role, ask any interview question, and it responds like an expert coach — giving structured, interview-ready answers with tips baked in.

This is the local-first, privacy-friendly alternative to expensive interview prep platforms.

---

## ✨ Features

- 🧠 **Role-aware coaching** — just type your target role (e.g. "Data Engineer", "SDE-2 at Google") and the AI adapts
- 📋 **Structured answers** — responses follow bullet points, STAR method for behavioral, and code blocks for technical
- 💡 **Instant tips** — every answer ends with a coaching tip to level up your delivery
- 🔒 **100% local** — no data sent to any cloud, no API key needed
- ⚡ **Lightweight** — just 2 Python files to understand the whole project
- 📓 **Jupyter notebook included** — see the step-by-step build process from scratch

---

## 🗂️ Project Structure

```
ai_interview_prep/
│
├── interview_prep.py      # 🚀 Main Streamlit app (the chatbot UI)
├── chatbot.ipynb          # 📓 Development notebook (step-by-step build)
├── .gitignore             # 🚫 Files to ignore in git
└── README.md              # 📖 You are here!
```

---

## 🛠️ Tech Stack

| Tool | Role |
|------|------|
| [Python](https://www.python.org/) | Core language |
| [Streamlit](https://streamlit.io/) | Web UI framework |
| [Ollama](https://ollama.com/) | Local LLM runtime |
| [Mistral](https://mistral.ai/) | The AI model (runs via Ollama) |

---

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.10 or above
- [Ollama](https://ollama.com/download) — install it from their website

### 1. Clone the repository

```bash
git clone https://github.com/prvthmpcypher/ai_interview_prep.git
cd ai_interview_prep
```

### 2. Install Python dependencies

```bash
pip install streamlit ollama
```

### 3. Pull the Mistral model via Ollama

```bash
ollama pull mistral
```

> This downloads the Mistral 7B model (~4 GB). You only need to do this once.

### 4. Run the app

```bash
streamlit run interview_prep.py
```

Your browser will open automatically at `http://localhost:8501` 🎉

---

## 💬 How to Use

1. **Enter your target job role** — e.g. `Python Developer`, `Data Analyst`, `Full Stack Engineer`
2. **Type an interview question** — anything works:
   - *"Tell me about yourself"*
   - *"Explain the difference between SQL joins"*
   - *"How do you handle tight deadlines?"*
   - *"What is a REST API?"*
3. Click **💬 Get Answer** and your AI coach replies instantly

---

## 🧪 Try These Sample Questions

| Role | Question |
|------|----------|
| `Python Developer` | What is the difference between `@staticmethod` and `@classmethod`? |
| `Data Scientist` | How do you handle missing values in a dataset? |
| `Backend Engineer` | How would you design a URL shortener like Bitly? |
| `Any Role` | Tell me about a time you failed and what you learned from it |
| `Product Manager` | How do you prioritize features on a roadmap? |

---

## 🔭 How It Works

```
You type a question
        ↓
Streamlit sends it to Ollama
        ↓
Ollama runs Mistral locally on your CPU/GPU
        ↓
Mistral replies as an expert interview coach
        ↓
Answer appears on screen with tips
```

The system prompt injects the job role and rules (STAR method, code examples, tips) before every query — keeping the coach in character.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to open a [GitHub Issue](https://github.com/prvthmpcypher/ai_interview_prep/issues) or submit a pull request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m 'Add my feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a Pull Request

---

## 📜 License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

<div align="center">

## 👤 Author

<img src="https://github.com/prvthmpcypher.png" alt="prvthmpcypher" width="80" style="border-radius: 50%;"/>

**prvthmpcypher**

[![GitHub](https://img.shields.io/badge/GitHub-prvthmpcypher-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/prvthmpcypher)

*Building cool things with AI, one local model at a time.*

---

⭐ **If this helped you land a job, drop a star!** ⭐

</div>
