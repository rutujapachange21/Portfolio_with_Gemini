from flask import Flask, render_template, request, jsonify
import os

# Configure the templates directory to ensure it is found locally and on cloud servers
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates'))
app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def home():
    # Serves the main visual portfolio
    return render_template('index.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    try:
        data = request.get_json() if request.is_json else request.form
        name = data.get('name')
        email = data.get('email')
        subject = data.get('subject')
        message = data.get('message')
        
        # Log inquiries directly to your local terminal console
        print("\n" + "="*40)
        print("📥 NEW CONTACT INQUIRY RECEIVED")
        print("="*40)
        print(f"Sender:  {name} <{email}>")
        print(f"Subject: {subject}")
        print(f"Message: {message}")
        print("="*40 + "\n")
        
        return jsonify({
            "status": "success",
            "message": "Inquiry successfully logged in Flask backend!"
        }), 200
        
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 400

# This is the essential block that starts the web server when run locally!
if __name__ == '__main__':
    print("Starting local portfolio development server...")
    app.run(debug=True, host='127.0.0.1', port=5000)