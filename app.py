import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_wtf import FlaskForm
from wtforms import FileField, StringField, SubmitField
from wtforms.validators import DataRequired
from telethon import TelegramClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Telegram API credentials
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')  # Channel ID (e.g., -100XXXXXXXXXX)

# Initialize Telegram client
client = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

# Flask app setup
app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Replace with a secure random key
UPLOAD_FOLDER = 'uploads'
DOWNLOAD_FOLDER = 'downloads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Flask-WTF form for file upload
class UploadForm(FlaskForm):
    file = FileField("Choose File", validators=[DataRequired()])
    submit = SubmitField("Upload")

# Flask-WTF form for search
class SearchForm(FlaskForm):
    query = StringField("Search Query", validators=[DataRequired()])
    submit = SubmitField("Search")

# Home route
@app.route('/', methods=['GET', 'POST'])
def index():
    upload_form = UploadForm()
    search_form = SearchForm()
    files = []

    # Handle file upload
    if upload_form.validate_on_submit() and 'file' in request.files:
        file = upload_form.file.data
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        
        # Upload to Telegram channel
        client.loop.run_until_complete(
            client.send_file(CHANNEL_ID, file_path, caption=f"File: {file.filename}")
        )
        os.remove(file_path)
        return redirect(url_for('index'))

    # Handle file search
    if search_form.validate_on_submit():
        query = search_form.query.data.lower()
        async def search_files():
            async for message in client.iter_messages(CHANNEL_ID):
                if message.file and query in (message.file.name or "").lower():
                    files.append(message.file.name)
        client.loop.run_until_complete(search_files())

    return render_template('index.html', upload_form=upload_form, search_form=search_form, files=files)

# Route to list all files
@app.route('/files')
def list_files():
    files = []
    async def fetch_files():
        async for message in client.iter_messages(CHANNEL_ID):
            if message.file:
                files.append(message.file.name)
    client.loop.run_until_complete(fetch_files())
    return render_template('files.html', files=files)

# Route to download a file
@app.route('/download/<file_name>')
def download_file(file_name):
    async def fetch_and_download():
        async for message in client.iter_messages(CHANNEL_ID):
            if message.file and message.file.name == file_name:
                file_path = os.path.join(DOWNLOAD_FOLDER, file_name)
                await message.download_media(file_path)
                return file_path
    file_path = client.loop.run_until_complete(fetch_and_download())
    if file_path:
        return send_from_directory(DOWNLOAD_FOLDER, file_name, as_attachment=True)
    return "File not found", 404

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
