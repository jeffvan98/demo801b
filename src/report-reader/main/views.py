from os import environ
from flask import Blueprint, render_template

name = environ.get("REPORT_READER_NAME", "Report Reader")
main_bp = Blueprint(
    "main", 
    __name__, 
    template_folder="templates", 
    static_folder="static")

@main_bp.route("/")
def index():    
    return render_template("index.html", name=name)

@main_bp.route("/explore")
def explore():
    return render_template("explore.html", name=name)

@main_bp.route("/about")
def about():
    return render_template("about.html", name=name)
