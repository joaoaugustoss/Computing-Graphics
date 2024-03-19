"""
@author: João Augusto dos Santos Silva - 724667
Trabalho 1 - Computação gráfica
"""
import tkinter as tk
import math as m
import numpy as np

class PointMarkerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Trabalho 1 - Computação Gráfica 2024/1 - João Augusto dos Santos Silva")

        self.canvas_width = 600
        self.canvas_height = 600

        self.points = []  # Stores marked points
        self.original_points = [] # Stores updated points

        self.frame_left = tk.Frame(master)
        self.frame_left.pack(side=tk.LEFT, fill=tk.Y)

        self.canvas = tk.Canvas(master, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.canvas.bind("<Button-1>", self.mark_point)

        self.center_x = self.canvas_width / 2
        self.center_y = self.canvas_height / 2

        # Raster options
        self.input_label_s0 = tk.Label(self.frame_left, text="Raster Algorithms")
        self.input_label_s0.pack()
        self.processing_options = tk.StringVar(value="Select Processing")
        self.processing_options.trace("w", self.processing_options)
        self.option_menu = tk.OptionMenu(self.frame_left, self.processing_options,
                                          "DDA", "Bresenham", "Bresenham Circle")
        self.option_menu.pack(pady=10)

        # Transformations options
        self.input_label_s1 = tk.Label(self.frame_left, text="Transformations")
        self.input_label_s1.pack()
        self.processing_geometric_options = tk.StringVar(value="Select Transformation")
        self.processing_geometric_options.trace("w", self.processing_geometric_options)
        self.option_geometric_menu = tk.OptionMenu(self.frame_left, self.processing_geometric_options,
                                          "Translation", "Scale", "Rotation", "Reflection X", "Reflection Y", "Reflection XY")
        self.option_geometric_menu.pack(pady=10)

        # Clipping options
        self.input_label_s2 = tk.Label(self.frame_left, text="Clipping Algorithms")
        self.input_label_s2.pack()
        self.processing_clipping_options = tk.StringVar(value="Select Clipping")
        self.processing_clipping_options.trace("w", self.processing_clipping_options)
        self.option_menu = tk.OptionMenu(self.frame_left, self.processing_clipping_options,
                                          "Cohen Sutherland", "Liang Barsky")
        self.option_menu.pack(pady=10)

        # Rotation input
        self.input_label_ro = tk.Label(self.frame_left, text="Rotation")
        self.input_label_ro.pack()
        self.input_txt_ro = tk.Text(self.frame_left, height = 1, width = 20)
        self.input_txt_ro.pack() 
        self.input_txt_ro.insert('1.0', '30')

        # Scale input
        self.input_label_sc = tk.Label(self.frame_left, text="Scale")
        self.input_label_sc.pack()
        self.input_txt_sc = tk.Text(self.frame_left, height = 1, width = 20)
        self.input_txt_sc.pack() 
        self.input_txt_sc.insert('1.0', '(2,1)')

        # Translation input
        self.input_label_tr = tk.Label(self.frame_left, text="Translation")
        self.input_label_tr.pack()
        self.input_txt_tr = tk.Text(self.frame_left, height = 1, width = 20)
        self.input_txt_tr.pack() 
        self.input_txt_tr.insert('1.0', '(2,2)')

        # Calculate button for raster algorithms
        self.process_button = tk.Button(self.frame_left, text="Raster", command=self.button_click)
        self.process_button.pack(pady=10)

        # Geometric button to calculate the desired transformation
        self.process_button = tk.Button(self.frame_left, text="Transformations", command=self.button_geometric)
        self.process_button.pack(pady=10)

        # Clipping button to clip the screen
        self.clipping_button = tk.Button(self.frame_left, text="Clipping", command=self.button_clipping)
        self.clipping_button.pack(pady=10)

        # Clear button to clear the screen
        self.clear_button = tk.Button(self.frame_left, text="Clear", command=self.clear_click)
        self.clear_button.pack(pady=10)

    """
    function clear_click
    @params: none
    This function was created to delete all points on screen and
    clear all data structures that store points informations
    @return: none
    """
    def clear_click(self):
        self.points = []
        self.original_points = []
        for item in self.canvas.find_all():
            self.canvas.delete(item)

    """
    function mark_point
    @params: event
    This function was created to listen for a event on screen and 
    store the points selected by the user
    @return: none
    """
    def mark_point(self, event):
        x, y = event.x - self.center_x, self.center_y - event.y  # Adjusts coordinates to central point (0,0) on the center of the screen
        self.canvas.create_oval(event.x-2, event.y-2, event.x+2, event.y+2, fill="red")
        self.canvas.create_line(event.x, event.y, event.x+1, event.y+1, width=3, fill="red")
        self.points.append((int(x), int(y)))  # Appends adjusted coordinates to points list

    """
    function plot_point
    @params: x, y (coordinates)
    This function was created to plot the desired points on screen,
    It has a for loop in order to create several lines and make it more
    visible on screen
    @return: none
    """
    def plot_point(self, x, y, c):
        radius = 1  # point radius
        x, y = x + self.center_x, self.center_y - y
        self.canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill=c)
        for i in range(5):  # plot 5 lines for a thicker segment
            self.canvas.create_line(x-radius, y-radius+i, x+radius, y+radius+i, width=radius, fill=c)

    ##############################################
    ################### Raster ###################
    ##############################################
    """
    function button_click
    @params: none
    This function was created to listen for the button Calculate actions.
    If the button is pressed, it gets the selected algorithm and calls its function
    @return: none
    """
    def button_click(self):
        processing_type = self.processing_options.get()
        foo = 0

        if processing_type == 'DDA':
            p = self.points
            self.points = []
            for i in range(len(p)-1):
                self.original_points.append((p[i], p[i+1]))
                self.DDA(p[i], p[i+1], 'red')
                foo = i
            self.original_points.append((p[foo+1], p[0]))
            self.DDA(p[foo+1], p[0], 'red')

        elif processing_type == 'Bresenham':
            p = self.points
            self.points = []
            for i in range(len(p)-1):
                self.original_points.append((p[i], p[i+1]))
                self.bresenham(p[i], p[i+1], 'red')
                foo = i
            self.original_points.append((p[foo+1], p[0]))
            self.bresenham(p[foo+1], p[0], 'red')

        elif processing_type == 'Bresenham Circle':
            p = self.points
            self.points = []
            self.bresenham_circle(p[0], p[1], 'red')

    """
    function symetric_plot
    @params: x, y, xc, yc, color
    This function is a auxiliar function to plot all points
    calculated from function bresenham_circle
    @return: none
    """
    def symetric_plot(self, x, y, xc, yc, c):
        self.plot_point(xc + x, yc + y, c)
        self.plot_point(xc + x, yc - y, c)
        self.plot_point(xc - x, yc + y, c)
        self.plot_point(xc - x, yc - y, c)

        self.plot_point(xc + y, yc + x, c)
        self.plot_point(xc + y, yc - x, c)
        self.plot_point(xc - y, yc + x, c)
        self.plot_point(xc - y, yc - x, c)


    """
    function bresenham_circle
    @params a, b (center and radius), color
    This function was created to plot a circunference from 
    2 points selected by the user
    @return: none
    """
    def bresenham_circle(self, a, b, c):
        r = m.sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2)
        x = 0; y = r; p = 3-2*r

        self.symetric_plot(x, y, a[0], a[1], c)

        while(x<y):
            if p < 0: p += 4*x + 6
            else:
                p += 4*(x-y) + 10
                y -= 1
            x += 1
            self.symetric_plot(x, y, a[0], a[1], c)

    """
    function bresenham
    @params: a, b (start and final point), color
    This is a implementation for the Bresenham raster algorithm,
    where the user selects the first and last point on the canva 
    and the algorithm creates a segment to connect both points
    @return: none
    """
    def bresenham(self, a, b, c):
        self.original_points.append((a, b))
        dx = b[0] - a[0]; dy = b[1] - a[1]
        x = a[0]; y = a[1]

        if dx > 0: x_inc = 1
        else: dx = -dx; x_inc = -1

        if dy > 0: y_inc = 1
        else: dy = -dy; y_inc = -1

        self.plot_point(x, y, c)

        if(dx>dy):
            p = 2*dy - dx
            c1 = 2*dy; c2 = 2*(dy-dx) 

            for i in range(dx-1):
                x += x_inc
                if p < 0: p+=c1
                else: p+=c2; y+=y_inc
                self.plot_point(x,y,c)
        else: 
            p = 2*dx - dy
            c1 = 2*dx; c2 = 2*(dx-dy)

            for i in range(dy-1):
                y += y_inc
                if p < 0: p+=c1
                else: p+=c2; x+=x_inc
                self.plot_point(x,y,c)

    """
    function DDA
    @params: a, b (start and final point), color
    This is a implementation for the DDA raster algorithm,
    where the user selects the first and last point on the canva 
    and the algorithm creates a segment to connect both points
    @return: none
    """
    def DDA(self, a, b, c):
        self.original_points.append((a, b))
        dx = b[0] - a[0]; dy = b[1] - a[1]

        if abs(dx) > abs(dy): passos = abs(dx)
        else: passos = abs(dy)

        x_inc = dx/passos
        y_inc = dy/passos

        x = a[0]; y = a[1]

        self.plot_point(x, y, c)

        for i in range(1, passos+2):
            x += x_inc; y += y_inc
            self.plot_point(round(x), round(y), c)

    ##############################################
    ################## Clipping ##################
    ##############################################
    """
    function button_clipping
    @params: none
    This function was created to listen for the button Clip actions.
    If the button is pressed, it gets the selected algorithm and calls its function
    @return: none
    """
    def button_clipping(self):
        processing_clipping = self.processing_clipping_options.get()

        if processing_clipping == 'Cohen Sutherland':
            p = self.points
            po = self.original_points
            self.clear_click()
            self.points = []
            p.sort()
            c_min = p[0]; c_max = p[1]

            self.DDA(c_min, (c_max[0], c_min[1]), 'black')
            self.DDA(c_max, (c_max[0], c_min[1]), 'black')
            self.DDA(c_max, (c_min[0], c_max[1]), 'black')
            self.DDA(c_min, (c_min[0], c_max[1]), 'black')

            for i in po:
                self.cohen_sutherland(i[0], i[1], c_min, c_max, 'red')

        elif processing_clipping == 'Liang Barsky':
            p = self.points
            po = self.original_points
            self.clear_click()
            self.points = []
            p.sort()
            c_min = p[0]; c_max = p[1]

            self.DDA(c_min, (c_max[0], c_min[1]), 'black')
            self.DDA(c_max, (c_max[0], c_min[1]), 'black')
            self.DDA(c_max, (c_min[0], c_max[1]), 'black')
            self.DDA(c_min, (c_min[0], c_max[1]), 'black')

            for i in po:
                self.liang_barksy(i[0], i[1], c_min, c_max, 'red')

    """
    function region_code
    @params: a, c_min, c_max (point and window limits)
    This is a auxiliar function for Cohen Sutherland algorithm,
    returns the region code for the desired point
    @return: region_code for point a
    """
    def region_code(self, a, c_min, c_max):
        cod = 0
        if a[0] < c_min[0]: cod += 1
        if a[0] > c_max[0]: cod += 2
        if a[1] < c_min[1]: cod += 4
        if a[1] > c_max[1]: cod += 8
        return cod

    """
    function cohen_sutherland
    @params point a, point b, window limits, color

    @return: none
    """ 
    def cohen_sutherland(self, a, b, c_min, c_max, c):
        accept = False; done = False
        xmin = c_min[0]; ymin = c_min[1]
        xmax = c_max[0]; ymax = c_max[1]
        x1 = a[0]; y1 = a[1]; x2 = b[0]; y2 = b[1]
        xint = 0; yint = 0

        while(done != True):
            c1 = self.region_code((x1,y1), c_min, c_max)
            c2 = self.region_code((x2,y2), c_min, c_max)
            if c1 == 0 and c2 == 0: accept = True; done = True
            elif c1 & c2 != 0: done = True
            else:
                if c1 != 0: cfora = c1
                else: cfora = c2
                if cfora & 1 == 1: # bit 0 (left limit)
                    xint = xmin
                    yint = y1 + (y2-y1) * (xmin-x1)/(x2-x1)
                elif cfora & 2 == 2: # bit 1 (right limit)
                    xint = xmax
                    yint = y1 + (y2-y1) * (xmax-x1)/(x2-x1)
                elif cfora & 4 == 4: # bit 2 (lower limit)
                    yint = ymin
                    xint = x1 + (x2-x1) * (ymin-y1)/(y2-y1)
                elif cfora & 8 == 8: # bit 3 (upper limit)
                    yint = ymax
                    xint = x1 + (x2-x1) * (ymax-y1)/(y2-y1)
                if cfora == c1: x1 = xint; y1 = yint
                else: x2 = xint; y2 = yint
        a = (round(x1), round(y1))
        b = (round(x2), round(y2))
        if accept: self.DDA(a,b,c)

    """
    function cliptest
    @params p, q
    This is a auxiliar function for Liang Barsky algorithm
    @return: True if it's inside the window, False if it's not
    """
    u1 = 0; u2 = 0 # declaring u1 and u2, class variables for Liang Barsky algorithm
    def cliptest(self, p, q):
        result = True
        r = 0
        if p < 0:
            r = q/p
            if r > self.u1: self.u1 = r
            elif r > self.u2: result = False
        elif p > 0:
            r = q/p
            if r < self.u2: self.u2 = r
            elif r < self.u1: result = False
        elif q < 0: result = False
        return result

    """
    function liang_barsky
    @params point a, point b, window limits, color

    @return: none
    """ 
    def liang_barksy(self, a, b, c_min, c_max, c):
        xmin = c_min[0]; ymin = c_min[1]
        xmax = c_max[0]; ymax = c_max[1]
        x1 = a[0]; y1 = a[1]; x2 = b[0]; y2 = b[1]
        self.u1 = 0; self.u2 = 1; dx = x2 - x1; dy = y2 - y1
        if self.cliptest(-dx, x1-xmin):
            if self.cliptest(dx, xmax-x1):
                if self.cliptest(-dy, y1-ymin):
                    if self.cliptest(dy, ymax-y1):
                        if(self.u2 < 1):
                            x2 = x1 + dx*self.u2
                            y2 = y1 + dy*self.u2
                        if(self.u1 > 0):
                            x1 = x1 + dx*self.u1
                            y1 = y1 + dy*self.u1
                        if x1 >= xmin and x1 <= xmax and x2 >= xmin and x2 <= xmax and y1 >= ymin and y1 <= ymax and y2 >= ymin and y2 <= ymax: # this condition clause is a implementation decision
                            self.DDA((round(x1), round(y1)), (round(x2), round(y2)), c)

    ##############################################
    ######### Tansformações Geométricas ##########
    ##############################################
    """
    function button_geometric
    @params: none
    This function was created to listen for the button Geometric actions.
    If the button is pressed, it gets the selected algorithm and calls its function
    @return: none
    """
    def button_geometric(self):
        processing_geometric = self.processing_geometric_options.get()

        if processing_geometric == 'Scale':
            p = self.original_points
            self.clear_click()
            scale = (int(self.input_txt_sc.get('1.0', 'end').split('(')[1].split(',')[0]), int(self.input_txt_sc.get('1.0', 'end').split('(')[1].split(',')[1].split(')')[0]))

            for i in p:
                a = self.scale(i[0], scale)
                b = self.scale(i[1], scale)
                self.DDA(a, b, 'red')

        elif processing_geometric == 'Rotation':
            p = self.original_points
            self.clear_click()
            o = int(self.input_txt_ro.get('1.0', 'end'))

            for i in p:
                a = self.rotation(i[0], o)
                b = self.rotation(i[1], o)
                self.DDA(a, b, 'red')

        elif processing_geometric == 'Translation':
            p = self.original_points
            self.clear_click()
            t = (int(self.input_txt_sc.get('1.0', 'end').split('(')[1].split(',')[0]), int(self.input_txt_sc.get('1.0', 'end').split('(')[1].split(',')[1].split(')')[0]))

            for i in p:
                a = self.translation(i[0], t)
                b = self.translation(i[1], t)
                self.DDA(a, b, 'red')
            
        elif processing_geometric == "Reflection X":
            p = self.original_points
            self.clear_click()

            for i in p:
                a = self.x_reflection(i[0])
                b = self.x_reflection(i[1])
                self.DDA(a, b, 'red')

        elif processing_geometric == "Reflection Y":
            p = self.original_points
            self.clear_click()

            for i in p:
                a = self.y_reflection(i[0])
                b = self.y_reflection(i[1])
                self.DDA(a, b, 'red')

        elif processing_geometric == "Reflection XY":
            p = self.original_points
            self.clear_click()

            for i in p:
                a = self.xy_reflection(i[0])
                b = self.xy_reflection(i[1])
                self.DDA(a, b, 'red')

    """
    function translation
    @params: point, translation values
    This functions calculates the new point from the desired translation
    @return: new point
    """
    def translation(self, a, t):
        return(a[0] + t[0], a[1] + t[1])

    """
    function scale
    @params: point, scale values
    This functions calculates the new point from the desired scale value
    @return: new point
    """
    def scale(self, a, s):
        return ((a[0] * s[0]), (a[1]* s[1]))

    """
    function rotation
    @params: point, angle values
    This functions calculates the new point from the desired rotation angle
    @return: new point
    """
    def rotation(self, a, o):
        x = a[0] * m.cos(m.radians(o)) - a[1] * m.sin(m.radians(o))
        y = a[0] * m.sin(m.radians(o)) + a[1] * m.cos(m.radians(o))
        return(round(x),round(y))

    """
    function x_reflection
    @params: point
    This functions calculates the reflected point on x axis
    @return: new point
    """
    def x_reflection(self, a):
        return(a[0], -a[1])

    """
    function y_reflection
    @params: point
    This functions calculates the reflected point on y axis
    @return: new point
    """
    def y_reflection(self, a):
        return(-a[0], a[1])

    """
    function xy_reflection
    @params: point
    This functions calculates the reflected point on axis x and y
    @return: new point
    """
    def xy_reflection(self, a):
        return(-a[0], -a[1])


def main():
    root = tk.Tk()
    app = PointMarkerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
