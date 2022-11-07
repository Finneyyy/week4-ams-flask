from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import *

app=Flask(__name__)

app.config['SECRET_KEY']='YOUR_SECRET_KEY'

class BasicForm(FlaskForm):
    first_name=StringField('First Name')
    last_name=StringField('Last Name')
    date_of_birth=DateField()
    favourite_number=DecimalField()
    favourite_food=SelectField("Favourite Food", choices=[('pizza','Pizza'),('spag','Spaghetti'),('chill','Chilli')])
    submit=SubmitField('Submit')
    
@app.route('/', methods=['GET','POST'])
@app.route('/home', methods=['GET','POST'])
def register():
    message=""
    form=BasicForm()
    '''
    first_name
    last_name
    date_of_birth
    favourite_number
    favourite_food => pizza, spaghetti, chilli
    '''
    if request.method=='POST':
        first_name=form.first_name.data
        last_name=form.last_name.data
        date_of_birth=form.date_of_birth.data
        favourite_number=form.favourite_number.data
        favourite_food=form.favourite_food.data
        if len(first_name)==0 or len(last_name)==0:
            message="Please supply both First and Last names"
        else:
            message=f"Thanks, {first_name} {last_name}!"
        
    return render_template('home.html', form=form, message=message)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')