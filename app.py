from flask import Flask, render_template, request

app = Flask(__name__)  # ✅ This should come first

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']

        with open('messages.txt', 'a') as f:
            f.write(f"Name: {name}\nMessage: {message}\n---\n")

        return "Thanks for contacting us!"
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

