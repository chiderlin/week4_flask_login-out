from flask import Flask, request, render_template, redirect, session

app = Flask(__name__)
app.secret_key = "test@test.com" # 金鑰

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/signin", methods=["POST"])
def signin():
    if request.method == "POST":
        session["account"] = request.form["account"]
        session["password"] = request.form["password"]
        if session["account"] and session["password"] == "test":
            return redirect("/member/")
        else:
            return redirect("/error/")


@app.route("/member/", methods=["GET"])
def member():
    if session["account"] == None: # 如果目前是未登入狀態就不能到/member網址
        return redirect("/")
    elif session["account"] and session["password"] != "test":
        return redirect("/")
    else:
        return render_template("member.html")


@app.route("/error/", methods=["GET"])
def error():
    if session["account"] == None:
        return redirect("/")
    else:
        return render_template("error.html")


@app.route("/signout", methods=["GET"])
def signout():
    session["account"] = None
    session["password"] = None
    return redirect("/")


@app.errorhandler(404)
def not_found(error):
    return render_template("page_not_found.html"), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000, debug=True)