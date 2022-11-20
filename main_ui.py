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

from interface_customer import ICustomer
from factory_customer import FactoryCustomer


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

        self._cust: ICustomer = None

    def _createSelectCustomerCombo(self):
        self.customer_combo_box = QComboBox()
        self.customer_combo_box.addItems(["", "Customer", "Lead"])
        layout = QFormLayout()
        layout.addRow(QLabel("Customer Type"), self.customer_combo_box)
        self.generalLayout.addLayout(layout, 0, 0)
        self.customer_combo_box.activated.connect(self._combobox_select)

    # Factory design pattern
    def _combobox_select(self):
        self.cust_type: str = self.customer_combo_box.currentText()
        self._cust: ICustomer = FactoryCustomer().create(self.cust_type)

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
        if self._cust:
            self._set_customer()
            try:
                self._cust.validate()
            except Exception as e:
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Validation Problem")
                dlg.setText(str(e))
                dlg.exec()
                pass
        else:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Warning")
            dlg.setText("Select type of customer")
            dlg.exec()

    def _set_customer(self):
        if self._cust:
            self._cust.customer_type = self.cust_type
            self._cust.customer_name = self.customer_name.text()
            self._cust.phone_number = self.phone_number.text()
            self._cust.bill_amount = self.bill_amount.text()
            self._cust.bill_date = self.bill_date.text()
            self._cust.address = self.address.toPlainText()


def main():
    app = QApplication([])
    window = Window()
    window.setWindowTitle("PyQt Demo")
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
