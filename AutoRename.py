__version__= '1.1'
import os
import sys

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

## ==> MAIN WINDOW
from ui_AutoRename import Ui_MainWindow

os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = 'plugins/platforms'

class mainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
		self.setWindowIcon(QIcon('ICON.ico'))
		self.setWindowTitle(f'AutoRename v{__version__} by @diagom02')

		self.settings = QSettings('remember_options.ini', QSettings.IniFormat)
		self.ui.default_folder.setText(self.settings.value("default_folder"))
		self.ui.fansubs.setText(self.settings.value("fansubs"))
		self.ui.anime_name.setText(self.settings.value("anime_name"))
		self.ui.Formato.setText(self.settings.value("Formato"))
		self.ui.ext_name.setText(self.settings.value("ext_name"))
		self.ui.final_result.setText(self.settings.value("final_result"))

		if self.settings.value("default_folder") is None:
			self.ui.default_folder.setText(os.path.join(os.getenv('USERPROFILE'), 'Downloads'))

		self.ui.fansubs.textChanged.connect(self.textChange)
		self.ui.anime_name.textChanged.connect(self.textChange)
		self.ui.Formato.textChanged.connect(self.textChange)
		self.ui.ext_name.textChanged.connect(self.textChange)

		self.ui.browse_button.clicked.connect(self.select_folder)
		self.ui.rename_button.clicked.connect(self.rename_files)

		self.show()

	def select_folder(self):
		folder_dir = QFileDialog.getExistingDirectory(self, 'Select Directory')
		self.ui.default_folder.setText(str(folder_dir))

	def rename_files(self):
		FanSubs = self.ui.fansubs.text()
		AnimeN  = self.ui.anime_name.text()
		EpNum   = 0
		Calidad = self.ui.Formato.text()
		ext     = self.ui.ext_name.text()

		path = self.ui.default_folder.text()+'/'
		
		for path, subdirs, files in os.walk(path):
			# filename = [os.path.join(path, file) for file in files]
			for old_name in files:
				EpNum += 1
				new_name = f'[{FanSubs}] {AnimeN} - {EpNum:02} [{Calidad}].{ext}'
				# print(new_name)
				os.rename(path+old_name, path+new_name)

	def textChange(self):
		FanSubs = self.ui.fansubs.text()
		AnimeN  = self.ui.anime_name.text()
		Calidad = self.ui.Formato.text()
		ext     = self.ui.ext_name.text()

		self.ui.final_result.setText(f'[{FanSubs}] {AnimeN} - # [{Calidad}].{ext}')


	def closeEvent(self, event):
		self.settings.setValue("default_folder", self.ui.default_folder.text())
		self.settings.setValue("fansubs", self.ui.fansubs.text())
		self.settings.setValue("anime_name", self.ui.anime_name.text())
		self.settings.setValue("Formato", self.ui.Formato.text())
		self.settings.setValue("ext_name", self.ui.ext_name.text())
		self.settings.setValue("final_result", self.ui.final_result.text())



if __name__ == '__main__':
	app = QApplication(sys.argv)
	main = mainWindow()
	sys.exit(app.exec_())