from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtWidgets import QMainWindow

from design import Ui_MainWindow

class Window(Ui_MainWindow, QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
    
    def initUI(self) -> None:
        db: QSqlDatabase = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('coffee.sqlite')
        if not db.open():
            print("Ошибка при открытии базы данных")
            return
        
        model: QSqlTableModel = QSqlTableModel(self, db)
        model.setTable('')  # TODO название главной таблицы
        model.select()
        self.table.setModel(model)
