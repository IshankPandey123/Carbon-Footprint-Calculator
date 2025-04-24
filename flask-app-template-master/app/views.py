from flask import render_template
from app import app
from app.forms import CarbonForm
from app.longcode import calculate_footprint


@app.route('/', methods=['GET','POST'])
def calculator():
    form = CarbonForm()

    if form.validate_on_submit():
        # mot = form.mot.data
        # avg_dist = float(form.avg_dist.data)*30
        fieldData = []
        for d in form.dat.data:
            fieldData.append([d['mot'],float(d['avg_dist'])])
        print(fieldData)
        monelec = float(form.monelec.data)
        freq = form.freq.data
        data = calculate_footprint(fieldData,monelec,freq)
        context = {
            'totem': data[0],
            'sugg': data[1]
        }
        chart = [
            ['Emissions', 'Values'],
            ['Transport Emissions', data[2]],
            ['Electricity Emissions', data[3]],
        ]
        form = CarbonForm(formdata=None) #tried to tackle the Form resubmission problem
        return render_template('new.html', **context, data=chart, form=form, show_modal=True)

    else:
        print(form.errors)
        context = {}
        chart = []
        form = CarbonForm()

    return render_template('new.html',**context,data=chart, form=form, show_modal="")


@app.route('/about')
def about():
    return render_template('about.html')


# @app.route('/show',methods=['POST'])
# # def plt_suggestions(data):
# #     context = {
# #         'totem' : data[0],
# #         'sugg'  : data[1]
# #     }
# #     chart = [
# #         ['Emissions', 'Values'],
# #         ['Transport Emissions',data[2]],
# #         ['Electricity Emissions',data[3]],
# #     ]
# #     return render_template('new.html',**context,data=chart,form=form)


