from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def index_1():
    return render_template('index.html')

@app.route('/inner-page')
def inner_page():
    return render_template('inner-page.html')

@app.route('/portfolio-details')
def portfolio_details():
    return render_template('portfolio-details.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/assets/<path:path>')
def serve_assets(path):
    return app.send_static_file('assets/' + path)

@app.route('/form/contact')
def contact_form():
    php_output = subprocess.check_output(['php', 'form/contact.php']).decode('utf-8')
    return php_output

if __name__ == '__main__':
    app.run(debug=True)
