# WhatsApp AI Chatbot

A simple WhatsApp automation bot built with Python, Selenium, and Gemini AI.

## Features

- Automatic WhatsApp replies
- Keyword-based responses
- AI-generated responses using Gemini API
- Real-time message monitoring
- Browser automation with Selenium

## Technologies Used

- Python
- Selenium
- Gemini API
- Microsoft Edge WebDriver

## Project Structure

```bash
whatsapp-ai-chatbot/
│
├── main.py
├── config.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/bonaarhousell/whatsapp-ai-chatbot.git
```

Move into the project folder:

```bash
cd whatsapp-ai-chatbot
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment (Windows):

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Create a `config.py` file:

```python
GROQ_API_KEY = "YOUR_GROQ_API_KEY"
```

## Run The Project

```bash
python main.py
```

## How It Works

1. Open WhatsApp Web
2. Scan QR Code
3. Open a target chat
4. The bot monitors incoming messages
5. Replies using:
   - predefined keyword responses
   - AI-generated responses

## Notes

- This project is for educational purposes only.
- Requires WhatsApp Web login.
- Requires Microsoft Edge installed.

## Future Improvements

- Better message detection
- Multi-chat support
- GUI interface
- Database logging
- Smarter AI prompts

## Author

Muhammad Nur Muliadi
