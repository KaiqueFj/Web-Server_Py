from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)
print(__name__)


@app.route("/")
def my_home():
    return render_template('index.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        return redirect('thank_you.html')
    else:
        return 'something went wrong, try again'




# @app.route("/favicon.ico")
# def blog():
#     return render_template('these are my thoughts')




