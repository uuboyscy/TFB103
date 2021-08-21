from flask import Flask, request
# import test123
import poker as p

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask!'

@app.route('/helloFlask/<username>')
def helloFlask(username):
    outStr = """<h1>Hello {} !</h1>"""
    return outStr.format(username)

@app.route('/hello_get')
def hello_get():
    username = request.args.get('username')
    userage = request.args.get('userage')
    outStr = """Hello {}, you are {} years old."""
    if username == None:
        return """What's your name ?"""
    if userage == None:
        return """Hello {} .""".format(username)
    return outStr.format(username, userage)

@app.route('/add')
def add():
    x = int(request.args.get('x'))
    y = int(request.args.get('y'))
    return str(x + y)

@app.route('/hello_post', methods=['GET', 'POST'])
def hello_post():
    outStr = """
    <form action="/hello_post" method="POST">
        <input name="username">
        <button type="submit">SUBMIT</button>
    </form>
    """
    method = request.method
    if method == 'POST':
        username = request.form.get('username')
        outStr += """
        <div>Hello {} .</div>
        """.format(username)

    return outStr

@app.route('/poker', method=['GET', 'POST'])
def poker():
    return ''

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

