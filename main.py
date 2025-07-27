from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('mickiewicz_site.html')

if __name__ == '__main__':
    app.run()
