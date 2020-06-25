from flask import Flask , render_template , url_for , request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
	with open('database.txt',mode='a') as database:
		name= data["name"]
		email= data["email"]
		message= data["message"]
		file = database.write(f'\n{name},{email},{message}')

@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
    	data=request.form.to_dict()
    	write_to_file(data)
    	return 'form submitted' 
    else:
      return 'something went wrong. Try again!'    
        