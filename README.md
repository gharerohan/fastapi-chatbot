# 🤖 FastAPI OpenAI Chatbot

A simple and interactive chatbot built using **FastAPI**, **HTML/CSS/JS**, and **OpenAI GPT models**.  
This project provides both an **API endpoint** and a clean **web UI** for chatting with an AI assistant.

---

## 🚀 Features

✅ FastAPI backend for handling chat requests  
✅ Uses OpenAI’s GPT model (via the official `openai` Python library)  
✅ Simple and responsive web UI (HTML + CSS + JavaScript)  
✅ Modular structure – easy to extend or integrate with other systems  
✅ Environment variable support for API key (`.env` file)

---

## 🧩 Project Structure

```

fastapi-chatbot/
│
├── main.py                # FastAPI backend (API + UI routes)
├── requirements.txt       # Python dependencies
├── .gitignore
├── templates/
│   └── index.html         # Chat UI
└── static/
├── style.css          # Chat UI styling
└── script.js          # Handles chat requests

````

---

## ⚙️ Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/gharerohan/fastapi-chatbot.git
cd fastapi-chatbot
````

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate      # On Windows
# or
source venv/bin/activate   # On macOS/Linux
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Your OpenAI API Key

Create a file named `.env` in your project folder:

```
OPENAI_API_KEY=your_openai_api_key_here
```

---

## 🧠 Usage

### Run the app:

```bash
uvicorn main:app --reload
```

Then open your browser and visit:
👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

You’ll see a simple chat UI that connects to your FastAPI backend.

---

## 🧾 API Endpoint

You can also use the `/chat` API endpoint directly with tools like **Postman** or **curl**.

**POST** `/chat`

```json
{
  "prompt": "Hello, who are you?"
}
```

**Response**

```json
{
  "response": "Hello! I'm a helpful AI assistant."
}
```

---

## 🖥️ Deployment (Optional)

To deploy online for free, you can use [Render.com](https://render.com):

1. Push this repo to GitHub
2. Connect Render to your GitHub
3. Create a new **Web Service**
4. Set:

   * **Start command:** `uvicorn main:app --host 0.0.0.0 --port 10000`
   * Add environment variable: `OPENAI_API_KEY`

---

## 🧰 Tech Stack

* **Backend:** FastAPI
* **Frontend:** HTML, CSS, JavaScript
* **AI Engine:** OpenAI GPT (gpt-4o-mini by default)

---

## 🧑‍💻 Author

**Rohan Gharé**
🔗 [GitHub Profile](https://github.com/gharerohan)

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

---

### 💡 Future Enhancements

* Add chat history persistence (SQLite or MongoDB)
* Support for multiple users/sessions
* Real-time streaming responses
* Better chat bubble UI (like ChatGPT)

```
