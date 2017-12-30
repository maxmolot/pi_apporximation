#!/usr/bin/python

import time
import sys
import random
import numpy as np
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
	, QLCDNumber, QMainWindow, QInputDialog, QDialogButtonBox)
from PyQt5.QtGui import QPainter, QPainterPath
from PyQt5.QtCore import Qt, QPoint, pyqtSignal, QTimer, QEventLoop

class MyWidget (QMainWindow):

	
	def __init__(self):
		self.firstTime = True
		super().__init__()
		self.setGeometry(100, 100,1501, 1501)
		self.totalPoints = 0
		self.randPoints = []
		self.makeArray()
		
		
	def reset(self):
		self.totalPoints = 0
		self.randPoints.clear()
		self.repaint()
		
	def paintEvent(self, event):
		print('painted')
		zeri = QPoint(0,0)
		paint = QPainter()
		paint.begin(self)
		paint.setRenderHint(QPainter.Antialiasing)
		paint.setBrush(Qt.white)
		paint.drawRect(event.rect())
		rad = 751
		center = QPoint(751,751)
		paint.drawEllipse(center, rad, rad)

		for subArray in self.randPoints:
			x = subArray[0]
			y = subArray[1]
			r = subArray[2]
			painted = subArray[3]
			if not painted:
				if r <= 750.5:
					paint.setPen(Qt.red)
					ButtonScreen.numberInside += 1
					ButtonScreen.numberTotal += 1
				else:
					paint.setPen(Qt.blue)
					ButtonScreen.numberTotal += 1
				paint.drawPoint(x,y)
				subArray[3] = True
		paint.end()
		
	def makeArray(self):
		
		for i in range (len(self.randPoints), self.totalPoints):
			x = random.randint(0, 1500)
			y = random.randint(0, 1500)
			r = np.sqrt((x-751)**2 + (y-751)**2)
			painted = False
			self.randPoints.append([x,y,r, painted])
		self.repaint()
	
	def closeEvent(self, event):
		sys.exit()
		
class ButtonScreen (QWidget):
	numberInside = 0
	numberTotal = 0
	
	def __init__(self):
		super().__init__()
		self.setGeometry(1700, 500, 900, 1000)
		self.initUI()
		
		self.randPoints = []
		self.window = MyWidget()
		self.window.show()
		
	def makeArray(self):
		
		self.randPoints.clear()
		for i in range (len(randPoints), self.totalPoints):
			x = random.randint(0, 1500)
			y = random.randint(0, 1500)
			r = np.sqrt((x-750)**2 + (y-750)**2)
			self.randPoints.append([x,y,r])
	
	def paintCircle(self):
		
		
		if self.window.isVisible():
			j = 0
			skipAmount = 10000
			for i in range(1, int(self.totalPoints/skipAmount) + 1):
				#print(i)
				for j in range(0, skipAmount):
					print('i')
					#self.window.randPoints.append(self.randPoints[i])
				#print(self.window.randPoints)
				self.window.update()
				print(i)
				if i%50 == 0:
					#print(i)
					self.updateLcd()
			
				loop = QEventLoop()
				QTimer.singleShot(0.1, loop.quit)
				loop.exec_()
				#print('out of timer')
			print(len(self.window.randPoints))
			self.updateLcd()
			print('done')
			
		"""		
		if self.window.isVisible():
			for i in self.randPoints:
				self.window.randPoints.append(i)
			self.window.repaint()
			self.updateLcd()
		"""
		
	def initUI(self):
		self.lcd = QLCDNumber(self)
		self.lcd.setDigitCount(10)
		btn = QPushButton('Start', self)
		reset = QPushButton('Reset',self)
		
		self.text = QInputDialog()
		self.text.setInputMode(QInputDialog.IntInput)
		self.text.setOptions(QInputDialog.NoButtons)
		self.text.setIntMinimum(1)
		self.text.setIntMaximum(1000000)
		btn.clicked.connect(self.buttonPush)
		reset.clicked.connect(self.reset)
		vbox = QVBoxLayout()
		vbox.addWidget(self.lcd)	
		vbox.addWidget(self.text)
		vbox.addWidget(btn)
		vbox.addWidget(reset)
		self.setLayout(vbox)
	

	def updateLcd(self):
		self.lcd.display(4 *ButtonScreen.numberInside/ButtonScreen.numberTotal)
	def buttonPush(self):
		print('start')
		self.window.totalPoints += self.text.intValue()
		self.window.makeArray()
		self.updateLcd()
		#self.paintCircle()
	def reset(self):
		self.window.reset()
		ButtonScreen.numberInside = 0
		ButtonScreen.numberTotal = 0
		self.lcd.display(0)

	def closeEvent(self, event):
		sys.exit()
		
if __name__=='__main__':
	app = QApplication(sys.argv)
	buttonScreen = ButtonScreen()
	buttonScreen.show()
	sys.exit(app.exec_())
	