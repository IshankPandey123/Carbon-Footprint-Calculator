from flask_wtf import FlaskForm
from wtforms import DecimalField, SelectField, FieldList, FormField
from wtforms.validators import InputRequired, NumberRange

class RowForm(FlaskForm):
    mot = SelectField(label='Mode of Transport', choices=["Car", "Bike", "Cycle", "Train", "Bus", "Foot"])
    avg_dist = DecimalField(u'Average Daily Distance Travelled (km)' ,default=0)
    class Meta:
        csrf = False

class CarbonForm(FlaskForm):
    dat = FieldList(FormField(RowForm),min_entries=4)
    # mot = SelectField(label='Mode of Transport', choices=["Car", "Bike", "Cycle", "Train", "Bus", "Foot"])
    # avg_dist = DecimalField(u'Average Daily Distance Travelled (km)',
    #                         validators=[InputRequired(), NumberRange(message="Please enter a valid decimal value")])
    monelec = DecimalField(u'Monthly electricity units consumed (kWh)',
                           validators=[InputRequired(), NumberRange(message="Please enter a valid decimal value")])
    freq = SelectField(label='Frequency', choices=["Quarterly","Monthly", "Annually"])
    class Meta:
        csrf = False