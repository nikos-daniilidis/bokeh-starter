import numpy as np

from bokeh.plotting import figure, output_file, show

N = 4000
x = np.random.random(size=N) * 100
y = np.random.random(size=N) * 100
radii = np.random.random(size=N) * 1.5
colors = ["#%02x%02x%02x" % (r, g, 150) for r, g in zip(np.floor(50+2*x), np.floor(30+2*y))]

def main():
	output_file("color_scatter.html", title="color scatter.py example", mode="cdn")
		
	TOOLS = "resize, crosshair, pan, wheel_zoom, box_zoom, reset, box_select, lasso_select"
	
	p = figure(tools=TOOLS, x_range=(0,100), y_range=(0,100))
	
	p.circle(x, y, radius=radii, fill_color=colors, fill_alpha=0.6, line_color=None)
	
	show(p)	

if __name__=="__main__":
	main()
