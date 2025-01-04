import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
)
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Window")
        self.setFixedSize(400, 300)

        # Layout utama
        main_layout = QVBoxLayout(self)

        # Latar belakang
        self.background_label = QLabel(self)
        pixmap = QPixmap("gambar.jpeg")  # Ganti dengan path gambar Anda
        self.background_label.setPixmap(pixmap)
        self.background_label.setScaledContents(True)
        self.background_label.setGeometry(0, 0, 400, 300)

        # Layout untuk widget login
        input_layout = QVBoxLayout()

        # Mengganti teks label "Welcome To Froggy Jumps Math Game"
        welcome_label = QLabel("Welcome To Froggy Jumps Math Game")
        welcome_label.setFont(QFont("Times New Roman", 18))  # Menggunakan font Times New Roman
        welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        welcome_label.setStyleSheet("color: black;")  # Warna teks merah

        # Menambahkan jarak ke atas label welcome
        input_layout.addWidget(welcome_label)
        input_layout.addSpacing(20)  # Menambahkan jarak antara welcome dan input fields

        # Memperbesar ukuran font untuk label Username dan mengganti warna putih
        username_label = QLabel("Username:")
        username_label.setFont(QFont("Times New Roman", 14))  # Ukuran font lebih besar
        username_label.setStyleSheet("color: white;")  # Warna teks putih
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter your username")
        self.username_input.setStyleSheet("padding: 5px; font-family: 'Times New Roman'; font-size: 10pt; color: black;")  # Teks input hitam

        # Memperbesar ukuran font untuk label Password dan mengganti warna putih
        password_label = QLabel("Password:")
        password_label.setFont(QFont("Times New Roman", 14))  # Ukuran font lebih besar
        password_label.setStyleSheet("color: white;")  # Warna teks putih
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter your password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setStyleSheet("padding: 5px; font-family: 'Times New Roman'; font-size: 10pt; color: black;")  # Teks input hitam

        # Menambahkan jarak sebelum tombol login
        input_layout.addWidget(username_label)
        input_layout.addWidget(self.username_input)
        input_layout.addWidget(password_label)
        input_layout.addWidget(self.password_input)
        
        # Menambahkan jarak sebelum tombol Login
        input_layout.addSpacing(20)  # Menambahkan jarak 20 piksel sebelum tombol login

        # Tombol login
        self.login_button = QPushButton("Login")
        self.login_button.setStyleSheet(
            "background-color: #0078D7; color: white; font-family: 'Times New Roman'; font-size: 12pt; padding: 5px;"
        )
        self.login_button.clicked.connect(self.check_login)

        input_layout.addWidget(self.login_button)

        input_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addLayout(input_layout)

        self.setLayout(main_layout)

    def check_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username == "game" and password == "start":
            self.login_button.setText("Login berhasil")
            self.login_button.setStyleSheet("background-color: green; color: white; font-family: 'Times New Roman';")
        else:
            self.login_button.setText("Login Failed!")
            self.login_button.setStyleSheet("background-color: red; color: white; font-family: 'Times New Roman';")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
