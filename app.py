from flask import Flask, render_template, request, redirect
app = Flask(__name__)

variable = []

@app.route('/', methods=["GET"])
def homepage():
  # view the posts page
  return render_template("posts.html", posts=variable)

@app.route('/form', methods=["GET"])
def displayform():
  # view the form
  return render_template("form.html")

@app.route('/domessage', methods=["POST"])
def doform():
  info2 = request.form.get("username")
  if len(info2) < 8:
    return redirect('form')
  else:
    # receive and process the form
    info = request.form.get("message")# the name attribute of the html form field
    variable.append(info)# save the data to a variable
    return redirect('/')
  

'''
Build a flask app with 2 pages
Form page sends message to sever via POST
All posts page displays all the messages
Index/layout includes links to view each page.

'''

if __name__ == '__main__':
  app.run(debug=True)



'''
if request.method == "GET":
    # get sends stuff to the user
    return render_template("page.html")
  else:
    # post sends stuff to the server
    return "POST!"
'''