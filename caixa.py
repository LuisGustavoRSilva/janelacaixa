import sys
# importar os compónentes para construção da janela
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTableView, QHBoxLayout, QVBoxLayout
# construção da classe janela com o nome caixa
class Caixa(QWidget):
    # Criação do metodo __init__ que inicia a janela e exibe ela em tela
    def __init__(self):
        super().__init__()
        # Vamos definir o tamanho e a posiçõa da tela 
        self.setGeometry(0,30,1000,800)

        # Vamos definir o titulo d anossa janela
        self.setWindowTitle("Caixa da loja")

        # Vamos criar as labels que representam as colunas esquerda e direita

        # Label da esquerda
        self.label_coluna_esquerda = QLabel()
        self.label_coluna_esquerda.setStyleSheet("QLabel {background-color: #01FFB9}")

        # Label da direita
        self.label_coluna_direita = QLabel()
        self.label_coluna_direita.setStyleSheet("Qlabel {background-color: #ff00ff}")

        # Criar o layput horizontal para as colunas
        self.h_layout = QHBoxLayout()

        # Vamos Adicionar as colunas esquerda e direita ao layout horizontal
        self.h_layout.addWidget(self.label_coluna_esquerda)
        self.h_layout.addWidget(self.label_coluna_direita)

        # Adicionar o layout na tela
        self.setLayout(self.h_layout)


app = QApplication(sys.argv)
cx = Caixa()
cx.show()
app.exec_()