from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import re

app = Flask(__name__)

@app.route("/")
def index():
    article_url = "https://en.wikipedia.org/wiki/Alan_Turing" #Only Wikipedia article URLs
    response = requests.get(article_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content_text = soup.find(id='mw-content-text')
    
    if content_text:
        text = content_text.get_text()
        text = re.sub(r'\[\d+\]', '', text)  # Remove reference tags like [1], [2], etc.
    else:
        text = "Content not found"

    words = text.split()
    return render_template("index.html", words=words)  # Render the template with words

if __name__ == "__main__":
    app.run(debug=True)
