from flask import Flask, render_template

# Initialize Flask app
app = Flask(__name__)

# Define routes and associated functions

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile/<username>')
def profile(username):
    # Pass username and isActive flag to profile.html template
    return render_template('profile.html', username=username, isActive=True)

@app.route('/books')
def book():
    # Define a list of dictionaries containing book details
    books = [
        {
            'name': 'Wheel of Time',
            'author': 'Robert Jordan',
            'cover': 'https://m.media-amazon.com/images/I/411-TSdxIrL.jpg'
        },
        {
            'name': 'Song of Ice and Fire',
            'author': 'George R.R. Martin',
            'cover': 'https://cdn.kobo.com/book-images/6701ad1a-fc89-4421-8e3f-79c36187d331/1200/1200/False/a-game-of-thrones-the-story-continues-books-1-5-a-game-of-thrones-a-clash-of-kings-a-storm-of-swords-a-feast-for-crows-a-dance-with-dragons-a-song-of-ice-and-fire.jpg'
        },
        {
            'name': 'Harry Potter',
            'author': 'J.K. Rowling',
            'cover': 'https://m.media-amazon.com/images/I/5165He67NEL.jpg'
        }
    ]

    # Pass the list of books to the books.html template
    return render_template('books.html', books=books)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)