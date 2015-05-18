import numpy as np
from bokeh.plotting import *

N = 100
x = np.linspace(0, 4*np.pi, N)
y0 = np.sin(x)
y1 = np.cos(x)
y2 = np.sin(x) + np.cos(x)

def main():
	s1 = figure(width=250, plot_height=250, title=None)
	s1.circle(x, y0, size=10, color="navy", alpha=0.5)

	s2 = figure(width=250, plot_height=250, title=None)
	s2.circle(x, y1, size=10, color="firebrick", alpha=0.5)

	s3 = figure(width=250, plot_height=250, title=None)
	s3.circle(x, y2, size=10, color="olive", alpha=0.5)

	p = gridplot([[s1, s2, s3]], toolbar_location=None)

	show(p)

if __name__=="__main__":
	main()
