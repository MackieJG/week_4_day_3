from flask import Flask, render_template
from controllers.book_controller import book_blueprint

app = Flask(__name__)
app.register_blueprint(book_blueprint)

@app.route('/')
def home():
    return render_template('/books/index.html')

if __name__ == '__main__':
    app.run()