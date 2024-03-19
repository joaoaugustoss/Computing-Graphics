# Trabalho 1 - Computação Gráfica
### Student: João Augusto dos Santos Silva - 724667
### Contact: joao.silva.452811@sga.pucminas.br
### Professor: Rosilane Ribeiro da Mota
### [Code Repository](https://github.com/joaoaugustoss/Computing-Graphics-Algorithms.git)
### [Code Presentation Video](https://drive.google.com/drive/folders/1jTHYOfLI6naLv41Bs3ab-Ef-lWoV_M4i?usp=sharing)
---
## Motivation
- This work aims to complement the knowledge acquired in the Computer Graphics course through the development of a practical application for the studied algorithms.
- At this work, several Computer Graphics algorithms with different purposes were developed. At first, we developed four Geometric Transformations (Translation, Scale, Rotation and Reflection), three Raster algorithms (DDA, Bresenham and Bresenham for Circunferences) and two Clipping algorithms (Cohen-Sutherland and Liang-Barsky).
- All the developed code was written in Python and tkinter library was used for the GUI.

---

## Development
In this section we'll discuss all decisions taken while developing the code. For this, this section is divided into subsections in order to explain each function separately and the data structures used.

#### Data Structures
For the implementation of the algorithms in the interface, I decided to use just 2 lists as data structures to store the points inputed on the screen. The first list, called ```points``` stores all the points received from the user, and this data structure is cleaned when a raster algorithm is called. Inside any of the raster functions implemented, the initial and final points are stored on our second list, called ```original_points```, so we can carry on with the transformations and the clipping.

- Example of what is stored in each list:
    - ```points``` -> ```[(x0,y0),(x1,y1),...,(xn,yn)]```
    - ```original_points``` -> ```[((x0,y0),(x1,y1)),((x3,y3),(x4,y4),(x5,y5)),...,((xm,ym),...,(xn,yn))]```

#### DDA 
Digital Differential Analyzer (DDA) algorithm is a method used for generating points on a line between two given endpoints. It's relatively simple and straightforward but may suffer from accuracy issues, especially when dealing with lines with steep slopes or when using integer arithmetic to round off floating-point coordinates. However, it remains a fundamental algorithm in computer graphics for its simplicity and efficiency in drawing lines.
- <strong>Input Parameters:</strong> For this algorithm, we take as input two lists and string c, list a for the initial point and b for the final point, each one containing points (x,y). The string C corresponds to the color parameter, which is a constant "red".
- <strong>Return:</strong> This function does not have a return, it just plots the calculated points to form the line.

#### Bresenham 
The Bresenham's line algorithm is another method for drawing lines in computer graphics, known for its efficiency and accuracy, especially when dealing with integer arithmetic. It's preferred over DDA for its ability to handle integer arithmetic efficiently, resulting in faster execution and better accuracy, particularly for lines with steep slopes. Additionally, it requires only integer addition and subtraction operations, making it suitable for implementation in hardware and software with limited computational resources.
- <strong>Input Parameters:</strong> For this algorithm, we take as input two lists and string c, list a for the initial point and b for the final point, each one containing points (x,y). The string C corresponds to the color parameter, which is a constant "red".
- <strong>Return:</strong> This function does not have a return, it just plots the calculated points to form the line.

#### Bresenham Circle 
Bresenham's circle algorithm is a method for drawing circles in computer graphics. It's known for its efficiency and simplicity. Unlike the midpoint circle algorithm, Bresenham's algorithm uses only integer arithmetic operations, making it suitable for implementation in hardware and software environments with limited computational resources.
- <strong>Input Parameters:</strong> For this algorithm, we take as input two lists and string c, list a for the center of the circle and b indicating the radius, each one containing points (x,y). The string C corresponds to the color parameter, which is a constant "red".
- <strong>Return:</strong> This function does not have a return, it just plots the calculated points to form the line.
- <strong>Auxiliar Functions:</strong> As a auxiliar function, we have the ```symetric_plot``` function that plot pixels for all the symetric points on the circle.

#### Cohen-Sutherland
The Cohen-Sutherland algorithm is a line-clipping algorithm used to determine whether a line segment is inside, outside, or partially inside a rectangular clipping window. It's widely used in computer graphics for efficiently discarding portions of lines that lie outside the viewport or clipping window.
- <strong>Input Parameters:</strong> For this algorithm, we take as input two lists a and b, for the initial and final point respectively, another two lists c_min and c_max with the points to delimit the clipping window and a string c, containing the color parameter.
- <strong>Return:</strong> This function does not have a return, it just plots the calculated points that are into the window.
- <strong>Auxiliar Functions:</strong> As a auxiliar function, we have the ```region_code``` function that returns the corresponding code of the region where the given point is positioned.

#### Liang-Barsky
The Liang-Barsky algorithm is another line-clipping algorithm used to efficiently determine whether a line segment lies entirely inside, outside, or partially inside a rectangular clipping window. It efficiently determines whether a line segment lies inside, outside, or partially inside a rectangular clipping window by performing simple parameter calculations and comparisons. It accurately determines the intersection points with the clipping window, allowing for precise rendering of line segments within specified boundaries.
- <strong>Input Parameters:</strong> For this algorithm, we take as input two lists a and b, for the initial and final point respectively, another two lists c_min and c_max with the points to delimit the clipping window and a string c, containing the color parameter.
- <strong>Return:</strong> This function does not have a return, it just plots the calculated points that are into the window.
- <strong>Auxiliar Functions:</strong> As a auxiliar function, we have the ```cliptest``` function that returns true if a point is inside the clipping window.
- <strong>Observation:</strong> While testing the code written from the pseudocode available on the slides, if a line is completely outside the window, its points can iterate through all if conditions from the code. For this, I decided to increase the number of tests, adding a if clause checking if the point is inside the boundaries, if it's, the point is plotted, if it's not, the point is discarted.

#### Translation
- <strong>Input Parameters:</strong> For this algorithm, we take as input two lists a and t, where a is the point to be translated and t is the translation vector.
- <strong>Return:</strong> This function returns the translated point.

#### Scale
- <strong>Input Parameters:</strong> For this algorithm, we take as input two lists a and s, where a is the point to be scaled and s is the scale vector.
- <strong>Return:</strong> This function returns the translated point.

#### Rotation
- <strong>Input Parameters:</strong> For this algorithm, we take as input list a, where it's the point to be reflected and the integer number o, corresponding to the rotation angle.
- <strong>Return:</strong> This function returns the rotated point.

#### Reflections
- <strong>Input Parameters:</strong> For this algorithm, we take as input list a, where it's the point to be reflected.
- <strong>Return:</strong> This function returns the reflected point.
---

## Interface
The image bellow shows the developed GUI to execute the algorithms.
On the left, we have a menu to select all the desired operations to be performed on the points shown at the canvas.
The description of each dropdown, text input and button is presented bellow.
#### Dropdowns
- <strong>Raster Algorithms:</strong>
    - Lists all Raster Algorithms implemented on this work (DDA, Bresenham and Bresenham Circunference).
- <strong>Transformations:</strong>
    - Lists all Geometric Transformations implemented on this work (Translation, Scale, Rotation, Reflection X, Reflection Y and Reflection XY).
- <strong>Clipping Algorithms:</strong>
    - Lists all Clipping Algorithms implemented on this work (Cohen-Sutherland and Liang-Barksy).

#### Text Inputs
- <strong>Rotation:</strong>
    - Degree value to rotate the points. Input expected is a integer number.
- <strong>Scale:</strong>
    - Values to scale the points. Input expected (x,y), where x and y are integer numbers.
- <strong>Translation:</strong>
    - Values to translate the points. Input expected (x,y), where x and y are integer numbers.

#### Buttons
- <strong>Raster:</strong>
    - This button is responsible for calling the selected raster function .
- <strong>Transformations:</strong>
    - This button is responsible for calling the selected transformation function with its proper parameters from its input.
- <strong>Clipping:</strong>
    - With the push of this button, the code will get the last two inputed points and consider both as the window limiters for the execution of the selected clipping algorithm. 
- <strong>Clear:</strong>
    - This button is responsible for cleaning the screen and deleting all points in our data structures.


<img title="Interface" src="/img/interface.png">

--- 

## Usage
In this final session, I present how to use the interface. At first, the program needs to be executed via terminal, using the command ```python3 interface.py```, after executing this command line, the user must pay attention for the following steps.

#### Raster Algorithms
- In order to use our Raster Algorithms, at first the user needs to select the points on screen, for this, it's necessary just to left-click on the blank canvas. After selecting the points, the desired raster algorithm must be selected on the first dropdown on the left side. When selected, the user must press the ```Raster``` button, and the selected algorithm will be executed.
- As a implementation decision, our raster algorithms connects the points following the order of the input, and connects the last point at the firts one.
- For the ```Bresenham Circle``` the user needs to input a point for the center and for the radius of the circle, after pressing ```Raster``` the calculated Circle will be displayed using the first marked point as the center and the second point as the radius.

#### Geometric Transformations
- In order to use our Geometric Transformations, at first the user needs to mark points on screen and use one of the Raster Algorithms.
- After using one of our Raster Algorithms, the user needs to select the desired Geometric Transformation to be executed, and after selecting and pressing the button ```Transformations```, the selected transformation will be applied to the initial and final point of the segment and call the ```DDA``` Raster Algorithm with the new points.
- This process is the same for all Geometric Transformations implemented in this work.

### Clipping Algorithms
- In order to use out Clipping Algorithms, at first the user needs to mark points on screen and use one of the Raster Algorithms.
- After using one of our Raster Algorithms, the user needs to select the desired Clipping Algorithm to be executed and mark two points to be consider the window limits for the clipping.
- After selecting the desired algorithm and marking the window limiters, the user must click on the button ```Clipping``` in order to execute the algorithm and have the results on screen.
