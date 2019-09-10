from PySide import QtCore, QtGui
import sys
from ui import Ui_Dialog

#Create application
app = QtGui.QApplication(sys.argv)

#Create form and init UI
Dialog = QtGui.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

#Hook Logic


#Run main Loop
sys.exit(app.exec_())