# Imort the app variable from the init
from marvel_phonebook_app import app

# Import specific packages from flask
from flask import render_template,request

# Import Our Form(s)
from marvel_phonebook_app.forms import AvengerInfoForm

# Default Home Route
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods = ['GET','POST'])
def register():
    # Init our Form
    form = AvengerInfoForm()
    # Validation of our form
    if request.method == 'POST' and form.validate():
        # Get Information from the form
        heroname = form.heroname.data
        phone = form.phone.data
        email = form.email.data
        password = form.password.data
        # Print the data to the server that comes from the form
        print(heroname,phone,email,password)

    return render_template('register.html',user_form = form)