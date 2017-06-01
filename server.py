from flask import Flask, request, redirect, render_template, flash  # Import Flask to allow us to create our app.
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
@app.route('/')          # The "@" symbol designates a "decorator" which attaches the following
                         # function to the '/' route. This means that whenever we send a request to
                         # localhost:5000/ we will run the following "hello_world" function.
def index():       
  return render_template('index.html') # Return 'Hello World!' to the response.

@app.route('/info', methods = ['POST'])
def info():
	name = request.form['name']
	location = request.form['location']
	language = request.form['language']
	comment = request.form['comment']
	if len(name) < 1:
		flash("Name cannot be empty!")
		return	render_template('index.html')	
	if len(comment) < 1:
		flash("Comment cannot be empty!")
		return	render_template('index.html')
	elif len(comment) > 120:
		flash("Comment cannot be more than 120 characters!")
		return	render_template('index.html')		
	return	render_template('info.html', name = name, location = location, language = language, comment = comment)
app.run(debug=True) 

# @app.route('/process', methods=['POST'])
# def process():
#   if len(request.form['name']) < 1:
#     flash("Name cannot be empty!") # just pass a string to the flash function
#   else:
#     flash("Success! Your name is {}".format(request.form['name'])) # just pass a string to the flash function
#   return redirect('/') # either way the application should return to the index and display the message
