from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    email = request.form['email']
    age = request.form['age']
    comments = request.form['comments']

    # Render the details on the web page
    return render_template('result.html', name=name, email=email, age=age, comments=comments)

@app.route('/download', methods=['POST'])
def download():
    name = request.form['name']
    email = request.form['email']
    age = request.form['age']
    comments = request.form['comments']

    # Create the content of the text file
    content = f"Name: {name}\nEmail: {email}\nAge: {age}\nComments: {comments}"

    # Create a downloadable response
    response = make_response(content)
    response.headers["Content-Disposition"] = "attachment; filename=details.txt"
    response.mimetype = 'text/plain'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

