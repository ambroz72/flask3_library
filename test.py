from flask import Flask
new=Flask(__name__)

@new.route('/profile/<int:id>')
def profile(id):
    return '<h1> Welocme Boss... %d </h1>' % id
new.run(debug=True)
