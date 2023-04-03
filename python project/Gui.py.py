import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QLabel, QFileDialog, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QPalette,QImage
from PyQt5 import QtGui
import numpy as np
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
import cv2
from PyQt5 import QtWidgets
from PyQt5.QtGui import QColor
import io
from PIL.ImageQt import ImageQt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from PIL import Image,ImageFilter

class ImageProcessor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.link = None
    def initUI(self):
        palette = QPalette()
        palette.setColor(QPalette.Background, QColor(180, 252, 255))
        self.setPalette(palette)
        toolbar = self.addToolBar("Image processor")
        load_button = QAction("Open", self)
        load_button.triggered.connect(self.loadImage)
        toolbar.addAction(load_button)
        dimension_button = QAction("Dimension", self)
        dimension_button.triggered.connect(self.showDimension)
        toolbar.addAction(dimension_button)
        histogram_button = QAction("Histogram", self)
        self.histogram_button = histogram_button  # Add this line
        histogram_button.triggered.connect(self.histo)
        toolbar.addAction(histogram_button)
        grey_button = QAction("Grey", self)
        grey_button.triggered.connect(self.makeGrey)
        toolbar.addAction(grey_button)
        contour_button = QAction("Contour", self)  # Create the contour button
        contour_button.triggered.connect(self.makeContour)  # Connect it to a method
        toolbar.addAction(contour_button)  # Add it to the toolbar
        to_original_button = QAction("Restore original", self)
        to_original_button.triggered.connect(self.restoreOriginal)
        toolbar.addAction(to_original_button)


       
        self.path_label = QLabel(self)
        self.path_label.setAlignment(Qt.AlignRight)
        self.path_label.setText("No image loaded.")
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.dimension_label = QLabel(self)
        self.dimension_label.setAlignment(Qt.AlignCenter)
        self.loading = QtWidgets.QLabel("Histogram")

        
    
        layout = QVBoxLayout()
        layout.addWidget(self.path_label)
        layout.addWidget(self.image_label)
        layout.addWidget(self.dimension_label)
        

    
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.setGeometry(100, 100, 800, 800)
        self.setWindowTitle("GUI Project")
        self.show()

    def loadImage(self):
        
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Images (*.png *.xpm *.jpg *.bmp *.gif);;All Files (*)", options=options)
        if file_name:
            self.pixmap = QPixmap(file_name)
            
            self.image_label.setPixmap(self.pixmap.scaled(self.image_label.width(), self.image_label.height(), QtCore.Qt.KeepAspectRatio))
            self.path_label.setText(file_name)

    def showDimension(self):
        try:
            width, height = self.pixmap.width(), self.pixmap.height()
            self.dimension_label.setText(f"The image dimension is: {width} x {height}")
        except AttributeError:
            print("Please load an image first.")
    def makeContour(self):
        try:
            image = Image.open(self.path_label.text())
            contour_im = image.filter(ImageFilter.CONTOUR)
            contour_im.save("contour.png")
            self.pixmap = QPixmap("contour.png")
            self.image_label.setPixmap(self.pixmap.scaled(self.image_label.width(), self.image_label.height(), Qt.KeepAspectRatio))
        except AttributeError:
            print("Please load an image first.") 
    def restoreOriginal(self):
        try:
            self.pixmap = QPixmap(self.path_label.text())
            self.image_label.setPixmap(self.pixmap.scaled(self.image_label.width(), self.image_label.height(), Qt.KeepAspectRatio))
        except AttributeError:
             print("Please load an image first.")
    def histo(self):
            img = cv2.imread(self.path_label.text())
            Image_Height = img.shape[0]
            Image_Width = img.shape[1]
            Image_Channels = img.shape[2]
            Histogram = np.zeros([256, Image_Channels], np.int32)
            for x in range(0, Image_Height):
                for y in range(0, Image_Width):
                    for c in range(0, Image_Channels):
                        Histogram[img[x, y, c], c] += 1
            plt.title("Color Image Histogram")
            plt.xlabel("Intensity Level")
            plt.xlim([0, 256])
            plt.plot(Histogram[:, 0], 'b') 
            plt.plot(Histogram[:, 1], 'g')  
            plt.plot(Histogram[:, 2], 'r') 
            plt.show()
    def makeGrey(self):
        try:
             qimage = self.pixmap.toImage()
             h, w, c = qimage.height(), qimage.width(), 4
             ptr = qimage.bits()
             ptr.setsize(qimage.byteCount())
             arr = np.array(ptr).reshape(h, w, c)
             image = Image.fromarray(arr)
             grey_im = image.convert('L')
             grey_im.save("grey.png")
             self.pixmap = QtGui.QPixmap("grey.png")
             self.image_label.setPixmap(self.pixmap)
             self.image_label.setScaledContents(True)
        except AttributeError:
             print("Please load an image first.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    image_processor = ImageProcessor()
    sys.exit(app.exec_())
   
