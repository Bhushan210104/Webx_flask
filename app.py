from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample project data
projects = [
    {"title": "Study Prep", "description": "A centralised Study platform", "image": "static/book.png", "link": "#"},
    {"title": "AI Chatbot", "description": "An AI-powered chatbot for customer service.", "image": "static/chatbot.png", "link": "#"},
    {"title": "E-Commerce App", "description": "An online store with payment integration.", "image": "static/ecommerce.png", "link": "#"}
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', projects=projects)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        return redirect(url_for('success', name=name, email=email, subject=subject, message=message))
    return render_template('contact.html')

@app.route('/success')
def success():
    name = request.args.get('name')
    email = request.args.get('email')
    subject = request.args.get('subject')
    message = request.args.get('message')
    return render_template('success.html', name=name, email=email, subject=subject, message=message)

if __name__ == '__main__':
    app.run(debug=True)
