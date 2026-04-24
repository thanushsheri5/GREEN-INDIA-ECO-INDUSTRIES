from flask import Flask, render_template
import os

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')


# Optional: Health check (useful for Render)
@app.route('/health')
def health():
    return "OK", 200


# Run app
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)