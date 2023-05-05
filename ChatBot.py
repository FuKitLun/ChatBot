import sys
import pygame

from PyQt5.QtWidgets import QApplication, QGraphicsScene
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

app = QApplication(sys.argv)
web_view = QWebEngineView()
web_view.load(QUrl("https://web.powerva.microsoft.com/environments/Default-cf4ee560-9e28-412f-b4ca-a93f404bde4e/bots/new_bot_df3f6c1e13df458a8e2bb5ab5f132400/webchat"))
web_view.show()
app.exec_()

# Create a graphics scene and add the web view to it
scene = QGraphicsScene()
scene.addWidget(web_view)


