# Telegramcloud

# Telegram Cloud Storage Bot

This project allows you to use a private Telegram channel as an unlimited cloud storage solution. The bot automatically uploads files to your private channel, making them easily accessible remotely, just like a cloud storage service.

## Features
- Upload files to your Telegram channel automatically.
- Retrieve uploaded files using Telegram bot commands.
- Manage file storage securely and remotely.
- Deployable on platforms like Heroku for 24/7 operation.

---

## Project Structure

```
telegram-cloud-bot/
â”œâ”€â”€ app.py                # Main Flask app for bot interaction
â”œâ”€â”€ requirements.txt      # Python dependencies
â”œâ”€â”€ .gitignore            # Files to ignore in Git
â”œâ”€â”€ .env                  # Environment variables (not included in Git)
â”œâ”€â”€ runtime.txt           # Specifies Python version for Heroku
â”œâ”€â”€ Procfile              # Specifies how to run the app on Heroku
```

---

## Setup Instructions

### 1. Clone the Repository

Clone this repository to your local machine:
```bash
git clone https://github.com/yourusername/telegram-cloud-bot.git
cd telegram-cloud-bot
```

### 2. Install Dependencies

Install the required Python libraries:
```bash
pip install -r requirements.txt
```

### 3. Configure `.env`

Create a `.env` file in the root directory and add the following environment variables:

```plaintext
API_ID=your_telegram_api_id
API_HASH=your_telegram_api_hash
BOT_TOKEN=your_telegram_bot_token
CHANNEL_ID=your_private_channel_id
SECRET_KEY=your_flask_secret_key
```

You can get your **API_ID** and **API_HASH** by creating a Telegram application on [Telegram's official website](https://my.telegram.org/auth). Also, create a **bot** by talking to [BotFather](https://core.telegram.org/bots#botfather).

### 4. Run the Bot Locally

Run the bot locally to test its functionality:

```bash
python app.py
```

Access the bot in Telegram and test uploading files.

---

## Deploy to Heroku

### 1. Deploy Manually

1. Ensure that the Heroku CLI is installed on your machine.
2. Log in to Heroku:
   ```bash
   heroku login
   ```
3. Create a new Heroku app:
   ```bash
   heroku create
   ```
4. Push your code to Heroku:
   ```bash
   git push heroku main
   ```
5. Set environment variables on Heroku:
   ```bash
   heroku config:set API_ID=your_telegram_api_id API_HASH=your_telegram_api_hash BOT_TOKEN=your_telegram_bot_token CHANNEL_ID=your_private_channel_id SECRET_KEY=your_flask_secret_key
   ```

### 2. Deploy with One Click

You can deploy this app directly to Heroku using the button below:

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/yourusername/telegram-cloud-bot)

---

## Files Explained

### 1. `app.py`

The main Python script containing:
- Flask app setup.
- Telegram Bot API interactions.
- Upload and download logic for the channel.

### 2. `requirements.txt`

Contains the Python libraries required for the project:
```plaintext
Flask==2.3.2
python-telegram-bot==20.5
python-dotenv==1.0.0
```

### 3. `.gitignore`

Prevents sensitive files and unnecessary system files from being committed to Git:
```plaintext
.env
__pycache__/
*.pyc
*.log
venv/
```

### 4. `Procfile`

Specifies how Heroku should run the app:
```plaintext
web: python app.py
```

### 5. `runtime.txt`

Defines the Python version for Heroku:
```plaintext
python-3.10.12
```

---

## How It Works

1. The bot uses the Telegram Bot API to receive and respond to user commands.
2. Files sent to the bot are uploaded to a private Telegram channel.
3. The bot can list files in the channel or retrieve them using commands.

---

## Security Tips

- **Never hard-code sensitive data** like API keys. Use environment variables for security.
- **Keep your `.env` file out of Git** by adding it to the `.gitignore` file.
- **Rotate your secret keys** periodically to enhance security.

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

If you have any questions or need further help, feel free to open an issue or contact me!
