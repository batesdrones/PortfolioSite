from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
    greeting = "Welcome to Andy's Data Science Portfolio Website"
    return render_template('index.html',
                           greeting=greeting)
@app.route('/about/')
def about():
    return render_template('about.html')
@app.route('/portfolio/')
def portfolio():
    return render_template('portfolio.html')
@app.route('/portfolio/bs_example')
def bs_example():
    return render_template('bs_example.html')
if __name__ == '__main__':
    app.run(debug=True)