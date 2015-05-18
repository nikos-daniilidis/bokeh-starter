import numpy as np
from bokeh.plotting import *
from bokeh.models import ColumnDataSource

N = 300
x = np.linspace(0, 4*np.pi, N)
y0 = np.sin(x)
y1 = np.cos(x)

def main():
	output_file("linked_brushing.html", title="linked brushing example")

	source = ColumnDataSource(data=dict(x=x, y0=y0, y1=y1))

	TOOLS = "pan,wheel_zoom,box_zoom,reset,save,box_select,lasso_select"

	left = figure(tools=TOOLS, width=350, height=350, title=None)
	left.circle('x', 'y0', source=source)

	right = figure(tools=TOOLS, width=350, height=350, title=None)
	right.circle('x', 'y1', source=source)

	p = gridplot([[left, right]])

	show(p)

if __name__=="__main__":
	main()
