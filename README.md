# AI-Powered PDF Summarizer

The AI-Powered PDF Summarizer is a web application that allows users to upload PDF documents, extract key insights, and generate customizable summaries using OpenAI's GPT-4 model. The application provides options for brief, detailed, and technical summaries and offers both a web interface and an API for integration.

## Key Highlights

1️⃣ **Versatile PDF Summarization**: Supports all types of PDF documents, including research papers, reports, and business documents. 2️⃣ **Customizable Summaries**: Generate brief, detailed, or technical summaries based on your needs. 3️⃣ **User-Friendly Interface**: Streamlit-powered web app for seamless interaction. 4️⃣ **API Integration**: FastAPI endpoint for programmatic access to summarization. 5️⃣ **Downloadable Output**: Save summaries as text files directly from the app. 6️⃣ **Containerized Deployment**: Fully dockerized for easy setup and deployment.

## Features

1️⃣ **PDF Upload and Parsing**: Upload PDF files and automatically extract text content. 2️⃣ **Customizable Summaries**: Choose between brief, detailed, and technical summary types. 3️⃣ **Streamlit Interface**: User-friendly web app for uploading files and viewing summaries. 4️⃣ **API Endpoint**: FastAPI endpoint for programmatic access to the summarization service. 5️⃣ **Downloadable Summaries**: Option to download summaries as text files.

## Technology Stack

- **Python 3.12**
- **Streamlit**: Frontend for web app
- **FastAPI**: API for backend integration
- **OpenAI API**: GPT-4 for summarization
- **PyMuPDF (fitz)**: PDF parsing
- **Docker**: Containerization

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/ai-powered-pdf-summarizer.git
cd ai-powered-pdf-summarizer
```

2. **Create a virtual environment and activate it:**

```bash
python3.12 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Set up the environment variables:** Create a `.env` file with the following content:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

### **Streamlit App**

```bash
streamlit run app/main.py
```

Access the app at `http://localhost:8501`

### **API Server**

```bash
uvicorn api.api:app --reload
```

Access the API at `http://localhost:8000/summarize`

## Docker

```bash
docker build -t ai-pdf-summarizer .
docker run -p 8000:8000 ai-pdf-summarizer
```

## Testing

```bash
pytest tests/
```

## License

This project is licensed under the MIT License.
