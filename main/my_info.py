from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def page_index():
    my_name = "Robo Cop"
    return render_template("my_info.html", name=my_name)



app.run(host='0.0.0.0', port=80)