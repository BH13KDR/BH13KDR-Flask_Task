from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', users=users)

users = [
    {"nickname": "traveler", "name": "Alex"},
    {"nickname": "photographer", "name": "Sam"},
    {"nickname": "gourmet", "name": "Chris"}
]

if __name__ == '__main__':
    app.run(debug=True)