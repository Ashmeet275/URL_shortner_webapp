# URL Shortener Web App

A simple and lightweight URL shortener web application built with Python and Flask. This application allows users to convert long URLs into easily shareable short links, track visit counts, and manage their shortened URLs.

## Features

- **Shorten URLs:** Generate a random 6-character short code for any valid long URL.
- **Redirection:** Seamlessly redirect from the short URL to the original destination.
- **Analytics (Visit Tracking):** Keep track of how many times a shortened URL has been accessed.
- **Manage Links:** View a list of all shortened URLs and delete them if no longer needed.
- **404 Handling:** Custom error page for invalid or non-existent short links.

## Technologies Used

- **Backend:** Python, Flask
- **Database:** SQLite3 (managed via custom models)
- **Frontend:** HTML/CSS (Jinja2 templates)

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Installation and Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Ashmeet275/URL_shortner_webapp.git
   cd URL_shortner_webapp
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv .venv
   # On Windows
   .venv\Scripts\activate
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```
   The application will start running in debug mode. Open your web browser and navigate to `http://127.0.0.1:5000/`.

## Usage

- Enter a valid URL into the input field on the home page and submit.
- A new short URL will be generated and displayed in the list below.
- Click on the short URL to be redirected to the original link.
- Use the delete button to remove a link from the database.

## License
This project is open-source and available for educational and personal use.
