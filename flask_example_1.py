import bokeh
from flask import Flask, url_for, render_template
from markupsafe import escape
from bokeh.plotting import figure, output_file, show

def create_bar_chart():
    fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
    counts = [5, 3, 4, 2, 4, 6]

    p = figure(x_range=fruits, plot_height=250, title="Fruit Counts",
               toolbar_location=None, tools="")

    p.vbar(x=fruits, top=counts, width=0.9)

    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    return p

###########

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route("/demo")
def chart():
    plot = create_bar_chart()
    script, div = bokeh.embed.components(plot)

    return render_template('testing_template.html',
                           the_div=div, the_script=script)