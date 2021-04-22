from flask import render_template, request, redirect, url_for
from . import main


@main.route("/")
def index():
    """
    View root page function that returns the index page and its data
    """

    top_headlines = get_news()
    title = "Welcome to Pitches App"

    return render_template(
        "index.html", title=title
    )