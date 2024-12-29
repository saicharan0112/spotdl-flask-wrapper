from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Initial form page.

@app.route('/manage_response', methods=['POST'])
def manage_response():
    # Get user inputs
    link = request.form['spotify-link']
    outdir = request.form['output_path']
    
    # Run the subprocess (spotdl command)
    try:
        result = subprocess.check_output(
            ["spotdl", "--output", outdir, link],
            stderr=subprocess.STDOUT,
            text=True
        )
        message = f"{result}"
    except subprocess.CalledProcessError as e:
        message = f"Error occurred: {e.output}"

    # Send the message back to the webpage
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
