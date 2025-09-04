# 🩺 Healthcare AI Assistant

A modern **Django + Smarty** web app that integrates AI to analyze and simplify medical texts.  
Clean UI powered by the **Smarty Bootstrap 5 theme**, responsive, and production-ready.

---

## ✨ Features
- 🧠 **AI Agent (DeepSeek)** – instant medical text analysis  
- 🎨 **Smarty UI** – professional theme, RTL ready  
- ⚡ **Fast & Lightweight** – Django + PostgreSQL backend  
- 🔒 **Privacy Focused** – secure handling of inputs  

---

## 🚀 Quick Start

1. **Clone the repo**
   ```bash
   git clone https://github.com/abdulwahed-sweden/healthcare-ai.git
   cd healthcare-ai
   ```

2. **Create virtual environment & install deps**
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Run migrations**
   ```bash
   python manage.py migrate
   ```

4. **Start the server**
   ```bash
   python manage.py runserver
   ```

5. **Open:** http://localhost:8000

---

## 🛠️ Tech Stack
- **Backend:** Django, PostgreSQL
- **Frontend:** Smarty Bootstrap 5 Theme, Font Awesome
- **AI:** DeepSeek API integration
- **DevOps:** Docker-ready, collectstatic for production

---

## 📂 Project Structure
```
healthcare-ai/
├── backend/
│   ├── templates/      # Django templates (Smarty integrated)
│   ├── static/         # Smarty assets (CSS, JS, fonts)
│   └── ...
├── requirements.txt
├── manage.py
└── README.md