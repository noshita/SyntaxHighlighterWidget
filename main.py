#!/usr/bin/env python

import os,json, re

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import (QApplication, QMainWindow,
                             QGridLayout, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton)
from PyQt5.QtWebKitWidgets import QWebView, QWebPage, QWebFrame


import gui



PARENTDIR=os.path.dirname(os.path.abspath(__file__))
CONFIGPATH = os.path.join(PARENTDIR,"config.json")
with open(CONFIGPATH,"r") as f:
    CONFIG=json.load(f)

if "SyntaxHighlighterPath" in CONFIG:
    SyntaxHighlighterPath = os.path.normpath(os.path.join(PARENTDIR,CONFIG["SyntaxHighlighterPath"]))
    # print(PARENTDIR,SyntaxHighlighterPath)
else:
    print("Error [config.json]: SyntaxHighlighterPath is required.")

if "AdditionalBrushesPath" in CONFIG:
    AdditionalBrushesPath = os.path.normpath(os.path.join(PARENTDIR,CONFIG["AdditionalBrushesPath"]))
else:
    print("Error [config.json]: AdditionalBrushesPath is required even if it is 'None'.")



HEADER_TOP = """<!DOCTYPE HTML">
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Syntax Highlighter</title>
        <link type="text/css" rel="stylesheet" href="%(shPath)s/styles/shCore.css" />
    </head>
        <link type="text/css" rel="stylesheet" href="%(shPath)s/styles/shThemeDefault.css" />
        <link type="text/css" rel="stylesheet" href="%(shPath)s/scripts/shCore.js" />
        <script type="text/javascript" src="%(shPath)s/scripts/shCore.js"></script>
""" % {"shPath":SyntaxHighlighterPath}



HEADER_BOTTOM = """<script type="text/javascript" src="%(brush)s"></script>
    </head>
    <body>
        <pre class="brush: %(lang)s">
"""

FOOTER = """
        </pre>
        <script type="text/javascript">
            SyntaxHighlighter.all();
</script>
    </body>
</html>
"""

BRUSHPTN=re.compile(r"shBrush(\w+)\.js")

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = gui.Ui_MainWindow()
        self.ui.setupUi(self)

        self._setBrushesCmbBox(os.path.join(SyntaxHighlighterPath,"scripts"),AdditionalBrushesPath)
        # self.brush = os.path.join(SyntaxHighlighterPath,"scripts/shBrushPython.js")
        # print(self.brush)
        # self.lang = "python"
        self.ui.cmbBox.currentIndex = 1
        self.chooseBrush()

        self.highlight()

        self.ui.pTxtEdtrInput.textChanged.connect(self.highlight)
        self.ui.cmbBox.currentIndexChanged.connect(self.chooseBrush)
        



    def highlight(self):
        HEADER = HEADER_TOP + HEADER_BOTTOM % {"brush": self.brush, "lang": self.lang}
        BODY = self.ui.pTxtEdtrInput.toPlainText()
        # self.testExport(HEADER+BODY+FOOTER, os.path.join(PARENTDIR,"test.html"))
        # self.ui.webVOutput.load(QUrl("file:///Users/noshita/working_dir/syntaxhighlighterWidget/test.html"))
        self.ui.webVOutput.setHtml(HEADER+BODY+FOOTER, QUrl("file://"))
        self.ui.webVOutput.show()

    # def testExport(self,str,path):
    #     with open(path,"w") as f:
    #         print(str, file=f)

    def _setBrushesCmbBox(self, shPath, addBrushPath = None):
        paths = [shPath]
        if addBrushPath is not None:
            paths.append(addBrushPath)
        print(paths)
        self.brushes = {}
        for path in paths:
            files = os.listdir(path)
            for file in files:
                matched = BRUSHPTN.match(file)
                if matched is not None:
                    lang = matched.group(1).lower()
                    self.brushes[lang]=os.path.join(path, matched.group(0))
                    self.ui.cmbBox.addItem(lang)

    def chooseBrush(self):
        cmbBox = self.ui.cmbBox
        self.lang = cmbBox.currentText()
        self.brush = self.brushes[self.lang]
        self.highlight()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    main_window = MainWindow()

    main_window.show()
    sys.exit(app.exec_())
