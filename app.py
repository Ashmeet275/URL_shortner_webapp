from flask import Flask, request, redirect, render_template
from function_models import(init_db,
                            insert_url, 
                            get_url,
                            visit_count, 
                            get_allurls, 
                            del_url
                            )
import random
import string


app = Flask(__name__)

init_db()

def generate_short_code(len = 6):
    return "".join(random.choices(string.ascii_letters + string.digits, k = len))


@app.route("/",methods = ['GET','POST'])
def index():
    if request.method =='POST':
        original_url = request.form['url']
        short_code = generate_short_code()
        insert_url(original_url, short_code)
        return redirect("/")

    get_all_urls = get_allurls()
    return render_template("index.html",all_urls = get_all_urls)
    

@app.route("/<short_code>")
def redirect_url(short_code):
    url_data = get_url(short_code)
    if url_data:
        visit_count(short_code)
        return redirect(url_data[1])
    return render_template('err404.html')

@app.route("/delete/<short_code>", methods = ["POST"])
def delete_url(short_code):
    del_url(short_code)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
