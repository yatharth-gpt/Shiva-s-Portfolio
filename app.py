from flask import Flask, request, render_template

app = Flask(__name__)

# Aapka HTML page serve karne ke liye
@app.route('/')
def home():
    return render_template('index.html') # Apni HTML file ko 'templates' folder me rakhein

# Form ka data receive karne ke liye
@app.route('/submit-form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Yahan aap is data ko Database me save kar sakte hain
        # Ya apne aap ko email bhej sakte hain
        print(f"New Message from {name} ({email}): {message}")
        
        return "Thank you! Your message has been sent."

if __name__ == '__main__':
    app.run(debug=True)