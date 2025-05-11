from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", feedback=None, anchor="")

@app.route("/secret", methods=["POST"])
def secret():
    password = request.form.get("password", "").strip().lower()
    responses = {
        "1234": "Lol that's your best guess? Try again 😆",
        "diti": "Awww you're close! But not quite there.",
        "princess": "Getting warmer... 👀",
        "i love you": "😳 Confessing now?",
        "daddy": "You're killing me here princess🫠",
        "4587": "Won't be that easy princess🫠",
        "daddy's princess": "Well that you are but sadly not the passcode😔",
        "1309": None
    }

    if password == "1309":
        return render_template("secret.html")
    elif password in responses:
        return render_template("index.html", feedback=responses[password], anchor="#locked-section")
    else:
        return render_template("index.html", feedback="Nope. Try again, lovebug 🐞", anchor="#locked-section")

app.run(host="0.0.0.0", port=81)
