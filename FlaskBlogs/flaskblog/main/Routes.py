from flask import render_template, request, Blueprint
from flaskblog.Models import Post
from flask_login import login_required

main = Blueprint('main', __name__, template_folder='template')


@main.route("/")
@login_required
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('Home.html', posts=posts)


@main.route("/about")
def about():
    return render_template('About.html', title='About')
