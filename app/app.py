from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from converter import converter

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'test_key'

class ReusableForm(Form):
    input_value = TextField('Integer Value:', validators=[validators.required()])
    
    @app.route("/", methods=['GET', 'POST'])
    def index():
        form = ReusableForm(request.form)
        result = ''
        if request.method == 'POST':
            input_value = int(request.form['input_value'])
    
        if form.validate():
            result = converter.int_to_roman_converter(input_value)
        else:
            flash('Please enter integer from 1-3999')
    
        return render_template('index.html', form=form, result=result)

