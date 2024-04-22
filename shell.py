import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Установка размеров окна
        self.setGeometry(0, 0, 800, 500)  # Ширина 800, высота 500
        
        # Установка заголовка окна
        self.setWindowTitle("X11 Test")
        
        # Создание метки с текстом
        label = QLabel("Привет, мир!", self)
        label.setGeometry(10, 10, 780, 480)  # Установка размеров метки
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
