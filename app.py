from flask import Flask, render_template, send_from_directory
import os

# Create Flask app
app = Flask(
    __name__,
    template_folder='templates',
    static_folder='static'
)

# Home Route
@app.route('/')
def home():
    return render_template('index.html')


# Optional: Route for direct static access (extra safety for Render)
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(app.static_folder, filename)


# Health check route (helps Render avoid crashes)
@app.route('/health')
def health():
    return "OK", 200


# Error handler (prevents blank 500 page)
@app.errorhandler(500)
def internal_error(error):
    return "Something went wrong on server!", 500


# Run app
if __name__ == '__main__':
    # Use PORT from Render or default 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)