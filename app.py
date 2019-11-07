import ipaddress
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Optional, IPAddress
from flask_wtf import FlaskForm
from flask import Flask, request, redirect, render_template, url_for, flash
from ipcalc import subnet_info


app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class IPCalcForm(FlaskForm):
    subnet = StringField('Subnet', validators=[DataRequired()])
    new_prefix = IntegerField('New Prefix', validators=[Optional()])

@app.route('/', methods=["GET", "POST"])
def index():
    form = IPCalcForm()
    if form.validate_on_submit():
        try:
            subnet = ipaddress.ip_network(form.data['subnet'])
            main_subnet = subnet_info(subnet)
            if form.data['new_prefix'] != '':
                new_prefixes_out = []                
                new_subnets = subnet.subnets(new_prefix=form.data['new_prefix'])

                for new_subnet in new_subnets:
                    new_prefixes_out.append(subnet_info(new_subnet))

            return render_template('results.html', main_subnet=main_subnet,
                                    new_prefixes_out=new_prefixes_out)
        except ValueError:
            return redirect(url_for('index'))
    return render_template('index.html', form=form)


if __name__ == "__main__":
    app.run(debug=True, port=8080)