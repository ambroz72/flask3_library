from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html',username=username,isActive=True)

@app.route('/books')
def book():
    books=[{'name':'Wheel of Time','author':'Robert jorden','cover':'https://m.media-amazon.com/images/I/411-TSdxIrL.jpg'},
               {'name':'Song of ice and fire ','author':'George RR Martin' ,'cover':'https://cdn.kobo.com/book-images/6701ad1a-fc89-4421-8e3f-79c36187d331/1200/1200/False/a-game-of-thrones-the-story-continues-books-1-5-a-game-of-thrones-a-clash-of-kings-a-storm-of-swords-a-feast-for-crows-a-dance-with-dragons-a-song-of-ice-and-fire.jpg' } ,
                {'name':'Harry Potter  ','author':'JK Rowling' ,'cover':'https://m.media-amazon.com/images/I/5165He67NEL.jpg' } ]

    return render_template('books.html',books=books)

app.run(debug=True)