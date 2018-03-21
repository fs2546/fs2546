from flask import Flask
from flask import render_template
from flask import redirect, url_for 
from flask import make_response, request 
from flask import abort
app = Flask(__name__)
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

@app.route('/')
def index():
    username = request.cookies.get('username')
    return 'Nice to see you again,{}'.format(username)

@app.route('/user/<username>')
def user_index(username):
    if username == 'invalid':
        abort(404)
    resp = make_response(render_template('user_index.html',username=username))
    resp.set_cookie('username',username)
    return resp
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post {}'.format(post_id)

if __name__ == '__main__':
    app.run()
