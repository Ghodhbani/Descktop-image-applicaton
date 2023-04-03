# Descktop-image-applicaton
This is a GUI application built using PyQt5 library, which provides a set of Python bindings for the Qt application framework.

The application has a class named ImageProcessor, which inherits from the QMainWindow class. This class defines the main window and all the widgets and actions that appear on the user interface.

The widgets used in this application include:

QLabel: used to display the path of the loaded image, the image itself, and the image dimension.
QToolBar: used to hold the actions (buttons) to open an image, display its dimension, show its histogram, convert it to grayscale, and show its contour.
QFileDialog: used to open a file dialog to browse and select an image.
FigureCanvasQTAgg: used to display the histogram plot.
QVBoxLayout and QHBoxLayout: used to create layouts for the widgets.
The actions available in this application include:

loadImage: opens a file dialog to browse and select an image file, and displays the selected image on the user interface.
showDimension: displays the width and height of the loaded image.
histo: displays the histogram plot of the loaded image.
makeGrey: converts the loaded image to grayscale and displays it.
makeContour: applies a contour filter to the loaded image and displays it.
restoreOriginal: displays the original loaded image if it has been modified by any of the above actions.
The application uses other Python libraries such as numpy, cv2, matplotlib, and PIL to handle image processing operations.
