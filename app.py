from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
@app.route("/check", methods=["GET", "POST"])
def home():
  result = None
  if request.method == "POST":
    try:
      # HTML फॉर्म से डेटा ले रहे हैं
      name = request.form.get("name")
      age = int(request.form.get("age"))
      marks = float(request.form.get("marks"))
      income = float(request.form.get("income"))
      category = request.form.get("category")

      # आपका पुराना लॉजिक
      if category == "General":
        if age <= 18 and marks >= 70 and income <= 300000:
          result = " You are eligible."
        else:
          result = " You are not eligible."

      elif category == "OBC":
        if age <= 19 and marks >= 60 and income <= 300000:
          result = "You are eligible."
        else:
          result = " You are not eligible."

      elif category == "SC":
        if age <= 20 and marks >= 50 and income <= 500000:
          result = " You are eligible."
        else:
          result = " You are not eligible."

      elif category == "ST":
        if age <= 20 and marks >= 50 and income <= 500000:
          result = " You are eligible."
        else:
          result = " You are not eligible."
      else:
        result = "Invalid category."

    except Exception as e:
      result = "Please enter valid details."

  return render_template("index.html", result=result)


if __name__ == "__main__":
  app.run(debug=True)