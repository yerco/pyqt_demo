import sys
import datetime

from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QWidget,
    QGridLayout,
    QComboBox,
    QMainWindow,
    QFormLayout,
    QLineEdit,
    QTextEdit,
    QPushButton,
    QTableWidget,
    QMessageBox,
    QTableWidgetItem
)

from middle_layer import Customer, Lead, CustomerBase


# mixed naming conventions due to Qt's camel case
class Window(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("PyQt Demo")
        #self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        self.generalLayout = QGridLayout()
        # central widget is needed
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        self._createSelectCustomerCombo()
        self._createCustomerNameEntry()
        self._createPhoneNumberEntry()
        self._createBillAmountEntry()
        self._createBillDateEntry()
        self._createAddressEntry()
        self._createValidateButton()
        self._createDataTable()

    def _createSelectCustomerCombo(self):
        self.customer_combo_box = QComboBox()
        self.customer_combo_box.addItems(["", "Customer", "Lead"])
        layout = QFormLayout()
        layout.addRow(QLabel("Customer Type"), self.customer_combo_box)
        self.generalLayout.addLayout(layout, 0, 0)
        self.customer_combo_box.activated.connect(self._combobox_select)

    def _combobox_select(self, txt_selection):
        self.cust_type = self.customer_combo_box.currentText()
        if self.cust_type == "Customer":
            self._cust = Customer()
        if self.cust_type == "Lead":
            self._lead = Lead()

    def _createCustomerNameEntry(self):
        layout = QFormLayout()
        self.customer_name = QLineEdit()
        layout.addRow(QLabel("Customer Name"), self.customer_name)
        self.generalLayout.addLayout(layout, 1, 0)

    def _createPhoneNumberEntry(self):
        layout = QFormLayout()
        self.phone_number = QLineEdit()
        layout.addRow(QLabel("Phone Number"), self.phone_number)
        self.generalLayout.addLayout(layout, 2, 0)

    def _createBillAmountEntry(self):
        layout = QFormLayout()
        self.bill_amount = QLineEdit()
        layout.addRow(QLabel("Bill Amount"), self.bill_amount)
        self.generalLayout.addLayout(layout, 0, 1)

    def _createBillDateEntry(self):
        layout = QFormLayout()
        self.bill_date = QLineEdit()
        layout.addRow(QLabel("Bill Date"), self.bill_date)
        self.generalLayout.addLayout(layout, 1, 1)

    def _createAddressEntry(self):
        layout = QFormLayout()
        self.address = QTextEdit()
        self.address.setFixedSize(250, 70)
        layout.addRow(QLabel("Address"), self.address)
        self.generalLayout.addLayout(layout, 2, 1)

    def _createDataTable(self):
        table = QTableWidget()
        table.setRowCount(3)
        table.setColumnCount(7)
        self.generalLayout.addWidget(table, 4, 0, 1, 2)

    def _createValidateButton(self):
        button = QPushButton("Validate")
        self.generalLayout.addWidget(button, 3, 0)
        button.clicked.connect(self._customer_validation)

    def _customer_validation(self):
        if self.cust_type == "Customer":
            self._cust.validate()
        if self.cust_type == "Lead":
            self._lead.validate()


def main():
    app = QApplication([])
    window = Window()
    window.setWindowTitle("PyQt Demo")
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()