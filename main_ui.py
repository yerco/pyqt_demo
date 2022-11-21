import sys

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
from factory_dal import FactoryDAL


# mixed naming conventions due to Qt's camel case
class Window(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)

        # Default DAL
        self.dal_type = "CustomerDAL"

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
        # self._createValidateButton()
        self._createSaveButton()
        self._createDataTable()
        self._createAddButton()
        self._createSelectDALCombo()  # loading default DAL
        self._loadGrid()

        self._cust: ICustomer = None

    def _createSelectCustomerCombo(self):
        self.customer_combo_box = QComboBox()
        self.customer_combo_box.addItems(["", "Customer", "Lead", "SelfService", "HomeDelivery"])
        layout = QFormLayout()
        layout.addRow(QLabel("Customer Type"), self.customer_combo_box)
        self.generalLayout.addLayout(layout, 0, 0)
        self.customer_combo_box.activated.connect(self._combobox_select)

    # Factory design pattern
    def _combobox_select(self):
        self.cust_type: str = self.customer_combo_box.currentText()
        self._cust: ICustomer = FactoryCustomer().create(self.cust_type)

    def _createSelectDALCombo(self):
        # Default DAL CustomerDAL
        self.dal = FactoryDAL().create(self.dal_type)
        self.combo_box_dal = QComboBox()
        self.combo_box_dal.addItems(["CustomerDAL", "SQLAlchemyDAL"])
        layout = QFormLayout()
        layout.addRow(QLabel("DAL"), self.combo_box_dal)
        self.generalLayout.addLayout(layout, 0, 2, 1, 1)
        self.combo_box_dal.activated.connect(self._combobox_dal)

    def _combobox_dal(self):
        self.dal_type = self.combo_box_dal.currentText()
        self.dal = FactoryDAL().create(self.dal_type)

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

    def _createAddButton(self):
        button = QPushButton("Add")
        self.generalLayout.addWidget(button, 3, 0, 1, 1)
        button.clicked.connect(self._add_record)

    def _add_record(self):
        if self._cust:
            try:
                self._set_customer()
                self.dal.add(self._cust)  # in memory
                self._loadGridInMemory()
                self._clear_customer_dialog()
            except Exception as e:
                dlg = QMessageBox(self)
                dlg.setWindowTitle("Validation Problem")
                dlg.setText(str(e))
                dlg.exec()
                pass

    def _createSaveButton(self):
        button = QPushButton("Save")
        self.generalLayout.addWidget(button, 3, 1, 1, 1)
        button.clicked.connect(self._customer_save)

    def _customer_save(self):
        self.dal.save()
        self._clear_customer_dialog()
        self._loadGrid()

    def _loadGridInMemory(self):
        self.table = QTableWidget()
        custs = self.dal.get_data()  # in memory
        self._fill_grid(custs)

    def _loadGrid(self):
        self.table = QTableWidget()
        self.table.setRowCount(0)
        custs = self.dal.search()  # from the DB
        self._fill_grid(custs)

    def _fill_grid(self, custs):
        self.table.setRowCount(len(custs))
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(["customer type", "customer name", "phone", "bill amount",
                                              "bill date", "address", "id"])
        for i, field in enumerate(custs):
            customer_type = QTableWidgetItem(field.customer_type)
            self.table.setItem(i, 0, customer_type)
            customer_name = QTableWidgetItem(field.customer_name)
            self.table.setItem(i, 1, customer_name)
            phone_number = QTableWidgetItem(field.phone_number)
            self.table.setItem(i, 2, phone_number)
            bill_amount = QTableWidgetItem(field.bill_amount)
            self.table.setItem(i, 3, bill_amount)
            bill_date = QTableWidgetItem(field.bill_date)
            self.table.setItem(i, 4, bill_date)
            address = QTableWidgetItem(field.address)
            self.table.setItem(i, 5, address)
            pk = QTableWidgetItem(str(field.id))
            self.table.setItem(i, 6, pk)
        self.generalLayout.addWidget(self.table, 4, 0, 1, 3)
        self.table.verticalHeader().sectionClicked.connect(self._clicked_row)

    def _clicked_row(self):
        ...

    def _clear_customer_dialog(self):
        self.customer_combo_box.update()
        self.customer_name.clear()
        self.phone_number.clear()
        self.bill_amount.clear()
        self.bill_amount.clear()
        self.address.clear()


def main():
    app = QApplication([])
    window = Window()
    window.setWindowTitle("PyQt Demo")
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
