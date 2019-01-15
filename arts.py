from gtts import gTTS
from PyQt5 import QtCore, QtWidgets, QtMultimedia, QtGui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
import os
import subprocess
import io


class Ui_arts(object):

    def setupUi(self, arts):
        self.iss =''
        self.z=[]

        self.inputForlocal=''
        self.direct=''
        self.player = QtMultimedia.QMediaPlayer()
        self.player2 = QtMultimedia.QMediaPlayer()
        self.sound = QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile('test.mp3'))
        self.sound2=QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile('os4.wav'))
        arts.setObjectName("arts")
        arts.resize(768, 522)
        self.Select = QtWidgets.QPushButton(arts)
        self.Select.setGeometry(QtCore.QRect(640, 40, 81, 51))
        self.Select.setObjectName("Select")
        self.Read = QtWidgets.QPushButton(arts)
        self.Read.setGeometry(QtCore.QRect(640, 100, 81, 51))
        self.Read.setObjectName("Read")
        self.Play = QtWidgets.QPushButton(arts)
        self.Play.setGeometry(QtCore.QRect(640, 160, 81, 51))
        self.Play.setObjectName("Play")
        self.ReadLocal = QtWidgets.QPushButton(arts)
        self.ReadLocal.setGeometry(QtCore.QRect(640, 220, 81, 51))
        self.ReadLocal.setObjectName("ReadLocal")


        self.playLocal = QtWidgets.QPushButton(arts)
        self.playLocal.setGeometry(QtCore.QRect(640, 280, 81, 51))
        self.playLocal.setObjectName("playLocal")
        self.textbox = QtWidgets.QTextEdit(arts)
        self.textbox.setGeometry(QtCore.QRect(80, 40, 471, 391))
        self.textbox.setObjectName("textbox")
#BUTTON FOR OPEN FILE
        self.Select.clicked.connect(self.openFileNameDialog)
#BUTTON FOR SENDING THE TEXT TO GOOGLE AND GET AUDIO
        self.Read.clicked.connect(self.readtext)
#BUTTON FOR PLAYING AUDIO
        self.Play.clicked.connect(self.playmusic)
# BUTTON FOR Reading Local
        self.ReadLocal.clicked.connect(self.encoder)

# BUTTON FOR  Generate local audio
        self.playLocal.clicked.connect(self.playmusicFromLocal)

        self.retranslateUi(arts)
        QtCore.QMetaObject.connectSlotsByName(arts)

    def retranslateUi(self, arts):
        _translate = QtCore.QCoreApplication.translate
        arts.setWindowTitle(_translate("arts", "arabic text reader"))
        self.Select.setText(_translate("arts", "Select file"))
        self.Read.setText(_translate("arts", "Read"))
        self.Play.setText(_translate("arts", "Play"))
        self.ReadLocal.setText(_translate("arts", "ReadLocal"))
        self.playLocal.setText(_translate("arts", "playLocal"))


#OPEN FILE AND DISPLAY CONTENT FUNC
    def openFileNameDialog(self):
        currentFile = 'arts.py'
        realPath = os.path.realpath(currentFile)  # /home/user/test/my_script.py
        dirPath = os.path.dirname(realPath)

        test = os.listdir(dirPath)

        for item in test:
            if item.endswith(".wav"):
                os.remove(os.path.join(dirPath, item))
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.direct, _ = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        with open(self.direct,encoding='utf-8') as lines:
            for line in lines :
                self.iss=self.iss+'\n'+line
                self.textbox.setText(self.iss)

#ASK GOOGLE FOR AUDIO FUNC
    def readtext(self):
        tts = gTTS(text=self.iss, lang='ar')
        tts.save("test.mp3")

#PLAY THE MUSIC FUNC
    def playmusic(self):
        self.player.setMedia(self.sound)
        self.player.setVolume(100)
        self.player.play()

    def encoder(self):
        
        i = 0
        with open(self.direct,encoding='utf-8') as lines:
            for line in lines :
                self.inputForlocal=self.inputForlocal+line
        input='c'+'c'+self.inputForlocal+'c'+'c'
        

        for char in input:
            if (char == 'ح'):
                a0 = i + 1
                b0 = i + 2
                c0 = i + 3
                d0 = i + 4
                if (a0 < len(input)):
                    if (input[a0] == '\0'):
                        self.z.append('file ' + "'" + "library\\signs.wav" + "'")
                    elif ((input[a0] == 'َ') and (input[b0] == 'د') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + 'library\\7a\\20-ح.wav' + "'")
                    elif ((input[a0] == 'َ') and (input[b0] == 'ج') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\17-ح.wav" + "'")
                    elif ((input[a0] == 'َ') and (input[b0] == 'ح') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\18-ح.wav" + "'")
                    elif ((input[a0] == 'َ') and (input[b0] == 'خ') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\19-ح.wav" + "'")
                    elif ((input[a0] == 'َ') and (input[b0] == 'ه') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\36-ح.wav" + "'")
                    elif ((input[a0] == 'َ') and (input[b0] == 'ع') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\28-ح.wav" + "'")
                    elif ((input[a0] == 'َ') and (input[b0] == 'غ') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\29-ح.wav" + "'")
                    elif ((input[a0] == 'َ') and (input[b0] == 'ف') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\30-ح.wav" + "'")
                    elif ((input[a0] == 'َ') and (input[b0] == 'ق') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\31-ح.wav" + "'")
                    elif ((input[a0] == 'َ') and (input[b0] == 'ث') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\16-ح.wav" + "'")
                    elif ((input[a0] == 'َ') and (input[b0] == 'ص') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\25-ح.wav" + "'")
                    elif ((input[a0] == 'َ') and (input[b0] == 'ض') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\26-ح.wav" + "'")
                    elif ((input[a0] == 'َ') and (input[b0] == 'ذ') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\21-ح.wav" + "'")
                    elif ((input[a0] == 'َ') and (input[b0] == 'ط') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\27-ح.wav" + "'")
                    elif ((input[a0] == 'َ') and (input[b0] == 'ك') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\32-ح.wav" + "'")
                    elif ((input[a0] == 'َ') and (input[b0] == 'م') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\34-ح.wav" + "'")
                    elif ((input[a0] == 'َ') and (input[b0] == 'ن') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\35-ح.wav" + "'")
                    elif ((input[a0] == 'َ') and (input[b0] == 'ت') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\15-ح.wav" + "'")
                    elif ((input[a0] == 'َ') and (input[b0] == 'أ') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\13-ح.wav" + "'")
                    elif ((input[a0] == 'َ') and (input[b0] == 'ل') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\33-ح.wav" + "'")
                    elif ((input[a0] == 'َ') and (input[b0] == 'ب') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\14-ح.wav" + "'")
                    elif ((input[a0] == 'َ') and (input[b0] == 'ي') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\37-ح.wav" + "'")
                    elif ((input[a0] == 'َ') and (input[b0] == 'س') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\23-ح.wav" + "'")
                    elif ((input[a0] == 'َ') and (input[b0] == 'ش') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\24-ح.wav" + "'")
                    elif ((input[a0] == 'َ') and (input[b0] == 'ظ') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\26-ح.wav" + "'")
                    elif ((input[a0] == 'َ') and (input[b0] == 'ز') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\z1.wav" + "'")
                    elif ((input[a0] == 'َ') and (input[b0] == 'و') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\signs.wav" + "'")
                    elif ((input[a0] == 'َ') and (input[b0] == 'ة') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\15-ح.wav" + "'")
                    elif ((input[a0] == 'َ') and (input[b0] == 'ر') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\22-ح.wav" + "'")
                    elif ((input[a0] == 'َ') and (input[b0] == 'ؤ') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\13-ح.wav" + "'")
                    elif ((input[a0] == 'َ') and (input[b0] == 'ء') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\13-ح.wav" + "'")
                    elif ((input[a0] == 'َ') and (input[b0] == 'ئ') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\13-ح.wav" + "'")


                    elif ((input[a0] == 'ُ') and (input[b0] == 'د') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\45-ح.wav" + "'")
                    elif ((input[a0] == 'ُ') and (input[b0] == 'ج') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\42-ح.wav" + "'")
                    elif ((input[a0] == 'ُ') and (input[b0] == 'ح') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\43-ح.wav" + "'")
                    elif ((input[a0] == 'ُ') and (input[b0] == 'خ') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\44-ح.wav" + "'")
                    elif ((input[a0] == 'ُ') and (input[b0] == 'ه') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\61-ح.wav" + "'")
                    elif ((input[a0] == 'ُ') and (input[b0] == 'ع') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\53-ح.wav" + "'")
                    elif ((input[a0] == 'ُ') and (input[b0] == 'غ') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\54-ح.wav" + "'")
                    elif ((input[a0] == 'ُ') and (input[b0] == 'ف') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\55-ح.wav" + "'")
                    elif ((input[a0] == 'ُ') and (input[b0] == 'ق') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\56-ح.wav" + "'")
                    elif ((input[a0] == 'ُ') and (input[b0] == 'ث') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\41-ح.wav" + "'")
                    elif ((input[a0] == 'ُ') and (input[b0] == 'ص') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\50-ح.wav" + "'")
                    elif ((input[a0] == 'ُ') and (input[b0] == 'ض') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\51-ح.wav" + "'")
                    elif ((input[a0] == 'ُ') and (input[b0] == 'ذ') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\46-ح.wav" + "'")
                    elif ((input[a0] == 'ُ') and (input[b0] == 'ط') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\52-ح.wav" + "'")
                    elif ((input[a0] == 'ُ') and (input[b0] == 'ك') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\57-ح.wav" + "'")
                    elif ((input[a0] == 'ُ') and (input[b0] == 'م') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\59-ح.wav" + "'")
                    elif ((input[a0] == 'ُ') and (input[b0] == 'ن') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\60-ح.wav" + "'")
                    elif ((input[a0] == 'ُ') and (input[b0] == 'ت') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\40-ح.wav" + "'")
                    elif ((input[a0] == 'ُ') and (input[b0] == 'أ') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\38-ح.wav" + "'")
                    elif ((input[a0] == 'ُ') and (input[b0] == 'ل') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\58-ح.wav" + "'")
                    elif ((input[a0] == 'ُ') and (input[b0] == 'ب') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\39-ح.wav" + "'")
                    elif ((input[a0] == 'ُ') and (input[b0] == 'ي') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\62-ح.wav" + "'")
                    elif ((input[a0] == 'ُ') and (input[b0] == 'س') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\48-ح.wav" + "'")
                    elif ((input[a0] == 'ُ') and (input[b0] == 'ش') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\49-ح.wav" + "'")
                    elif ((input[a0] == 'ُ') and (input[b0] == 'ظ') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\51-ح.wav" + "'")
                    elif ((input[a0] == 'ُ') and (input[b0] == 'ز') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\z2.wav" + "'")
                    elif ((input[a0] == 'ُ') and (input[b0] == 'و') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\signs.wav" + "'")
                    elif ((input[a0] == 'ُ') and (input[b0] == 'ة') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\40-ح.wav" + "'")
                    elif ((input[a0] == 'ُ') and (input[b0] == 'ر') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\47-ح.wav" + "'")
                    elif ((input[a0] == 'ُ') and (input[b0] == 'ؤ') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\38-ح.wav" + "'")
                    elif ((input[a0] == 'ُ') and (input[b0] == 'ء') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\38-ح.wav" + "'")
                    elif ((input[a0] == 'ُ') and (input[b0] == 'ئ') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\38-ح.wav" + "'")



                    elif ((input[a0] == 'ِ') and (input[b0] == 'د') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\70-ح.wav" + "'")
                    elif ((input[a0] == 'ِ') and (input[b0] == 'ج') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\67-ح.wav" + "'")
                    elif ((input[a0] == 'ِ') and (input[b0] == 'ح') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\68-ح.wav" + "'")
                    elif ((input[a0] == 'ِ') and (input[b0] == 'خ') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\69-ح.wav" + "'")
                    elif ((input[a0] == 'ِ') and (input[b0] == 'ه') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\86-ح.wav" + "'")
                    elif ((input[a0] == 'ِ') and (input[b0] == 'ع') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\78-ح.wav" + "'")
                    elif ((input[a0] == 'ِ') and (input[b0] == 'غ') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\79-ح.wav" + "'")
                    elif ((input[a0] == 'ِ') and (input[b0] == 'ف') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\80-ح.wav" + "'")
                    elif ((input[a0] == 'ِ') and (input[b0] == 'ق') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\81-ح.wav" + "'")
                    elif ((input[a0] == 'ِ') and (input[b0] == 'ث') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\66-ح.wav" + "'")
                    elif ((input[a0] == 'ِ') and (input[b0] == 'ص') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\75-ح.wav" + "'")
                    elif ((input[a0] == 'ِ') and (input[b0] == 'ض') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\76-ح.wav" + "'")
                    elif ((input[a0] == 'ِ') and (input[b0] == 'ذ') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\71-ح.wav" + "'")
                    elif ((input[a0] == 'ِ') and (input[b0] == 'ط') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\77-ح.wav" + "'")
                    elif ((input[a0] == 'ِ') and (input[b0] == 'ك') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\82-ح.wav" + "'")
                    elif ((input[a0] == 'ِ') and (input[b0] == 'م') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\84-ح.wav" + "'")
                    elif ((input[a0] == 'ِ') and (input[b0] == 'ن') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\85-ح.wav" + "'")
                    elif ((input[a0] == 'ِ') and (input[b0] == 'ت') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\65-ح.wav" + "'")
                    elif ((input[a0] == 'ِ') and (input[b0] == 'أ') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\63-ح.wav" + "'")
                    elif ((input[a0] == 'ِ') and (input[b0] == 'ل') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\83-ح.wav" + "'")
                    elif ((input[a0] == 'ِ') and (input[b0] == 'ب') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\64-ح.wav" + "'")
                    elif ((input[a0] == 'ِ') and (input[b0] == 'ي') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\87-ح.wav" + "'")
                    elif ((input[a0] == 'ِ') and (input[b0] == 'س') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\73-ح.wav" + "'")
                    elif ((input[a0] == 'ِ') and (input[b0] == 'ش') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\74-ح.wav" + "'")
                    elif ((input[a0] == 'ِ') and (input[b0] == 'ظ') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\76-ح.wav" + "'")
                    elif ((input[a0] == 'ِ') and (input[b0] == 'ز') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\z3.wav" + "'")
                    elif ((input[a0] == 'ِ') and (input[b0] == 'و') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\signs.wav" + "'")
                    elif ((input[a0] == 'ِ') and (input[b0] == 'ة') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\65-ح.wav" + "'")
                    elif ((input[a0] == 'ِ') and (input[b0] == 'ر') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\72-ح.wav" + "'")
                    elif ((input[a0] == 'ِ') and (input[b0] == 'ؤ') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\63-ح.wav" + "'")
                    elif ((input[a0] == 'ِ') and (input[b0] == 'ء') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\63-ح.wav" + "'")
                    elif ((input[a0] == 'ِ') and (input[b0] == 'ئ') and (input[c0] == 'ْ')):
                        self.z.append('file ' + "'" + "library\\7a\\63-ح.wav" + "'")





                    elif ((input[a0] == 'َ') and ((input[b0] == 'ا') or (input[b0] == 'ى'))):
                        self.z.append('file ' + "'" + "library\\7a\\04-ح.wav" + "'")
                    elif (input[a0] == 'ُ' and input[b0] == 'و'):
                        self.z.append('file ' + "'" + "library\\7a\\05-ح.wav" + "'")
                    elif (input[a0] == 'ِ' and input[b0] == 'ي'):
                        self.z.append('file ' + "'" + "library\\7a\\06-ح.wav" + "'")
                    elif (input[a0] == 'ً'):
                        self.z.append('file ' + "'" + "library\\7a\\07-ح.wav" + "'")
                    elif (input[a0] == 'ٌ'):
                        self.z.append('file ' + "'" + "library\\7a\\08-ح.wav" + "'")
                    elif (input[a0] == 'ٍ'):
                        self.z.append('file ' + "'" + "library\\7a\\09-ح.wav" + "'")
                    elif (input[a0] == 'َ'):
                        self.z.append('file ' + "'" + "library\\7a\\01-ح.wav" + "'")
                    elif (input[a0] == 'ُ'):
                        self.z.append('file ' + "'" + "library\\7a\\02-ح.wav" + "'")
                    elif (input[a0] == 'ِ'):
                        self.z.append('file ' + "'" + "library\\7a\\03-ح.wav" + "'")
                    elif (input[a0] == 'ْ'):
                        self.z.append('file ' + "'" + "library\\7a\\signs.wav" + "'")
                    else:
                        self.z.append('file ' + "'" + "library\\7a\\signs.wav" + "'")







                else:
                    self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                a0 = 0
                b0 = 0
                d0 = 0
                c0 = 0




            elif (char == 'ج'):

                a1 = i + 1

                b1 = i + 2

                c1 = i + 3

                d1 = i + 4

                if (a1 < (len(input))):

                    if (input[a1] == '\0'):

                        self.z.append('file ' + "'" + "library\\signs.wav" + "'")


                    elif ((input[a1] == 'َ') and (input[b1] == 'د') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\j\\20-ج.wav' + "'")


                    elif ((input[a1] == 'َ') and (input[b1] == 'ج') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\17-ج.wav" + "'")


                    elif ((input[a1] == 'َ') and (input[b1] == 'ح') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\18-ج.wav" + "'")


                    elif ((input[a1] == 'َ') and (input[b1] == 'خ') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\19-ج.wav" + "'")


                    elif ((input[a1] == 'َ') and (input[b1] == 'ه') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\36-ج.wav" + "'")


                    elif ((input[a1] == 'َ') and (input[b1] == 'ع') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\28-ج.wav" + "'")


                    elif ((input[a1] == 'َ') and (input[b1] == 'غ') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\29-ج.wav" + "'")


                    elif ((input[a1] == 'َ') and (input[b1] == 'ف') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\30-ج.wav" + "'")


                    elif ((input[a1] == 'َ') and (input[b1] == 'ق') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\31-ج.wav" + "'")


                    elif ((input[a1] == 'َ') and (input[b1] == 'ث') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\16-ج.wav" + "'")


                    elif ((input[a1] == 'َ') and (input[b1] == 'ص') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\25-ج.wav" + "'")


                    elif ((input[a1] == 'َ') and (input[b1] == 'ض') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\26-ج.wav" + "'")


                    elif ((input[a1] == 'َ') and (input[b1] == 'ذ') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\21-ج.wav" + "'")


                    elif ((input[a1] == 'َ') and (input[b1] == 'ط') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\27-ج.wav" + "'")


                    elif ((input[a1] == 'َ') and (input[b1] == 'ك') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\32-ج.wav" + "'")


                    elif ((input[a1] == 'َ') and (input[b1] == 'م') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\34-ج.wav" + "'")


                    elif ((input[a1] == 'َ') and (input[b1] == 'ن') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\35-ج.wav" + "'")


                    elif ((input[a1] == 'َ') and (input[b1] == 'ت') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\15-ج.wav" + "'")


                    elif ((input[a1] == 'َ') and (input[b1] == 'أ') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\13-ج.wav" + "'")


                    elif ((input[a1] == 'َ') and (input[b1] == 'ل') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\33-ج.wav" + "'")


                    elif ((input[a1] == 'َ') and (input[b1] == 'ب') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\14-ج.wav" + "'")


                    elif ((input[a1] == 'َ') and (input[b1] == 'ي') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\37-ج.wav" + "'")


                    elif ((input[a1] == 'َ') and (input[b1] == 'س') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\23-ج.wav" + "'")


                    elif ((input[a1] == 'َ') and (input[b1] == 'ش') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\24-ج.wav" + "'")


                    elif ((input[a1] == 'َ') and (input[b1] == 'ظ') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\26-ج.wav" + "'")


                    elif ((input[a1] == 'َ') and (input[b1] == 'ز') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\z1.wav" + "'")


                    elif ((input[a1] == 'َ') and (input[b1] == 'و') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\signs.wav" + "'")


                    elif ((input[a1] == 'َ') and (input[b1] == 'ة') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\15-ج.wav" + "'")


                    elif ((input[a1] == 'َ') and (input[b1] == 'ر') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\22-ج.wav" + "'")


                    elif ((input[a1] == 'َ') and (input[b1] == 'ؤ') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\13-ج.wav" + "'")


                    elif ((input[a1] == 'َ') and (input[b1] == 'ء') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\13-ج.wav" + "'")


                    elif ((input[a1] == 'َ') and (input[b1] == 'ئ') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\13-ج.wav" + "'")




                    elif ((input[a1] == 'ُ') and (input[b1] == 'د') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\45-ج.wav" + "'")


                    elif ((input[a1] == 'ُ') and (input[b1] == 'ج') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\42-ج.wav" + "'")


                    elif ((input[a1] == 'ُ') and (input[b1] == 'ح') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\43-ج.wav" + "'")


                    elif ((input[a1] == 'ُ') and (input[b1] == 'خ') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\44-ج.wav" + "'")


                    elif ((input[a1] == 'ُ') and (input[b1] == 'ه') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\61-ج.wav" + "'")


                    elif ((input[a1] == 'ُ') and (input[b1] == 'ع') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\53-ج.wav" + "'")


                    elif ((input[a1] == 'ُ') and (input[b1] == 'غ') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\54-ج.wav" + "'")


                    elif ((input[a1] == 'ُ') and (input[b1] == 'ف') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\55-ج.wav" + "'")


                    elif ((input[a1] == 'ُ') and (input[b1] == 'ق') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\56-ج.wav" + "'")


                    elif ((input[a1] == 'ُ') and (input[b1] == 'ث') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\41-ج.wav" + "'")


                    elif ((input[a1] == 'ُ') and (input[b1] == 'ص') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\50-ج.wav" + "'")


                    elif ((input[a1] == 'ُ') and (input[b1] == 'ض') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\51-ج.wav" + "'")


                    elif ((input[a1] == 'ُ') and (input[b1] == 'ذ') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\46-ج.wav" + "'")


                    elif ((input[a1] == 'ُ') and (input[b1] == 'ط') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\52-ج.wav" + "'")


                    elif ((input[a1] == 'ُ') and (input[b1] == 'ك') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\57-ج.wav" + "'")


                    elif ((input[a1] == 'ُ') and (input[b1] == 'م') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\59-ج.wav" + "'")


                    elif ((input[a1] == 'ُ') and (input[b1] == 'ن') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\60-ج.wav" + "'")


                    elif ((input[a1] == 'ُ') and (input[b1] == 'ت') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\40-ج.wav" + "'")


                    elif ((input[a1] == 'ُ') and (input[b1] == 'أ') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\38-ج.wav" + "'")


                    elif ((input[a1] == 'ُ') and (input[b1] == 'ل') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\58-ج.wav" + "'")


                    elif ((input[a1] == 'ُ') and (input[b1] == 'ب') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\39-ج.wav" + "'")


                    elif ((input[a1] == 'ُ') and (input[b1] == 'ي') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\62-ج.wav" + "'")


                    elif ((input[a1] == 'ُ') and (input[b1] == 'س') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\48-ج.wav" + "'")


                    elif ((input[a1] == 'ُ') and (input[b1] == 'ش') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\49-ج.wav" + "'")


                    elif ((input[a1] == 'ُ') and (input[b1] == 'ظ') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\51-ج.wav" + "'")


                    elif ((input[a1] == 'ُ') and (input[b1] == 'ز') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\z2.wav" + "'")


                    elif ((input[a1] == 'ُ') and (input[b1] == 'و') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\signs.wav" + "'")


                    elif ((input[a1] == 'ُ') and (input[b1] == 'ة') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\40-ج.wav" + "'")


                    elif ((input[a1] == 'ُ') and (input[b1] == 'ر') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\47-ج.wav" + "'")


                    elif ((input[a1] == 'ُ') and (input[b1] == 'ؤ') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\38-ج.wav" + "'")


                    elif ((input[a1] == 'ُ') and (input[b1] == 'ء') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\38-ج.wav" + "'")


                    elif ((input[a1] == 'ُ') and (input[b1] == 'ئ') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\38-ج.wav" + "'")





                    elif ((input[a1] == 'ِ') and (input[b1] == 'د') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\70-ج.wav" + "'")


                    elif ((input[a1] == 'ِ') and (input[b1] == 'ج') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\67-ج.wav" + "'")


                    elif ((input[a1] == 'ِ') and (input[b1] == 'ح') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\68-ج.wav" + "'")


                    elif ((input[a1] == 'ِ') and (input[b1] == 'خ') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\69-ج.wav" + "'")


                    elif ((input[a1] == 'ِ') and (input[b1] == 'ه') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\86-ج.wav" + "'")


                    elif ((input[a1] == 'ِ') and (input[b1] == 'ع') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\78-ج.wav" + "'")


                    elif ((input[a1] == 'ِ') and (input[b1] == 'غ') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\79-ج.wav" + "'")


                    elif ((input[a1] == 'ِ') and (input[b1] == 'ف') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\80-ج.wav" + "'")


                    elif ((input[a1] == 'ِ') and (input[b1] == 'ق') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\81-ج.wav" + "'")


                    elif ((input[a1] == 'ِ') and (input[b1] == 'ث') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\66-ج.wav" + "'")


                    elif ((input[a1] == 'ِ') and (input[b1] == 'ص') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\75-ج.wav" + "'")


                    elif ((input[a1] == 'ِ') and (input[b1] == 'ض') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\76-ج.wav" + "'")


                    elif ((input[a1] == 'ِ') and (input[b1] == 'ذ') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\71-ج.wav" + "'")


                    elif ((input[a1] == 'ِ') and (input[b1] == 'ط') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\77-ج.wav" + "'")


                    elif ((input[a1] == 'ِ') and (input[b1] == 'ك') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\82-ج.wav" + "'")


                    elif ((input[a1] == 'ِ') and (input[b1] == 'م') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\84-ج.wav" + "'")


                    elif ((input[a1] == 'ِ') and (input[b1] == 'ن') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\85-ج.wav" + "'")


                    elif ((input[a1] == 'ِ') and (input[b1] == 'ت') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\65-ج.wav" + "'")


                    elif ((input[a1] == 'ِ') and (input[b1] == 'أ') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\63-ج.wav" + "'")


                    elif ((input[a1] == 'ِ') and (input[b1] == 'ل') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\83-ج.wav" + "'")


                    elif ((input[a1] == 'ِ') and (input[b1] == 'ب') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\64-ج.wav" + "'")


                    elif ((input[a1] == 'ِ') and (input[b1] == 'ي') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\87-ج.wav" + "'")


                    elif ((input[a1] == 'ِ') and (input[b1] == 'س') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\73-ج.wav" + "'")


                    elif ((input[a1] == 'ِ') and (input[b1] == 'ش') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\74-ج.wav" + "'")


                    elif ((input[a1] == 'ِ') and (input[b1] == 'ظ') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\76-ج.wav" + "'")


                    elif ((input[a1] == 'ِ') and (input[b1] == 'ز') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\z3.wav" + "'")


                    elif ((input[a1] == 'ِ') and (input[b1] == 'و') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\signs.wav" + "'")


                    elif ((input[a1] == 'ِ') and (input[b1] == 'ة') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\65-ج.wav" + "'")


                    elif ((input[a1] == 'ِ') and (input[b1] == 'ر') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\72-ج.wav" + "'")


                    elif ((input[a1] == 'ِ') and (input[b1] == 'ؤ') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\63-ج.wav" + "'")


                    elif ((input[a1] == 'ِ') and (input[b1] == 'ء') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\63-ج.wav" + "'")


                    elif ((input[a1] == 'ِ') and (input[b1] == 'ئ') and (input[c1] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\j\\63-ج.wav" + "'")







                    elif ((input[a1] == 'َ') and ((input[b1] == 'ا') or (input[b1] == 'ى'))):

                        self.z.append('file ' + "'" + "library\\j\\04-ج.wav" + "'")


                    elif (input[a1] == 'ُ' and input[b1] == 'و'):

                        self.z.append('file ' + "'" + "library\\j\\05-ج.wav" + "'")


                    elif (input[a1] == 'ِ' and input[b1] == 'ي'):

                        self.z.append('file ' + "'" + "library\\j\\06-ج.wav" + "'")


                    elif (input[a1] == 'ً'):

                        self.z.append('file ' + "'" + "library\\j\\07-ج.wav" + "'")


                    elif (input[a1] == 'ٌ'):

                        self.z.append('file ' + "'" + "library\\j\\08-ج.wav" + "'")


                    elif (input[a1] == 'ٍ'):

                        self.z.append('file ' + "'" + "library\\j\\09-ج.wav" + "'")


                    elif (input[a1] == 'َ'):

                        self.z.append('file ' + "'" + "library\\j\\01-ج.wav" + "'")


                    elif (input[a1] == 'ُ'):

                        self.z.append('file ' + "'" + "library\\j\\02-ج.wav" + "'")


                    elif (input[a1] == 'ِ'):

                        self.z.append('file ' + "'" + "library\\j\\03-ج.wav" + "'")


                    elif (input[a1] == 'ْ'):

                        self.z.append('file ' + "'" + "library\\j\\signs.wav" + "'")


                    else:

                        self.z.append('file ' + "'" + "library\\j\\signs.wav" + "'")









                else:

                    self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                a1 = 0

                b1 = 0

                d1 = 0

                c1 = 0





            elif (char == 'خ'):

                a2 = i + 1

                b2 = i + 2

                c2 = i + 3

                d2 = i + 4

                if (a2 < (len(input))):

                    if (input[a2] == '\0'):

                        self.z.append('file ' + "'" + "library\\signs.wav" + "'")


                    elif ((input[a2] == 'َ') and (input[b2] == 'د') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\5a\\20-خ.wav' + "'")


                    elif ((input[a2] == 'َ') and (input[b2] == 'ج') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\17-خ.wav" + "'")


                    elif ((input[a2] == 'َ') and (input[b2] == 'ح') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\18-خ.wav" + "'")


                    elif ((input[a2] == 'َ') and (input[b2] == 'خ') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\19-خ.wav" + "'")


                    elif ((input[a2] == 'َ') and (input[b2] == 'ه') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\36-خ.wav" + "'")


                    elif ((input[a2] == 'َ') and (input[b2] == 'ع') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\28-خ.wav" + "'")


                    elif ((input[a2] == 'َ') and (input[b2] == 'غ') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\29-خ.wav" + "'")


                    elif ((input[a2] == 'َ') and (input[b2] == 'ف') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\30-خ.wav" + "'")


                    elif ((input[a2] == 'َ') and (input[b2] == 'ق') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\31-خ.wav" + "'")


                    elif ((input[a2] == 'َ') and (input[b2] == 'ث') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\16-خ.wav" + "'")


                    elif ((input[a2] == 'َ') and (input[b2] == 'ص') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\25-خ.wav" + "'")


                    elif ((input[a2] == 'َ') and (input[b2] == 'ض') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\26-خ.wav" + "'")


                    elif ((input[a2] == 'َ') and (input[b2] == 'ذ') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\21-خ.wav" + "'")


                    elif ((input[a2] == 'َ') and (input[b2] == 'ط') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\27-خ.wav" + "'")


                    elif ((input[a2] == 'َ') and (input[b2] == 'ك') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\32-خ.wav" + "'")


                    elif ((input[a2] == 'َ') and (input[b2] == 'م') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\34-خ.wav" + "'")


                    elif ((input[a2] == 'َ') and (input[b2] == 'ن') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\35-خ.wav" + "'")


                    elif ((input[a2] == 'َ') and (input[b2] == 'ت') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\15-خ.wav" + "'")


                    elif ((input[a2] == 'َ') and (input[b2] == 'أ') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\13-خ.wav" + "'")


                    elif ((input[a2] == 'َ') and (input[b2] == 'ل') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\33-خ.wav" + "'")


                    elif ((input[a2] == 'َ') and (input[b2] == 'ب') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\14-خ.wav" + "'")


                    elif ((input[a2] == 'َ') and (input[b2] == 'ي') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\37-خ.wav" + "'")


                    elif ((input[a2] == 'َ') and (input[b2] == 'س') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\23-خ.wav" + "'")


                    elif ((input[a2] == 'َ') and (input[b2] == 'ش') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\24-خ.wav" + "'")


                    elif ((input[a2] == 'َ') and (input[b2] == 'ظ') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\26-خ.wav" + "'")


                    elif ((input[a2] == 'َ') and (input[b2] == 'ز') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\z1.wav" + "'")


                    elif ((input[a2] == 'َ') and (input[b2] == 'و') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\signs.wav" + "'")


                    elif ((input[a2] == 'َ') and (input[b2] == 'ة') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\15-خ.wav" + "'")


                    elif ((input[a2] == 'َ') and (input[b2] == 'ر') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\22-خ.wav" + "'")


                    elif ((input[a2] == 'َ') and (input[b2] == 'ؤ') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\13-خ.wav" + "'")


                    elif ((input[a2] == 'َ') and (input[b2] == 'ء') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\13-خ.wav" + "'")


                    elif ((input[a2] == 'َ') and (input[b2] == 'ئ') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\13-خ.wav" + "'")




                    elif ((input[a2] == 'ُ') and (input[b2] == 'د') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\45-خ.wav" + "'")


                    elif ((input[a2] == 'ُ') and (input[b2] == 'ج') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\42-خ.wav" + "'")


                    elif ((input[a2] == 'ُ') and (input[b2] == 'ح') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\43-خ.wav" + "'")


                    elif ((input[a2] == 'ُ') and (input[b2] == 'خ') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\44-خ.wav" + "'")


                    elif ((input[a2] == 'ُ') and (input[b2] == 'ه') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\61-خ.wav" + "'")


                    elif ((input[a2] == 'ُ') and (input[b2] == 'ع') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\53-خ.wav" + "'")


                    elif ((input[a2] == 'ُ') and (input[b2] == 'غ') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\54-خ.wav" + "'")


                    elif ((input[a2] == 'ُ') and (input[b2] == 'ف') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\55-خ.wav" + "'")


                    elif ((input[a2] == 'ُ') and (input[b2] == 'ق') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\56-خ.wav" + "'")


                    elif ((input[a2] == 'ُ') and (input[b2] == 'ث') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\41-خ.wav" + "'")


                    elif ((input[a2] == 'ُ') and (input[b2] == 'ص') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\50-خ.wav" + "'")


                    elif ((input[a2] == 'ُ') and (input[b2] == 'ض') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\51-خ.wav" + "'")


                    elif ((input[a2] == 'ُ') and (input[b2] == 'ذ') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\46-خ.wav" + "'")


                    elif ((input[a2] == 'ُ') and (input[b2] == 'ط') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\52-خ.wav" + "'")


                    elif ((input[a2] == 'ُ') and (input[b2] == 'ك') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\57-خ.wav" + "'")


                    elif ((input[a2] == 'ُ') and (input[b2] == 'م') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\59-خ.wav" + "'")


                    elif ((input[a2] == 'ُ') and (input[b2] == 'ن') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\60-خ.wav" + "'")


                    elif ((input[a2] == 'ُ') and (input[b2] == 'ت') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\40-خ.wav" + "'")


                    elif ((input[a2] == 'ُ') and (input[b2] == 'أ') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\38-خ.wav" + "'")


                    elif ((input[a2] == 'ُ') and (input[b2] == 'ل') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\58-خ.wav" + "'")


                    elif ((input[a2] == 'ُ') and (input[b2] == 'ب') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\39-خ.wav" + "'")


                    elif ((input[a2] == 'ُ') and (input[b2] == 'ي') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\62-خ.wav" + "'")


                    elif ((input[a2] == 'ُ') and (input[b2] == 'س') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\48-خ.wav" + "'")


                    elif ((input[a2] == 'ُ') and (input[b2] == 'ش') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\49-خ.wav" + "'")


                    elif ((input[a2] == 'ُ') and (input[b2] == 'ظ') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\51-خ.wav" + "'")


                    elif ((input[a2] == 'ُ') and (input[b2] == 'ز') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\z2.wav" + "'")


                    elif ((input[a2] == 'ُ') and (input[b2] == 'و') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\signs.wav" + "'")


                    elif ((input[a2] == 'ُ') and (input[b2] == 'ة') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\40-خ.wav" + "'")


                    elif ((input[a2] == 'ُ') and (input[b2] == 'ر') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\47-خ.wav" + "'")


                    elif ((input[a2] == 'ُ') and (input[b2] == 'ؤ') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\38-خ.wav" + "'")


                    elif ((input[a2] == 'ُ') and (input[b2] == 'ء') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\38-خ.wav" + "'")


                    elif ((input[a2] == 'ُ') and (input[b2] == 'ئ') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\38-خ.wav" + "'")





                    elif ((input[a2] == 'ِ') and (input[b2] == 'د') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\70-خ.wav" + "'")


                    elif ((input[a2] == 'ِ') and (input[b2] == 'ج') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\67-خ.wav" + "'")


                    elif ((input[a2] == 'ِ') and (input[b2] == 'ح') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\68-خ.wav" + "'")


                    elif ((input[a2] == 'ِ') and (input[b2] == 'خ') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\69-خ.wav" + "'")


                    elif ((input[a2] == 'ِ') and (input[b2] == 'ه') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\86-خ.wav" + "'")


                    elif ((input[a2] == 'ِ') and (input[b2] == 'ع') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\78-خ.wav" + "'")


                    elif ((input[a2] == 'ِ') and (input[b2] == 'غ') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\79-خ.wav" + "'")


                    elif ((input[a2] == 'ِ') and (input[b2] == 'ف') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\80-خ.wav" + "'")


                    elif ((input[a2] == 'ِ') and (input[b2] == 'ق') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\81-خ.wav" + "'")


                    elif ((input[a2] == 'ِ') and (input[b2] == 'ث') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\66-خ.wav" + "'")


                    elif ((input[a2] == 'ِ') and (input[b2] == 'ص') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\75-خ.wav" + "'")


                    elif ((input[a2] == 'ِ') and (input[b2] == 'ض') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\76-خ.wav" + "'")


                    elif ((input[a2] == 'ِ') and (input[b2] == 'ذ') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\71-خ.wav" + "'")


                    elif ((input[a2] == 'ِ') and (input[b2] == 'ط') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\77-خ.wav" + "'")


                    elif ((input[a2] == 'ِ') and (input[b2] == 'ك') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\82-خ.wav" + "'")


                    elif ((input[a2] == 'ِ') and (input[b2] == 'م') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\84-خ.wav" + "'")


                    elif ((input[a2] == 'ِ') and (input[b2] == 'ن') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\85-خ.wav" + "'")


                    elif ((input[a2] == 'ِ') and (input[b2] == 'ت') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\65-خ.wav" + "'")


                    elif ((input[a2] == 'ِ') and (input[b2] == 'أ') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\63-خ.wav" + "'")


                    elif ((input[a2] == 'ِ') and (input[b2] == 'ل') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\83-خ.wav" + "'")


                    elif ((input[a2] == 'ِ') and (input[b2] == 'ب') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\64-خ.wav" + "'")


                    elif ((input[a2] == 'ِ') and (input[b2] == 'ي') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\87-خ.wav" + "'")


                    elif ((input[a2] == 'ِ') and (input[b2] == 'س') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\73-خ.wav" + "'")


                    elif ((input[a2] == 'ِ') and (input[b2] == 'ش') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\74-خ.wav" + "'")


                    elif ((input[a2] == 'ِ') and (input[b2] == 'ظ') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\76-خ.wav" + "'")


                    elif ((input[a2] == 'ِ') and (input[b2] == 'ز') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\z3.wav" + "'")


                    elif ((input[a2] == 'ِ') and (input[b2] == 'و') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\signs.wav" + "'")


                    elif ((input[a2] == 'ِ') and (input[b2] == 'ة') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\65-خ.wav" + "'")


                    elif ((input[a2] == 'ِ') and (input[b2] == 'ر') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\72-خ.wav" + "'")


                    elif ((input[a2] == 'ِ') and (input[b2] == 'ؤ') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\63-خ.wav" + "'")


                    elif ((input[a2] == 'ِ') and (input[b2] == 'ء') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\63-خ.wav" + "'")


                    elif ((input[a2] == 'ِ') and (input[b2] == 'ئ') and (input[c2] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\5a\\63-خ.wav" + "'")







                    elif ((input[a2] == 'َ') and ((input[b2] == 'ا') or (input[b2] == 'ى'))):

                        self.z.append('file ' + "'" + "library\\5a\\04-خ.wav" + "'")


                    elif (input[a2] == 'ُ' and input[b2] == 'و'):

                        self.z.append('file ' + "'" + "library\\5a\\05-خ.wav" + "'")


                    elif (input[a2] == 'ِ' and input[b2] == 'ي'):

                        self.z.append('file ' + "'" + "library\\5a\\06-خ.wav" + "'")


                    elif (input[a2] == 'ً'):

                        self.z.append('file ' + "'" + "library\\5a\\07-خ.wav" + "'")


                    elif (input[a2] == 'ٌ'):

                        self.z.append('file ' + "'" + "library\\5a\\08-خ.wav" + "'")


                    elif (input[a2] == 'ٍ'):

                        self.z.append('file ' + "'" + "library\\5a\\09-خ.wav" + "'")


                    elif (input[a2] == 'َ'):

                        self.z.append('file ' + "'" + "library\\5a\\01-خ.wav" + "'")


                    elif (input[a2] == 'ُ'):

                        self.z.append('file ' + "'" + "library\\5a\\02-خ.wav" + "'")


                    elif (input[a2] == 'ِ'):

                        self.z.append('file ' + "'" + "library\\5a\\03-خ.wav" + "'")


                    elif (input[a2] == 'ْ'):

                        self.z.append('file ' + "'" + "library\\5a\\signs.wav" + "'")


                    else:

                        self.z.append('file ' + "'" + "library\\5a\\signs.wav" + "'")









                else:

                    self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                a2 = 0

                b2 = 0

                d2 = 0

                c2 = 0




            elif (char == 'ه'):

                a3 = i + 1

                b3 = i + 2

                c3 = i + 3

                d3 = i + 4

                if (a3 < (len(input))):

                    if (input[a3] == '\0'):

                        self.z.append('file ' + "'" + "library\\signs.wav" + "'")


                    elif ((input[a3] == 'َ') and (input[b3] == 'د') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\h\\20-ه.wav' + "'")


                    elif ((input[a3] == 'َ') and (input[b3] == 'ج') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\17-ه.wav" + "'")


                    elif ((input[a3] == 'َ') and (input[b3] == 'ح') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\18-ه.wav" + "'")


                    elif ((input[a3] == 'َ') and (input[b3] == 'خ') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\19-ه.wav" + "'")


                    elif ((input[a3] == 'َ') and (input[b3] == 'ه') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\36-ه.wav" + "'")


                    elif ((input[a3] == 'َ') and (input[b3] == 'ع') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\28-ه.wav" + "'")


                    elif ((input[a3] == 'َ') and (input[b3] == 'غ') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\29-ه.wav" + "'")


                    elif ((input[a3] == 'َ') and (input[b3] == 'ف') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\30-ه.wav" + "'")


                    elif ((input[a3] == 'َ') and (input[b3] == 'ق') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\31-ه.wav" + "'")


                    elif ((input[a3] == 'َ') and (input[b3] == 'ث') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\16-ه.wav" + "'")


                    elif ((input[a3] == 'َ') and (input[b3] == 'ص') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\25-ه.wav" + "'")


                    elif ((input[a3] == 'َ') and (input[b3] == 'ض') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\26-ه.wav" + "'")


                    elif ((input[a3] == 'َ') and (input[b3] == 'ذ') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\21-ه.wav" + "'")


                    elif ((input[a3] == 'َ') and (input[b3] == 'ط') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\27-ه.wav" + "'")


                    elif ((input[a3] == 'َ') and (input[b3] == 'ك') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\32-ه.wav" + "'")


                    elif ((input[a3] == 'َ') and (input[b3] == 'م') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\34-ه.wav" + "'")


                    elif ((input[a3] == 'َ') and (input[b3] == 'ن') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\35-ه.wav" + "'")


                    elif ((input[a3] == 'َ') and (input[b3] == 'ت') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\15-ه.wav" + "'")


                    elif ((input[a3] == 'َ') and (input[b3] == 'أ') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\13-ه.wav" + "'")


                    elif ((input[a3] == 'َ') and (input[b3] == 'ل') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\33-ه.wav" + "'")


                    elif ((input[a3] == 'َ') and (input[b3] == 'ب') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\14-ه.wav" + "'")


                    elif ((input[a3] == 'َ') and (input[b3] == 'ي') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\37-ه.wav" + "'")


                    elif ((input[a3] == 'َ') and (input[b3] == 'س') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\23-ه.wav" + "'")


                    elif ((input[a3] == 'َ') and (input[b3] == 'ش') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\24-ه.wav" + "'")


                    elif ((input[a3] == 'َ') and (input[b3] == 'ظ') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\26-ه.wav" + "'")


                    elif ((input[a3] == 'َ') and (input[b3] == 'ز') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\z1.wav" + "'")


                    elif ((input[a3] == 'َ') and (input[b3] == 'و') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\signs.wav" + "'")


                    elif ((input[a3] == 'َ') and (input[b3] == 'ة') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\15-ه.wav" + "'")


                    elif ((input[a3] == 'َ') and (input[b3] == 'ر') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\22-ه.wav" + "'")


                    elif ((input[a3] == 'َ') and (input[b3] == 'ؤ') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\13-ه.wav" + "'")


                    elif ((input[a3] == 'َ') and (input[b3] == 'ء') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\13-ه.wav" + "'")


                    elif ((input[a3] == 'َ') and (input[b3] == 'ئ') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\13-ه.wav" + "'")




                    elif ((input[a3] == 'ُ') and (input[b3] == 'د') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\45-ه.wav" + "'")


                    elif ((input[a3] == 'ُ') and (input[b3] == 'ج') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\42-ه.wav" + "'")


                    elif ((input[a3] == 'ُ') and (input[b3] == 'ح') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\43-ه.wav" + "'")


                    elif ((input[a3] == 'ُ') and (input[b3] == 'خ') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\44-ه.wav" + "'")


                    elif ((input[a3] == 'ُ') and (input[b3] == 'ه') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\61-ه.wav" + "'")


                    elif ((input[a3] == 'ُ') and (input[b3] == 'ع') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\53-ه.wav" + "'")


                    elif ((input[a3] == 'ُ') and (input[b3] == 'غ') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\54-ه.wav" + "'")


                    elif ((input[a3] == 'ُ') and (input[b3] == 'ف') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\55-ه.wav" + "'")


                    elif ((input[a3] == 'ُ') and (input[b3] == 'ق') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\56-ه.wav" + "'")


                    elif ((input[a3] == 'ُ') and (input[b3] == 'ث') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\41-ه.wav" + "'")


                    elif ((input[a3] == 'ُ') and (input[b3] == 'ص') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\50-ه.wav" + "'")


                    elif ((input[a3] == 'ُ') and (input[b3] == 'ض') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\51-ه.wav" + "'")


                    elif ((input[a3] == 'ُ') and (input[b3] == 'ذ') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\46-ه.wav" + "'")


                    elif ((input[a3] == 'ُ') and (input[b3] == 'ط') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\52-ه.wav" + "'")


                    elif ((input[a3] == 'ُ') and (input[b3] == 'ك') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\57-ه.wav" + "'")


                    elif ((input[a3] == 'ُ') and (input[b3] == 'م') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\59-ه.wav" + "'")


                    elif ((input[a3] == 'ُ') and (input[b3] == 'ن') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\60-ه.wav" + "'")


                    elif ((input[a3] == 'ُ') and (input[b3] == 'ت') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\40-ه.wav" + "'")


                    elif ((input[a3] == 'ُ') and (input[b3] == 'أ') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\38-ه.wav" + "'")


                    elif ((input[a3] == 'ُ') and (input[b3] == 'ل') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\58-ه.wav" + "'")


                    elif ((input[a3] == 'ُ') and (input[b3] == 'ب') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\39-ه.wav" + "'")


                    elif ((input[a3] == 'ُ') and (input[b3] == 'ي') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\62-ه.wav" + "'")


                    elif ((input[a3] == 'ُ') and (input[b3] == 'س') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\48-ه.wav" + "'")


                    elif ((input[a3] == 'ُ') and (input[b3] == 'ش') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\49-ه.wav" + "'")


                    elif ((input[a3] == 'ُ') and (input[b3] == 'ظ') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\51-ه.wav" + "'")


                    elif ((input[a3] == 'ُ') and (input[b3] == 'ز') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\z2.wav" + "'")


                    elif ((input[a3] == 'ُ') and (input[b3] == 'و') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\signs.wav" + "'")


                    elif ((input[a3] == 'ُ') and (input[b3] == 'ة') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\40-ه.wav" + "'")


                    elif ((input[a3] == 'ُ') and (input[b3] == 'ر') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\47-ه.wav" + "'")


                    elif ((input[a3] == 'ُ') and (input[b3] == 'ؤ') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\38-ه.wav" + "'")


                    elif ((input[a3] == 'ُ') and (input[b3] == 'ء') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\38-ه.wav" + "'")


                    elif ((input[a3] == 'ُ') and (input[b3] == 'ئ') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\38-ه.wav" + "'")





                    elif ((input[a3] == 'ِ') and (input[b3] == 'د') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\70-ه.wav" + "'")


                    elif ((input[a3] == 'ِ') and (input[b3] == 'ج') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\67-ه.wav" + "'")


                    elif ((input[a3] == 'ِ') and (input[b3] == 'ح') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\68-ه.wav" + "'")


                    elif ((input[a3] == 'ِ') and (input[b3] == 'خ') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\69-ه.wav" + "'")


                    elif ((input[a3] == 'ِ') and (input[b3] == 'ه') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\86-ه.wav" + "'")


                    elif ((input[a3] == 'ِ') and (input[b3] == 'ع') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\78-ه.wav" + "'")


                    elif ((input[a3] == 'ِ') and (input[b3] == 'غ') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\79-ه.wav" + "'")


                    elif ((input[a3] == 'ِ') and (input[b3] == 'ف') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\80-ه.wav" + "'")


                    elif ((input[a3] == 'ِ') and (input[b3] == 'ق') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\81-ه.wav" + "'")


                    elif ((input[a3] == 'ِ') and (input[b3] == 'ث') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\66-ه.wav" + "'")


                    elif ((input[a3] == 'ِ') and (input[b3] == 'ص') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\75-ه.wav" + "'")


                    elif ((input[a3] == 'ِ') and (input[b3] == 'ض') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\76-ه.wav" + "'")


                    elif ((input[a3] == 'ِ') and (input[b3] == 'ذ') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\71-ه.wav" + "'")


                    elif ((input[a3] == 'ِ') and (input[b3] == 'ط') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\77-ه.wav" + "'")


                    elif ((input[a3] == 'ِ') and (input[b3] == 'ك') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\82-ه.wav" + "'")


                    elif ((input[a3] == 'ِ') and (input[b3] == 'م') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\84-ه.wav" + "'")


                    elif ((input[a3] == 'ِ') and (input[b3] == 'ن') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\85-ه.wav" + "'")


                    elif ((input[a3] == 'ِ') and (input[b3] == 'ت') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\65-ه.wav" + "'")


                    elif ((input[a3] == 'ِ') and (input[b3] == 'أ') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\63-ه.wav" + "'")


                    elif ((input[a3] == 'ِ') and (input[b3] == 'ل') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\83-ه.wav" + "'")


                    elif ((input[a3] == 'ِ') and (input[b3] == 'ب') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\64-ه.wav" + "'")


                    elif ((input[a3] == 'ِ') and (input[b3] == 'ي') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\87-ه.wav" + "'")


                    elif ((input[a3] == 'ِ') and (input[b3] == 'س') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\73-ه.wav" + "'")


                    elif ((input[a3] == 'ِ') and (input[b3] == 'ش') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\74-ه.wav" + "'")


                    elif ((input[a3] == 'ِ') and (input[b3] == 'ظ') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\76-ه.wav" + "'")


                    elif ((input[a3] == 'ِ') and (input[b3] == 'ز') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\z3.wav" + "'")


                    elif ((input[a3] == 'ِ') and (input[b3] == 'و') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\signs.wav" + "'")


                    elif ((input[a3] == 'ِ') and (input[b3] == 'ة') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\65-ه.wav" + "'")


                    elif ((input[a3] == 'ِ') and (input[b3] == 'ر') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\72-ه.wav" + "'")


                    elif ((input[a3] == 'ِ') and (input[b3] == 'ؤ') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\63-ه.wav" + "'")


                    elif ((input[a3] == 'ِ') and (input[b3] == 'ء') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\63-ه.wav" + "'")


                    elif ((input[a3] == 'ِ') and (input[b3] == 'ئ') and (input[c3] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\h\\63-ه.wav" + "'")







                    elif ((input[a3] == 'َ') and ((input[b3] == 'ا') or (input[b3] == 'ى'))):

                        self.z.append('file ' + "'" + "library\\h\\04-ه.wav" + "'")


                    elif (input[a3] == 'ُ' and input[b3] == 'و'):

                        self.z.append('file ' + "'" + "library\\h\\05-ه.wav" + "'")


                    elif (input[a3] == 'ِ' and input[b3] == 'ي'):

                        self.z.append('file ' + "'" + "library\\h\\06-ه.wav" + "'")


                    elif (input[a3] == 'ً'):

                        self.z.append('file ' + "'" + "library\\h\\07-ه.wav" + "'")


                    elif (input[a3] == 'ٌ'):

                        self.z.append('file ' + "'" + "library\\h\\08-ه.wav" + "'")


                    elif (input[a3] == 'ٍ'):

                        self.z.append('file ' + "'" + "library\\h\\09-ه.wav" + "'")


                    elif (input[a3] == 'َ'):

                        self.z.append('file ' + "'" + "library\\h\\01-ه.wav" + "'")


                    elif (input[a3] == 'ُ'):

                        self.z.append('file ' + "'" + "library\\h\\02-ه.wav" + "'")


                    elif (input[a3] == 'ِ'):

                        self.z.append('file ' + "'" + "library\\h\\03-ه.wav" + "'")


                    elif (input[a3] == 'ْ'):

                        self.z.append('file ' + "'" + "library\\h\\signs.wav" + "'")


                    else:

                        self.z.append('file ' + "'" + "library\\h\\signs.wav" + "'")









                else:

                    self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                a3 = 0

                b3 = 0

                d3 = 0

                c3 = 0

            elif (char == 'ع'):

                a4 = i + 1

                b4 = i + 2

                c4 = i + 3

                d4 = i + 4

                if (a4 < (len(input))):

                    if (input[a4] == '\0'):

                        self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                    elif ((input[a4] == 'َ') and (input[b4] == 'د') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\3a\\20-ع.wav' + "'")

                    elif ((input[a4] == 'َ') and (input[b4] == 'ج') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\17-ع.wav" + "'")

                    elif ((input[a4] == 'َ') and (input[b4] == 'ح') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\18-ع.wav" + "'")

                    elif ((input[a4] == 'َ') and (input[b4] == 'خ') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\19-ع.wav" + "'")

                    elif ((input[a4] == 'َ') and (input[b4] == 'ه') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\36-ع.wav" + "'")

                    elif ((input[a4] == 'َ') and (input[b4] == 'ع') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\28-ع.wav" + "'")

                    elif ((input[a4] == 'َ') and (input[b4] == 'غ') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\29-ع.wav" + "'")

                    elif ((input[a4] == 'َ') and (input[b4] == 'ف') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\30-ع.wav" + "'")

                    elif ((input[a4] == 'َ') and (input[b4] == 'ق') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\31-ع.wav" + "'")

                    elif ((input[a4] == 'َ') and (input[b4] == 'ث') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\16-ع.wav" + "'")

                    elif ((input[a4] == 'َ') and (input[b4] == 'ص') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\25-ع.wav" + "'")

                    elif ((input[a4] == 'َ') and (input[b4] == 'ض') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\26-ع.wav" + "'")

                    elif ((input[a4] == 'َ') and (input[b4] == 'ذ') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\21-ع.wav" + "'")

                    elif ((input[a4] == 'َ') and (input[b4] == 'ط') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\27-ع.wav" + "'")

                    elif ((input[a4] == 'َ') and (input[b4] == 'ك') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\32-ع.wav" + "'")

                    elif ((input[a4] == 'َ') and (input[b4] == 'م') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\34-ع.wav" + "'")

                    elif ((input[a4] == 'َ') and (input[b4] == 'ن') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\35-ع.wav" + "'")

                    elif ((input[a4] == 'َ') and (input[b4] == 'ت') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\15-ع.wav" + "'")

                    elif ((input[a4] == 'َ') and (input[b4] == 'أ') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\13-ع.wav" + "'")

                    elif ((input[a4] == 'َ') and (input[b4] == 'ل') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\33-ع.wav" + "'")

                    elif ((input[a4] == 'َ') and (input[b4] == 'ب') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\14-ع.wav" + "'")

                    elif ((input[a4] == 'َ') and (input[b4] == 'ي') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\37-ع.wav" + "'")

                    elif ((input[a4] == 'َ') and (input[b4] == 'س') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\23-ع.wav" + "'")

                    elif ((input[a4] == 'َ') and (input[b4] == 'ش') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\24-ع.wav" + "'")

                    elif ((input[a4] == 'َ') and (input[b4] == 'ظ') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\26-ع.wav" + "'")

                    elif ((input[a4] == 'َ') and (input[b4] == 'ز') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\z1.wav" + "'")

                    elif ((input[a4] == 'َ') and (input[b4] == 'و') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\signs.wav" + "'")

                    elif ((input[a4] == 'َ') and (input[b4] == 'ة') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\15-ع.wav" + "'")

                    elif ((input[a4] == 'َ') and (input[b4] == 'ر') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\22-ع.wav" + "'")

                    elif ((input[a4] == 'َ') and (input[b4] == 'ؤ') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\13-ع.wav" + "'")

                    elif ((input[a4] == 'َ') and (input[b4] == 'ء') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\13-ع.wav" + "'")

                    elif ((input[a4] == 'َ') and (input[b4] == 'ئ') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\13-ع.wav" + "'")



                    elif ((input[a4] == 'ُ') and (input[b4] == 'د') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\45-ع.wav" + "'")

                    elif ((input[a4] == 'ُ') and (input[b4] == 'ج') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\42-ع.wav" + "'")

                    elif ((input[a4] == 'ُ') and (input[b4] == 'ح') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\43-ع.wav" + "'")

                    elif ((input[a4] == 'ُ') and (input[b4] == 'خ') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\44-ع.wav" + "'")

                    elif ((input[a4] == 'ُ') and (input[b4] == 'ه') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\61-ع.wav" + "'")

                    elif ((input[a4] == 'ُ') and (input[b4] == 'ع') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\53-ع.wav" + "'")

                    elif ((input[a4] == 'ُ') and (input[b4] == 'غ') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\54-ع.wav" + "'")

                    elif ((input[a4] == 'ُ') and (input[b4] == 'ف') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\55-ع.wav" + "'")

                    elif ((input[a4] == 'ُ') and (input[b4] == 'ق') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\56-ع.wav" + "'")

                    elif ((input[a4] == 'ُ') and (input[b4] == 'ث') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\41-ع.wav" + "'")

                    elif ((input[a4] == 'ُ') and (input[b4] == 'ص') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\50-ع.wav" + "'")

                    elif ((input[a4] == 'ُ') and (input[b4] == 'ض') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\51-ع.wav" + "'")

                    elif ((input[a4] == 'ُ') and (input[b4] == 'ذ') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\46-ع.wav" + "'")

                    elif ((input[a4] == 'ُ') and (input[b4] == 'ط') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\52-ع.wav" + "'")

                    elif ((input[a4] == 'ُ') and (input[b4] == 'ك') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\57-ع.wav" + "'")

                    elif ((input[a4] == 'ُ') and (input[b4] == 'م') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\59-ع.wav" + "'")

                    elif ((input[a4] == 'ُ') and (input[b4] == 'ن') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\60-ع.wav" + "'")

                    elif ((input[a4] == 'ُ') and (input[b4] == 'ت') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\40-ع.wav" + "'")

                    elif ((input[a4] == 'ُ') and (input[b4] == 'أ') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\38-ع.wav" + "'")

                    elif ((input[a4] == 'ُ') and (input[b4] == 'ل') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\58-ع.wav" + "'")

                    elif ((input[a4] == 'ُ') and (input[b4] == 'ب') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\39-ع.wav" + "'")

                    elif ((input[a4] == 'ُ') and (input[b4] == 'ي') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\62-ع.wav" + "'")

                    elif ((input[a4] == 'ُ') and (input[b4] == 'س') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\48-ع.wav" + "'")

                    elif ((input[a4] == 'ُ') and (input[b4] == 'ش') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\49-ع.wav" + "'")

                    elif ((input[a4] == 'ُ') and (input[b4] == 'ظ') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\51-ع.wav" + "'")

                    elif ((input[a4] == 'ُ') and (input[b4] == 'ز') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\z2.wav" + "'")

                    elif ((input[a4] == 'ُ') and (input[b4] == 'و') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\signs.wav" + "'")

                    elif ((input[a4] == 'ُ') and (input[b4] == 'ة') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\40-ع.wav" + "'")

                    elif ((input[a4] == 'ُ') and (input[b4] == 'ر') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\47-ع.wav" + "'")

                    elif ((input[a4] == 'ُ') and (input[b4] == 'ؤ') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\38-ع.wav" + "'")

                    elif ((input[a4] == 'ُ') and (input[b4] == 'ء') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\38-ع.wav" + "'")

                    elif ((input[a4] == 'ُ') and (input[b4] == 'ئ') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\38-ع.wav" + "'")




                    elif ((input[a4] == 'ِ') and (input[b4] == 'د') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\70-ع.wav" + "'")

                    elif ((input[a4] == 'ِ') and (input[b4] == 'ج') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\67-ع.wav" + "'")

                    elif ((input[a4] == 'ِ') and (input[b4] == 'ح') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\68-ع.wav" + "'")

                    elif ((input[a4] == 'ِ') and (input[b4] == 'خ') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\69-ع.wav" + "'")

                    elif ((input[a4] == 'ِ') and (input[b4] == 'ه') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\86-ع.wav" + "'")

                    elif ((input[a4] == 'ِ') and (input[b4] == 'ع') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\78-ع.wav" + "'")

                    elif ((input[a4] == 'ِ') and (input[b4] == 'غ') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\79-ع.wav" + "'")

                    elif ((input[a4] == 'ِ') and (input[b4] == 'ف') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\80-ع.wav" + "'")

                    elif ((input[a4] == 'ِ') and (input[b4] == 'ق') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\81-ع.wav" + "'")

                    elif ((input[a4] == 'ِ') and (input[b4] == 'ث') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\66-ع.wav" + "'")

                    elif ((input[a4] == 'ِ') and (input[b4] == 'ص') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\75-ع.wav" + "'")

                    elif ((input[a4] == 'ِ') and (input[b4] == 'ض') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\76-ع.wav" + "'")

                    elif ((input[a4] == 'ِ') and (input[b4] == 'ذ') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\71-ع.wav" + "'")

                    elif ((input[a4] == 'ِ') and (input[b4] == 'ط') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\77-ع.wav" + "'")

                    elif ((input[a4] == 'ِ') and (input[b4] == 'ك') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\82-ع.wav" + "'")

                    elif ((input[a4] == 'ِ') and (input[b4] == 'م') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\84-ع.wav" + "'")

                    elif ((input[a4] == 'ِ') and (input[b4] == 'ن') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\85-ع.wav" + "'")

                    elif ((input[a4] == 'ِ') and (input[b4] == 'ت') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\65-ع.wav" + "'")

                    elif ((input[a4] == 'ِ') and (input[b4] == 'أ') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\63-ع.wav" + "'")

                    elif ((input[a4] == 'ِ') and (input[b4] == 'ل') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\83-ع.wav" + "'")

                    elif ((input[a4] == 'ِ') and (input[b4] == 'ب') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\64-ع.wav" + "'")

                    elif ((input[a4] == 'ِ') and (input[b4] == 'ي') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\87-ع.wav" + "'")

                    elif ((input[a4] == 'ِ') and (input[b4] == 'س') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\73-ع.wav" + "'")

                    elif ((input[a4] == 'ِ') and (input[b4] == 'ش') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\74-ع.wav" + "'")

                    elif ((input[a4] == 'ِ') and (input[b4] == 'ظ') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\76-ع.wav" + "'")

                    elif ((input[a4] == 'ِ') and (input[b4] == 'ز') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\z3.wav" + "'")

                    elif ((input[a4] == 'ِ') and (input[b4] == 'و') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\signs.wav" + "'")

                    elif ((input[a4] == 'ِ') and (input[b4] == 'ة') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\65-ع.wav" + "'")

                    elif ((input[a4] == 'ِ') and (input[b4] == 'ر') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\72-ع.wav" + "'")

                    elif ((input[a4] == 'ِ') and (input[b4] == 'ؤ') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\63-ع.wav" + "'")

                    elif ((input[a4] == 'ِ') and (input[b4] == 'ء') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\63-ع.wav" + "'")

                    elif ((input[a4] == 'ِ') and (input[b4] == 'ئ') and (input[c4] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\3a\\63-ع.wav" + "'")






                    elif ((input[a4] == 'َ') and ((input[b4] == 'ا') or (input[b4] == 'ى'))):

                        self.z.append('file ' + "'" + "library\\3a\\04-ع.wav" + "'")

                    elif (input[a4] == 'ُ' and input[b4] == 'و'):

                        self.z.append('file ' + "'" + "library\\3a\\05-ع.wav" + "'")

                    elif (input[a4] == 'ِ' and input[b4] == 'ي'):

                        self.z.append('file ' + "'" + "library\\3a\\06-ع.wav" + "'")

                    elif (input[a4] == 'ً'):

                        self.z.append('file ' + "'" + "library\\3a\\07-ع.wav" + "'")

                    elif (input[a4] == 'ٌ'):

                        self.z.append('file ' + "'" + "library\\3a\\08-ع.wav" + "'")

                    elif (input[a4] == 'ٍ'):

                        self.z.append('file ' + "'" + "library\\3a\\09-ع.wav" + "'")

                    elif (input[a4] == 'َ'):

                        self.z.append('file ' + "'" + "library\\3a\\01-ع.wav" + "'")

                    elif (input[a4] == 'ُ'):

                        self.z.append('file ' + "'" + "library\\3a\\02-ع.wav" + "'")

                    elif (input[a4] == 'ِ'):

                        self.z.append('file ' + "'" + "library\\3a\\03-ع.wav" + "'")

                    elif (input[a4] == 'ْ'):

                        self.z.append('file ' + "'" + "library\\3a\\signs.wav" + "'")

                    else:

                        self.z.append('file ' + "'" + "library\\3a\\signs.wav" + "'")








                else:

                    self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                a4 = 0

                b4 = 0

                d4 = 0

                c4 = 0

            elif (char == 'غ'):

                a5 = i + 1

                b5 = i + 2

                c5 = i + 3

                d5 = i + 4

                if (a5 < (len(input))):

                    if (input[a5] == '\0'):

                        self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                    elif ((input[a5] == 'َ') and (input[b5] == 'د') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\gha\\20-غ.wav' + "'")

                    elif ((input[a5] == 'َ') and (input[b5] == 'ج') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\17-غ.wav" + "'")

                    elif ((input[a5] == 'َ') and (input[b5] == 'ح') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\18-غ.wav" + "'")

                    elif ((input[a5] == 'َ') and (input[b5] == 'خ') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\19-غ.wav" + "'")

                    elif ((input[a5] == 'َ') and (input[b5] == 'ه') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\36-غ.wav" + "'")

                    elif ((input[a5] == 'َ') and (input[b5] == 'ع') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\28-غ.wav" + "'")

                    elif ((input[a5] == 'َ') and (input[b5] == 'غ') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\29-غ.wav" + "'")

                    elif ((input[a5] == 'َ') and (input[b5] == 'ف') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\30-غ.wav" + "'")

                    elif ((input[a5] == 'َ') and (input[b5] == 'ق') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\31-غ.wav" + "'")

                    elif ((input[a5] == 'َ') and (input[b5] == 'ث') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\16-غ.wav" + "'")

                    elif ((input[a5] == 'َ') and (input[b5] == 'ص') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\25-غ.wav" + "'")

                    elif ((input[a5] == 'َ') and (input[b5] == 'ض') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\26-غ.wav" + "'")

                    elif ((input[a5] == 'َ') and (input[b5] == 'ذ') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\21-غ.wav" + "'")

                    elif ((input[a5] == 'َ') and (input[b5] == 'ط') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\27-غ.wav" + "'")

                    elif ((input[a5] == 'َ') and (input[b5] == 'ك') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\32-غ.wav" + "'")

                    elif ((input[a5] == 'َ') and (input[b5] == 'م') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\34-غ.wav" + "'")

                    elif ((input[a5] == 'َ') and (input[b5] == 'ن') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\35-غ.wav" + "'")

                    elif ((input[a5] == 'َ') and (input[b5] == 'ت') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\15-غ.wav" + "'")

                    elif ((input[a5] == 'َ') and (input[b5] == 'أ') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\13-غ.wav" + "'")

                    elif ((input[a5] == 'َ') and (input[b5] == 'ل') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\33-غ.wav" + "'")

                    elif ((input[a5] == 'َ') and (input[b5] == 'ب') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\14-غ.wav" + "'")

                    elif ((input[a5] == 'َ') and (input[b5] == 'ي') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\37-غ.wav" + "'")

                    elif ((input[a5] == 'َ') and (input[b5] == 'س') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\23-غ.wav" + "'")

                    elif ((input[a5] == 'َ') and (input[b5] == 'ش') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\24-غ.wav" + "'")

                    elif ((input[a5] == 'َ') and (input[b5] == 'ظ') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\26-غ.wav" + "'")

                    elif ((input[a5] == 'َ') and (input[b5] == 'ز') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\z1.wav" + "'")

                    elif ((input[a5] == 'َ') and (input[b5] == 'و') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\signs.wav" + "'")

                    elif ((input[a5] == 'َ') and (input[b5] == 'ة') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\15-غ.wav" + "'")

                    elif ((input[a5] == 'َ') and (input[b5] == 'ر') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\22-غ.wav" + "'")

                    elif ((input[a5] == 'َ') and (input[b5] == 'ؤ') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\13-غ.wav" + "'")

                    elif ((input[a5] == 'َ') and (input[b5] == 'ء') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\13-غ.wav" + "'")

                    elif ((input[a5] == 'َ') and (input[b5] == 'ئ') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\13-غ.wav" + "'")



                    elif ((input[a5] == 'ُ') and (input[b5] == 'د') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\45-غ.wav" + "'")

                    elif ((input[a5] == 'ُ') and (input[b5] == 'ج') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\42-غ.wav" + "'")

                    elif ((input[a5] == 'ُ') and (input[b5] == 'ح') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\43-غ.wav" + "'")

                    elif ((input[a5] == 'ُ') and (input[b5] == 'خ') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\44-غ.wav" + "'")

                    elif ((input[a5] == 'ُ') and (input[b5] == 'ه') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\61-غ.wav" + "'")

                    elif ((input[a5] == 'ُ') and (input[b5] == 'ع') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\53-غ.wav" + "'")

                    elif ((input[a5] == 'ُ') and (input[b5] == 'غ') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\54-غ.wav" + "'")

                    elif ((input[a5] == 'ُ') and (input[b5] == 'ف') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\55-غ.wav" + "'")

                    elif ((input[a5] == 'ُ') and (input[b5] == 'ق') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\56-غ.wav" + "'")

                    elif ((input[a5] == 'ُ') and (input[b5] == 'ث') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\41-غ.wav" + "'")

                    elif ((input[a5] == 'ُ') and (input[b5] == 'ص') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\50-غ.wav" + "'")

                    elif ((input[a5] == 'ُ') and (input[b5] == 'ض') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\51-غ.wav" + "'")

                    elif ((input[a5] == 'ُ') and (input[b5] == 'ذ') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\46-غ.wav" + "'")

                    elif ((input[a5] == 'ُ') and (input[b5] == 'ط') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\52-غ.wav" + "'")

                    elif ((input[a5] == 'ُ') and (input[b5] == 'ك') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\57-غ.wav" + "'")

                    elif ((input[a5] == 'ُ') and (input[b5] == 'م') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\59-غ.wav" + "'")

                    elif ((input[a5] == 'ُ') and (input[b5] == 'ن') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\60-غ.wav" + "'")

                    elif ((input[a5] == 'ُ') and (input[b5] == 'ت') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\40-غ.wav" + "'")

                    elif ((input[a5] == 'ُ') and (input[b5] == 'أ') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\38-غ.wav" + "'")

                    elif ((input[a5] == 'ُ') and (input[b5] == 'ل') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\58-غ.wav" + "'")

                    elif ((input[a5] == 'ُ') and (input[b5] == 'ب') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\39-غ.wav" + "'")

                    elif ((input[a5] == 'ُ') and (input[b5] == 'ي') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\62-غ.wav" + "'")

                    elif ((input[a5] == 'ُ') and (input[b5] == 'س') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\48-غ.wav" + "'")

                    elif ((input[a5] == 'ُ') and (input[b5] == 'ش') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\49-غ.wav" + "'")

                    elif ((input[a5] == 'ُ') and (input[b5] == 'ظ') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\51-غ.wav" + "'")

                    elif ((input[a5] == 'ُ') and (input[b5] == 'ز') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\z2.wav" + "'")

                    elif ((input[a5] == 'ُ') and (input[b5] == 'و') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\signs.wav" + "'")

                    elif ((input[a5] == 'ُ') and (input[b5] == 'ة') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\40-غ.wav" + "'")

                    elif ((input[a5] == 'ُ') and (input[b5] == 'ر') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\47-غ.wav" + "'")

                    elif ((input[a5] == 'ُ') and (input[b5] == 'ؤ') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\38-غ.wav" + "'")

                    elif ((input[a5] == 'ُ') and (input[b5] == 'ء') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\38-غ.wav" + "'")

                    elif ((input[a5] == 'ُ') and (input[b5] == 'ئ') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\38-غ.wav" + "'")




                    elif ((input[a5] == 'ِ') and (input[b5] == 'د') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\70-غ.wav" + "'")

                    elif ((input[a5] == 'ِ') and (input[b5] == 'ج') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\67-غ.wav" + "'")

                    elif ((input[a5] == 'ِ') and (input[b5] == 'ح') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\68-غ.wav" + "'")

                    elif ((input[a5] == 'ِ') and (input[b5] == 'خ') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\69-غ.wav" + "'")

                    elif ((input[a5] == 'ِ') and (input[b5] == 'ه') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\86-غ.wav" + "'")

                    elif ((input[a5] == 'ِ') and (input[b5] == 'ع') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\78-غ.wav" + "'")

                    elif ((input[a5] == 'ِ') and (input[b5] == 'غ') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\79-غ.wav" + "'")

                    elif ((input[a5] == 'ِ') and (input[b5] == 'ف') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\80-غ.wav" + "'")

                    elif ((input[a5] == 'ِ') and (input[b5] == 'ق') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\81-غ.wav" + "'")

                    elif ((input[a5] == 'ِ') and (input[b5] == 'ث') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\66-غ.wav" + "'")

                    elif ((input[a5] == 'ِ') and (input[b5] == 'ص') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\75-غ.wav" + "'")

                    elif ((input[a5] == 'ِ') and (input[b5] == 'ض') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\76-غ.wav" + "'")

                    elif ((input[a5] == 'ِ') and (input[b5] == 'ذ') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\71-غ.wav" + "'")

                    elif ((input[a5] == 'ِ') and (input[b5] == 'ط') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\77-غ.wav" + "'")

                    elif ((input[a5] == 'ِ') and (input[b5] == 'ك') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\82-غ.wav" + "'")

                    elif ((input[a5] == 'ِ') and (input[b5] == 'م') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\84-غ.wav" + "'")

                    elif ((input[a5] == 'ِ') and (input[b5] == 'ن') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\85-غ.wav" + "'")

                    elif ((input[a5] == 'ِ') and (input[b5] == 'ت') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\65-غ.wav" + "'")

                    elif ((input[a5] == 'ِ') and (input[b5] == 'أ') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\63-غ.wav" + "'")

                    elif ((input[a5] == 'ِ') and (input[b5] == 'ل') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\83-غ.wav" + "'")

                    elif ((input[a5] == 'ِ') and (input[b5] == 'ب') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\64-غ.wav" + "'")

                    elif ((input[a5] == 'ِ') and (input[b5] == 'ي') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\87-غ.wav" + "'")

                    elif ((input[a5] == 'ِ') and (input[b5] == 'س') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\73-غ.wav" + "'")

                    elif ((input[a5] == 'ِ') and (input[b5] == 'ش') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\74-غ.wav" + "'")

                    elif ((input[a5] == 'ِ') and (input[b5] == 'ظ') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\76-غ.wav" + "'")

                    elif ((input[a5] == 'ِ') and (input[b5] == 'ز') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\z3.wav" + "'")

                    elif ((input[a5] == 'ِ') and (input[b5] == 'و') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\signs.wav" + "'")

                    elif ((input[a5] == 'ِ') and (input[b5] == 'ة') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\65-غ.wav" + "'")

                    elif ((input[a5] == 'ِ') and (input[b5] == 'ر') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\72-غ.wav" + "'")

                    elif ((input[a5] == 'ِ') and (input[b5] == 'ؤ') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\63-غ.wav" + "'")

                    elif ((input[a5] == 'ِ') and (input[b5] == 'ء') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\63-غ.wav" + "'")

                    elif ((input[a5] == 'ِ') and (input[b5] == 'ئ') and (input[c5] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\gha\\63-غ.wav" + "'")






                    elif ((input[a5] == 'َ') and ((input[b5] == 'ا') or (input[b5] == 'ى'))):

                        self.z.append('file ' + "'" + "library\\gha\\04-غ.wav" + "'")

                    elif (input[a5] == 'ُ' and input[b5] == 'و'):

                        self.z.append('file ' + "'" + "library\\gha\\05-غ.wav" + "'")

                    elif (input[a5] == 'ِ' and input[b5] == 'ي'):

                        self.z.append('file ' + "'" + "library\\gha\\06-غ.wav" + "'")

                    elif (input[a5] == 'ً'):

                        self.z.append('file ' + "'" + "library\\gha\\07-غ.wav" + "'")

                    elif (input[a5] == 'ٌ'):

                        self.z.append('file ' + "'" + "library\\gha\\08-غ.wav" + "'")

                    elif (input[a5] == 'ٍ'):

                        self.z.append('file ' + "'" + "library\\gha\\09-غ.wav" + "'")

                    elif (input[a5] == 'َ'):

                        self.z.append('file ' + "'" + "library\\gha\\01-غ.wav" + "'")

                    elif (input[a5] == 'ُ'):

                        self.z.append('file ' + "'" + "library\\gha\\02-غ.wav" + "'")

                    elif (input[a5] == 'ِ'):

                        self.z.append('file ' + "'" + "library\\gha\\03-غ.wav" + "'")

                    elif (input[a5] == 'ْ'):

                        self.z.append('file ' + "'" + "library\\gha\\signs.wav" + "'")

                    else:

                        self.z.append('file ' + "'" + "library\\gha\\signs.wav" + "'")








                else:

                    self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                a5 = 0

                b5 = 0

                d5 = 0

                c5 = 0

            elif (char == 'ف'):

                a6 = i + 1

                b6 = i + 2

                c6 = i + 3

                d6 = i + 4

                if (a6 < (len(input))):

                    if (input[a6] == '\0'):

                        self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                    elif ((input[a6] == 'َ') and (input[b6] == 'د') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\f\\20-ف.wav' + "'")

                    elif ((input[a6] == 'َ') and (input[b6] == 'ج') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\17-ف.wav" + "'")

                    elif ((input[a6] == 'َ') and (input[b6] == 'ح') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\18-ف.wav" + "'")

                    elif ((input[a6] == 'َ') and (input[b6] == 'خ') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\19-ف.wav" + "'")

                    elif ((input[a6] == 'َ') and (input[b6] == 'ه') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\36-ف.wav" + "'")

                    elif ((input[a6] == 'َ') and (input[b6] == 'ع') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\28-ف.wav" + "'")

                    elif ((input[a6] == 'َ') and (input[b6] == 'غ') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\29-ف.wav" + "'")

                    elif ((input[a6] == 'َ') and (input[b6] == 'ف') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\30-ف.wav" + "'")

                    elif ((input[a6] == 'َ') and (input[b6] == 'ق') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\31-ف.wav" + "'")

                    elif ((input[a6] == 'َ') and (input[b6] == 'ث') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\16-ف.wav" + "'")

                    elif ((input[a6] == 'َ') and (input[b6] == 'ص') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\25-ف.wav" + "'")

                    elif ((input[a6] == 'َ') and (input[b6] == 'ض') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\26-ف.wav" + "'")

                    elif ((input[a6] == 'َ') and (input[b6] == 'ذ') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\21-ف.wav" + "'")

                    elif ((input[a6] == 'َ') and (input[b6] == 'ط') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\27-ف.wav" + "'")

                    elif ((input[a6] == 'َ') and (input[b6] == 'ك') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\32-ف.wav" + "'")

                    elif ((input[a6] == 'َ') and (input[b6] == 'م') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\34-ف.wav" + "'")

                    elif ((input[a6] == 'َ') and (input[b6] == 'ن') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\35-ف.wav" + "'")

                    elif ((input[a6] == 'َ') and (input[b6] == 'ت') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\15-ف.wav" + "'")

                    elif ((input[a6] == 'َ') and (input[b6] == 'أ') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\13-ف.wav" + "'")

                    elif ((input[a6] == 'َ') and (input[b6] == 'ل') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\33-ف.wav" + "'")

                    elif ((input[a6] == 'َ') and (input[b6] == 'ب') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\14-ف.wav" + "'")

                    elif ((input[a6] == 'َ') and (input[b6] == 'ي') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\37-ف.wav" + "'")

                    elif ((input[a6] == 'َ') and (input[b6] == 'س') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\23-ف.wav" + "'")

                    elif ((input[a6] == 'َ') and (input[b6] == 'ش') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\24-ف.wav" + "'")

                    elif ((input[a6] == 'َ') and (input[b6] == 'ظ') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\26-ف.wav" + "'")

                    elif ((input[a6] == 'َ') and (input[b6] == 'ز') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\z1.wav" + "'")

                    elif ((input[a6] == 'َ') and (input[b6] == 'و') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\signs.wav" + "'")

                    elif ((input[a6] == 'َ') and (input[b6] == 'ة') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\15-ف.wav" + "'")

                    elif ((input[a6] == 'َ') and (input[b6] == 'ر') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\22-ف.wav" + "'")

                    elif ((input[a6] == 'َ') and (input[b6] == 'ؤ') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\13-ف.wav" + "'")

                    elif ((input[a6] == 'َ') and (input[b6] == 'ء') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\13-ف.wav" + "'")

                    elif ((input[a6] == 'َ') and (input[b6] == 'ئ') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\13-ف.wav" + "'")



                    elif ((input[a6] == 'ُ') and (input[b6] == 'د') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\45-ف.wav" + "'")

                    elif ((input[a6] == 'ُ') and (input[b6] == 'ج') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\42-ف.wav" + "'")

                    elif ((input[a6] == 'ُ') and (input[b6] == 'ح') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\43-ف.wav" + "'")

                    elif ((input[a6] == 'ُ') and (input[b6] == 'خ') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\44-ف.wav" + "'")

                    elif ((input[a6] == 'ُ') and (input[b6] == 'ه') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\61-ف.wav" + "'")

                    elif ((input[a6] == 'ُ') and (input[b6] == 'ع') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\53-ف.wav" + "'")

                    elif ((input[a6] == 'ُ') and (input[b6] == 'غ') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\54-ف.wav" + "'")

                    elif ((input[a6] == 'ُ') and (input[b6] == 'ف') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\55-ف.wav" + "'")

                    elif ((input[a6] == 'ُ') and (input[b6] == 'ق') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\56-ف.wav" + "'")

                    elif ((input[a6] == 'ُ') and (input[b6] == 'ث') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\41-ف.wav" + "'")

                    elif ((input[a6] == 'ُ') and (input[b6] == 'ص') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\50-ف.wav" + "'")

                    elif ((input[a6] == 'ُ') and (input[b6] == 'ض') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\51-ف.wav" + "'")

                    elif ((input[a6] == 'ُ') and (input[b6] == 'ذ') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\46-ف.wav" + "'")

                    elif ((input[a6] == 'ُ') and (input[b6] == 'ط') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\52-ف.wav" + "'")

                    elif ((input[a6] == 'ُ') and (input[b6] == 'ك') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\57-ف.wav" + "'")

                    elif ((input[a6] == 'ُ') and (input[b6] == 'م') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\59-ف.wav" + "'")

                    elif ((input[a6] == 'ُ') and (input[b6] == 'ن') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\60-ف.wav" + "'")

                    elif ((input[a6] == 'ُ') and (input[b6] == 'ت') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\40-ف.wav" + "'")

                    elif ((input[a6] == 'ُ') and (input[b6] == 'أ') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\38-ف.wav" + "'")

                    elif ((input[a6] == 'ُ') and (input[b6] == 'ل') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\58-ف.wav" + "'")

                    elif ((input[a6] == 'ُ') and (input[b6] == 'ب') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\39-ف.wav" + "'")

                    elif ((input[a6] == 'ُ') and (input[b6] == 'ي') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\62-ف.wav" + "'")

                    elif ((input[a6] == 'ُ') and (input[b6] == 'س') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\48-ف.wav" + "'")

                    elif ((input[a6] == 'ُ') and (input[b6] == 'ش') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\49-ف.wav" + "'")

                    elif ((input[a6] == 'ُ') and (input[b6] == 'ظ') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\51-ف.wav" + "'")

                    elif ((input[a6] == 'ُ') and (input[b6] == 'ز') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\z2.wav" + "'")

                    elif ((input[a6] == 'ُ') and (input[b6] == 'و') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\signs.wav" + "'")

                    elif ((input[a6] == 'ُ') and (input[b6] == 'ة') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\40-ف.wav" + "'")

                    elif ((input[a6] == 'ُ') and (input[b6] == 'ر') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\47-ف.wav" + "'")

                    elif ((input[a6] == 'ُ') and (input[b6] == 'ؤ') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\38-ف.wav" + "'")

                    elif ((input[a6] == 'ُ') and (input[b6] == 'ء') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\38-ف.wav" + "'")

                    elif ((input[a6] == 'ُ') and (input[b6] == 'ئ') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\38-ف.wav" + "'")




                    elif ((input[a6] == 'ِ') and (input[b6] == 'د') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\70-ف.wav" + "'")

                    elif ((input[a6] == 'ِ') and (input[b6] == 'ج') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\67-ف.wav" + "'")

                    elif ((input[a6] == 'ِ') and (input[b6] == 'ح') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\68-ف.wav" + "'")

                    elif ((input[a6] == 'ِ') and (input[b6] == 'خ') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\69-ف.wav" + "'")

                    elif ((input[a6] == 'ِ') and (input[b6] == 'ه') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\86-ف.wav" + "'")

                    elif ((input[a6] == 'ِ') and (input[b6] == 'ع') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\78-ف.wav" + "'")

                    elif ((input[a6] == 'ِ') and (input[b6] == 'غ') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\79-ف.wav" + "'")

                    elif ((input[a6] == 'ِ') and (input[b6] == 'ف') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\80-ف.wav" + "'")

                    elif ((input[a6] == 'ِ') and (input[b6] == 'ق') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\81-ف.wav" + "'")

                    elif ((input[a6] == 'ِ') and (input[b6] == 'ث') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\66-ف.wav" + "'")

                    elif ((input[a6] == 'ِ') and (input[b6] == 'ص') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\75-ف.wav" + "'")

                    elif ((input[a6] == 'ِ') and (input[b6] == 'ض') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\76-ف.wav" + "'")

                    elif ((input[a6] == 'ِ') and (input[b6] == 'ذ') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\71-ف.wav" + "'")

                    elif ((input[a6] == 'ِ') and (input[b6] == 'ط') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\77-ف.wav" + "'")

                    elif ((input[a6] == 'ِ') and (input[b6] == 'ك') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\82-ف.wav" + "'")

                    elif ((input[a6] == 'ِ') and (input[b6] == 'م') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\84-ف.wav" + "'")

                    elif ((input[a6] == 'ِ') and (input[b6] == 'ن') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\85-ف.wav" + "'")

                    elif ((input[a6] == 'ِ') and (input[b6] == 'ت') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\65-ف.wav" + "'")

                    elif ((input[a6] == 'ِ') and (input[b6] == 'أ') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\63-ف.wav" + "'")

                    elif ((input[a6] == 'ِ') and (input[b6] == 'ل') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\83-ف.wav" + "'")

                    elif ((input[a6] == 'ِ') and (input[b6] == 'ب') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\64-ف.wav" + "'")

                    elif ((input[a6] == 'ِ') and (input[b6] == 'ي') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\87-ف.wav" + "'")

                    elif ((input[a6] == 'ِ') and (input[b6] == 'س') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\73-ف.wav" + "'")

                    elif ((input[a6] == 'ِ') and (input[b6] == 'ش') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\74-ف.wav" + "'")

                    elif ((input[a6] == 'ِ') and (input[b6] == 'ظ') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\76-ف.wav" + "'")

                    elif ((input[a6] == 'ِ') and (input[b6] == 'ز') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\z3.wav" + "'")

                    elif ((input[a6] == 'ِ') and (input[b6] == 'و') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\signs.wav" + "'")

                    elif ((input[a6] == 'ِ') and (input[b6] == 'ة') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\65-ف.wav" + "'")

                    elif ((input[a6] == 'ِ') and (input[b6] == 'ر') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\72-ف.wav" + "'")

                    elif ((input[a6] == 'ِ') and (input[b6] == 'ؤ') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\63-ف.wav" + "'")

                    elif ((input[a6] == 'ِ') and (input[b6] == 'ء') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\63-ف.wav" + "'")

                    elif ((input[a6] == 'ِ') and (input[b6] == 'ئ') and (input[c6] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\f\\63-ف.wav" + "'")






                    elif ((input[a6] == 'َ') and ((input[b6] == 'ا') or (input[b6] == 'ى'))):

                        self.z.append('file ' + "'" + "library\\f\\04-ف.wav" + "'")

                    elif (input[a6] == 'ُ' and input[b6] == 'و'):

                        self.z.append('file ' + "'" + "library\\f\\05-ف.wav" + "'")

                    elif (input[a6] == 'ِ' and input[b6] == 'ي'):

                        self.z.append('file ' + "'" + "library\\f\\06-ف.wav" + "'")

                    elif (input[a6] == 'ً'):

                        self.z.append('file ' + "'" + "library\\f\\07-ف.wav" + "'")

                    elif (input[a6] == 'ٌ'):

                        self.z.append('file ' + "'" + "library\\f\\08-ف.wav" + "'")

                    elif (input[a6] == 'ٍ'):

                        self.z.append('file ' + "'" + "library\\f\\09-ف.wav" + "'")

                    elif (input[a6] == 'َ'):

                        self.z.append('file ' + "'" + "library\\f\\01-ف.wav" + "'")

                    elif (input[a6] == 'ُ'):

                        self.z.append('file ' + "'" + "library\\f\\02-ف.wav" + "'")

                    elif (input[a6] == 'ِ'):

                        self.z.append('file ' + "'" + "library\\f\\03-ف.wav" + "'")

                    elif (input[a6] == 'ْ'):

                        self.z.append('file ' + "'" + "library\\f\\signs.wav" + "'")

                    else:

                        self.z.append('file ' + "'" + "library\\f\\signs.wav" + "'")








                else:

                    self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                a6 = 0

                b6 = 0

                d6 = 0

                c6 = 0

            elif (char == 'ق'):

                a7 = i + 1

                b7 = i + 2

                c7 = i + 3

                d7 = i + 4

                if (a7 < (len(input))):

                    if (input[a7] == '\0'):

                        self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                    elif ((input[a7] == 'َ') and (input[b7] == 'د') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\9a\\20-ق.wav' + "'")

                    elif ((input[a7] == 'َ') and (input[b7] == 'ج') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\17-ق.wav" + "'")

                    elif ((input[a7] == 'َ') and (input[b7] == 'ح') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\18-ق.wav" + "'")

                    elif ((input[a7] == 'َ') and (input[b7] == 'خ') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\19-ق.wav" + "'")

                    elif ((input[a7] == 'َ') and (input[b7] == 'ه') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\36-ق.wav" + "'")

                    elif ((input[a7] == 'َ') and (input[b7] == 'ع') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\28-ق.wav" + "'")

                    elif ((input[a7] == 'َ') and (input[b7] == 'غ') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\29-ق.wav" + "'")

                    elif ((input[a7] == 'َ') and (input[b7] == 'ف') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\30-ق.wav" + "'")

                    elif ((input[a7] == 'َ') and (input[b7] == 'ق') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\31-ق.wav" + "'")

                    elif ((input[a7] == 'َ') and (input[b7] == 'ث') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\16-ق.wav" + "'")

                    elif ((input[a7] == 'َ') and (input[b7] == 'ص') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\25-ق.wav" + "'")

                    elif ((input[a7] == 'َ') and (input[b7] == 'ض') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\26-ق.wav" + "'")

                    elif ((input[a7] == 'َ') and (input[b7] == 'ذ') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\21-ق.wav" + "'")

                    elif ((input[a7] == 'َ') and (input[b7] == 'ط') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\27-ق.wav" + "'")

                    elif ((input[a7] == 'َ') and (input[b7] == 'ك') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\32-ق.wav" + "'")

                    elif ((input[a7] == 'َ') and (input[b7] == 'م') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\34-ق.wav" + "'")

                    elif ((input[a7] == 'َ') and (input[b7] == 'ن') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\35-ق.wav" + "'")

                    elif ((input[a7] == 'َ') and (input[b7] == 'ت') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\15-ق.wav" + "'")

                    elif ((input[a7] == 'َ') and (input[b7] == 'أ') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\13-ق.wav" + "'")

                    elif ((input[a7] == 'َ') and (input[b7] == 'ل') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\33-ق.wav" + "'")

                    elif ((input[a7] == 'َ') and (input[b7] == 'ب') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\14-ق.wav" + "'")

                    elif ((input[a7] == 'َ') and (input[b7] == 'ي') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\37-ق.wav" + "'")

                    elif ((input[a7] == 'َ') and (input[b7] == 'س') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\23-ق.wav" + "'")

                    elif ((input[a7] == 'َ') and (input[b7] == 'ش') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\24-ق.wav" + "'")

                    elif ((input[a7] == 'َ') and (input[b7] == 'ظ') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\26-ق.wav" + "'")

                    elif ((input[a7] == 'َ') and (input[b7] == 'ز') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\z1.wav" + "'")

                    elif ((input[a7] == 'َ') and (input[b7] == 'و') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\signs.wav" + "'")

                    elif ((input[a7] == 'َ') and (input[b7] == 'ة') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\15-ق.wav" + "'")

                    elif ((input[a7] == 'َ') and (input[b7] == 'ر') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\22-ق.wav" + "'")

                    elif ((input[a7] == 'َ') and (input[b7] == 'ؤ') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\13-ق.wav" + "'")

                    elif ((input[a7] == 'َ') and (input[b7] == 'ء') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\13-ق.wav" + "'")

                    elif ((input[a7] == 'َ') and (input[b7] == 'ئ') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\13-ق.wav" + "'")



                    elif ((input[a7] == 'ُ') and (input[b7] == 'د') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\45-ق.wav" + "'")

                    elif ((input[a7] == 'ُ') and (input[b7] == 'ج') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\42-ق.wav" + "'")

                    elif ((input[a7] == 'ُ') and (input[b7] == 'ح') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\43-ق.wav" + "'")

                    elif ((input[a7] == 'ُ') and (input[b7] == 'خ') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\44-ق.wav" + "'")

                    elif ((input[a7] == 'ُ') and (input[b7] == 'ه') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\61-ق.wav" + "'")

                    elif ((input[a7] == 'ُ') and (input[b7] == 'ع') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\53-ق.wav" + "'")

                    elif ((input[a7] == 'ُ') and (input[b7] == 'غ') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\54-ق.wav" + "'")

                    elif ((input[a7] == 'ُ') and (input[b7] == 'ف') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\55-ق.wav" + "'")

                    elif ((input[a7] == 'ُ') and (input[b7] == 'ق') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\56-ق.wav" + "'")

                    elif ((input[a7] == 'ُ') and (input[b7] == 'ث') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\41-ق.wav" + "'")

                    elif ((input[a7] == 'ُ') and (input[b7] == 'ص') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\50-ق.wav" + "'")

                    elif ((input[a7] == 'ُ') and (input[b7] == 'ض') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\51-ق.wav" + "'")

                    elif ((input[a7] == 'ُ') and (input[b7] == 'ذ') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\46-ق.wav" + "'")

                    elif ((input[a7] == 'ُ') and (input[b7] == 'ط') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\52-ق.wav" + "'")

                    elif ((input[a7] == 'ُ') and (input[b7] == 'ك') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\57-ق.wav" + "'")

                    elif ((input[a7] == 'ُ') and (input[b7] == 'م') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\59-ق.wav" + "'")

                    elif ((input[a7] == 'ُ') and (input[b7] == 'ن') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\60-ق.wav" + "'")

                    elif ((input[a7] == 'ُ') and (input[b7] == 'ت') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\40-ق.wav" + "'")

                    elif ((input[a7] == 'ُ') and (input[b7] == 'أ') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\38-ق.wav" + "'")

                    elif ((input[a7] == 'ُ') and (input[b7] == 'ل') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\58-ق.wav" + "'")

                    elif ((input[a7] == 'ُ') and (input[b7] == 'ب') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\39-ق.wav" + "'")

                    elif ((input[a7] == 'ُ') and (input[b7] == 'ي') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\62-ق.wav" + "'")

                    elif ((input[a7] == 'ُ') and (input[b7] == 'س') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\48-ق.wav" + "'")

                    elif ((input[a7] == 'ُ') and (input[b7] == 'ش') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\49-ق.wav" + "'")

                    elif ((input[a7] == 'ُ') and (input[b7] == 'ظ') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\51-ق.wav" + "'")

                    elif ((input[a7] == 'ُ') and (input[b7] == 'ز') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\z2.wav" + "'")

                    elif ((input[a7] == 'ُ') and (input[b7] == 'و') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\signs.wav" + "'")

                    elif ((input[a7] == 'ُ') and (input[b7] == 'ة') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\40-ق.wav" + "'")

                    elif ((input[a7] == 'ُ') and (input[b7] == 'ر') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\47-ق.wav" + "'")

                    elif ((input[a7] == 'ُ') and (input[b7] == 'ؤ') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\38-ق.wav" + "'")

                    elif ((input[a7] == 'ُ') and (input[b7] == 'ء') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\38-ق.wav" + "'")

                    elif ((input[a7] == 'ُ') and (input[b7] == 'ئ') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\38-ق.wav" + "'")




                    elif ((input[a7] == 'ِ') and (input[b7] == 'د') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\70-ق.wav" + "'")

                    elif ((input[a7] == 'ِ') and (input[b7] == 'ج') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\67-ق.wav" + "'")

                    elif ((input[a7] == 'ِ') and (input[b7] == 'ح') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\68-ق.wav" + "'")

                    elif ((input[a7] == 'ِ') and (input[b7] == 'خ') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\69-ق.wav" + "'")

                    elif ((input[a7] == 'ِ') and (input[b7] == 'ه') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\86-ق.wav" + "'")

                    elif ((input[a7] == 'ِ') and (input[b7] == 'ع') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\78-ق.wav" + "'")

                    elif ((input[a7] == 'ِ') and (input[b7] == 'غ') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\79-ق.wav" + "'")

                    elif ((input[a7] == 'ِ') and (input[b7] == 'ف') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\80-ق.wav" + "'")

                    elif ((input[a7] == 'ِ') and (input[b7] == 'ق') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\81-ق.wav" + "'")

                    elif ((input[a7] == 'ِ') and (input[b7] == 'ث') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\66-ق.wav" + "'")

                    elif ((input[a7] == 'ِ') and (input[b7] == 'ص') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\75-ق.wav" + "'")

                    elif ((input[a7] == 'ِ') and (input[b7] == 'ض') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\76-ق.wav" + "'")

                    elif ((input[a7] == 'ِ') and (input[b7] == 'ذ') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\71-ق.wav" + "'")

                    elif ((input[a7] == 'ِ') and (input[b7] == 'ط') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\77-ق.wav" + "'")

                    elif ((input[a7] == 'ِ') and (input[b7] == 'ك') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\82-ق.wav" + "'")

                    elif ((input[a7] == 'ِ') and (input[b7] == 'م') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\84-ق.wav" + "'")

                    elif ((input[a7] == 'ِ') and (input[b7] == 'ن') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\85-ق.wav" + "'")

                    elif ((input[a7] == 'ِ') and (input[b7] == 'ت') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\65-ق.wav" + "'")

                    elif ((input[a7] == 'ِ') and (input[b7] == 'أ') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\63-ق.wav" + "'")

                    elif ((input[a7] == 'ِ') and (input[b7] == 'ل') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\83-ق.wav" + "'")

                    elif ((input[a7] == 'ِ') and (input[b7] == 'ب') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\64-ق.wav" + "'")

                    elif ((input[a7] == 'ِ') and (input[b7] == 'ي') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\87-ق.wav" + "'")

                    elif ((input[a7] == 'ِ') and (input[b7] == 'س') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\73-ق.wav" + "'")

                    elif ((input[a7] == 'ِ') and (input[b7] == 'ش') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\74-ق.wav" + "'")

                    elif ((input[a7] == 'ِ') and (input[b7] == 'ظ') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\76-ق.wav" + "'")

                    elif ((input[a7] == 'ِ') and (input[b7] == 'ز') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\z3.wav" + "'")

                    elif ((input[a7] == 'ِ') and (input[b7] == 'و') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\signs.wav" + "'")

                    elif ((input[a7] == 'ِ') and (input[b7] == 'ة') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\65-ق.wav" + "'")

                    elif ((input[a7] == 'ِ') and (input[b7] == 'ر') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\72-ق.wav" + "'")

                    elif ((input[a7] == 'ِ') and (input[b7] == 'ؤ') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\63-ق.wav" + "'")

                    elif ((input[a7] == 'ِ') and (input[b7] == 'ء') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\63-ق.wav" + "'")

                    elif ((input[a7] == 'ِ') and (input[b7] == 'ئ') and (input[c7] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\9a\\63-ق.wav" + "'")






                    elif ((input[a7] == 'َ') and ((input[b7] == 'ا') or (input[b7] == 'ى'))):

                        self.z.append('file ' + "'" + "library\\9a\\04-ق.wav" + "'")

                    elif (input[a7] == 'ُ' and input[b7] == 'و'):

                        self.z.append('file ' + "'" + "library\\9a\\05-ق.wav" + "'")

                    elif (input[a7] == 'ِ' and input[b7] == 'ي'):

                        self.z.append('file ' + "'" + "library\\9a\\06-ق.wav" + "'")

                    elif (input[a7] == 'ً'):

                        self.z.append('file ' + "'" + "library\\9a\\07-ق.wav" + "'")

                    elif (input[a7] == 'ٌ'):

                        self.z.append('file ' + "'" + "library\\9a\\08-ق.wav" + "'")

                    elif (input[a7] == 'ٍ'):

                        self.z.append('file ' + "'" + "library\\9a\\09-ق.wav" + "'")

                    elif (input[a7] == 'َ'):

                        self.z.append('file ' + "'" + "library\\9a\\01-ق.wav" + "'")

                    elif (input[a7] == 'ُ'):

                        self.z.append('file ' + "'" + "library\\9a\\02-ق.wav" + "'")

                    elif (input[a7] == 'ِ'):

                        self.z.append('file ' + "'" + "library\\9a\\03-ق.wav" + "'")

                    elif (input[a7] == 'ْ'):

                        self.z.append('file ' + "'" + "library\\9a\\signs.wav" + "'")

                    else:

                        self.z.append('file ' + "'" + "library\\9a\\signs.wav" + "'")








                else:

                    self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                a7 = 0

                b7 = 0

                d7 = 0

                c7 = 0

            elif (char == 'ث'):

                a8 = i + 1

                b8 = i + 2

                c8 = i + 3

                d8 = i + 4

                if (a8 < (len(input))):

                    if (input[a8] == '\0'):

                        self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                    elif ((input[a8] == 'َ') and (input[b8] == 'د') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\ethe\\20-ث.wav' + "'")

                    elif ((input[a8] == 'َ') and (input[b8] == 'ج') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\17-ث.wav" + "'")

                    elif ((input[a8] == 'َ') and (input[b8] == 'ح') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\18-ث.wav" + "'")

                    elif ((input[a8] == 'َ') and (input[b8] == 'خ') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\19-ث.wav" + "'")

                    elif ((input[a8] == 'َ') and (input[b8] == 'ه') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\36-ث.wav" + "'")

                    elif ((input[a8] == 'َ') and (input[b8] == 'ع') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\28-ث.wav" + "'")

                    elif ((input[a8] == 'َ') and (input[b8] == 'غ') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\29-ث.wav" + "'")

                    elif ((input[a8] == 'َ') and (input[b8] == 'ف') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\30-ث.wav" + "'")

                    elif ((input[a8] == 'َ') and (input[b8] == 'ق') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\31-ث.wav" + "'")

                    elif ((input[a8] == 'َ') and (input[b8] == 'ث') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\16-ث.wav" + "'")

                    elif ((input[a8] == 'َ') and (input[b8] == 'ص') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\25-ث.wav" + "'")

                    elif ((input[a8] == 'َ') and (input[b8] == 'ض') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\26-ث.wav" + "'")

                    elif ((input[a8] == 'َ') and (input[b8] == 'ذ') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\21-ث.wav" + "'")

                    elif ((input[a8] == 'َ') and (input[b8] == 'ط') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\27-ث.wav" + "'")

                    elif ((input[a8] == 'َ') and (input[b8] == 'ك') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\32-ث.wav" + "'")

                    elif ((input[a8] == 'َ') and (input[b8] == 'م') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\34-ث.wav" + "'")

                    elif ((input[a8] == 'َ') and (input[b8] == 'ن') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\35-ث.wav" + "'")

                    elif ((input[a8] == 'َ') and (input[b8] == 'ت') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\15-ث.wav" + "'")

                    elif ((input[a8] == 'َ') and (input[b8] == 'أ') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\13-ث.wav" + "'")

                    elif ((input[a8] == 'َ') and (input[b8] == 'ل') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\33-ث.wav" + "'")

                    elif ((input[a8] == 'َ') and (input[b8] == 'ب') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\14-ث.wav" + "'")

                    elif ((input[a8] == 'َ') and (input[b8] == 'ي') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\37-ث.wav" + "'")

                    elif ((input[a8] == 'َ') and (input[b8] == 'س') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\23-ث.wav" + "'")

                    elif ((input[a8] == 'َ') and (input[b8] == 'ش') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\24-ث.wav" + "'")

                    elif ((input[a8] == 'َ') and (input[b8] == 'ظ') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\26-ث.wav" + "'")

                    elif ((input[a8] == 'َ') and (input[b8] == 'ز') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\z1.wav" + "'")

                    elif ((input[a8] == 'َ') and (input[b8] == 'و') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\signs.wav" + "'")

                    elif ((input[a8] == 'َ') and (input[b8] == 'ة') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\15-ث.wav" + "'")

                    elif ((input[a8] == 'َ') and (input[b8] == 'ر') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\22-ث.wav" + "'")

                    elif ((input[a8] == 'َ') and (input[b8] == 'ؤ') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\13-ث.wav" + "'")

                    elif ((input[a8] == 'َ') and (input[b8] == 'ء') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\13-ث.wav" + "'")

                    elif ((input[a8] == 'َ') and (input[b8] == 'ئ') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\13-ث.wav" + "'")



                    elif ((input[a8] == 'ُ') and (input[b8] == 'د') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\45-ث.wav" + "'")

                    elif ((input[a8] == 'ُ') and (input[b8] == 'ج') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\42-ث.wav" + "'")

                    elif ((input[a8] == 'ُ') and (input[b8] == 'ح') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\43-ث.wav" + "'")

                    elif ((input[a8] == 'ُ') and (input[b8] == 'خ') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\44-ث.wav" + "'")

                    elif ((input[a8] == 'ُ') and (input[b8] == 'ه') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\61-ث.wav" + "'")

                    elif ((input[a8] == 'ُ') and (input[b8] == 'ع') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\53-ث.wav" + "'")

                    elif ((input[a8] == 'ُ') and (input[b8] == 'غ') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\54-ث.wav" + "'")

                    elif ((input[a8] == 'ُ') and (input[b8] == 'ف') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\55-ث.wav" + "'")

                    elif ((input[a8] == 'ُ') and (input[b8] == 'ق') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\56-ث.wav" + "'")

                    elif ((input[a8] == 'ُ') and (input[b8] == 'ث') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\41-ث.wav" + "'")

                    elif ((input[a8] == 'ُ') and (input[b8] == 'ص') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\50-ث.wav" + "'")

                    elif ((input[a8] == 'ُ') and (input[b8] == 'ض') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\51-ث.wav" + "'")

                    elif ((input[a8] == 'ُ') and (input[b8] == 'ذ') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\46-ث.wav" + "'")

                    elif ((input[a8] == 'ُ') and (input[b8] == 'ط') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\52-ث.wav" + "'")

                    elif ((input[a8] == 'ُ') and (input[b8] == 'ك') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\57-ث.wav" + "'")

                    elif ((input[a8] == 'ُ') and (input[b8] == 'م') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\59-ث.wav" + "'")

                    elif ((input[a8] == 'ُ') and (input[b8] == 'ن') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\60-ث.wav" + "'")

                    elif ((input[a8] == 'ُ') and (input[b8] == 'ت') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\40-ث.wav" + "'")

                    elif ((input[a8] == 'ُ') and (input[b8] == 'أ') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\38-ث.wav" + "'")

                    elif ((input[a8] == 'ُ') and (input[b8] == 'ل') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\58-ث.wav" + "'")

                    elif ((input[a8] == 'ُ') and (input[b8] == 'ب') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\39-ث.wav" + "'")

                    elif ((input[a8] == 'ُ') and (input[b8] == 'ي') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\62-ث.wav" + "'")

                    elif ((input[a8] == 'ُ') and (input[b8] == 'س') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\48-ث.wav" + "'")

                    elif ((input[a8] == 'ُ') and (input[b8] == 'ش') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\49-ث.wav" + "'")

                    elif ((input[a8] == 'ُ') and (input[b8] == 'ظ') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\51-ث.wav" + "'")

                    elif ((input[a8] == 'ُ') and (input[b8] == 'ز') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\z2.wav" + "'")

                    elif ((input[a8] == 'ُ') and (input[b8] == 'و') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\signs.wav" + "'")

                    elif ((input[a8] == 'ُ') and (input[b8] == 'ة') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\40-ث.wav" + "'")

                    elif ((input[a8] == 'ُ') and (input[b8] == 'ر') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\47-ث.wav" + "'")

                    elif ((input[a8] == 'ُ') and (input[b8] == 'ؤ') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\38-ث.wav" + "'")

                    elif ((input[a8] == 'ُ') and (input[b8] == 'ء') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\38-ث.wav" + "'")

                    elif ((input[a8] == 'ُ') and (input[b8] == 'ئ') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\38-ث.wav" + "'")




                    elif ((input[a8] == 'ِ') and (input[b8] == 'د') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\70-ث.wav" + "'")

                    elif ((input[a8] == 'ِ') and (input[b8] == 'ج') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\67-ث.wav" + "'")

                    elif ((input[a8] == 'ِ') and (input[b8] == 'ح') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\68-ث.wav" + "'")

                    elif ((input[a8] == 'ِ') and (input[b8] == 'خ') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\69-ث.wav" + "'")

                    elif ((input[a8] == 'ِ') and (input[b8] == 'ه') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\86-ث.wav" + "'")

                    elif ((input[a8] == 'ِ') and (input[b8] == 'ع') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\78-ث.wav" + "'")

                    elif ((input[a8] == 'ِ') and (input[b8] == 'غ') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\79-ث.wav" + "'")

                    elif ((input[a8] == 'ِ') and (input[b8] == 'ف') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\80-ث.wav" + "'")

                    elif ((input[a8] == 'ِ') and (input[b8] == 'ق') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\81-ث.wav" + "'")

                    elif ((input[a8] == 'ِ') and (input[b8] == 'ث') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\66-ث.wav" + "'")

                    elif ((input[a8] == 'ِ') and (input[b8] == 'ص') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\75-ث.wav" + "'")

                    elif ((input[a8] == 'ِ') and (input[b8] == 'ض') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\76-ث.wav" + "'")

                    elif ((input[a8] == 'ِ') and (input[b8] == 'ذ') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\71-ث.wav" + "'")

                    elif ((input[a8] == 'ِ') and (input[b8] == 'ط') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\77-ث.wav" + "'")

                    elif ((input[a8] == 'ِ') and (input[b8] == 'ك') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\82-ث.wav" + "'")

                    elif ((input[a8] == 'ِ') and (input[b8] == 'م') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\84-ث.wav" + "'")

                    elif ((input[a8] == 'ِ') and (input[b8] == 'ن') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\85-ث.wav" + "'")

                    elif ((input[a8] == 'ِ') and (input[b8] == 'ت') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\65-ث.wav" + "'")

                    elif ((input[a8] == 'ِ') and (input[b8] == 'أ') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\63-ث.wav" + "'")

                    elif ((input[a8] == 'ِ') and (input[b8] == 'ل') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\83-ث.wav" + "'")

                    elif ((input[a8] == 'ِ') and (input[b8] == 'ب') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\64-ث.wav" + "'")

                    elif ((input[a8] == 'ِ') and (input[b8] == 'ي') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\87-ث.wav" + "'")

                    elif ((input[a8] == 'ِ') and (input[b8] == 'س') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\73-ث.wav" + "'")

                    elif ((input[a8] == 'ِ') and (input[b8] == 'ش') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\74-ث.wav" + "'")

                    elif ((input[a8] == 'ِ') and (input[b8] == 'ظ') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\76-ث.wav" + "'")

                    elif ((input[a8] == 'ِ') and (input[b8] == 'ز') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\z3.wav" + "'")

                    elif ((input[a8] == 'ِ') and (input[b8] == 'و') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\signs.wav" + "'")

                    elif ((input[a8] == 'ِ') and (input[b8] == 'ة') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\65-ث.wav" + "'")

                    elif ((input[a8] == 'ِ') and (input[b8] == 'ر') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\72-ث.wav" + "'")

                    elif ((input[a8] == 'ِ') and (input[b8] == 'ؤ') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\63-ث.wav" + "'")

                    elif ((input[a8] == 'ِ') and (input[b8] == 'ء') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\63-ث.wav" + "'")

                    elif ((input[a8] == 'ِ') and (input[b8] == 'ئ') and (input[c8] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ethe\\63-ث.wav" + "'")






                    elif ((input[a8] == 'َ') and ((input[b8] == 'ا') or (input[b8] == 'ى'))):

                        self.z.append('file ' + "'" + "library\\ethe\\04-ث.wav" + "'")

                    elif (input[a8] == 'ُ' and input[b8] == 'و'):

                        self.z.append('file ' + "'" + "library\\ethe\\05-ث.wav" + "'")

                    elif (input[a8] == 'ِ' and input[b8] == 'ي'):

                        self.z.append('file ' + "'" + "library\\ethe\\06-ث.wav" + "'")

                    elif (input[a8] == 'ً'):

                        self.z.append('file ' + "'" + "library\\ethe\\07-ث.wav" + "'")

                    elif (input[a8] == 'ٌ'):

                        self.z.append('file ' + "'" + "library\\ethe\\08-ث.wav" + "'")

                    elif (input[a8] == 'ٍ'):

                        self.z.append('file ' + "'" + "library\\ethe\\09-ث.wav" + "'")

                    elif (input[a8] == 'َ'):

                        self.z.append('file ' + "'" + "library\\ethe\\01-ث.wav" + "'")

                    elif (input[a8] == 'ُ'):

                        self.z.append('file ' + "'" + "library\\ethe\\02-ث.wav" + "'")

                    elif (input[a8] == 'ِ'):

                        self.z.append('file ' + "'" + "library\\ethe\\03-ث.wav" + "'")

                    elif (input[a8] == 'ْ'):

                        self.z.append('file ' + "'" + "library\\ethe\\signs.wav" + "'")

                    else:

                        self.z.append('file ' + "'" + "library\\ethe\\signs.wav" + "'")








                else:

                    self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                a8 = 0

                b8 = 0

                d8 = 0

                c8 = 0

            elif (char == 'ص'):

                a9 = i + 1

                b9 = i + 2

                c9 = i + 3

                d9 = i + 4

                if (a9 < (len(input))):

                    if (input[a9] == '\0'):

                        self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                    elif ((input[a9] == 'َ') and (input[b9] == 'د') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\sa\\20-ص.wav' + "'")

                    elif ((input[a9] == 'َ') and (input[b9] == 'ج') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\17-ص.wav" + "'")

                    elif ((input[a9] == 'َ') and (input[b9] == 'ح') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\18-ص.wav" + "'")

                    elif ((input[a9] == 'َ') and (input[b9] == 'خ') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\19-ص.wav" + "'")

                    elif ((input[a9] == 'َ') and (input[b9] == 'ه') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\36-ص.wav" + "'")

                    elif ((input[a9] == 'َ') and (input[b9] == 'ع') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\28-ص.wav" + "'")

                    elif ((input[a9] == 'َ') and (input[b9] == 'غ') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\29-ص.wav" + "'")

                    elif ((input[a9] == 'َ') and (input[b9] == 'ف') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\30-ص.wav" + "'")

                    elif ((input[a9] == 'َ') and (input[b9] == 'ق') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\31-ص.wav" + "'")

                    elif ((input[a9] == 'َ') and (input[b9] == 'ث') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\16-ص.wav" + "'")

                    elif ((input[a9] == 'َ') and (input[b9] == 'ص') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\25-ص.wav" + "'")

                    elif ((input[a9] == 'َ') and (input[b9] == 'ض') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\26-ص.wav" + "'")

                    elif ((input[a9] == 'َ') and (input[b9] == 'ذ') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\21-ص.wav" + "'")

                    elif ((input[a9] == 'َ') and (input[b9] == 'ط') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\27-ص.wav" + "'")

                    elif ((input[a9] == 'َ') and (input[b9] == 'ك') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\32-ص.wav" + "'")

                    elif ((input[a9] == 'َ') and (input[b9] == 'م') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\34-ص.wav" + "'")

                    elif ((input[a9] == 'َ') and (input[b9] == 'ن') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\35-ص.wav" + "'")

                    elif ((input[a9] == 'َ') and (input[b9] == 'ت') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\15-ص.wav" + "'")

                    elif ((input[a9] == 'َ') and (input[b9] == 'أ') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\13-ص.wav" + "'")

                    elif ((input[a9] == 'َ') and (input[b9] == 'ل') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\33-ص.wav" + "'")

                    elif ((input[a9] == 'َ') and (input[b9] == 'ب') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\14-ص.wav" + "'")

                    elif ((input[a9] == 'َ') and (input[b9] == 'ي') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\37-ص.wav" + "'")

                    elif ((input[a9] == 'َ') and (input[b9] == 'س') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\23-ص.wav" + "'")

                    elif ((input[a9] == 'َ') and (input[b9] == 'ش') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\24-ص.wav" + "'")

                    elif ((input[a9] == 'َ') and (input[b9] == 'ظ') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\26-ص.wav" + "'")

                    elif ((input[a9] == 'َ') and (input[b9] == 'ز') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\z1.wav" + "'")

                    elif ((input[a9] == 'َ') and (input[b9] == 'و') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\signs.wav" + "'")

                    elif ((input[a9] == 'َ') and (input[b9] == 'ة') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\15-ص.wav" + "'")

                    elif ((input[a9] == 'َ') and (input[b9] == 'ر') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\22-ص.wav" + "'")

                    elif ((input[a9] == 'َ') and (input[b9] == 'ؤ') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\13-ص.wav" + "'")

                    elif ((input[a9] == 'َ') and (input[b9] == 'ء') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\13-ص.wav" + "'")

                    elif ((input[a9] == 'َ') and (input[b9] == 'ئ') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\13-ص.wav" + "'")



                    elif ((input[a9] == 'ُ') and (input[b9] == 'د') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\45-ص.wav" + "'")

                    elif ((input[a9] == 'ُ') and (input[b9] == 'ج') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\42-ص.wav" + "'")

                    elif ((input[a9] == 'ُ') and (input[b9] == 'ح') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\43-ص.wav" + "'")

                    elif ((input[a9] == 'ُ') and (input[b9] == 'خ') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\44-ص.wav" + "'")

                    elif ((input[a9] == 'ُ') and (input[b9] == 'ه') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\61-ص.wav" + "'")

                    elif ((input[a9] == 'ُ') and (input[b9] == 'ع') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\53-ص.wav" + "'")

                    elif ((input[a9] == 'ُ') and (input[b9] == 'غ') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\54-ص.wav" + "'")

                    elif ((input[a9] == 'ُ') and (input[b9] == 'ف') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\55-ص.wav" + "'")

                    elif ((input[a9] == 'ُ') and (input[b9] == 'ق') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\56-ص.wav" + "'")

                    elif ((input[a9] == 'ُ') and (input[b9] == 'ث') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\41-ص.wav" + "'")

                    elif ((input[a9] == 'ُ') and (input[b9] == 'ص') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\50-ص.wav" + "'")

                    elif ((input[a9] == 'ُ') and (input[b9] == 'ض') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\51-ص.wav" + "'")

                    elif ((input[a9] == 'ُ') and (input[b9] == 'ذ') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\46-ص.wav" + "'")

                    elif ((input[a9] == 'ُ') and (input[b9] == 'ط') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\52-ص.wav" + "'")

                    elif ((input[a9] == 'ُ') and (input[b9] == 'ك') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\57-ص.wav" + "'")

                    elif ((input[a9] == 'ُ') and (input[b9] == 'م') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\59-ص.wav" + "'")

                    elif ((input[a9] == 'ُ') and (input[b9] == 'ن') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\60-ص.wav" + "'")

                    elif ((input[a9] == 'ُ') and (input[b9] == 'ت') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\40-ص.wav" + "'")

                    elif ((input[a9] == 'ُ') and (input[b9] == 'أ') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\38-ص.wav" + "'")

                    elif ((input[a9] == 'ُ') and (input[b9] == 'ل') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\58-ص.wav" + "'")

                    elif ((input[a9] == 'ُ') and (input[b9] == 'ب') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\39-ص.wav" + "'")

                    elif ((input[a9] == 'ُ') and (input[b9] == 'ي') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\62-ص.wav" + "'")

                    elif ((input[a9] == 'ُ') and (input[b9] == 'س') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\48-ص.wav" + "'")

                    elif ((input[a9] == 'ُ') and (input[b9] == 'ش') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\49-ص.wav" + "'")

                    elif ((input[a9] == 'ُ') and (input[b9] == 'ظ') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\51-ص.wav" + "'")

                    elif ((input[a9] == 'ُ') and (input[b9] == 'ز') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\z2.wav" + "'")

                    elif ((input[a9] == 'ُ') and (input[b9] == 'و') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\signs.wav" + "'")

                    elif ((input[a9] == 'ُ') and (input[b9] == 'ة') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\40-ص.wav" + "'")

                    elif ((input[a9] == 'ُ') and (input[b9] == 'ر') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\47-ص.wav" + "'")

                    elif ((input[a9] == 'ُ') and (input[b9] == 'ؤ') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\38-ص.wav" + "'")

                    elif ((input[a9] == 'ُ') and (input[b9] == 'ء') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\38-ص.wav" + "'")

                    elif ((input[a9] == 'ُ') and (input[b9] == 'ئ') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\38-ص.wav" + "'")




                    elif ((input[a9] == 'ِ') and (input[b9] == 'د') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\70-ص.wav" + "'")

                    elif ((input[a9] == 'ِ') and (input[b9] == 'ج') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\67-ص.wav" + "'")

                    elif ((input[a9] == 'ِ') and (input[b9] == 'ح') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\68-ص.wav" + "'")

                    elif ((input[a9] == 'ِ') and (input[b9] == 'خ') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\69-ص.wav" + "'")

                    elif ((input[a9] == 'ِ') and (input[b9] == 'ه') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\86-ص.wav" + "'")

                    elif ((input[a9] == 'ِ') and (input[b9] == 'ع') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\78-ص.wav" + "'")

                    elif ((input[a9] == 'ِ') and (input[b9] == 'غ') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\79-ص.wav" + "'")

                    elif ((input[a9] == 'ِ') and (input[b9] == 'ف') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\80-ص.wav" + "'")

                    elif ((input[a9] == 'ِ') and (input[b9] == 'ق') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\81-ص.wav" + "'")

                    elif ((input[a9] == 'ِ') and (input[b9] == 'ث') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\66-ص.wav" + "'")

                    elif ((input[a9] == 'ِ') and (input[b9] == 'ص') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\75-ص.wav" + "'")

                    elif ((input[a9] == 'ِ') and (input[b9] == 'ض') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\76-ص.wav" + "'")

                    elif ((input[a9] == 'ِ') and (input[b9] == 'ذ') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\71-ص.wav" + "'")

                    elif ((input[a9] == 'ِ') and (input[b9] == 'ط') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\77-ص.wav" + "'")

                    elif ((input[a9] == 'ِ') and (input[b9] == 'ك') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\82-ص.wav" + "'")

                    elif ((input[a9] == 'ِ') and (input[b9] == 'م') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\84-ص.wav" + "'")

                    elif ((input[a9] == 'ِ') and (input[b9] == 'ن') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\85-ص.wav" + "'")

                    elif ((input[a9] == 'ِ') and (input[b9] == 'ت') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\65-ص.wav" + "'")

                    elif ((input[a9] == 'ِ') and (input[b9] == 'أ') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\63-ص.wav" + "'")

                    elif ((input[a9] == 'ِ') and (input[b9] == 'ل') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\83-ص.wav" + "'")

                    elif ((input[a9] == 'ِ') and (input[b9] == 'ب') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\64-ص.wav" + "'")

                    elif ((input[a9] == 'ِ') and (input[b9] == 'ي') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\87-ص.wav" + "'")

                    elif ((input[a9] == 'ِ') and (input[b9] == 'س') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\73-ص.wav" + "'")

                    elif ((input[a9] == 'ِ') and (input[b9] == 'ش') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\74-ص.wav" + "'")

                    elif ((input[a9] == 'ِ') and (input[b9] == 'ظ') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\76-ص.wav" + "'")

                    elif ((input[a9] == 'ِ') and (input[b9] == 'ز') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\z3.wav" + "'")

                    elif ((input[a9] == 'ِ') and (input[b9] == 'و') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\signs.wav" + "'")

                    elif ((input[a9] == 'ِ') and (input[b9] == 'ة') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\65-ص.wav" + "'")

                    elif ((input[a9] == 'ِ') and (input[b9] == 'ر') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\72-ص.wav" + "'")

                    elif ((input[a9] == 'ِ') and (input[b9] == 'ؤ') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\63-ص.wav" + "'")

                    elif ((input[a9] == 'ِ') and (input[b9] == 'ء') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\63-ص.wav" + "'")

                    elif ((input[a9] == 'ِ') and (input[b9] == 'ئ') and (input[c9] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\sa\\63-ص.wav" + "'")






                    elif ((input[a9] == 'َ') and ((input[b9] == 'ا') or (input[b9] == 'ى'))):

                        self.z.append('file ' + "'" + "library\\sa\\04-ص.wav" + "'")

                    elif (input[a9] == 'ُ' and input[b9] == 'و'):

                        self.z.append('file ' + "'" + "library\\sa\\05-ص.wav" + "'")

                    elif (input[a9] == 'ِ' and input[b9] == 'ي'):

                        self.z.append('file ' + "'" + "library\\sa\\06-ص.wav" + "'")

                    elif (input[a9] == 'ً'):

                        self.z.append('file ' + "'" + "library\\sa\\07-ص.wav" + "'")

                    elif (input[a9] == 'ٌ'):

                        self.z.append('file ' + "'" + "library\\sa\\08-ص.wav" + "'")

                    elif (input[a9] == 'ٍ'):

                        self.z.append('file ' + "'" + "library\\sa\\09-ص.wav" + "'")

                    elif (input[a9] == 'َ'):

                        self.z.append('file ' + "'" + "library\\sa\\01-ص.wav" + "'")

                    elif (input[a9] == 'ُ'):

                        self.z.append('file ' + "'" + "library\\sa\\02-ص.wav" + "'")

                    elif (input[a9] == 'ِ'):

                        self.z.append('file ' + "'" + "library\\sa\\03-ص.wav" + "'")

                    elif (input[a9] == 'ْ'):

                        self.z.append('file ' + "'" + "library\\sa\\signs.wav" + "'")

                    else:

                        self.z.append('file ' + "'" + "library\\sa\\signs.wav" + "'")








                else:

                    self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                a9 = 0

                b9 = 0

                d9 = 0

                c9 = 0

            elif (char == 'ض'):

                a10 = i + 1

                b10 = i + 2

                c10 = i + 3

                d10 = i + 4

                if (a10 < (len(input))):

                    if (input[a10] == '\0'):

                        self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                    elif ((input[a10] == 'َ') and (input[b10] == 'د') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\dha\\20-ض.wav' + "'")

                    elif ((input[a10] == 'َ') and (input[b10] == 'ج') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\17-ض.wav" + "'")

                    elif ((input[a10] == 'َ') and (input[b10] == 'ح') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\18-ض.wav" + "'")

                    elif ((input[a10] == 'َ') and (input[b10] == 'خ') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\19-ض.wav" + "'")

                    elif ((input[a10] == 'َ') and (input[b10] == 'ه') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\36-ض.wav" + "'")

                    elif ((input[a10] == 'َ') and (input[b10] == 'ع') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\28-ض.wav" + "'")

                    elif ((input[a10] == 'َ') and (input[b10] == 'غ') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\29-ض.wav" + "'")

                    elif ((input[a10] == 'َ') and (input[b10] == 'ف') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\30-ض.wav" + "'")

                    elif ((input[a10] == 'َ') and (input[b10] == 'ق') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\31-ض.wav" + "'")

                    elif ((input[a10] == 'َ') and (input[b10] == 'ث') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\16-ض.wav" + "'")

                    elif ((input[a10] == 'َ') and (input[b10] == 'ص') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\25-ض.wav" + "'")

                    elif ((input[a10] == 'َ') and (input[b10] == 'ض') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\26-ض.wav" + "'")

                    elif ((input[a10] == 'َ') and (input[b10] == 'ذ') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\21-ض.wav" + "'")

                    elif ((input[a10] == 'َ') and (input[b10] == 'ط') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\27-ض.wav" + "'")

                    elif ((input[a10] == 'َ') and (input[b10] == 'ك') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\32-ض.wav" + "'")

                    elif ((input[a10] == 'َ') and (input[b10] == 'م') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\34-ض.wav" + "'")

                    elif ((input[a10] == 'َ') and (input[b10] == 'ن') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\35-ض.wav" + "'")

                    elif ((input[a10] == 'َ') and (input[b10] == 'ت') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\15-ض.wav" + "'")

                    elif ((input[a10] == 'َ') and (input[b10] == 'أ') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\13-ض.wav" + "'")

                    elif ((input[a10] == 'َ') and (input[b10] == 'ل') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\33-ض.wav" + "'")

                    elif ((input[a10] == 'َ') and (input[b10] == 'ب') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\14-ض.wav" + "'")

                    elif ((input[a10] == 'َ') and (input[b10] == 'ي') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\37-ض.wav" + "'")

                    elif ((input[a10] == 'َ') and (input[b10] == 'س') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\23-ض.wav" + "'")

                    elif ((input[a10] == 'َ') and (input[b10] == 'ش') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\24-ض.wav" + "'")

                    elif ((input[a10] == 'َ') and (input[b10] == 'ظ') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\26-ض.wav" + "'")

                    elif ((input[a10] == 'َ') and (input[b10] == 'ز') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\z1.wav" + "'")

                    elif ((input[a10] == 'َ') and (input[b10] == 'و') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\signs.wav" + "'")

                    elif ((input[a10] == 'َ') and (input[b10] == 'ة') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\15-ض.wav" + "'")

                    elif ((input[a10] == 'َ') and (input[b10] == 'ر') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\22-ض.wav" + "'")

                    elif ((input[a10] == 'َ') and (input[b10] == 'ؤ') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\13-ض.wav" + "'")

                    elif ((input[a10] == 'َ') and (input[b10] == 'ء') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\13-ض.wav" + "'")

                    elif ((input[a10] == 'َ') and (input[b10] == 'ئ') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\13-ض.wav" + "'")



                    elif ((input[a10] == 'ُ') and (input[b10] == 'د') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\45-ض.wav" + "'")

                    elif ((input[a10] == 'ُ') and (input[b10] == 'ج') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\42-ض.wav" + "'")

                    elif ((input[a10] == 'ُ') and (input[b10] == 'ح') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\43-ض.wav" + "'")

                    elif ((input[a10] == 'ُ') and (input[b10] == 'خ') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\44-ض.wav" + "'")

                    elif ((input[a10] == 'ُ') and (input[b10] == 'ه') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\61-ض.wav" + "'")

                    elif ((input[a10] == 'ُ') and (input[b10] == 'ع') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\53-ض.wav" + "'")

                    elif ((input[a10] == 'ُ') and (input[b10] == 'غ') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\54-ض.wav" + "'")

                    elif ((input[a10] == 'ُ') and (input[b10] == 'ف') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\55-ض.wav" + "'")

                    elif ((input[a10] == 'ُ') and (input[b10] == 'ق') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\56-ض.wav" + "'")

                    elif ((input[a10] == 'ُ') and (input[b10] == 'ث') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\41-ض.wav" + "'")

                    elif ((input[a10] == 'ُ') and (input[b10] == 'ص') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\50-ض.wav" + "'")

                    elif ((input[a10] == 'ُ') and (input[b10] == 'ض') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\51-ض.wav" + "'")

                    elif ((input[a10] == 'ُ') and (input[b10] == 'ذ') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\46-ض.wav" + "'")

                    elif ((input[a10] == 'ُ') and (input[b10] == 'ط') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\52-ض.wav" + "'")

                    elif ((input[a10] == 'ُ') and (input[b10] == 'ك') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\57-ض.wav" + "'")

                    elif ((input[a10] == 'ُ') and (input[b10] == 'م') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\59-ض.wav" + "'")

                    elif ((input[a10] == 'ُ') and (input[b10] == 'ن') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\60-ض.wav" + "'")

                    elif ((input[a10] == 'ُ') and (input[b10] == 'ت') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\40-ض.wav" + "'")

                    elif ((input[a10] == 'ُ') and (input[b10] == 'أ') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\38-ض.wav" + "'")

                    elif ((input[a10] == 'ُ') and (input[b10] == 'ل') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\58-ض.wav" + "'")

                    elif ((input[a10] == 'ُ') and (input[b10] == 'ب') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\39-ض.wav" + "'")

                    elif ((input[a10] == 'ُ') and (input[b10] == 'ي') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\62-ض.wav" + "'")

                    elif ((input[a10] == 'ُ') and (input[b10] == 'س') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\48-ض.wav" + "'")

                    elif ((input[a10] == 'ُ') and (input[b10] == 'ش') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\49-ض.wav" + "'")

                    elif ((input[a10] == 'ُ') and (input[b10] == 'ظ') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\51-ض.wav" + "'")

                    elif ((input[a10] == 'ُ') and (input[b10] == 'ز') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\z2.wav" + "'")

                    elif ((input[a10] == 'ُ') and (input[b10] == 'و') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\signs.wav" + "'")

                    elif ((input[a10] == 'ُ') and (input[b10] == 'ة') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\40-ض.wav" + "'")

                    elif ((input[a10] == 'ُ') and (input[b10] == 'ر') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\47-ض.wav" + "'")

                    elif ((input[a10] == 'ُ') and (input[b10] == 'ؤ') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\38-ض.wav" + "'")

                    elif ((input[a10] == 'ُ') and (input[b10] == 'ء') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\38-ض.wav" + "'")

                    elif ((input[a10] == 'ُ') and (input[b10] == 'ئ') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\38-ض.wav" + "'")




                    elif ((input[a10] == 'ِ') and (input[b10] == 'د') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\70-ض.wav" + "'")

                    elif ((input[a10] == 'ِ') and (input[b10] == 'ج') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\67-ض.wav" + "'")

                    elif ((input[a10] == 'ِ') and (input[b10] == 'ح') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\68-ض.wav" + "'")

                    elif ((input[a10] == 'ِ') and (input[b10] == 'خ') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\69-ض.wav" + "'")

                    elif ((input[a10] == 'ِ') and (input[b10] == 'ه') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\86-ض.wav" + "'")

                    elif ((input[a10] == 'ِ') and (input[b10] == 'ع') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\78-ض.wav" + "'")

                    elif ((input[a10] == 'ِ') and (input[b10] == 'غ') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\79-ض.wav" + "'")

                    elif ((input[a10] == 'ِ') and (input[b10] == 'ف') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\80-ض.wav" + "'")

                    elif ((input[a10] == 'ِ') and (input[b10] == 'ق') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\81-ض.wav" + "'")

                    elif ((input[a10] == 'ِ') and (input[b10] == 'ث') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\66-ض.wav" + "'")

                    elif ((input[a10] == 'ِ') and (input[b10] == 'ص') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\75-ض.wav" + "'")

                    elif ((input[a10] == 'ِ') and (input[b10] == 'ض') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\76-ض.wav" + "'")

                    elif ((input[a10] == 'ِ') and (input[b10] == 'ذ') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\71-ض.wav" + "'")

                    elif ((input[a10] == 'ِ') and (input[b10] == 'ط') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\77-ض.wav" + "'")

                    elif ((input[a10] == 'ِ') and (input[b10] == 'ك') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\82-ض.wav" + "'")

                    elif ((input[a10] == 'ِ') and (input[b10] == 'م') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\84-ض.wav" + "'")

                    elif ((input[a10] == 'ِ') and (input[b10] == 'ن') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\85-ض.wav" + "'")

                    elif ((input[a10] == 'ِ') and (input[b10] == 'ت') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\65-ض.wav" + "'")

                    elif ((input[a10] == 'ِ') and (input[b10] == 'أ') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\63-ض.wav" + "'")

                    elif ((input[a10] == 'ِ') and (input[b10] == 'ل') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\83-ض.wav" + "'")

                    elif ((input[a10] == 'ِ') and (input[b10] == 'ب') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\64-ض.wav" + "'")

                    elif ((input[a10] == 'ِ') and (input[b10] == 'ي') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\87-ض.wav" + "'")

                    elif ((input[a10] == 'ِ') and (input[b10] == 'س') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\73-ض.wav" + "'")

                    elif ((input[a10] == 'ِ') and (input[b10] == 'ش') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\74-ض.wav" + "'")

                    elif ((input[a10] == 'ِ') and (input[b10] == 'ظ') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\76-ض.wav" + "'")

                    elif ((input[a10] == 'ِ') and (input[b10] == 'ز') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\z3.wav" + "'")

                    elif ((input[a10] == 'ِ') and (input[b10] == 'و') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\signs.wav" + "'")

                    elif ((input[a10] == 'ِ') and (input[b10] == 'ة') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\65-ض.wav" + "'")

                    elif ((input[a10] == 'ِ') and (input[b10] == 'ر') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\72-ض.wav" + "'")

                    elif ((input[a10] == 'ِ') and (input[b10] == 'ؤ') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\63-ض.wav" + "'")

                    elif ((input[a10] == 'ِ') and (input[b10] == 'ء') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\63-ض.wav" + "'")

                    elif ((input[a10] == 'ِ') and (input[b10] == 'ئ') and (input[c10] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\63-ض.wav" + "'")






                    elif ((input[a10] == 'َ') and ((input[b10] == 'ا') or (input[b10] == 'ى'))):

                        self.z.append('file ' + "'" + "library\\dha\\04-ض.wav" + "'")

                    elif (input[a10] == 'ُ' and input[b10] == 'و'):

                        self.z.append('file ' + "'" + "library\\dha\\05-ض.wav" + "'")

                    elif (input[a10] == 'ِ' and input[b10] == 'ي'):

                        self.z.append('file ' + "'" + "library\\dha\\06-ض.wav" + "'")

                    elif (input[a10] == 'ً'):

                        self.z.append('file ' + "'" + "library\\dha\\07-ض.wav" + "'")

                    elif (input[a10] == 'ٌ'):

                        self.z.append('file ' + "'" + "library\\dha\\08-ض.wav" + "'")

                    elif (input[a10] == 'ٍ'):

                        self.z.append('file ' + "'" + "library\\dha\\09-ض.wav" + "'")

                    elif (input[a10] == 'َ'):

                        self.z.append('file ' + "'" + "library\\dha\\01-ض.wav" + "'")

                    elif (input[a10] == 'ُ'):

                        self.z.append('file ' + "'" + "library\\dha\\02-ض.wav" + "'")

                    elif (input[a10] == 'ِ'):

                        self.z.append('file ' + "'" + "library\\dha\\03-ض.wav" + "'")

                    elif (input[a10] == 'ْ'):

                        self.z.append('file ' + "'" + "library\\dha\\signs.wav" + "'")

                    else:

                        self.z.append('file ' + "'" + "library\\dha\\signs.wav" + "'")








                else:

                    self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                a10 = 0

                b10 = 0

                d10 = 0

                c10 = 0

            elif (char == 'ذ'):

                a11 = i + 1

                b11 = i + 2

                c11 = i + 3

                d11 = i + 4

                if (a11 < (len(input))):

                    if (input[a11] == '\0'):

                        self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                    elif ((input[a11] == 'َ') and (input[b11] == 'د') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\tha\\20-ذ.wav' + "'")

                    elif ((input[a11] == 'َ') and (input[b11] == 'ج') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\17-ذ.wav" + "'")

                    elif ((input[a11] == 'َ') and (input[b11] == 'ح') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\18-ذ.wav" + "'")

                    elif ((input[a11] == 'َ') and (input[b11] == 'خ') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\19-ذ.wav" + "'")

                    elif ((input[a11] == 'َ') and (input[b11] == 'ه') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\36-ذ.wav" + "'")

                    elif ((input[a11] == 'َ') and (input[b11] == 'ع') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\28-ذ.wav" + "'")

                    elif ((input[a11] == 'َ') and (input[b11] == 'غ') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\29-ذ.wav" + "'")

                    elif ((input[a11] == 'َ') and (input[b11] == 'ف') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\30-ذ.wav" + "'")

                    elif ((input[a11] == 'َ') and (input[b11] == 'ق') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\31-ذ.wav" + "'")

                    elif ((input[a11] == 'َ') and (input[b11] == 'ث') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\16-ذ.wav" + "'")

                    elif ((input[a11] == 'َ') and (input[b11] == 'ص') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\25-ذ.wav" + "'")

                    elif ((input[a11] == 'َ') and (input[b11] == 'ض') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\26-ذ.wav" + "'")

                    elif ((input[a11] == 'َ') and (input[b11] == 'ذ') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\21-ذ.wav" + "'")

                    elif ((input[a11] == 'َ') and (input[b11] == 'ط') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\27-ذ.wav" + "'")

                    elif ((input[a11] == 'َ') and (input[b11] == 'ك') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\32-ذ.wav" + "'")

                    elif ((input[a11] == 'َ') and (input[b11] == 'م') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\34-ذ.wav" + "'")

                    elif ((input[a11] == 'َ') and (input[b11] == 'ن') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\35-ذ.wav" + "'")

                    elif ((input[a11] == 'َ') and (input[b11] == 'ت') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\15-ذ.wav" + "'")

                    elif ((input[a11] == 'َ') and (input[b11] == 'أ') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\13-ذ.wav" + "'")

                    elif ((input[a11] == 'َ') and (input[b11] == 'ل') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\33-ذ.wav" + "'")

                    elif ((input[a11] == 'َ') and (input[b11] == 'ب') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\14-ذ.wav" + "'")

                    elif ((input[a11] == 'َ') and (input[b11] == 'ي') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\37-ذ.wav" + "'")

                    elif ((input[a11] == 'َ') and (input[b11] == 'س') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\23-ذ.wav" + "'")

                    elif ((input[a11] == 'َ') and (input[b11] == 'ش') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\24-ذ.wav" + "'")

                    elif ((input[a11] == 'َ') and (input[b11] == 'ظ') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\26-ذ.wav" + "'")

                    elif ((input[a11] == 'َ') and (input[b11] == 'ز') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\z1.wav" + "'")

                    elif ((input[a11] == 'َ') and (input[b11] == 'و') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\signs.wav" + "'")

                    elif ((input[a11] == 'َ') and (input[b11] == 'ة') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\15-ذ.wav" + "'")

                    elif ((input[a11] == 'َ') and (input[b11] == 'ر') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\22-ذ.wav" + "'")

                    elif ((input[a11] == 'َ') and (input[b11] == 'ؤ') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\13-ذ.wav" + "'")

                    elif ((input[a11] == 'َ') and (input[b11] == 'ء') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\13-ذ.wav" + "'")

                    elif ((input[a11] == 'َ') and (input[b11] == 'ئ') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\13-ذ.wav" + "'")



                    elif ((input[a11] == 'ُ') and (input[b11] == 'د') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\45-ذ.wav" + "'")

                    elif ((input[a11] == 'ُ') and (input[b11] == 'ج') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\42-ذ.wav" + "'")

                    elif ((input[a11] == 'ُ') and (input[b11] == 'ح') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\43-ذ.wav" + "'")

                    elif ((input[a11] == 'ُ') and (input[b11] == 'خ') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\44-ذ.wav" + "'")

                    elif ((input[a11] == 'ُ') and (input[b11] == 'ه') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\61-ذ.wav" + "'")

                    elif ((input[a11] == 'ُ') and (input[b11] == 'ع') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\53-ذ.wav" + "'")

                    elif ((input[a11] == 'ُ') and (input[b11] == 'غ') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\54-ذ.wav" + "'")

                    elif ((input[a11] == 'ُ') and (input[b11] == 'ف') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\55-ذ.wav" + "'")

                    elif ((input[a11] == 'ُ') and (input[b11] == 'ق') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\56-ذ.wav" + "'")

                    elif ((input[a11] == 'ُ') and (input[b11] == 'ث') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\41-ذ.wav" + "'")

                    elif ((input[a11] == 'ُ') and (input[b11] == 'ص') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\50-ذ.wav" + "'")

                    elif ((input[a11] == 'ُ') and (input[b11] == 'ض') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\51-ذ.wav" + "'")

                    elif ((input[a11] == 'ُ') and (input[b11] == 'ذ') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\46-ذ.wav" + "'")

                    elif ((input[a11] == 'ُ') and (input[b11] == 'ط') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\52-ذ.wav" + "'")

                    elif ((input[a11] == 'ُ') and (input[b11] == 'ك') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\57-ذ.wav" + "'")

                    elif ((input[a11] == 'ُ') and (input[b11] == 'م') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\59-ذ.wav" + "'")

                    elif ((input[a11] == 'ُ') and (input[b11] == 'ن') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\60-ذ.wav" + "'")

                    elif ((input[a11] == 'ُ') and (input[b11] == 'ت') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\40-ذ.wav" + "'")

                    elif ((input[a11] == 'ُ') and (input[b11] == 'أ') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\38-ذ.wav" + "'")

                    elif ((input[a11] == 'ُ') and (input[b11] == 'ل') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\58-ذ.wav" + "'")

                    elif ((input[a11] == 'ُ') and (input[b11] == 'ب') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\39-ذ.wav" + "'")

                    elif ((input[a11] == 'ُ') and (input[b11] == 'ي') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\62-ذ.wav" + "'")

                    elif ((input[a11] == 'ُ') and (input[b11] == 'س') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\48-ذ.wav" + "'")

                    elif ((input[a11] == 'ُ') and (input[b11] == 'ش') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\49-ذ.wav" + "'")

                    elif ((input[a11] == 'ُ') and (input[b11] == 'ظ') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\51-ذ.wav" + "'")

                    elif ((input[a11] == 'ُ') and (input[b11] == 'ز') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\z2.wav" + "'")

                    elif ((input[a11] == 'ُ') and (input[b11] == 'و') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\signs.wav" + "'")

                    elif ((input[a11] == 'ُ') and (input[b11] == 'ة') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\40-ذ.wav" + "'")

                    elif ((input[a11] == 'ُ') and (input[b11] == 'ر') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\47-ذ.wav" + "'")

                    elif ((input[a11] == 'ُ') and (input[b11] == 'ؤ') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\38-ذ.wav" + "'")

                    elif ((input[a11] == 'ُ') and (input[b11] == 'ء') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\38-ذ.wav" + "'")

                    elif ((input[a11] == 'ُ') and (input[b11] == 'ئ') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\38-ذ.wav" + "'")




                    elif ((input[a11] == 'ِ') and (input[b11] == 'د') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\70-ذ.wav" + "'")

                    elif ((input[a11] == 'ِ') and (input[b11] == 'ج') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\67-ذ.wav" + "'")

                    elif ((input[a11] == 'ِ') and (input[b11] == 'ح') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\68-ذ.wav" + "'")

                    elif ((input[a11] == 'ِ') and (input[b11] == 'خ') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\69-ذ.wav" + "'")

                    elif ((input[a11] == 'ِ') and (input[b11] == 'ه') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\86-ذ.wav" + "'")

                    elif ((input[a11] == 'ِ') and (input[b11] == 'ع') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\78-ذ.wav" + "'")

                    elif ((input[a11] == 'ِ') and (input[b11] == 'غ') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\79-ذ.wav" + "'")

                    elif ((input[a11] == 'ِ') and (input[b11] == 'ف') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\80-ذ.wav" + "'")

                    elif ((input[a11] == 'ِ') and (input[b11] == 'ق') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\81-ذ.wav" + "'")

                    elif ((input[a11] == 'ِ') and (input[b11] == 'ث') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\66-ذ.wav" + "'")

                    elif ((input[a11] == 'ِ') and (input[b11] == 'ص') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\75-ذ.wav" + "'")

                    elif ((input[a11] == 'ِ') and (input[b11] == 'ض') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\76-ذ.wav" + "'")

                    elif ((input[a11] == 'ِ') and (input[b11] == 'ذ') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\71-ذ.wav" + "'")

                    elif ((input[a11] == 'ِ') and (input[b11] == 'ط') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\77-ذ.wav" + "'")

                    elif ((input[a11] == 'ِ') and (input[b11] == 'ك') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\82-ذ.wav" + "'")

                    elif ((input[a11] == 'ِ') and (input[b11] == 'م') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\84-ذ.wav" + "'")

                    elif ((input[a11] == 'ِ') and (input[b11] == 'ن') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\85-ذ.wav" + "'")

                    elif ((input[a11] == 'ِ') and (input[b11] == 'ت') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\65-ذ.wav" + "'")

                    elif ((input[a11] == 'ِ') and (input[b11] == 'أ') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\63-ذ.wav" + "'")

                    elif ((input[a11] == 'ِ') and (input[b11] == 'ل') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\83-ذ.wav" + "'")

                    elif ((input[a11] == 'ِ') and (input[b11] == 'ب') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\64-ذ.wav" + "'")

                    elif ((input[a11] == 'ِ') and (input[b11] == 'ي') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\87-ذ.wav" + "'")

                    elif ((input[a11] == 'ِ') and (input[b11] == 'س') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\73-ذ.wav" + "'")

                    elif ((input[a11] == 'ِ') and (input[b11] == 'ش') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\74-ذ.wav" + "'")

                    elif ((input[a11] == 'ِ') and (input[b11] == 'ظ') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\76-ذ.wav" + "'")

                    elif ((input[a11] == 'ِ') and (input[b11] == 'ز') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\z3.wav" + "'")

                    elif ((input[a11] == 'ِ') and (input[b11] == 'و') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\signs.wav" + "'")

                    elif ((input[a11] == 'ِ') and (input[b11] == 'ة') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\65-ذ.wav" + "'")

                    elif ((input[a11] == 'ِ') and (input[b11] == 'ر') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\72-ذ.wav" + "'")

                    elif ((input[a11] == 'ِ') and (input[b11] == 'ؤ') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\63-ذ.wav" + "'")

                    elif ((input[a11] == 'ِ') and (input[b11] == 'ء') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\63-ذ.wav" + "'")

                    elif ((input[a11] == 'ِ') and (input[b11] == 'ئ') and (input[c11] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\tha\\63-ذ.wav" + "'")






                    elif ((input[a11] == 'َ') and ((input[b11] == 'ا') or (input[b11] == 'ى'))):

                        self.z.append('file ' + "'" + "library\\tha\\04-ذ.wav" + "'")

                    elif (input[a11] == 'ُ' and input[b11] == 'و'):

                        self.z.append('file ' + "'" + "library\\tha\\05-ذ.wav" + "'")

                    elif (input[a11] == 'ِ' and input[b11] == 'ي'):

                        self.z.append('file ' + "'" + "library\\tha\\06-ذ.wav" + "'")

                    elif (input[a11] == 'ً'):

                        self.z.append('file ' + "'" + "library\\tha\\07-ذ.wav" + "'")

                    elif (input[a11] == 'ٌ'):

                        self.z.append('file ' + "'" + "library\\tha\\08-ذ.wav" + "'")

                    elif (input[a11] == 'ٍ'):

                        self.z.append('file ' + "'" + "library\\tha\\09-ذ.wav" + "'")

                    elif (input[a11] == 'َ'):

                        self.z.append('file ' + "'" + "library\\tha\\01-ذ.wav" + "'")

                    elif (input[a11] == 'ُ'):

                        self.z.append('file ' + "'" + "library\\tha\\02-ذ.wav" + "'")

                    elif (input[a11] == 'ِ'):

                        self.z.append('file ' + "'" + "library\\tha\\03-ذ.wav" + "'")

                    elif (input[a11] == 'ْ'):

                        self.z.append('file ' + "'" + "library\\tha\\signs.wav" + "'")

                    else:

                        self.z.append('file ' + "'" + "library\\tha\\signs.wav" + "'")








                else:

                    self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                a11 = 0

                b11 = 0

                d11 = 0

                c11 = 0

            elif (char == 'ط'):

                a12 = i + 1

                b12 = i + 2

                c12 = i + 3

                d12 = i + 4

                if (a12 < (len(input))):

                    if (input[a12] == '\0'):

                        self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                    elif ((input[a12] == 'َ') and (input[b12] == 'د') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\ta\\20-ط.wav' + "'")

                    elif ((input[a12] == 'َ') and (input[b12] == 'ج') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\17-ط.wav" + "'")

                    elif ((input[a12] == 'َ') and (input[b12] == 'ح') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\18-ط.wav" + "'")

                    elif ((input[a12] == 'َ') and (input[b12] == 'خ') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\19-ط.wav" + "'")

                    elif ((input[a12] == 'َ') and (input[b12] == 'ه') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\36-ط.wav" + "'")

                    elif ((input[a12] == 'َ') and (input[b12] == 'ع') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\28-ط.wav" + "'")

                    elif ((input[a12] == 'َ') and (input[b12] == 'غ') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\29-ط.wav" + "'")

                    elif ((input[a12] == 'َ') and (input[b12] == 'ف') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\30-ط.wav" + "'")

                    elif ((input[a12] == 'َ') and (input[b12] == 'ق') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\31-ط.wav" + "'")

                    elif ((input[a12] == 'َ') and (input[b12] == 'ث') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\16-ط.wav" + "'")

                    elif ((input[a12] == 'َ') and (input[b12] == 'ص') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\25-ط.wav" + "'")

                    elif ((input[a12] == 'َ') and (input[b12] == 'ض') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\26-ط.wav" + "'")

                    elif ((input[a12] == 'َ') and (input[b12] == 'ذ') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\21-ط.wav" + "'")

                    elif ((input[a12] == 'َ') and (input[b12] == 'ط') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\27-ط.wav" + "'")

                    elif ((input[a12] == 'َ') and (input[b12] == 'ك') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\32-ط.wav" + "'")

                    elif ((input[a12] == 'َ') and (input[b12] == 'م') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\34-ط.wav" + "'")

                    elif ((input[a12] == 'َ') and (input[b12] == 'ن') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\35-ط.wav" + "'")

                    elif ((input[a12] == 'َ') and (input[b12] == 'ت') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\15-ط.wav" + "'")

                    elif ((input[a12] == 'َ') and (input[b12] == 'أ') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\13-ط.wav" + "'")

                    elif ((input[a12] == 'َ') and (input[b12] == 'ل') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\33-ط.wav" + "'")

                    elif ((input[a12] == 'َ') and (input[b12] == 'ب') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\14-ط.wav" + "'")

                    elif ((input[a12] == 'َ') and (input[b12] == 'ي') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\37-ط.wav" + "'")

                    elif ((input[a12] == 'َ') and (input[b12] == 'س') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\23-ط.wav" + "'")

                    elif ((input[a12] == 'َ') and (input[b12] == 'ش') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\24-ط.wav" + "'")

                    elif ((input[a12] == 'َ') and (input[b12] == 'ظ') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\26-ط.wav" + "'")

                    elif ((input[a12] == 'َ') and (input[b12] == 'ز') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\z1.wav" + "'")

                    elif ((input[a12] == 'َ') and (input[b12] == 'و') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\signs.wav" + "'")

                    elif ((input[a12] == 'َ') and (input[b12] == 'ة') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\15-ط.wav" + "'")

                    elif ((input[a12] == 'َ') and (input[b12] == 'ر') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\22-ط.wav" + "'")

                    elif ((input[a12] == 'َ') and (input[b12] == 'ؤ') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\13-ط.wav" + "'")

                    elif ((input[a12] == 'َ') and (input[b12] == 'ء') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\13-ط.wav" + "'")

                    elif ((input[a12] == 'َ') and (input[b12] == 'ئ') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\13-ط.wav" + "'")



                    elif ((input[a12] == 'ُ') and (input[b12] == 'د') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\45-ط.wav" + "'")

                    elif ((input[a12] == 'ُ') and (input[b12] == 'ج') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\42-ط.wav" + "'")

                    elif ((input[a12] == 'ُ') and (input[b12] == 'ح') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\43-ط.wav" + "'")

                    elif ((input[a12] == 'ُ') and (input[b12] == 'خ') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\44-ط.wav" + "'")

                    elif ((input[a12] == 'ُ') and (input[b12] == 'ه') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\61-ط.wav" + "'")

                    elif ((input[a12] == 'ُ') and (input[b12] == 'ع') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\53-ط.wav" + "'")

                    elif ((input[a12] == 'ُ') and (input[b12] == 'غ') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\54-ط.wav" + "'")

                    elif ((input[a12] == 'ُ') and (input[b12] == 'ف') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\55-ط.wav" + "'")

                    elif ((input[a12] == 'ُ') and (input[b12] == 'ق') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\56-ط.wav" + "'")

                    elif ((input[a12] == 'ُ') and (input[b12] == 'ث') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\41-ط.wav" + "'")

                    elif ((input[a12] == 'ُ') and (input[b12] == 'ص') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\50-ط.wav" + "'")

                    elif ((input[a12] == 'ُ') and (input[b12] == 'ض') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\51-ط.wav" + "'")

                    elif ((input[a12] == 'ُ') and (input[b12] == 'ذ') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\46-ط.wav" + "'")

                    elif ((input[a12] == 'ُ') and (input[b12] == 'ط') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\52-ط.wav" + "'")

                    elif ((input[a12] == 'ُ') and (input[b12] == 'ك') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\57-ط.wav" + "'")

                    elif ((input[a12] == 'ُ') and (input[b12] == 'م') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\59-ط.wav" + "'")

                    elif ((input[a12] == 'ُ') and (input[b12] == 'ن') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\60-ط.wav" + "'")

                    elif ((input[a12] == 'ُ') and (input[b12] == 'ت') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\40-ط.wav" + "'")

                    elif ((input[a12] == 'ُ') and (input[b12] == 'أ') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\38-ط.wav" + "'")

                    elif ((input[a12] == 'ُ') and (input[b12] == 'ل') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\58-ط.wav" + "'")

                    elif ((input[a12] == 'ُ') and (input[b12] == 'ب') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\39-ط.wav" + "'")

                    elif ((input[a12] == 'ُ') and (input[b12] == 'ي') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\62-ط.wav" + "'")

                    elif ((input[a12] == 'ُ') and (input[b12] == 'س') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\48-ط.wav" + "'")

                    elif ((input[a12] == 'ُ') and (input[b12] == 'ش') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\49-ط.wav" + "'")

                    elif ((input[a12] == 'ُ') and (input[b12] == 'ظ') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\51-ط.wav" + "'")

                    elif ((input[a12] == 'ُ') and (input[b12] == 'ز') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\z2.wav" + "'")

                    elif ((input[a12] == 'ُ') and (input[b12] == 'و') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\signs.wav" + "'")

                    elif ((input[a12] == 'ُ') and (input[b12] == 'ة') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\40-ط.wav" + "'")

                    elif ((input[a12] == 'ُ') and (input[b12] == 'ر') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\47-ط.wav" + "'")

                    elif ((input[a12] == 'ُ') and (input[b12] == 'ؤ') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\38-ط.wav" + "'")

                    elif ((input[a12] == 'ُ') and (input[b12] == 'ء') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\38-ط.wav" + "'")

                    elif ((input[a12] == 'ُ') and (input[b12] == 'ئ') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\38-ط.wav" + "'")




                    elif ((input[a12] == 'ِ') and (input[b12] == 'د') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\70-ط.wav" + "'")

                    elif ((input[a12] == 'ِ') and (input[b12] == 'ج') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\67-ط.wav" + "'")

                    elif ((input[a12] == 'ِ') and (input[b12] == 'ح') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\68-ط.wav" + "'")

                    elif ((input[a12] == 'ِ') and (input[b12] == 'خ') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\69-ط.wav" + "'")

                    elif ((input[a12] == 'ِ') and (input[b12] == 'ه') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\86-ط.wav" + "'")

                    elif ((input[a12] == 'ِ') and (input[b12] == 'ع') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\78-ط.wav" + "'")

                    elif ((input[a12] == 'ِ') and (input[b12] == 'غ') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\79-ط.wav" + "'")

                    elif ((input[a12] == 'ِ') and (input[b12] == 'ف') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\80-ط.wav" + "'")

                    elif ((input[a12] == 'ِ') and (input[b12] == 'ق') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\81-ط.wav" + "'")

                    elif ((input[a12] == 'ِ') and (input[b12] == 'ث') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\66-ط.wav" + "'")

                    elif ((input[a12] == 'ِ') and (input[b12] == 'ص') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\75-ط.wav" + "'")

                    elif ((input[a12] == 'ِ') and (input[b12] == 'ض') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\76-ط.wav" + "'")

                    elif ((input[a12] == 'ِ') and (input[b12] == 'ذ') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\71-ط.wav" + "'")

                    elif ((input[a12] == 'ِ') and (input[b12] == 'ط') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\77-ط.wav" + "'")

                    elif ((input[a12] == 'ِ') and (input[b12] == 'ك') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\82-ط.wav" + "'")

                    elif ((input[a12] == 'ِ') and (input[b12] == 'م') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\84-ط.wav" + "'")

                    elif ((input[a12] == 'ِ') and (input[b12] == 'ن') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\85-ط.wav" + "'")

                    elif ((input[a12] == 'ِ') and (input[b12] == 'ت') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\65-ط.wav" + "'")

                    elif ((input[a12] == 'ِ') and (input[b12] == 'أ') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\63-ط.wav" + "'")

                    elif ((input[a12] == 'ِ') and (input[b12] == 'ل') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\83-ط.wav" + "'")

                    elif ((input[a12] == 'ِ') and (input[b12] == 'ب') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\64-ط.wav" + "'")

                    elif ((input[a12] == 'ِ') and (input[b12] == 'ي') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\87-ط.wav" + "'")

                    elif ((input[a12] == 'ِ') and (input[b12] == 'س') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\73-ط.wav" + "'")

                    elif ((input[a12] == 'ِ') and (input[b12] == 'ش') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\74-ط.wav" + "'")

                    elif ((input[a12] == 'ِ') and (input[b12] == 'ظ') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\76-ط.wav" + "'")

                    elif ((input[a12] == 'ِ') and (input[b12] == 'ز') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\z3.wav" + "'")

                    elif ((input[a12] == 'ِ') and (input[b12] == 'و') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\signs.wav" + "'")

                    elif ((input[a12] == 'ِ') and (input[b12] == 'ة') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\65-ط.wav" + "'")

                    elif ((input[a12] == 'ِ') and (input[b12] == 'ر') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\72-ط.wav" + "'")

                    elif ((input[a12] == 'ِ') and (input[b12] == 'ؤ') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\63-ط.wav" + "'")

                    elif ((input[a12] == 'ِ') and (input[b12] == 'ء') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\63-ط.wav" + "'")

                    elif ((input[a12] == 'ِ') and (input[b12] == 'ئ') and (input[c12] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ta\\63-ط.wav" + "'")






                    elif ((input[a12] == 'َ') and ((input[b12] == 'ا') or (input[b12] == 'ى'))):

                        self.z.append('file ' + "'" + "library\\ta\\04-ط.wav" + "'")

                    elif (input[a12] == 'ُ' and input[b12] == 'و'):

                        self.z.append('file ' + "'" + "library\\ta\\05-ط.wav" + "'")

                    elif (input[a12] == 'ِ' and input[b12] == 'ي'):

                        self.z.append('file ' + "'" + "library\\ta\\06-ط.wav" + "'")

                    elif (input[a12] == 'ً'):

                        self.z.append('file ' + "'" + "library\\ta\\07-ط.wav" + "'")

                    elif (input[a12] == 'ٌ'):

                        self.z.append('file ' + "'" + "library\\ta\\08-ط.wav" + "'")

                    elif (input[a12] == 'ٍ'):

                        self.z.append('file ' + "'" + "library\\ta\\09-ط.wav" + "'")

                    elif (input[a12] == 'َ'):

                        self.z.append('file ' + "'" + "library\\ta\\01-ط.wav" + "'")

                    elif (input[a12] == 'ُ'):

                        self.z.append('file ' + "'" + "library\\ta\\02-ط.wav" + "'")

                    elif (input[a12] == 'ِ'):

                        self.z.append('file ' + "'" + "library\\ta\\03-ط.wav" + "'")

                    elif (input[a12] == 'ْ'):

                        self.z.append('file ' + "'" + "library\\ta\\signs.wav" + "'")

                    else:

                        self.z.append('file ' + "'" + "library\\ta\\signs.wav" + "'")








                else:

                    self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                a12 = 0

                b12 = 0

                d12 = 0

                c12 = 0

            elif (char == 'ك'):

                a13 = i + 1

                b13 = i + 2

                c13 = i + 3

                d13 = i + 4

                if (a13 < (len(input))):

                    if (input[a13] == '\0'):

                        self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                    elif ((input[a13] == 'َ') and (input[b13] == 'د') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\k\\20-ك.wav' + "'")

                    elif ((input[a13] == 'َ') and (input[b13] == 'ج') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\17-ك.wav" + "'")

                    elif ((input[a13] == 'َ') and (input[b13] == 'ح') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\18-ك.wav" + "'")

                    elif ((input[a13] == 'َ') and (input[b13] == 'خ') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\19-ك.wav" + "'")

                    elif ((input[a13] == 'َ') and (input[b13] == 'ه') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\36-ك.wav" + "'")

                    elif ((input[a13] == 'َ') and (input[b13] == 'ع') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\28-ك.wav" + "'")

                    elif ((input[a13] == 'َ') and (input[b13] == 'غ') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\29-ك.wav" + "'")

                    elif ((input[a13] == 'َ') and (input[b13] == 'ف') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\30-ك.wav" + "'")

                    elif ((input[a13] == 'َ') and (input[b13] == 'ق') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\31-ك.wav" + "'")

                    elif ((input[a13] == 'َ') and (input[b13] == 'ث') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\16-ك.wav" + "'")

                    elif ((input[a13] == 'َ') and (input[b13] == 'ص') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\25-ك.wav" + "'")

                    elif ((input[a13] == 'َ') and (input[b13] == 'ض') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\26-ك.wav" + "'")

                    elif ((input[a13] == 'َ') and (input[b13] == 'ذ') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\21-ك.wav" + "'")

                    elif ((input[a13] == 'َ') and (input[b13] == 'ط') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\27-ك.wav" + "'")

                    elif ((input[a13] == 'َ') and (input[b13] == 'ك') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\32-ك.wav" + "'")

                    elif ((input[a13] == 'َ') and (input[b13] == 'م') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\34-ك.wav" + "'")

                    elif ((input[a13] == 'َ') and (input[b13] == 'ن') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\35-ك.wav" + "'")

                    elif ((input[a13] == 'َ') and (input[b13] == 'ت') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\15-ك.wav" + "'")

                    elif ((input[a13] == 'َ') and (input[b13] == 'أ') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\13-ك.wav" + "'")

                    elif ((input[a13] == 'َ') and (input[b13] == 'ل') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\33-ك.wav" + "'")

                    elif ((input[a13] == 'َ') and (input[b13] == 'ب') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\14-ك.wav" + "'")

                    elif ((input[a13] == 'َ') and (input[b13] == 'ي') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\37-ك.wav" + "'")

                    elif ((input[a13] == 'َ') and (input[b13] == 'س') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\23-ك.wav" + "'")

                    elif ((input[a13] == 'َ') and (input[b13] == 'ش') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\24-ك.wav" + "'")

                    elif ((input[a13] == 'َ') and (input[b13] == 'ظ') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\26-ك.wav" + "'")

                    elif ((input[a13] == 'َ') and (input[b13] == 'ز') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\z1.wav" + "'")

                    elif ((input[a13] == 'َ') and (input[b13] == 'و') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\signs.wav" + "'")

                    elif ((input[a13] == 'َ') and (input[b13] == 'ة') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\15-ك.wav" + "'")

                    elif ((input[a13] == 'َ') and (input[b13] == 'ر') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\22-ك.wav" + "'")

                    elif ((input[a13] == 'َ') and (input[b13] == 'ؤ') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\13-ك.wav" + "'")

                    elif ((input[a13] == 'َ') and (input[b13] == 'ء') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\13-ك.wav" + "'")

                    elif ((input[a13] == 'َ') and (input[b13] == 'ئ') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\13-ك.wav" + "'")



                    elif ((input[a13] == 'ُ') and (input[b13] == 'د') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\45-ك.wav" + "'")

                    elif ((input[a13] == 'ُ') and (input[b13] == 'ج') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\42-ك.wav" + "'")

                    elif ((input[a13] == 'ُ') and (input[b13] == 'ح') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\43-ك.wav" + "'")

                    elif ((input[a13] == 'ُ') and (input[b13] == 'خ') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\44-ك.wav" + "'")

                    elif ((input[a13] == 'ُ') and (input[b13] == 'ه') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\61-ك.wav" + "'")

                    elif ((input[a13] == 'ُ') and (input[b13] == 'ع') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\53-ك.wav" + "'")

                    elif ((input[a13] == 'ُ') and (input[b13] == 'غ') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\54-ك.wav" + "'")

                    elif ((input[a13] == 'ُ') and (input[b13] == 'ف') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\55-ك.wav" + "'")

                    elif ((input[a13] == 'ُ') and (input[b13] == 'ق') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\56-ك.wav" + "'")

                    elif ((input[a13] == 'ُ') and (input[b13] == 'ث') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\41-ك.wav" + "'")

                    elif ((input[a13] == 'ُ') and (input[b13] == 'ص') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\50-ك.wav" + "'")

                    elif ((input[a13] == 'ُ') and (input[b13] == 'ض') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\51-ك.wav" + "'")

                    elif ((input[a13] == 'ُ') and (input[b13] == 'ذ') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\46-ك.wav" + "'")

                    elif ((input[a13] == 'ُ') and (input[b13] == 'ط') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\52-ك.wav" + "'")

                    elif ((input[a13] == 'ُ') and (input[b13] == 'ك') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\57-ك.wav" + "'")

                    elif ((input[a13] == 'ُ') and (input[b13] == 'م') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\59-ك.wav" + "'")

                    elif ((input[a13] == 'ُ') and (input[b13] == 'ن') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\60-ك.wav" + "'")

                    elif ((input[a13] == 'ُ') and (input[b13] == 'ت') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\40-ك.wav" + "'")

                    elif ((input[a13] == 'ُ') and (input[b13] == 'أ') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\38-ك.wav" + "'")

                    elif ((input[a13] == 'ُ') and (input[b13] == 'ل') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\58-ك.wav" + "'")

                    elif ((input[a13] == 'ُ') and (input[b13] == 'ب') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\39-ك.wav" + "'")

                    elif ((input[a13] == 'ُ') and (input[b13] == 'ي') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\62-ك.wav" + "'")

                    elif ((input[a13] == 'ُ') and (input[b13] == 'س') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\48-ك.wav" + "'")

                    elif ((input[a13] == 'ُ') and (input[b13] == 'ش') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\49-ك.wav" + "'")

                    elif ((input[a13] == 'ُ') and (input[b13] == 'ظ') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\51-ك.wav" + "'")

                    elif ((input[a13] == 'ُ') and (input[b13] == 'ز') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\z2.wav" + "'")

                    elif ((input[a13] == 'ُ') and (input[b13] == 'و') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\signs.wav" + "'")

                    elif ((input[a13] == 'ُ') and (input[b13] == 'ة') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\40-ك.wav" + "'")

                    elif ((input[a13] == 'ُ') and (input[b13] == 'ر') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\47-ك.wav" + "'")

                    elif ((input[a13] == 'ُ') and (input[b13] == 'ؤ') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\38-ك.wav" + "'")

                    elif ((input[a13] == 'ُ') and (input[b13] == 'ء') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\38-ك.wav" + "'")

                    elif ((input[a13] == 'ُ') and (input[b13] == 'ئ') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\38-ك.wav" + "'")




                    elif ((input[a13] == 'ِ') and (input[b13] == 'د') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\70-ك.wav" + "'")

                    elif ((input[a13] == 'ِ') and (input[b13] == 'ج') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\67-ك.wav" + "'")

                    elif ((input[a13] == 'ِ') and (input[b13] == 'ح') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\68-ك.wav" + "'")

                    elif ((input[a13] == 'ِ') and (input[b13] == 'خ') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\69-ك.wav" + "'")

                    elif ((input[a13] == 'ِ') and (input[b13] == 'ه') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\86-ك.wav" + "'")

                    elif ((input[a13] == 'ِ') and (input[b13] == 'ع') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\78-ك.wav" + "'")

                    elif ((input[a13] == 'ِ') and (input[b13] == 'غ') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\79-ك.wav" + "'")

                    elif ((input[a13] == 'ِ') and (input[b13] == 'ف') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\80-ك.wav" + "'")

                    elif ((input[a13] == 'ِ') and (input[b13] == 'ق') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\81-ك.wav" + "'")

                    elif ((input[a13] == 'ِ') and (input[b13] == 'ث') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\66-ك.wav" + "'")

                    elif ((input[a13] == 'ِ') and (input[b13] == 'ص') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\75-ك.wav" + "'")

                    elif ((input[a13] == 'ِ') and (input[b13] == 'ض') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\76-ك.wav" + "'")

                    elif ((input[a13] == 'ِ') and (input[b13] == 'ذ') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\71-ك.wav" + "'")

                    elif ((input[a13] == 'ِ') and (input[b13] == 'ط') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\77-ك.wav" + "'")

                    elif ((input[a13] == 'ِ') and (input[b13] == 'ك') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\82-ك.wav" + "'")

                    elif ((input[a13] == 'ِ') and (input[b13] == 'م') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\84-ك.wav" + "'")

                    elif ((input[a13] == 'ِ') and (input[b13] == 'ن') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\85-ك.wav" + "'")

                    elif ((input[a13] == 'ِ') and (input[b13] == 'ت') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\65-ك.wav" + "'")

                    elif ((input[a13] == 'ِ') and (input[b13] == 'أ') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\63-ك.wav" + "'")

                    elif ((input[a13] == 'ِ') and (input[b13] == 'ل') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\83-ك.wav" + "'")

                    elif ((input[a13] == 'ِ') and (input[b13] == 'ب') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\64-ك.wav" + "'")

                    elif ((input[a13] == 'ِ') and (input[b13] == 'ي') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\87-ك.wav" + "'")

                    elif ((input[a13] == 'ِ') and (input[b13] == 'س') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\73-ك.wav" + "'")

                    elif ((input[a13] == 'ِ') and (input[b13] == 'ش') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\74-ك.wav" + "'")

                    elif ((input[a13] == 'ِ') and (input[b13] == 'ظ') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\76-ك.wav" + "'")

                    elif ((input[a13] == 'ِ') and (input[b13] == 'ز') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\z3.wav" + "'")

                    elif ((input[a13] == 'ِ') and (input[b13] == 'و') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\signs.wav" + "'")

                    elif ((input[a13] == 'ِ') and (input[b13] == 'ة') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\65-ك.wav" + "'")

                    elif ((input[a13] == 'ِ') and (input[b13] == 'ر') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\72-ك.wav" + "'")

                    elif ((input[a13] == 'ِ') and (input[b13] == 'ؤ') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\63-ك.wav" + "'")

                    elif ((input[a13] == 'ِ') and (input[b13] == 'ء') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\63-ك.wav" + "'")

                    elif ((input[a13] == 'ِ') and (input[b13] == 'ئ') and (input[c13] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\k\\63-ك.wav" + "'")






                    elif ((input[a13] == 'َ') and ((input[b13] == 'ا') or (input[b13] == 'ى'))):

                        self.z.append('file ' + "'" + "library\\k\\04-ك.wav" + "'")

                    elif (input[a13] == 'ُ' and input[b13] == 'و'):

                        self.z.append('file ' + "'" + "library\\k\\05-ك.wav" + "'")

                    elif (input[a13] == 'ِ' and input[b13] == 'ي'):

                        self.z.append('file ' + "'" + "library\\k\\06-ك.wav" + "'")

                    elif (input[a13] == 'ً'):

                        self.z.append('file ' + "'" + "library\\k\\07-ك.wav" + "'")

                    elif (input[a13] == 'ٌ'):

                        self.z.append('file ' + "'" + "library\\k\\08-ك.wav" + "'")

                    elif (input[a13] == 'ٍ'):

                        self.z.append('file ' + "'" + "library\\k\\09-ك.wav" + "'")

                    elif (input[a13] == 'َ'):

                        self.z.append('file ' + "'" + "library\\k\\01-ك.wav" + "'")

                    elif (input[a13] == 'ُ'):

                        self.z.append('file ' + "'" + "library\\k\\02-ك.wav" + "'")

                    elif (input[a13] == 'ِ'):

                        self.z.append('file ' + "'" + "library\\k\\03-ك.wav" + "'")

                    elif (input[a13] == 'ْ'):

                        self.z.append('file ' + "'" + "library\\k\\signs.wav" + "'")

                    else:

                        self.z.append('file ' + "'" + "library\\k\\signs.wav" + "'")








                else:

                    self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                a13 = 0

                b13 = 0

                d13 = 0

                c13 = 0

            elif (char == 'م'):

                a14 = i + 1

                b14 = i + 2

                c14 = i + 3

                d14 = i + 4

                if (a14 < (len(input))):

                    if (input[a14] == '\0'):

                        self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                    elif ((input[a14] == 'َ') and (input[b14] == 'د') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\m\\20-م.wav' + "'")

                    elif ((input[a14] == 'َ') and (input[b14] == 'ج') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\17-م.wav" + "'")

                    elif ((input[a14] == 'َ') and (input[b14] == 'ح') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\18-م.wav" + "'")

                    elif ((input[a14] == 'َ') and (input[b14] == 'خ') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\19-م.wav" + "'")

                    elif ((input[a14] == 'َ') and (input[b14] == 'ه') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\36-م.wav" + "'")

                    elif ((input[a14] == 'َ') and (input[b14] == 'ع') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\28-م.wav" + "'")

                    elif ((input[a14] == 'َ') and (input[b14] == 'غ') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\29-م.wav" + "'")

                    elif ((input[a14] == 'َ') and (input[b14] == 'ف') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\30-م.wav" + "'")

                    elif ((input[a14] == 'َ') and (input[b14] == 'ق') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\31-م.wav" + "'")

                    elif ((input[a14] == 'َ') and (input[b14] == 'ث') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\16-م.wav" + "'")

                    elif ((input[a14] == 'َ') and (input[b14] == 'ص') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\25-م.wav" + "'")

                    elif ((input[a14] == 'َ') and (input[b14] == 'ض') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\26-م.wav" + "'")

                    elif ((input[a14] == 'َ') and (input[b14] == 'ذ') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\21-م.wav" + "'")

                    elif ((input[a14] == 'َ') and (input[b14] == 'ط') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\27-م.wav" + "'")

                    elif ((input[a14] == 'َ') and (input[b14] == 'ك') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\32-م.wav" + "'")

                    elif ((input[a14] == 'َ') and (input[b14] == 'م') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\34-م.wav" + "'")

                    elif ((input[a14] == 'َ') and (input[b14] == 'ن') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\35-م.wav" + "'")

                    elif ((input[a14] == 'َ') and (input[b14] == 'ت') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\15-م.wav" + "'")

                    elif ((input[a14] == 'َ') and (input[b14] == 'أ') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\13-م.wav" + "'")

                    elif ((input[a14] == 'َ') and (input[b14] == 'ل') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\33-م.wav" + "'")

                    elif ((input[a14] == 'َ') and (input[b14] == 'ب') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\14-م.wav" + "'")

                    elif ((input[a14] == 'َ') and (input[b14] == 'ي') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\37-م.wav" + "'")

                    elif ((input[a14] == 'َ') and (input[b14] == 'س') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\23-م.wav" + "'")

                    elif ((input[a14] == 'َ') and (input[b14] == 'ش') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\24-م.wav" + "'")

                    elif ((input[a14] == 'َ') and (input[b14] == 'ظ') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\26-م.wav" + "'")

                    elif ((input[a14] == 'َ') and (input[b14] == 'ز') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\z1.wav" + "'")

                    elif ((input[a14] == 'َ') and (input[b14] == 'و') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\signs.wav" + "'")

                    elif ((input[a14] == 'َ') and (input[b14] == 'ة') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\15-م.wav" + "'")

                    elif ((input[a14] == 'َ') and (input[b14] == 'ر') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\22-م.wav" + "'")

                    elif ((input[a14] == 'َ') and (input[b14] == 'ؤ') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\13-م.wav" + "'")

                    elif ((input[a14] == 'َ') and (input[b14] == 'ء') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\13-م.wav" + "'")

                    elif ((input[a14] == 'َ') and (input[b14] == 'ئ') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\13-م.wav" + "'")



                    elif ((input[a14] == 'ُ') and (input[b14] == 'د') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\45-م.wav" + "'")

                    elif ((input[a14] == 'ُ') and (input[b14] == 'ج') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\42-م.wav" + "'")

                    elif ((input[a14] == 'ُ') and (input[b14] == 'ح') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\43-م.wav" + "'")

                    elif ((input[a14] == 'ُ') and (input[b14] == 'خ') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\44-م.wav" + "'")

                    elif ((input[a14] == 'ُ') and (input[b14] == 'ه') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\61-م.wav" + "'")

                    elif ((input[a14] == 'ُ') and (input[b14] == 'ع') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\53-م.wav" + "'")

                    elif ((input[a14] == 'ُ') and (input[b14] == 'غ') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\54-م.wav" + "'")

                    elif ((input[a14] == 'ُ') and (input[b14] == 'ف') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\55-م.wav" + "'")

                    elif ((input[a14] == 'ُ') and (input[b14] == 'ق') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\56-م.wav" + "'")

                    elif ((input[a14] == 'ُ') and (input[b14] == 'ث') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\41-م.wav" + "'")

                    elif ((input[a14] == 'ُ') and (input[b14] == 'ص') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\50-م.wav" + "'")

                    elif ((input[a14] == 'ُ') and (input[b14] == 'ض') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\51-م.wav" + "'")

                    elif ((input[a14] == 'ُ') and (input[b14] == 'ذ') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\46-م.wav" + "'")

                    elif ((input[a14] == 'ُ') and (input[b14] == 'ط') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\52-م.wav" + "'")

                    elif ((input[a14] == 'ُ') and (input[b14] == 'ك') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\57-م.wav" + "'")

                    elif ((input[a14] == 'ُ') and (input[b14] == 'م') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\59-م.wav" + "'")

                    elif ((input[a14] == 'ُ') and (input[b14] == 'ن') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\60-م.wav" + "'")

                    elif ((input[a14] == 'ُ') and (input[b14] == 'ت') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\40-م.wav" + "'")

                    elif ((input[a14] == 'ُ') and (input[b14] == 'أ') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\38-م.wav" + "'")

                    elif ((input[a14] == 'ُ') and (input[b14] == 'ل') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\58-م.wav" + "'")

                    elif ((input[a14] == 'ُ') and (input[b14] == 'ب') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\39-م.wav" + "'")

                    elif ((input[a14] == 'ُ') and (input[b14] == 'ي') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\62-م.wav" + "'")

                    elif ((input[a14] == 'ُ') and (input[b14] == 'س') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\48-م.wav" + "'")

                    elif ((input[a14] == 'ُ') and (input[b14] == 'ش') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\49-م.wav" + "'")

                    elif ((input[a14] == 'ُ') and (input[b14] == 'ظ') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\51-م.wav" + "'")

                    elif ((input[a14] == 'ُ') and (input[b14] == 'ز') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\z2.wav" + "'")

                    elif ((input[a14] == 'ُ') and (input[b14] == 'و') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\signs.wav" + "'")

                    elif ((input[a14] == 'ُ') and (input[b14] == 'ة') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\40-م.wav" + "'")

                    elif ((input[a14] == 'ُ') and (input[b14] == 'ر') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\47-م.wav" + "'")

                    elif ((input[a14] == 'ُ') and (input[b14] == 'ؤ') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\38-م.wav" + "'")

                    elif ((input[a14] == 'ُ') and (input[b14] == 'ء') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\38-م.wav" + "'")

                    elif ((input[a14] == 'ُ') and (input[b14] == 'ئ') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\38-م.wav" + "'")




                    elif ((input[a14] == 'ِ') and (input[b14] == 'د') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\70-م.wav" + "'")

                    elif ((input[a14] == 'ِ') and (input[b14] == 'ج') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\67-م.wav" + "'")

                    elif ((input[a14] == 'ِ') and (input[b14] == 'ح') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\68-م.wav" + "'")

                    elif ((input[a14] == 'ِ') and (input[b14] == 'خ') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\69-م.wav" + "'")

                    elif ((input[a14] == 'ِ') and (input[b14] == 'ه') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\86-م.wav" + "'")

                    elif ((input[a14] == 'ِ') and (input[b14] == 'ع') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\78-م.wav" + "'")

                    elif ((input[a14] == 'ِ') and (input[b14] == 'غ') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\79-م.wav" + "'")

                    elif ((input[a14] == 'ِ') and (input[b14] == 'ف') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\80-م.wav" + "'")

                    elif ((input[a14] == 'ِ') and (input[b14] == 'ق') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\81-م.wav" + "'")

                    elif ((input[a14] == 'ِ') and (input[b14] == 'ث') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\66-م.wav" + "'")

                    elif ((input[a14] == 'ِ') and (input[b14] == 'ص') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\75-م.wav" + "'")

                    elif ((input[a14] == 'ِ') and (input[b14] == 'ض') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\76-م.wav" + "'")

                    elif ((input[a14] == 'ِ') and (input[b14] == 'ذ') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\71-م.wav" + "'")

                    elif ((input[a14] == 'ِ') and (input[b14] == 'ط') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\77-م.wav" + "'")

                    elif ((input[a14] == 'ِ') and (input[b14] == 'ك') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\82-م.wav" + "'")

                    elif ((input[a14] == 'ِ') and (input[b14] == 'م') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\84-م.wav" + "'")

                    elif ((input[a14] == 'ِ') and (input[b14] == 'ن') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\85-م.wav" + "'")

                    elif ((input[a14] == 'ِ') and (input[b14] == 'ت') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\65-م.wav" + "'")

                    elif ((input[a14] == 'ِ') and (input[b14] == 'أ') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\63-م.wav" + "'")

                    elif ((input[a14] == 'ِ') and (input[b14] == 'ل') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\83-م.wav" + "'")

                    elif ((input[a14] == 'ِ') and (input[b14] == 'ب') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\64-م.wav" + "'")

                    elif ((input[a14] == 'ِ') and (input[b14] == 'ي') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\87-م.wav" + "'")

                    elif ((input[a14] == 'ِ') and (input[b14] == 'س') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\73-م.wav" + "'")

                    elif ((input[a14] == 'ِ') and (input[b14] == 'ش') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\74-م.wav" + "'")

                    elif ((input[a14] == 'ِ') and (input[b14] == 'ظ') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\76-م.wav" + "'")

                    elif ((input[a14] == 'ِ') and (input[b14] == 'ز') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\z3.wav" + "'")

                    elif ((input[a14] == 'ِ') and (input[b14] == 'و') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\signs.wav" + "'")

                    elif ((input[a14] == 'ِ') and (input[b14] == 'ة') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\65-م.wav" + "'")

                    elif ((input[a14] == 'ِ') and (input[b14] == 'ر') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\72-م.wav" + "'")

                    elif ((input[a14] == 'ِ') and (input[b14] == 'ؤ') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\63-م.wav" + "'")

                    elif ((input[a14] == 'ِ') and (input[b14] == 'ء') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\63-م.wav" + "'")

                    elif ((input[a14] == 'ِ') and (input[b14] == 'ئ') and (input[c14] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\m\\63-م.wav" + "'")






                    elif ((input[a14] == 'َ') and ((input[b14] == 'ا') or (input[b14] == 'ى'))):

                        self.z.append('file ' + "'" + "library\\m\\04-م.wav" + "'")

                    elif (input[a14] == 'ُ' and input[b14] == 'و'):

                        self.z.append('file ' + "'" + "library\\m\\05-م.wav" + "'")

                    elif (input[a14] == 'ِ' and input[b14] == 'ي'):

                        self.z.append('file ' + "'" + "library\\m\\06-م.wav" + "'")

                    elif (input[a14] == 'ً'):

                        self.z.append('file ' + "'" + "library\\m\\07-م.wav" + "'")

                    elif (input[a14] == 'ٌ'):

                        self.z.append('file ' + "'" + "library\\m\\08-م.wav" + "'")

                    elif (input[a14] == 'ٍ'):

                        self.z.append('file ' + "'" + "library\\m\\09-م.wav" + "'")

                    elif (input[a14] == 'َ'):

                        self.z.append('file ' + "'" + "library\\m\\01-م.wav" + "'")

                    elif (input[a14] == 'ُ'):

                        self.z.append('file ' + "'" + "library\\m\\02-م.wav" + "'")

                    elif (input[a14] == 'ِ'):

                        self.z.append('file ' + "'" + "library\\m\\03-م.wav" + "'")

                    elif (input[a14] == 'ْ'):

                        self.z.append('file ' + "'" + "library\\m\\signs.wav" + "'")

                    else:

                        self.z.append('file ' + "'" + "library\\m\\signs.wav" + "'")








                else:

                    self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                a14 = 0

                b14 = 0

                d14 = 0

                c14 = 0

            elif (char == 'ن'):

                a15 = i + 1

                b15 = i + 2

                c15 = i + 3

                d15 = i + 4

                if (a15 < (len(input))):

                    if (input[a15] == '\0'):

                        self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                    elif ((input[a15] == 'َ') and (input[b15] == 'د') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\n\\20-ن.wav' + "'")

                    elif ((input[a15] == 'َ') and (input[b15] == 'ج') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\17-ن.wav" + "'")

                    elif ((input[a15] == 'َ') and (input[b15] == 'ح') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\18-ن.wav" + "'")

                    elif ((input[a15] == 'َ') and (input[b15] == 'خ') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\19-ن.wav" + "'")

                    elif ((input[a15] == 'َ') and (input[b15] == 'ه') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\36-ن.wav" + "'")

                    elif ((input[a15] == 'َ') and (input[b15] == 'ع') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\28-ن.wav" + "'")

                    elif ((input[a15] == 'َ') and (input[b15] == 'غ') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\29-ن.wav" + "'")

                    elif ((input[a15] == 'َ') and (input[b15] == 'ف') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\30-ن.wav" + "'")

                    elif ((input[a15] == 'َ') and (input[b15] == 'ق') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\31-ن.wav" + "'")

                    elif ((input[a15] == 'َ') and (input[b15] == 'ث') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\16-ن.wav" + "'")

                    elif ((input[a15] == 'َ') and (input[b15] == 'ص') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\25-ن.wav" + "'")

                    elif ((input[a15] == 'َ') and (input[b15] == 'ض') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\26-ن.wav" + "'")

                    elif ((input[a15] == 'َ') and (input[b15] == 'ذ') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\21-ن.wav" + "'")

                    elif ((input[a15] == 'َ') and (input[b15] == 'ط') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\27-ن.wav" + "'")

                    elif ((input[a15] == 'َ') and (input[b15] == 'ك') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\32-ن.wav" + "'")

                    elif ((input[a15] == 'َ') and (input[b15] == 'م') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\34-ن.wav" + "'")

                    elif ((input[a15] == 'َ') and (input[b15] == 'ن') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\35-ن.wav" + "'")

                    elif ((input[a15] == 'َ') and (input[b15] == 'ت') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\15-ن.wav" + "'")

                    elif ((input[a15] == 'َ') and (input[b15] == 'أ') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\13-ن.wav" + "'")

                    elif ((input[a15] == 'َ') and (input[b15] == 'ل') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\33-ن.wav" + "'")

                    elif ((input[a15] == 'َ') and (input[b15] == 'ب') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\14-ن.wav" + "'")

                    elif ((input[a15] == 'َ') and (input[b15] == 'ي') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\37-ن.wav" + "'")

                    elif ((input[a15] == 'َ') and (input[b15] == 'س') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\23-ن.wav" + "'")

                    elif ((input[a15] == 'َ') and (input[b15] == 'ش') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\24-ن.wav" + "'")

                    elif ((input[a15] == 'َ') and (input[b15] == 'ظ') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\26-ن.wav" + "'")

                    elif ((input[a15] == 'َ') and (input[b15] == 'ز') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\z1.wav" + "'")

                    elif ((input[a15] == 'َ') and (input[b15] == 'و') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\signs.wav" + "'")

                    elif ((input[a15] == 'َ') and (input[b15] == 'ة') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\15-ن.wav" + "'")

                    elif ((input[a15] == 'َ') and (input[b15] == 'ر') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\22-ن.wav" + "'")

                    elif ((input[a15] == 'َ') and (input[b15] == 'ؤ') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\13-ن.wav" + "'")

                    elif ((input[a15] == 'َ') and (input[b15] == 'ء') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\13-ن.wav" + "'")

                    elif ((input[a15] == 'َ') and (input[b15] == 'ئ') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\13-ن.wav" + "'")



                    elif ((input[a15] == 'ُ') and (input[b15] == 'د') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\45-ن.wav" + "'")

                    elif ((input[a15] == 'ُ') and (input[b15] == 'ج') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\42-ن.wav" + "'")

                    elif ((input[a15] == 'ُ') and (input[b15] == 'ح') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\43-ن.wav" + "'")

                    elif ((input[a15] == 'ُ') and (input[b15] == 'خ') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\44-ن.wav" + "'")

                    elif ((input[a15] == 'ُ') and (input[b15] == 'ه') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\61-ن.wav" + "'")

                    elif ((input[a15] == 'ُ') and (input[b15] == 'ع') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\53-ن.wav" + "'")

                    elif ((input[a15] == 'ُ') and (input[b15] == 'غ') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\54-ن.wav" + "'")

                    elif ((input[a15] == 'ُ') and (input[b15] == 'ف') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\55-ن.wav" + "'")

                    elif ((input[a15] == 'ُ') and (input[b15] == 'ق') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\56-ن.wav" + "'")

                    elif ((input[a15] == 'ُ') and (input[b15] == 'ث') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\41-ن.wav" + "'")

                    elif ((input[a15] == 'ُ') and (input[b15] == 'ص') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\50-ن.wav" + "'")

                    elif ((input[a15] == 'ُ') and (input[b15] == 'ض') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\51-ن.wav" + "'")

                    elif ((input[a15] == 'ُ') and (input[b15] == 'ذ') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\46-ن.wav" + "'")

                    elif ((input[a15] == 'ُ') and (input[b15] == 'ط') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\52-ن.wav" + "'")

                    elif ((input[a15] == 'ُ') and (input[b15] == 'ك') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\57-ن.wav" + "'")

                    elif ((input[a15] == 'ُ') and (input[b15] == 'م') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\59-ن.wav" + "'")

                    elif ((input[a15] == 'ُ') and (input[b15] == 'ن') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\60-ن.wav" + "'")

                    elif ((input[a15] == 'ُ') and (input[b15] == 'ت') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\40-ن.wav" + "'")

                    elif ((input[a15] == 'ُ') and (input[b15] == 'أ') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\38-ن.wav" + "'")

                    elif ((input[a15] == 'ُ') and (input[b15] == 'ل') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\58-ن.wav" + "'")

                    elif ((input[a15] == 'ُ') and (input[b15] == 'ب') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\39-ن.wav" + "'")

                    elif ((input[a15] == 'ُ') and (input[b15] == 'ي') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\62-ن.wav" + "'")

                    elif ((input[a15] == 'ُ') and (input[b15] == 'س') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\48-ن.wav" + "'")

                    elif ((input[a15] == 'ُ') and (input[b15] == 'ش') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\49-ن.wav" + "'")

                    elif ((input[a15] == 'ُ') and (input[b15] == 'ظ') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\51-ن.wav" + "'")

                    elif ((input[a15] == 'ُ') and (input[b15] == 'ز') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\z2.wav" + "'")

                    elif ((input[a15] == 'ُ') and (input[b15] == 'و') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\signs.wav" + "'")

                    elif ((input[a15] == 'ُ') and (input[b15] == 'ة') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\40-ن.wav" + "'")

                    elif ((input[a15] == 'ُ') and (input[b15] == 'ر') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\47-ن.wav" + "'")

                    elif ((input[a15] == 'ُ') and (input[b15] == 'ؤ') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\38-ن.wav" + "'")

                    elif ((input[a15] == 'ُ') and (input[b15] == 'ء') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\38-ن.wav" + "'")

                    elif ((input[a15] == 'ُ') and (input[b15] == 'ئ') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\38-ن.wav" + "'")




                    elif ((input[a15] == 'ِ') and (input[b15] == 'د') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\70-ن.wav" + "'")

                    elif ((input[a15] == 'ِ') and (input[b15] == 'ج') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\67-ن.wav" + "'")

                    elif ((input[a15] == 'ِ') and (input[b15] == 'ح') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\68-ن.wav" + "'")

                    elif ((input[a15] == 'ِ') and (input[b15] == 'خ') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\69-ن.wav" + "'")

                    elif ((input[a15] == 'ِ') and (input[b15] == 'ه') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\86-ن.wav" + "'")

                    elif ((input[a15] == 'ِ') and (input[b15] == 'ع') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\78-ن.wav" + "'")

                    elif ((input[a15] == 'ِ') and (input[b15] == 'غ') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\79-ن.wav" + "'")

                    elif ((input[a15] == 'ِ') and (input[b15] == 'ف') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\80-ن.wav" + "'")

                    elif ((input[a15] == 'ِ') and (input[b15] == 'ق') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\81-ن.wav" + "'")

                    elif ((input[a15] == 'ِ') and (input[b15] == 'ث') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\66-ن.wav" + "'")

                    elif ((input[a15] == 'ِ') and (input[b15] == 'ص') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\75-ن.wav" + "'")

                    elif ((input[a15] == 'ِ') and (input[b15] == 'ض') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\76-ن.wav" + "'")

                    elif ((input[a15] == 'ِ') and (input[b15] == 'ذ') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\71-ن.wav" + "'")

                    elif ((input[a15] == 'ِ') and (input[b15] == 'ط') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\77-ن.wav" + "'")

                    elif ((input[a15] == 'ِ') and (input[b15] == 'ك') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\82-ن.wav" + "'")

                    elif ((input[a15] == 'ِ') and (input[b15] == 'م') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\84-ن.wav" + "'")

                    elif ((input[a15] == 'ِ') and (input[b15] == 'ن') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\85-ن.wav" + "'")

                    elif ((input[a15] == 'ِ') and (input[b15] == 'ت') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\65-ن.wav" + "'")

                    elif ((input[a15] == 'ِ') and (input[b15] == 'أ') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\63-ن.wav" + "'")

                    elif ((input[a15] == 'ِ') and (input[b15] == 'ل') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\83-ن.wav" + "'")

                    elif ((input[a15] == 'ِ') and (input[b15] == 'ب') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\64-ن.wav" + "'")

                    elif ((input[a15] == 'ِ') and (input[b15] == 'ي') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\87-ن.wav" + "'")

                    elif ((input[a15] == 'ِ') and (input[b15] == 'س') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\73-ن.wav" + "'")

                    elif ((input[a15] == 'ِ') and (input[b15] == 'ش') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\74-ن.wav" + "'")

                    elif ((input[a15] == 'ِ') and (input[b15] == 'ظ') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\76-ن.wav" + "'")

                    elif ((input[a15] == 'ِ') and (input[b15] == 'ز') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\z3.wav" + "'")

                    elif ((input[a15] == 'ِ') and (input[b15] == 'و') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\signs.wav" + "'")

                    elif ((input[a15] == 'ِ') and (input[b15] == 'ة') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\65-ن.wav" + "'")

                    elif ((input[a15] == 'ِ') and (input[b15] == 'ر') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\72-ن.wav" + "'")

                    elif ((input[a15] == 'ِ') and (input[b15] == 'ؤ') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\63-ن.wav" + "'")

                    elif ((input[a15] == 'ِ') and (input[b15] == 'ء') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\63-ن.wav" + "'")

                    elif ((input[a15] == 'ِ') and (input[b15] == 'ئ') and (input[c15] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\n\\63-ن.wav" + "'")






                    elif ((input[a15] == 'َ') and ((input[b15] == 'ا') or (input[b15] == 'ى'))):

                        self.z.append('file ' + "'" + "library\\n\\04-ن.wav" + "'")

                    elif (input[a15] == 'ُ' and input[b15] == 'و'):

                        self.z.append('file ' + "'" + "library\\n\\05-ن.wav" + "'")

                    elif (input[a15] == 'ِ' and input[b15] == 'ي'):

                        self.z.append('file ' + "'" + "library\\n\\06-ن.wav" + "'")

                    elif (input[a15] == 'ً'):

                        self.z.append('file ' + "'" + "library\\n\\07-ن.wav" + "'")

                    elif (input[a15] == 'ٌ'):

                        self.z.append('file ' + "'" + "library\\n\\08-ن.wav" + "'")

                    elif (input[a15] == 'ٍ'):

                        self.z.append('file ' + "'" + "library\\n\\09-ن.wav" + "'")

                    elif (input[a15] == 'َ'):

                        self.z.append('file ' + "'" + "library\\n\\01-ن.wav" + "'")

                    elif (input[a15] == 'ُ'):

                        self.z.append('file ' + "'" + "library\\n\\02-ن.wav" + "'")

                    elif (input[a15] == 'ِ'):

                        self.z.append('file ' + "'" + "library\\n\\03-ن.wav" + "'")

                    elif (input[a15] == 'ْ'):

                        self.z.append('file ' + "'" + "library\\n\\signs.wav" + "'")

                    else:

                        self.z.append('file ' + "'" + "library\\n\\signs.wav" + "'")








                else:

                    self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                a15 = 0

                b15 = 0

                d15 = 0

                c15 = 0

            elif (char == 'ت'):

                a16 = i + 1

                b16 = i + 2

                c16 = i + 3

                d16 = i + 4

                if (a16 < (len(input))):

                    if (input[a16] == '\0'):

                        self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                    elif ((input[a16] == 'َ') and (input[b16] == 'د') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\t\\20-ت.wav' + "'")

                    elif ((input[a16] == 'َ') and (input[b16] == 'ج') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\17-ت.wav" + "'")

                    elif ((input[a16] == 'َ') and (input[b16] == 'ح') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\18-ت.wav" + "'")

                    elif ((input[a16] == 'َ') and (input[b16] == 'خ') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\19-ت.wav" + "'")

                    elif ((input[a16] == 'َ') and (input[b16] == 'ه') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\36-ت.wav" + "'")

                    elif ((input[a16] == 'َ') and (input[b16] == 'ع') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\28-ت.wav" + "'")

                    elif ((input[a16] == 'َ') and (input[b16] == 'غ') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\29-ت.wav" + "'")

                    elif ((input[a16] == 'َ') and (input[b16] == 'ف') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\30-ت.wav" + "'")

                    elif ((input[a16] == 'َ') and (input[b16] == 'ق') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\31-ت.wav" + "'")

                    elif ((input[a16] == 'َ') and (input[b16] == 'ث') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\16-ت.wav" + "'")

                    elif ((input[a16] == 'َ') and (input[b16] == 'ص') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\25-ت.wav" + "'")

                    elif ((input[a16] == 'َ') and (input[b16] == 'ض') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\26-ت.wav" + "'")

                    elif ((input[a16] == 'َ') and (input[b16] == 'ذ') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\21-ت.wav" + "'")

                    elif ((input[a16] == 'َ') and (input[b16] == 'ط') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\27-ت.wav" + "'")

                    elif ((input[a16] == 'َ') and (input[b16] == 'ك') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\32-ت.wav" + "'")

                    elif ((input[a16] == 'َ') and (input[b16] == 'م') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\34-ت.wav" + "'")

                    elif ((input[a16] == 'َ') and (input[b16] == 'ن') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\35-ت.wav" + "'")

                    elif ((input[a16] == 'َ') and (input[b16] == 'ت') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\15-ت.wav" + "'")

                    elif ((input[a16] == 'َ') and (input[b16] == 'أ') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\13-ت.wav" + "'")

                    elif ((input[a16] == 'َ') and (input[b16] == 'ل') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\33-ت.wav" + "'")

                    elif ((input[a16] == 'َ') and (input[b16] == 'ب') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\14-ت.wav" + "'")

                    elif ((input[a16] == 'َ') and (input[b16] == 'ي') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\37-ت.wav" + "'")

                    elif ((input[a16] == 'َ') and (input[b16] == 'س') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\23-ت.wav" + "'")

                    elif ((input[a16] == 'َ') and (input[b16] == 'ش') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\24-ت.wav" + "'")

                    elif ((input[a16] == 'َ') and (input[b16] == 'ظ') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\26-ت.wav" + "'")

                    elif ((input[a16] == 'َ') and (input[b16] == 'ز') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\z1.wav" + "'")

                    elif ((input[a16] == 'َ') and (input[b16] == 'و') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\signs.wav" + "'")

                    elif ((input[a16] == 'َ') and (input[b16] == 'ة') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\15-ت.wav" + "'")

                    elif ((input[a16] == 'َ') and (input[b16] == 'ر') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\22-ت.wav" + "'")

                    elif ((input[a16] == 'َ') and (input[b16] == 'ؤ') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\13-ت.wav" + "'")

                    elif ((input[a16] == 'َ') and (input[b16] == 'ء') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\13-ت.wav" + "'")

                    elif ((input[a16] == 'َ') and (input[b16] == 'ئ') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\13-ت.wav" + "'")



                    elif ((input[a16] == 'ُ') and (input[b16] == 'د') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\45-ت.wav" + "'")

                    elif ((input[a16] == 'ُ') and (input[b16] == 'ج') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\42-ت.wav" + "'")

                    elif ((input[a16] == 'ُ') and (input[b16] == 'ح') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\43-ت.wav" + "'")

                    elif ((input[a16] == 'ُ') and (input[b16] == 'خ') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\44-ت.wav" + "'")

                    elif ((input[a16] == 'ُ') and (input[b16] == 'ه') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\61-ت.wav" + "'")

                    elif ((input[a16] == 'ُ') and (input[b16] == 'ع') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\53-ت.wav" + "'")

                    elif ((input[a16] == 'ُ') and (input[b16] == 'غ') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\54-ت.wav" + "'")

                    elif ((input[a16] == 'ُ') and (input[b16] == 'ف') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\55-ت.wav" + "'")

                    elif ((input[a16] == 'ُ') and (input[b16] == 'ق') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\56-ت.wav" + "'")

                    elif ((input[a16] == 'ُ') and (input[b16] == 'ث') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\41-ت.wav" + "'")

                    elif ((input[a16] == 'ُ') and (input[b16] == 'ص') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\50-ت.wav" + "'")

                    elif ((input[a16] == 'ُ') and (input[b16] == 'ض') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\51-ت.wav" + "'")

                    elif ((input[a16] == 'ُ') and (input[b16] == 'ذ') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\46-ت.wav" + "'")

                    elif ((input[a16] == 'ُ') and (input[b16] == 'ط') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\52-ت.wav" + "'")

                    elif ((input[a16] == 'ُ') and (input[b16] == 'ك') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\57-ت.wav" + "'")

                    elif ((input[a16] == 'ُ') and (input[b16] == 'م') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\59-ت.wav" + "'")

                    elif ((input[a16] == 'ُ') and (input[b16] == 'ن') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\60-ت.wav" + "'")

                    elif ((input[a16] == 'ُ') and (input[b16] == 'ت') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\40-ت.wav" + "'")

                    elif ((input[a16] == 'ُ') and (input[b16] == 'أ') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\38-ت.wav" + "'")

                    elif ((input[a16] == 'ُ') and (input[b16] == 'ل') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\58-ت.wav" + "'")

                    elif ((input[a16] == 'ُ') and (input[b16] == 'ب') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\39-ت.wav" + "'")

                    elif ((input[a16] == 'ُ') and (input[b16] == 'ي') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\62-ت.wav" + "'")

                    elif ((input[a16] == 'ُ') and (input[b16] == 'س') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\48-ت.wav" + "'")

                    elif ((input[a16] == 'ُ') and (input[b16] == 'ش') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\49-ت.wav" + "'")

                    elif ((input[a16] == 'ُ') and (input[b16] == 'ظ') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\51-ت.wav" + "'")

                    elif ((input[a16] == 'ُ') and (input[b16] == 'ز') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\z2.wav" + "'")

                    elif ((input[a16] == 'ُ') and (input[b16] == 'و') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\signs.wav" + "'")

                    elif ((input[a16] == 'ُ') and (input[b16] == 'ة') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\40-ت.wav" + "'")

                    elif ((input[a16] == 'ُ') and (input[b16] == 'ر') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\47-ت.wav" + "'")

                    elif ((input[a16] == 'ُ') and (input[b16] == 'ؤ') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\38-ت.wav" + "'")

                    elif ((input[a16] == 'ُ') and (input[b16] == 'ء') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\38-ت.wav" + "'")

                    elif ((input[a16] == 'ُ') and (input[b16] == 'ئ') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\38-ت.wav" + "'")




                    elif ((input[a16] == 'ِ') and (input[b16] == 'د') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\70-ت.wav" + "'")

                    elif ((input[a16] == 'ِ') and (input[b16] == 'ج') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\67-ت.wav" + "'")

                    elif ((input[a16] == 'ِ') and (input[b16] == 'ح') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\68-ت.wav" + "'")

                    elif ((input[a16] == 'ِ') and (input[b16] == 'خ') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\69-ت.wav" + "'")

                    elif ((input[a16] == 'ِ') and (input[b16] == 'ه') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\86-ت.wav" + "'")

                    elif ((input[a16] == 'ِ') and (input[b16] == 'ع') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\78-ت.wav" + "'")

                    elif ((input[a16] == 'ِ') and (input[b16] == 'غ') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\79-ت.wav" + "'")

                    elif ((input[a16] == 'ِ') and (input[b16] == 'ف') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\80-ت.wav" + "'")

                    elif ((input[a16] == 'ِ') and (input[b16] == 'ق') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\81-ت.wav" + "'")

                    elif ((input[a16] == 'ِ') and (input[b16] == 'ث') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\66-ت.wav" + "'")

                    elif ((input[a16] == 'ِ') and (input[b16] == 'ص') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\75-ت.wav" + "'")

                    elif ((input[a16] == 'ِ') and (input[b16] == 'ض') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\76-ت.wav" + "'")

                    elif ((input[a16] == 'ِ') and (input[b16] == 'ذ') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\71-ت.wav" + "'")

                    elif ((input[a16] == 'ِ') and (input[b16] == 'ط') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\77-ت.wav" + "'")

                    elif ((input[a16] == 'ِ') and (input[b16] == 'ك') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\82-ت.wav" + "'")

                    elif ((input[a16] == 'ِ') and (input[b16] == 'م') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\84-ت.wav" + "'")

                    elif ((input[a16] == 'ِ') and (input[b16] == 'ن') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\85-ت.wav" + "'")

                    elif ((input[a16] == 'ِ') and (input[b16] == 'ت') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\65-ت.wav" + "'")

                    elif ((input[a16] == 'ِ') and (input[b16] == 'أ') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\63-ت.wav" + "'")

                    elif ((input[a16] == 'ِ') and (input[b16] == 'ل') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\83-ت.wav" + "'")

                    elif ((input[a16] == 'ِ') and (input[b16] == 'ب') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\64-ت.wav" + "'")

                    elif ((input[a16] == 'ِ') and (input[b16] == 'ي') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\87-ت.wav" + "'")

                    elif ((input[a16] == 'ِ') and (input[b16] == 'س') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\73-ت.wav" + "'")

                    elif ((input[a16] == 'ِ') and (input[b16] == 'ش') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\74-ت.wav" + "'")

                    elif ((input[a16] == 'ِ') and (input[b16] == 'ظ') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\76-ت.wav" + "'")

                    elif ((input[a16] == 'ِ') and (input[b16] == 'ز') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\z3.wav" + "'")

                    elif ((input[a16] == 'ِ') and (input[b16] == 'و') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\signs.wav" + "'")

                    elif ((input[a16] == 'ِ') and (input[b16] == 'ة') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\65-ت.wav" + "'")

                    elif ((input[a16] == 'ِ') and (input[b16] == 'ر') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\72-ت.wav" + "'")

                    elif ((input[a16] == 'ِ') and (input[b16] == 'ؤ') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\63-ت.wav" + "'")

                    elif ((input[a16] == 'ِ') and (input[b16] == 'ء') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\63-ت.wav" + "'")

                    elif ((input[a16] == 'ِ') and (input[b16] == 'ئ') and (input[c16] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\63-ت.wav" + "'")






                    elif ((input[a16] == 'َ') and ((input[b16] == 'ا') or (input[b16] == 'ى'))):

                        self.z.append('file ' + "'" + "library\\t\\04-ت.wav" + "'")

                    elif (input[a16] == 'ُ' and input[b16] == 'و'):

                        self.z.append('file ' + "'" + "library\\t\\05-ت.wav" + "'")

                    elif (input[a16] == 'ِ' and input[b16] == 'ي'):

                        self.z.append('file ' + "'" + "library\\t\\06-ت.wav" + "'")

                    elif (input[a16] == 'ً'):

                        self.z.append('file ' + "'" + "library\\t\\07-ت.wav" + "'")

                    elif (input[a16] == 'ٌ'):

                        self.z.append('file ' + "'" + "library\\t\\08-ت.wav" + "'")

                    elif (input[a16] == 'ٍ'):

                        self.z.append('file ' + "'" + "library\\t\\09-ت.wav" + "'")

                    elif (input[a16] == 'َ'):

                        self.z.append('file ' + "'" + "library\\t\\01-ت.wav" + "'")

                    elif (input[a16] == 'ُ'):

                        self.z.append('file ' + "'" + "library\\t\\02-ت.wav" + "'")

                    elif (input[a16] == 'ِ'):

                        self.z.append('file ' + "'" + "library\\t\\03-ت.wav" + "'")

                    elif (input[a16] == 'ْ'):

                        self.z.append('file ' + "'" + "library\\t\\signs.wav" + "'")

                    else:

                        self.z.append('file ' + "'" + "library\\t\\signs.wav" + "'")








                else:

                    self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                a16 = 0

                b16 = 0

                d16 = 0

                c16 = 0

            elif (char == 'أ'):

                a17 = i + 1

                b17 = i + 2

                c17 = i + 3

                d17 = i + 4

                if (a17 < (len(input))):

                    if (input[a17] == '\0'):

                        self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                    elif ((input[a17] == 'َ') and (input[b17] == 'د') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\a\\20-أ.wav' + "'")

                    elif ((input[a17] == 'َ') and (input[b17] == 'ج') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\17-أ.wav" + "'")

                    elif ((input[a17] == 'َ') and (input[b17] == 'ح') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\18-أ.wav" + "'")

                    elif ((input[a17] == 'َ') and (input[b17] == 'خ') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\19-أ.wav" + "'")

                    elif ((input[a17] == 'َ') and (input[b17] == 'ه') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\36-أ.wav" + "'")

                    elif ((input[a17] == 'َ') and (input[b17] == 'ع') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\28-أ.wav" + "'")

                    elif ((input[a17] == 'َ') and (input[b17] == 'غ') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\29-أ.wav" + "'")

                    elif ((input[a17] == 'َ') and (input[b17] == 'ف') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\30-أ.wav" + "'")

                    elif ((input[a17] == 'َ') and (input[b17] == 'ق') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\31-أ.wav" + "'")

                    elif ((input[a17] == 'َ') and (input[b17] == 'ث') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\16-أ.wav" + "'")

                    elif ((input[a17] == 'َ') and (input[b17] == 'ص') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\25-أ.wav" + "'")

                    elif ((input[a17] == 'َ') and (input[b17] == 'ض') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\26-أ.wav" + "'")

                    elif ((input[a17] == 'َ') and (input[b17] == 'ذ') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\21-أ.wav" + "'")

                    elif ((input[a17] == 'َ') and (input[b17] == 'ط') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\27-أ.wav" + "'")

                    elif ((input[a17] == 'َ') and (input[b17] == 'ك') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\32-أ.wav" + "'")

                    elif ((input[a17] == 'َ') and (input[b17] == 'م') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\34-أ.wav" + "'")

                    elif ((input[a17] == 'َ') and (input[b17] == 'ن') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\35-أ.wav" + "'")

                    elif ((input[a17] == 'َ') and (input[b17] == 'ت') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\15-أ.wav" + "'")

                    elif ((input[a17] == 'َ') and (input[b17] == 'أ') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\13-أ.wav" + "'")

                    elif ((input[a17] == 'َ') and (input[b17] == 'ل') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\33-أ.wav" + "'")

                    elif ((input[a17] == 'َ') and (input[b17] == 'ب') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\14-أ.wav" + "'")

                    elif ((input[a17] == 'َ') and (input[b17] == 'ي') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\37-أ.wav" + "'")

                    elif ((input[a17] == 'َ') and (input[b17] == 'س') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\23-أ.wav" + "'")

                    elif ((input[a17] == 'َ') and (input[b17] == 'ش') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\24-أ.wav" + "'")

                    elif ((input[a17] == 'َ') and (input[b17] == 'ظ') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\26-أ.wav" + "'")

                    elif ((input[a17] == 'َ') and (input[b17] == 'ز') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\z1.wav" + "'")

                    elif ((input[a17] == 'َ') and (input[b17] == 'و') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\signs.wav" + "'")

                    elif ((input[a17] == 'َ') and (input[b17] == 'ة') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\15-أ.wav" + "'")

                    elif ((input[a17] == 'َ') and (input[b17] == 'ر') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\22-أ.wav" + "'")

                    elif ((input[a17] == 'َ') and (input[b17] == 'ؤ') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\13-أ.wav" + "'")

                    elif ((input[a17] == 'َ') and (input[b17] == 'ء') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\13-أ.wav" + "'")

                    elif ((input[a17] == 'َ') and (input[b17] == 'ئ') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\13-أ.wav" + "'")



                    elif ((input[a17] == 'ُ') and (input[b17] == 'د') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\45-أ.wav" + "'")

                    elif ((input[a17] == 'ُ') and (input[b17] == 'ج') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\42-أ.wav" + "'")

                    elif ((input[a17] == 'ُ') and (input[b17] == 'ح') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\43-أ.wav" + "'")

                    elif ((input[a17] == 'ُ') and (input[b17] == 'خ') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\44-أ.wav" + "'")

                    elif ((input[a17] == 'ُ') and (input[b17] == 'ه') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\61-أ.wav" + "'")

                    elif ((input[a17] == 'ُ') and (input[b17] == 'ع') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\53-أ.wav" + "'")

                    elif ((input[a17] == 'ُ') and (input[b17] == 'غ') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\54-أ.wav" + "'")

                    elif ((input[a17] == 'ُ') and (input[b17] == 'ف') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\55-أ.wav" + "'")

                    elif ((input[a17] == 'ُ') and (input[b17] == 'ق') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\56-أ.wav" + "'")

                    elif ((input[a17] == 'ُ') and (input[b17] == 'ث') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\41-أ.wav" + "'")

                    elif ((input[a17] == 'ُ') and (input[b17] == 'ص') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\50-أ.wav" + "'")

                    elif ((input[a17] == 'ُ') and (input[b17] == 'ض') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\51-أ.wav" + "'")

                    elif ((input[a17] == 'ُ') and (input[b17] == 'ذ') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\46-أ.wav" + "'")

                    elif ((input[a17] == 'ُ') and (input[b17] == 'ط') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\52-أ.wav" + "'")

                    elif ((input[a17] == 'ُ') and (input[b17] == 'ك') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\57-أ.wav" + "'")

                    elif ((input[a17] == 'ُ') and (input[b17] == 'م') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\59-أ.wav" + "'")

                    elif ((input[a17] == 'ُ') and (input[b17] == 'ن') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\60-أ.wav" + "'")

                    elif ((input[a17] == 'ُ') and (input[b17] == 'ت') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\40-أ.wav" + "'")

                    elif ((input[a17] == 'ُ') and (input[b17] == 'أ') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\38-أ.wav" + "'")

                    elif ((input[a17] == 'ُ') and (input[b17] == 'ل') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\58-أ.wav" + "'")

                    elif ((input[a17] == 'ُ') and (input[b17] == 'ب') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\39-أ.wav" + "'")

                    elif ((input[a17] == 'ُ') and (input[b17] == 'ي') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\62-أ.wav" + "'")

                    elif ((input[a17] == 'ُ') and (input[b17] == 'س') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\48-أ.wav" + "'")

                    elif ((input[a17] == 'ُ') and (input[b17] == 'ش') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\49-أ.wav" + "'")

                    elif ((input[a17] == 'ُ') and (input[b17] == 'ظ') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\51-أ.wav" + "'")

                    elif ((input[a17] == 'ُ') and (input[b17] == 'ز') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\z2.wav" + "'")

                    elif ((input[a17] == 'ُ') and (input[b17] == 'و') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\signs.wav" + "'")

                    elif ((input[a17] == 'ُ') and (input[b17] == 'ة') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\40-أ.wav" + "'")

                    elif ((input[a17] == 'ُ') and (input[b17] == 'ر') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\47-أ.wav" + "'")

                    elif ((input[a17] == 'ُ') and (input[b17] == 'ؤ') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\38-أ.wav" + "'")

                    elif ((input[a17] == 'ُ') and (input[b17] == 'ء') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\38-أ.wav" + "'")

                    elif ((input[a17] == 'ُ') and (input[b17] == 'ئ') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\38-أ.wav" + "'")




                    elif ((input[a17] == 'ِ') and (input[b17] == 'د') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\70-أ.wav" + "'")

                    elif ((input[a17] == 'ِ') and (input[b17] == 'ج') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\67-أ.wav" + "'")

                    elif ((input[a17] == 'ِ') and (input[b17] == 'ح') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\68-أ.wav" + "'")

                    elif ((input[a17] == 'ِ') and (input[b17] == 'خ') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\69-أ.wav" + "'")

                    elif ((input[a17] == 'ِ') and (input[b17] == 'ه') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\86-أ.wav" + "'")

                    elif ((input[a17] == 'ِ') and (input[b17] == 'ع') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\78-أ.wav" + "'")

                    elif ((input[a17] == 'ِ') and (input[b17] == 'غ') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\79-أ.wav" + "'")

                    elif ((input[a17] == 'ِ') and (input[b17] == 'ف') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\80-أ.wav" + "'")

                    elif ((input[a17] == 'ِ') and (input[b17] == 'ق') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\81-أ.wav" + "'")

                    elif ((input[a17] == 'ِ') and (input[b17] == 'ث') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\66-أ.wav" + "'")

                    elif ((input[a17] == 'ِ') and (input[b17] == 'ص') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\75-أ.wav" + "'")

                    elif ((input[a17] == 'ِ') and (input[b17] == 'ض') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\76-أ.wav" + "'")

                    elif ((input[a17] == 'ِ') and (input[b17] == 'ذ') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\71-أ.wav" + "'")

                    elif ((input[a17] == 'ِ') and (input[b17] == 'ط') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\77-أ.wav" + "'")

                    elif ((input[a17] == 'ِ') and (input[b17] == 'ك') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\82-أ.wav" + "'")

                    elif ((input[a17] == 'ِ') and (input[b17] == 'م') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\84-أ.wav" + "'")

                    elif ((input[a17] == 'ِ') and (input[b17] == 'ن') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\85-أ.wav" + "'")

                    elif ((input[a17] == 'ِ') and (input[b17] == 'ت') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\65-أ.wav" + "'")

                    elif ((input[a17] == 'ِ') and (input[b17] == 'أ') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\63-أ.wav" + "'")

                    elif ((input[a17] == 'ِ') and (input[b17] == 'ل') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\83-أ.wav" + "'")

                    elif ((input[a17] == 'ِ') and (input[b17] == 'ب') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\64-أ.wav" + "'")

                    elif ((input[a17] == 'ِ') and (input[b17] == 'ي') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\87-أ.wav" + "'")

                    elif ((input[a17] == 'ِ') and (input[b17] == 'س') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\73-أ.wav" + "'")

                    elif ((input[a17] == 'ِ') and (input[b17] == 'ش') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\74-أ.wav" + "'")

                    elif ((input[a17] == 'ِ') and (input[b17] == 'ظ') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\76-أ.wav" + "'")

                    elif ((input[a17] == 'ِ') and (input[b17] == 'ز') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\z3.wav" + "'")

                    elif ((input[a17] == 'ِ') and (input[b17] == 'و') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\signs.wav" + "'")

                    elif ((input[a17] == 'ِ') and (input[b17] == 'ة') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\65-أ.wav" + "'")

                    elif ((input[a17] == 'ِ') and (input[b17] == 'ر') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\72-أ.wav" + "'")

                    elif ((input[a17] == 'ِ') and (input[b17] == 'ؤ') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\63-أ.wav" + "'")

                    elif ((input[a17] == 'ِ') and (input[b17] == 'ء') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\63-أ.wav" + "'")

                    elif ((input[a17] == 'ِ') and (input[b17] == 'ئ') and (input[c17] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\63-أ.wav" + "'")






                    elif ((input[a17] == 'َ') and ((input[b17] == 'ا') or (input[b17] == 'ى'))):

                        self.z.append('file ' + "'" + "library\\a\\04-أ.wav" + "'")

                    elif (input[a17] == 'ُ' and input[b17] == 'و'):

                        self.z.append('file ' + "'" + "library\\a\\05-أ.wav" + "'")

                    elif (input[a17] == 'ِ' and input[b17] == 'ي'):

                        self.z.append('file ' + "'" + "library\\a\\06-أ.wav" + "'")

                    elif (input[a17] == 'ً'):

                        self.z.append('file ' + "'" + "library\\a\\07-أ.wav" + "'")

                    elif (input[a17] == 'ٌ'):

                        self.z.append('file ' + "'" + "library\\a\\08-أ.wav" + "'")

                    elif (input[a17] == 'ٍ'):

                        self.z.append('file ' + "'" + "library\\a\\09-أ.wav" + "'")

                    elif (input[a17] == 'َ'):

                        self.z.append('file ' + "'" + "library\\a\\01-أ.wav" + "'")

                    elif (input[a17] == 'ُ'):

                        self.z.append('file ' + "'" + "library\\a\\02-أ.wav" + "'")

                    elif (input[a17] == 'ِ'):

                        self.z.append('file ' + "'" + "library\\a\\03-أ.wav" + "'")

                    elif (input[a17] == 'ْ'):

                        self.z.append('file ' + "'" + "library\\a\\signs.wav" + "'")

                    else:

                        self.z.append('file ' + "'" + "library\\a\\signs.wav" + "'")








                else:

                    self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                a17 = 0

                b17 = 0

                d17 = 0

                c17 = 0

            elif (char == 'ل'):

                a18 = i + 1

                b18 = i + 2

                c18 = i + 3

                d18 = i + 4

                if (a18 < (len(input))):

                    if (input[a18] == '\0'):

                        self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                    elif ((input[a18] == 'َ') and (input[b18] == 'د') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\L\\20-ل.wav' + "'")

                    elif ((input[a18] == 'َ') and (input[b18] == 'ج') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\17-ل.wav" + "'")

                    elif ((input[a18] == 'َ') and (input[b18] == 'ح') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\18-ل.wav" + "'")

                    elif ((input[a18] == 'َ') and (input[b18] == 'خ') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\19-ل.wav" + "'")

                    elif ((input[a18] == 'َ') and (input[b18] == 'ه') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\36-ل.wav" + "'")

                    elif ((input[a18] == 'َ') and (input[b18] == 'ع') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\28-ل.wav" + "'")

                    elif ((input[a18] == 'َ') and (input[b18] == 'غ') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\29-ل.wav" + "'")

                    elif ((input[a18] == 'َ') and (input[b18] == 'ف') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\30-ل.wav" + "'")

                    elif ((input[a18] == 'َ') and (input[b18] == 'ق') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\31-ل.wav" + "'")

                    elif ((input[a18] == 'َ') and (input[b18] == 'ث') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\16-ل.wav" + "'")

                    elif ((input[a18] == 'َ') and (input[b18] == 'ص') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\25-ل.wav" + "'")

                    elif ((input[a18] == 'َ') and (input[b18] == 'ض') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\26-ل.wav" + "'")

                    elif ((input[a18] == 'َ') and (input[b18] == 'ذ') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\21-ل.wav" + "'")

                    elif ((input[a18] == 'َ') and (input[b18] == 'ط') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\27-ل.wav" + "'")

                    elif ((input[a18] == 'َ') and (input[b18] == 'ك') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\32-ل.wav" + "'")

                    elif ((input[a18] == 'َ') and (input[b18] == 'م') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\34-ل.wav" + "'")

                    elif ((input[a18] == 'َ') and (input[b18] == 'ن') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\35-ل.wav" + "'")

                    elif ((input[a18] == 'َ') and (input[b18] == 'ت') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\15-ل.wav" + "'")

                    elif ((input[a18] == 'َ') and (input[b18] == 'أ') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\13-ل.wav" + "'")

                    elif ((input[a18] == 'َ') and (input[b18] == 'ل') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\33-ل.wav" + "'")

                    elif ((input[a18] == 'َ') and (input[b18] == 'ب') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\14-ل.wav" + "'")

                    elif ((input[a18] == 'َ') and (input[b18] == 'ي') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\37-ل.wav" + "'")

                    elif ((input[a18] == 'َ') and (input[b18] == 'س') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\23-ل.wav" + "'")

                    elif ((input[a18] == 'َ') and (input[b18] == 'ش') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\24-ل.wav" + "'")

                    elif ((input[a18] == 'َ') and (input[b18] == 'ظ') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\26-ل.wav" + "'")

                    elif ((input[a18] == 'َ') and (input[b18] == 'ز') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\z1.wav" + "'")

                    elif ((input[a18] == 'َ') and (input[b18] == 'و') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\signs.wav" + "'")

                    elif ((input[a18] == 'َ') and (input[b18] == 'ة') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\15-ل.wav" + "'")

                    elif ((input[a18] == 'َ') and (input[b18] == 'ر') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\22-ل.wav" + "'")

                    elif ((input[a18] == 'َ') and (input[b18] == 'ؤ') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\13-ل.wav" + "'")

                    elif ((input[a18] == 'َ') and (input[b18] == 'ء') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\13-ل.wav" + "'")

                    elif ((input[a18] == 'َ') and (input[b18] == 'ئ') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\13-ل.wav" + "'")



                    elif ((input[a18] == 'ُ') and (input[b18] == 'د') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\45-ل.wav" + "'")

                    elif ((input[a18] == 'ُ') and (input[b18] == 'ج') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\42-ل.wav" + "'")

                    elif ((input[a18] == 'ُ') and (input[b18] == 'ح') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\43-ل.wav" + "'")

                    elif ((input[a18] == 'ُ') and (input[b18] == 'خ') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\44-ل.wav" + "'")

                    elif ((input[a18] == 'ُ') and (input[b18] == 'ه') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\61-ل.wav" + "'")

                    elif ((input[a18] == 'ُ') and (input[b18] == 'ع') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\53-ل.wav" + "'")

                    elif ((input[a18] == 'ُ') and (input[b18] == 'غ') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\54-ل.wav" + "'")

                    elif ((input[a18] == 'ُ') and (input[b18] == 'ف') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\55-ل.wav" + "'")

                    elif ((input[a18] == 'ُ') and (input[b18] == 'ق') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\56-ل.wav" + "'")

                    elif ((input[a18] == 'ُ') and (input[b18] == 'ث') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\41-ل.wav" + "'")

                    elif ((input[a18] == 'ُ') and (input[b18] == 'ص') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\50-ل.wav" + "'")

                    elif ((input[a18] == 'ُ') and (input[b18] == 'ض') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\51-ل.wav" + "'")

                    elif ((input[a18] == 'ُ') and (input[b18] == 'ذ') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\46-ل.wav" + "'")

                    elif ((input[a18] == 'ُ') and (input[b18] == 'ط') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\52-ل.wav" + "'")

                    elif ((input[a18] == 'ُ') and (input[b18] == 'ك') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\57-ل.wav" + "'")

                    elif ((input[a18] == 'ُ') and (input[b18] == 'م') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\59-ل.wav" + "'")

                    elif ((input[a18] == 'ُ') and (input[b18] == 'ن') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\60-ل.wav" + "'")

                    elif ((input[a18] == 'ُ') and (input[b18] == 'ت') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\40-ل.wav" + "'")

                    elif ((input[a18] == 'ُ') and (input[b18] == 'أ') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\38-ل.wav" + "'")

                    elif ((input[a18] == 'ُ') and (input[b18] == 'ل') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\58-ل.wav" + "'")

                    elif ((input[a18] == 'ُ') and (input[b18] == 'ب') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\39-ل.wav" + "'")

                    elif ((input[a18] == 'ُ') and (input[b18] == 'ي') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\62-ل.wav" + "'")

                    elif ((input[a18] == 'ُ') and (input[b18] == 'س') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\48-ل.wav" + "'")

                    elif ((input[a18] == 'ُ') and (input[b18] == 'ش') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\49-ل.wav" + "'")

                    elif ((input[a18] == 'ُ') and (input[b18] == 'ظ') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\51-ل.wav" + "'")

                    elif ((input[a18] == 'ُ') and (input[b18] == 'ز') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\z2.wav" + "'")

                    elif ((input[a18] == 'ُ') and (input[b18] == 'و') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\signs.wav" + "'")

                    elif ((input[a18] == 'ُ') and (input[b18] == 'ة') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\40-ل.wav" + "'")

                    elif ((input[a18] == 'ُ') and (input[b18] == 'ر') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\47-ل.wav" + "'")

                    elif ((input[a18] == 'ُ') and (input[b18] == 'ؤ') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\38-ل.wav" + "'")

                    elif ((input[a18] == 'ُ') and (input[b18] == 'ء') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\38-ل.wav" + "'")

                    elif ((input[a18] == 'ُ') and (input[b18] == 'ئ') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\38-ل.wav" + "'")




                    elif ((input[a18] == 'ِ') and (input[b18] == 'د') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\70-ل.wav" + "'")

                    elif ((input[a18] == 'ِ') and (input[b18] == 'ج') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\67-ل.wav" + "'")

                    elif ((input[a18] == 'ِ') and (input[b18] == 'ح') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\68-ل.wav" + "'")

                    elif ((input[a18] == 'ِ') and (input[b18] == 'خ') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\69-ل.wav" + "'")

                    elif ((input[a18] == 'ِ') and (input[b18] == 'ه') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\86-ل.wav" + "'")

                    elif ((input[a18] == 'ِ') and (input[b18] == 'ع') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\78-ل.wav" + "'")

                    elif ((input[a18] == 'ِ') and (input[b18] == 'غ') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\79-ل.wav" + "'")

                    elif ((input[a18] == 'ِ') and (input[b18] == 'ف') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\80-ل.wav" + "'")

                    elif ((input[a18] == 'ِ') and (input[b18] == 'ق') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\81-ل.wav" + "'")

                    elif ((input[a18] == 'ِ') and (input[b18] == 'ث') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\66-ل.wav" + "'")

                    elif ((input[a18] == 'ِ') and (input[b18] == 'ص') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\75-ل.wav" + "'")

                    elif ((input[a18] == 'ِ') and (input[b18] == 'ض') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\76-ل.wav" + "'")

                    elif ((input[a18] == 'ِ') and (input[b18] == 'ذ') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\71-ل.wav" + "'")

                    elif ((input[a18] == 'ِ') and (input[b18] == 'ط') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\77-ل.wav" + "'")

                    elif ((input[a18] == 'ِ') and (input[b18] == 'ك') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\82-ل.wav" + "'")

                    elif ((input[a18] == 'ِ') and (input[b18] == 'م') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\84-ل.wav" + "'")

                    elif ((input[a18] == 'ِ') and (input[b18] == 'ن') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\85-ل.wav" + "'")

                    elif ((input[a18] == 'ِ') and (input[b18] == 'ت') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\65-ل.wav" + "'")

                    elif ((input[a18] == 'ِ') and (input[b18] == 'أ') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\63-ل.wav" + "'")

                    elif ((input[a18] == 'ِ') and (input[b18] == 'ل') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\83-ل.wav" + "'")

                    elif ((input[a18] == 'ِ') and (input[b18] == 'ب') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\64-ل.wav" + "'")

                    elif ((input[a18] == 'ِ') and (input[b18] == 'ي') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\87-ل.wav" + "'")

                    elif ((input[a18] == 'ِ') and (input[b18] == 'س') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\73-ل.wav" + "'")

                    elif ((input[a18] == 'ِ') and (input[b18] == 'ش') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\74-ل.wav" + "'")

                    elif ((input[a18] == 'ِ') and (input[b18] == 'ظ') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\76-ل.wav" + "'")

                    elif ((input[a18] == 'ِ') and (input[b18] == 'ز') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\z3.wav" + "'")

                    elif ((input[a18] == 'ِ') and (input[b18] == 'و') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\signs.wav" + "'")

                    elif ((input[a18] == 'ِ') and (input[b18] == 'ة') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\65-ل.wav" + "'")

                    elif ((input[a18] == 'ِ') and (input[b18] == 'ر') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\72-ل.wav" + "'")

                    elif ((input[a18] == 'ِ') and (input[b18] == 'ؤ') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\63-ل.wav" + "'")

                    elif ((input[a18] == 'ِ') and (input[b18] == 'ء') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\63-ل.wav" + "'")

                    elif ((input[a18] == 'ِ') and (input[b18] == 'ئ') and (input[c18] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\L\\63-ل.wav" + "'")






                    elif ((input[a18] == 'َ') and ((input[b18] == 'ا') or (input[b18] == 'ى'))):

                        self.z.append('file ' + "'" + "library\\L\\04-ل.wav" + "'")

                    elif (input[a18] == 'ُ' and input[b18] == 'و'):

                        self.z.append('file ' + "'" + "library\\L\\05-ل.wav" + "'")

                    elif (input[a18] == 'ِ' and input[b18] == 'ي'):

                        self.z.append('file ' + "'" + "library\\L\\06-ل.wav" + "'")

                    elif (input[a18] == 'ً'):

                        self.z.append('file ' + "'" + "library\\L\\07-ل.wav" + "'")

                    elif (input[a18] == 'ٌ'):

                        self.z.append('file ' + "'" + "library\\L\\08-ل.wav" + "'")

                    elif (input[a18] == 'ٍ'):

                        self.z.append('file ' + "'" + "library\\L\\09-ل.wav" + "'")

                    elif (input[a18] == 'َ'):

                        self.z.append('file ' + "'" + "library\\L\\01-ل.wav" + "'")

                    elif (input[a18] == 'ُ'):

                        self.z.append('file ' + "'" + "library\\L\\02-ل.wav" + "'")

                    elif (input[a18] == 'ِ'):

                        self.z.append('file ' + "'" + "library\\L\\03-ل.wav" + "'")

                    elif (input[a18] == 'ْ'):

                        self.z.append('file ' + "'" + "library\\L\\signs.wav" + "'")

                    else:

                        self.z.append('file ' + "'" + "library\\L\\signs.wav" + "'")








                else:

                    self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                a18 = 0

                b18 = 0

                d18 = 0

                c18 = 0

            elif (char == 'ب'):

                a19 = i + 1

                b19 = i + 2

                c19 = i + 3

                d19 = i + 4

                if (a19 < (len(input))):

                    if (input[a19] == '\0'):

                        self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                    elif ((input[a19] == 'َ') and (input[b19] == 'د') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\b\\20-ب.wav' + "'")

                    elif ((input[a19] == 'َ') and (input[b19] == 'ج') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\17-ب.wav" + "'")

                    elif ((input[a19] == 'َ') and (input[b19] == 'ح') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\18-ب.wav" + "'")

                    elif ((input[a19] == 'َ') and (input[b19] == 'خ') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\19-ب.wav" + "'")

                    elif ((input[a19] == 'َ') and (input[b19] == 'ه') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\36-ب.wav" + "'")

                    elif ((input[a19] == 'َ') and (input[b19] == 'ع') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\28-ب.wav" + "'")

                    elif ((input[a19] == 'َ') and (input[b19] == 'غ') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\29-ب.wav" + "'")

                    elif ((input[a19] == 'َ') and (input[b19] == 'ف') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\30-ب.wav" + "'")

                    elif ((input[a19] == 'َ') and (input[b19] == 'ق') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\31-ب.wav" + "'")

                    elif ((input[a19] == 'َ') and (input[b19] == 'ث') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\16-ب.wav" + "'")

                    elif ((input[a19] == 'َ') and (input[b19] == 'ص') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\25-ب.wav" + "'")

                    elif ((input[a19] == 'َ') and (input[b19] == 'ض') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\26-ب.wav" + "'")

                    elif ((input[a19] == 'َ') and (input[b19] == 'ذ') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\21-ب.wav" + "'")

                    elif ((input[a19] == 'َ') and (input[b19] == 'ط') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\27-ب.wav" + "'")

                    elif ((input[a19] == 'َ') and (input[b19] == 'ك') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\32-ب.wav" + "'")

                    elif ((input[a19] == 'َ') and (input[b19] == 'م') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\34-ب.wav" + "'")

                    elif ((input[a19] == 'َ') and (input[b19] == 'ن') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\35-ب.wav" + "'")

                    elif ((input[a19] == 'َ') and (input[b19] == 'ت') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\15-ب.wav" + "'")

                    elif ((input[a19] == 'َ') and (input[b19] == 'أ') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\13-ب.wav" + "'")

                    elif ((input[a19] == 'َ') and (input[b19] == 'ل') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\33-ب.wav" + "'")

                    elif ((input[a19] == 'َ') and (input[b19] == 'ب') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\14-ب.wav" + "'")

                    elif ((input[a19] == 'َ') and (input[b19] == 'ي') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\37-ب.wav" + "'")

                    elif ((input[a19] == 'َ') and (input[b19] == 'س') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\23-ب.wav" + "'")

                    elif ((input[a19] == 'َ') and (input[b19] == 'ش') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\24-ب.wav" + "'")

                    elif ((input[a19] == 'َ') and (input[b19] == 'ظ') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\26-ب.wav" + "'")

                    elif ((input[a19] == 'َ') and (input[b19] == 'ز') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\z1.wav" + "'")

                    elif ((input[a19] == 'َ') and (input[b19] == 'و') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\signs.wav" + "'")

                    elif ((input[a19] == 'َ') and (input[b19] == 'ة') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\15-ب.wav" + "'")

                    elif ((input[a19] == 'َ') and (input[b19] == 'ر') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\22-ب.wav" + "'")

                    elif ((input[a19] == 'َ') and (input[b19] == 'ؤ') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\13-ب.wav" + "'")

                    elif ((input[a19] == 'َ') and (input[b19] == 'ء') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\13-ب.wav" + "'")

                    elif ((input[a19] == 'َ') and (input[b19] == 'ئ') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\13-ب.wav" + "'")



                    elif ((input[a19] == 'ُ') and (input[b19] == 'د') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\45-ب.wav" + "'")

                    elif ((input[a19] == 'ُ') and (input[b19] == 'ج') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\42-ب.wav" + "'")

                    elif ((input[a19] == 'ُ') and (input[b19] == 'ح') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\43-ب.wav" + "'")

                    elif ((input[a19] == 'ُ') and (input[b19] == 'خ') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\44-ب.wav" + "'")

                    elif ((input[a19] == 'ُ') and (input[b19] == 'ه') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\61-ب.wav" + "'")

                    elif ((input[a19] == 'ُ') and (input[b19] == 'ع') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\53-ب.wav" + "'")

                    elif ((input[a19] == 'ُ') and (input[b19] == 'غ') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\54-ب.wav" + "'")

                    elif ((input[a19] == 'ُ') and (input[b19] == 'ف') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\55-ب.wav" + "'")

                    elif ((input[a19] == 'ُ') and (input[b19] == 'ق') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\56-ب.wav" + "'")

                    elif ((input[a19] == 'ُ') and (input[b19] == 'ث') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\41-ب.wav" + "'")

                    elif ((input[a19] == 'ُ') and (input[b19] == 'ص') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\50-ب.wav" + "'")

                    elif ((input[a19] == 'ُ') and (input[b19] == 'ض') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\51-ب.wav" + "'")

                    elif ((input[a19] == 'ُ') and (input[b19] == 'ذ') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\46-ب.wav" + "'")

                    elif ((input[a19] == 'ُ') and (input[b19] == 'ط') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\52-ب.wav" + "'")

                    elif ((input[a19] == 'ُ') and (input[b19] == 'ك') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\57-ب.wav" + "'")

                    elif ((input[a19] == 'ُ') and (input[b19] == 'م') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\59-ب.wav" + "'")

                    elif ((input[a19] == 'ُ') and (input[b19] == 'ن') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\60-ب.wav" + "'")

                    elif ((input[a19] == 'ُ') and (input[b19] == 'ت') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\40-ب.wav" + "'")

                    elif ((input[a19] == 'ُ') and (input[b19] == 'أ') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\38-ب.wav" + "'")

                    elif ((input[a19] == 'ُ') and (input[b19] == 'ل') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\58-ب.wav" + "'")

                    elif ((input[a19] == 'ُ') and (input[b19] == 'ب') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\39-ب.wav" + "'")

                    elif ((input[a19] == 'ُ') and (input[b19] == 'ي') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\62-ب.wav" + "'")

                    elif ((input[a19] == 'ُ') and (input[b19] == 'س') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\48-ب.wav" + "'")

                    elif ((input[a19] == 'ُ') and (input[b19] == 'ش') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\49-ب.wav" + "'")

                    elif ((input[a19] == 'ُ') and (input[b19] == 'ظ') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\51-ب.wav" + "'")

                    elif ((input[a19] == 'ُ') and (input[b19] == 'ز') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\z2.wav" + "'")

                    elif ((input[a19] == 'ُ') and (input[b19] == 'و') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\signs.wav" + "'")

                    elif ((input[a19] == 'ُ') and (input[b19] == 'ة') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\40-ب.wav" + "'")

                    elif ((input[a19] == 'ُ') and (input[b19] == 'ر') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\47-ب.wav" + "'")

                    elif ((input[a19] == 'ُ') and (input[b19] == 'ؤ') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\38-ب.wav" + "'")

                    elif ((input[a19] == 'ُ') and (input[b19] == 'ء') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\38-ب.wav" + "'")

                    elif ((input[a19] == 'ُ') and (input[b19] == 'ئ') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\38-ب.wav" + "'")




                    elif ((input[a19] == 'ِ') and (input[b19] == 'د') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\70-ب.wav" + "'")

                    elif ((input[a19] == 'ِ') and (input[b19] == 'ج') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\67-ب.wav" + "'")

                    elif ((input[a19] == 'ِ') and (input[b19] == 'ح') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\68-ب.wav" + "'")

                    elif ((input[a19] == 'ِ') and (input[b19] == 'خ') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\69-ب.wav" + "'")

                    elif ((input[a19] == 'ِ') and (input[b19] == 'ه') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\86-ب.wav" + "'")

                    elif ((input[a19] == 'ِ') and (input[b19] == 'ع') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\78-ب.wav" + "'")

                    elif ((input[a19] == 'ِ') and (input[b19] == 'غ') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\79-ب.wav" + "'")

                    elif ((input[a19] == 'ِ') and (input[b19] == 'ف') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\80-ب.wav" + "'")

                    elif ((input[a19] == 'ِ') and (input[b19] == 'ق') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\81-ب.wav" + "'")

                    elif ((input[a19] == 'ِ') and (input[b19] == 'ث') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\66-ب.wav" + "'")

                    elif ((input[a19] == 'ِ') and (input[b19] == 'ص') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\75-ب.wav" + "'")

                    elif ((input[a19] == 'ِ') and (input[b19] == 'ض') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\76-ب.wav" + "'")

                    elif ((input[a19] == 'ِ') and (input[b19] == 'ذ') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\71-ب.wav" + "'")

                    elif ((input[a19] == 'ِ') and (input[b19] == 'ط') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\77-ب.wav" + "'")

                    elif ((input[a19] == 'ِ') and (input[b19] == 'ك') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\82-ب.wav" + "'")

                    elif ((input[a19] == 'ِ') and (input[b19] == 'م') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\84-ب.wav" + "'")

                    elif ((input[a19] == 'ِ') and (input[b19] == 'ن') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\85-ب.wav" + "'")

                    elif ((input[a19] == 'ِ') and (input[b19] == 'ت') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\65-ب.wav" + "'")

                    elif ((input[a19] == 'ِ') and (input[b19] == 'أ') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\63-ب.wav" + "'")

                    elif ((input[a19] == 'ِ') and (input[b19] == 'ل') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\83-ب.wav" + "'")

                    elif ((input[a19] == 'ِ') and (input[b19] == 'ب') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\64-ب.wav" + "'")

                    elif ((input[a19] == 'ِ') and (input[b19] == 'ي') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\87-ب.wav" + "'")

                    elif ((input[a19] == 'ِ') and (input[b19] == 'س') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\73-ب.wav" + "'")

                    elif ((input[a19] == 'ِ') and (input[b19] == 'ش') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\74-ب.wav" + "'")

                    elif ((input[a19] == 'ِ') and (input[b19] == 'ظ') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\76-ب.wav" + "'")

                    elif ((input[a19] == 'ِ') and (input[b19] == 'ز') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\z3.wav" + "'")

                    elif ((input[a19] == 'ِ') and (input[b19] == 'و') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\signs.wav" + "'")

                    elif ((input[a19] == 'ِ') and (input[b19] == 'ة') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\65-ب.wav" + "'")

                    elif ((input[a19] == 'ِ') and (input[b19] == 'ر') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\72-ب.wav" + "'")

                    elif ((input[a19] == 'ِ') and (input[b19] == 'ؤ') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\63-ب.wav" + "'")

                    elif ((input[a19] == 'ِ') and (input[b19] == 'ء') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\63-ب.wav" + "'")

                    elif ((input[a19] == 'ِ') and (input[b19] == 'ئ') and (input[c19] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\b\\63-ب.wav" + "'")






                    elif ((input[a19] == 'َ') and ((input[b19] == 'ا') or (input[b19] == 'ى'))):

                        self.z.append('file ' + "'" + "library\\b\\04-ب.wav" + "'")

                    elif (input[a19] == 'ُ' and input[b19] == 'و'):

                        self.z.append('file ' + "'" + "library\\b\\05-ب.wav" + "'")

                    elif (input[a19] == 'ِ' and input[b19] == 'ي'):

                        self.z.append('file ' + "'" + "library\\b\\06-ب.wav" + "'")

                    elif (input[a19] == 'ً'):

                        self.z.append('file ' + "'" + "library\\b\\07-ب.wav" + "'")

                    elif (input[a19] == 'ٌ'):

                        self.z.append('file ' + "'" + "library\\b\\08-ب.wav" + "'")

                    elif (input[a19] == 'ٍ'):

                        self.z.append('file ' + "'" + "library\\b\\09-ب.wav" + "'")

                    elif (input[a19] == 'َ'):

                        self.z.append('file ' + "'" + "library\\b\\01-ب.wav" + "'")

                    elif (input[a19] == 'ُ'):

                        self.z.append('file ' + "'" + "library\\b\\02-ب.wav" + "'")

                    elif (input[a19] == 'ِ'):

                        self.z.append('file ' + "'" + "library\\b\\03-ب.wav" + "'")

                    elif (input[a19] == 'ْ'):

                        self.z.append('file ' + "'" + "library\\b\\signs.wav" + "'")

                    else:

                        self.z.append('file ' + "'" + "library\\b\\signs.wav" + "'")








                else:

                    self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                a19 = 0

                b19 = 0

                d19 = 0

                c19 = 0

            elif (char == 'ي'):

                a20 = i + 1

                b20 = i + 2

                c20 = i + 3

                d20 = i + 4

                if (a20 < (len(input))):

                    if (input[a20] == '\0'):

                        self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                    elif ((input[a20] == 'َ') and (input[b20] == 'د') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\y\\20-ي.wav' + "'")

                    elif ((input[a20] == 'َ') and (input[b20] == 'ج') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\17-ي.wav" + "'")

                    elif ((input[a20] == 'َ') and (input[b20] == 'ح') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\18-ي.wav" + "'")

                    elif ((input[a20] == 'َ') and (input[b20] == 'خ') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\19-ي.wav" + "'")

                    elif ((input[a20] == 'َ') and (input[b20] == 'ه') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\36-ي.wav" + "'")

                    elif ((input[a20] == 'َ') and (input[b20] == 'ع') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\28-ي.wav" + "'")

                    elif ((input[a20] == 'َ') and (input[b20] == 'غ') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\29-ي.wav" + "'")

                    elif ((input[a20] == 'َ') and (input[b20] == 'ف') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\30-ي.wav" + "'")

                    elif ((input[a20] == 'َ') and (input[b20] == 'ق') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\31-ي.wav" + "'")

                    elif ((input[a20] == 'َ') and (input[b20] == 'ث') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\16-ي.wav" + "'")

                    elif ((input[a20] == 'َ') and (input[b20] == 'ص') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\25-ي.wav" + "'")

                    elif ((input[a20] == 'َ') and (input[b20] == 'ض') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\26-ي.wav" + "'")

                    elif ((input[a20] == 'َ') and (input[b20] == 'ذ') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\21-ي.wav" + "'")

                    elif ((input[a20] == 'َ') and (input[b20] == 'ط') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\27-ي.wav" + "'")

                    elif ((input[a20] == 'َ') and (input[b20] == 'ك') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\32-ي.wav" + "'")

                    elif ((input[a20] == 'َ') and (input[b20] == 'م') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\34-ي.wav" + "'")

                    elif ((input[a20] == 'َ') and (input[b20] == 'ن') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\35-ي.wav" + "'")

                    elif ((input[a20] == 'َ') and (input[b20] == 'ت') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\15-ي.wav" + "'")

                    elif ((input[a20] == 'َ') and (input[b20] == 'أ') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\13-ي.wav" + "'")

                    elif ((input[a20] == 'َ') and (input[b20] == 'ل') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\33-ي.wav" + "'")

                    elif ((input[a20] == 'َ') and (input[b20] == 'ب') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\14-ي.wav" + "'")

                    elif ((input[a20] == 'َ') and (input[b20] == 'ي') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\37-ي.wav" + "'")

                    elif ((input[a20] == 'َ') and (input[b20] == 'س') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\23-ي.wav" + "'")

                    elif ((input[a20] == 'َ') and (input[b20] == 'ش') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\24-ي.wav" + "'")

                    elif ((input[a20] == 'َ') and (input[b20] == 'ظ') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\26-ي.wav" + "'")

                    elif ((input[a20] == 'َ') and (input[b20] == 'ز') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\z1.wav" + "'")

                    elif ((input[a20] == 'َ') and (input[b20] == 'و') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\signs.wav" + "'")

                    elif ((input[a20] == 'َ') and (input[b20] == 'ة') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\15-ي.wav" + "'")

                    elif ((input[a20] == 'َ') and (input[b20] == 'ر') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\22-ي.wav" + "'")

                    elif ((input[a20] == 'َ') and (input[b20] == 'ؤ') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\13-ي.wav" + "'")

                    elif ((input[a20] == 'َ') and (input[b20] == 'ء') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\13-ي.wav" + "'")

                    elif ((input[a20] == 'َ') and (input[b20] == 'ئ') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\13-ي.wav" + "'")



                    elif ((input[a20] == 'ُ') and (input[b20] == 'د') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\45-ي.wav" + "'")

                    elif ((input[a20] == 'ُ') and (input[b20] == 'ج') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\42-ي.wav" + "'")

                    elif ((input[a20] == 'ُ') and (input[b20] == 'ح') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\43-ي.wav" + "'")

                    elif ((input[a20] == 'ُ') and (input[b20] == 'خ') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\44-ي.wav" + "'")

                    elif ((input[a20] == 'ُ') and (input[b20] == 'ه') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\61-ي.wav" + "'")

                    elif ((input[a20] == 'ُ') and (input[b20] == 'ع') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\53-ي.wav" + "'")

                    elif ((input[a20] == 'ُ') and (input[b20] == 'غ') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\54-ي.wav" + "'")

                    elif ((input[a20] == 'ُ') and (input[b20] == 'ف') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\55-ي.wav" + "'")

                    elif ((input[a20] == 'ُ') and (input[b20] == 'ق') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\56-ي.wav" + "'")

                    elif ((input[a20] == 'ُ') and (input[b20] == 'ث') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\41-ي.wav" + "'")

                    elif ((input[a20] == 'ُ') and (input[b20] == 'ص') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\50-ي.wav" + "'")

                    elif ((input[a20] == 'ُ') and (input[b20] == 'ض') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\51-ي.wav" + "'")

                    elif ((input[a20] == 'ُ') and (input[b20] == 'ذ') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\46-ي.wav" + "'")

                    elif ((input[a20] == 'ُ') and (input[b20] == 'ط') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\52-ي.wav" + "'")

                    elif ((input[a20] == 'ُ') and (input[b20] == 'ك') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\57-ي.wav" + "'")

                    elif ((input[a20] == 'ُ') and (input[b20] == 'م') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\59-ي.wav" + "'")

                    elif ((input[a20] == 'ُ') and (input[b20] == 'ن') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\60-ي.wav" + "'")

                    elif ((input[a20] == 'ُ') and (input[b20] == 'ت') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\40-ي.wav" + "'")

                    elif ((input[a20] == 'ُ') and (input[b20] == 'أ') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\38-ي.wav" + "'")

                    elif ((input[a20] == 'ُ') and (input[b20] == 'ل') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\58-ي.wav" + "'")

                    elif ((input[a20] == 'ُ') and (input[b20] == 'ب') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\39-ي.wav" + "'")

                    elif ((input[a20] == 'ُ') and (input[b20] == 'ي') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\62-ي.wav" + "'")

                    elif ((input[a20] == 'ُ') and (input[b20] == 'س') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\48-ي.wav" + "'")

                    elif ((input[a20] == 'ُ') and (input[b20] == 'ش') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\49-ي.wav" + "'")

                    elif ((input[a20] == 'ُ') and (input[b20] == 'ظ') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\51-ي.wav" + "'")

                    elif ((input[a20] == 'ُ') and (input[b20] == 'ز') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\z2.wav" + "'")

                    elif ((input[a20] == 'ُ') and (input[b20] == 'و') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\signs.wav" + "'")

                    elif ((input[a20] == 'ُ') and (input[b20] == 'ة') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\40-ي.wav" + "'")

                    elif ((input[a20] == 'ُ') and (input[b20] == 'ر') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\47-ي.wav" + "'")

                    elif ((input[a20] == 'ُ') and (input[b20] == 'ؤ') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\38-ي.wav" + "'")

                    elif ((input[a20] == 'ُ') and (input[b20] == 'ء') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\38-ي.wav" + "'")

                    elif ((input[a20] == 'ُ') and (input[b20] == 'ئ') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\38-ي.wav" + "'")




                    elif ((input[a20] == 'ِ') and (input[b20] == 'د') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\70-ي.wav" + "'")

                    elif ((input[a20] == 'ِ') and (input[b20] == 'ج') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\67-ي.wav" + "'")

                    elif ((input[a20] == 'ِ') and (input[b20] == 'ح') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\68-ي.wav" + "'")

                    elif ((input[a20] == 'ِ') and (input[b20] == 'خ') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\69-ي.wav" + "'")

                    elif ((input[a20] == 'ِ') and (input[b20] == 'ه') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\86-ي.wav" + "'")

                    elif ((input[a20] == 'ِ') and (input[b20] == 'ع') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\78-ي.wav" + "'")

                    elif ((input[a20] == 'ِ') and (input[b20] == 'غ') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\79-ي.wav" + "'")

                    elif ((input[a20] == 'ِ') and (input[b20] == 'ف') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\80-ي.wav" + "'")

                    elif ((input[a20] == 'ِ') and (input[b20] == 'ق') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\81-ي.wav" + "'")

                    elif ((input[a20] == 'ِ') and (input[b20] == 'ث') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\66-ي.wav" + "'")

                    elif ((input[a20] == 'ِ') and (input[b20] == 'ص') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\75-ي.wav" + "'")

                    elif ((input[a20] == 'ِ') and (input[b20] == 'ض') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\76-ي.wav" + "'")

                    elif ((input[a20] == 'ِ') and (input[b20] == 'ذ') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\71-ي.wav" + "'")

                    elif ((input[a20] == 'ِ') and (input[b20] == 'ط') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\77-ي.wav" + "'")

                    elif ((input[a20] == 'ِ') and (input[b20] == 'ك') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\82-ي.wav" + "'")

                    elif ((input[a20] == 'ِ') and (input[b20] == 'م') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\84-ي.wav" + "'")

                    elif ((input[a20] == 'ِ') and (input[b20] == 'ن') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\85-ي.wav" + "'")

                    elif ((input[a20] == 'ِ') and (input[b20] == 'ت') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\65-ي.wav" + "'")

                    elif ((input[a20] == 'ِ') and (input[b20] == 'أ') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\63-ي.wav" + "'")

                    elif ((input[a20] == 'ِ') and (input[b20] == 'ل') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\83-ي.wav" + "'")

                    elif ((input[a20] == 'ِ') and (input[b20] == 'ب') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\64-ي.wav" + "'")

                    elif ((input[a20] == 'ِ') and (input[b20] == 'ي') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\87-ي.wav" + "'")

                    elif ((input[a20] == 'ِ') and (input[b20] == 'س') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\73-ي.wav" + "'")

                    elif ((input[a20] == 'ِ') and (input[b20] == 'ش') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\74-ي.wav" + "'")

                    elif ((input[a20] == 'ِ') and (input[b20] == 'ظ') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\76-ي.wav" + "'")

                    elif ((input[a20] == 'ِ') and (input[b20] == 'ز') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\z3.wav" + "'")

                    elif ((input[a20] == 'ِ') and (input[b20] == 'و') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\signs.wav" + "'")

                    elif ((input[a20] == 'ِ') and (input[b20] == 'ة') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\65-ي.wav" + "'")

                    elif ((input[a20] == 'ِ') and (input[b20] == 'ر') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\72-ي.wav" + "'")

                    elif ((input[a20] == 'ِ') and (input[b20] == 'ؤ') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\63-ي.wav" + "'")

                    elif ((input[a20] == 'ِ') and (input[b20] == 'ء') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\63-ي.wav" + "'")

                    elif ((input[a20] == 'ِ') and (input[b20] == 'ئ') and (input[c20] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\y\\63-ي.wav" + "'")






                    elif ((input[a20] == 'َ') and ((input[b20] == 'ا') or (input[b20] == 'ى'))):

                        self.z.append('file ' + "'" + "library\\y\\04-ي.wav" + "'")

                    elif (input[a20] == 'ُ' and input[b20] == 'و'):

                        self.z.append('file ' + "'" + "library\\y\\05-ي.wav" + "'")

                    elif (input[a20] == 'ِ' and input[b20] == 'ي'):

                        self.z.append('file ' + "'" + "library\\y\\06-ي.wav" + "'")

                    elif (input[a20] == 'ً'):

                        self.z.append('file ' + "'" + "library\\y\\07-ي.wav" + "'")

                    elif (input[a20] == 'ٌ'):

                        self.z.append('file ' + "'" + "library\\y\\08-ي.wav" + "'")

                    elif (input[a20] == 'ٍ'):

                        self.z.append('file ' + "'" + "library\\y\\09-ي.wav" + "'")

                    elif (input[a20] == 'َ'):

                        self.z.append('file ' + "'" + "library\\y\\01-ي.wav" + "'")

                    elif (input[a20] == 'ُ'):

                        self.z.append('file ' + "'" + "library\\y\\02-ي.wav" + "'")

                    elif (input[a20] == 'ِ'):

                        self.z.append('file ' + "'" + "library\\y\\03-ي.wav" + "'")

                    elif (input[a20] == 'ْ'):

                        self.z.append('file ' + "'" + "library\\y\\signs.wav" + "'")

                    else:

                        self.z.append('file ' + "'" + "library\\y\\signs.wav" + "'")








                else:

                    self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                a20 = 0

                b20 = 0

                d20 = 0

                c20 = 0

            elif (char == 'س'):

                a21 = i + 1

                b21 = i + 2

                c21 = i + 3

                d21 = i + 4

                if (a21 < (len(input))):

                    if (input[a21] == '\0'):

                        self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                    elif ((input[a21] == 'َ') and (input[b21] == 'د') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\s\\20-س.wav' + "'")

                    elif ((input[a21] == 'َ') and (input[b21] == 'ج') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\17-س.wav" + "'")

                    elif ((input[a21] == 'َ') and (input[b21] == 'ح') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\18-س.wav" + "'")

                    elif ((input[a21] == 'َ') and (input[b21] == 'خ') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\19-س.wav" + "'")

                    elif ((input[a21] == 'َ') and (input[b21] == 'ه') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\36-س.wav" + "'")

                    elif ((input[a21] == 'َ') and (input[b21] == 'ع') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\28-س.wav" + "'")

                    elif ((input[a21] == 'َ') and (input[b21] == 'غ') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\29-س.wav" + "'")

                    elif ((input[a21] == 'َ') and (input[b21] == 'ف') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\30-س.wav" + "'")

                    elif ((input[a21] == 'َ') and (input[b21] == 'ق') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\31-س.wav" + "'")

                    elif ((input[a21] == 'َ') and (input[b21] == 'ث') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\16-س.wav" + "'")

                    elif ((input[a21] == 'َ') and (input[b21] == 'ص') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\25-س.wav" + "'")

                    elif ((input[a21] == 'َ') and (input[b21] == 'ض') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\26-س.wav" + "'")

                    elif ((input[a21] == 'َ') and (input[b21] == 'ذ') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\21-س.wav" + "'")

                    elif ((input[a21] == 'َ') and (input[b21] == 'ط') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\27-س.wav" + "'")

                    elif ((input[a21] == 'َ') and (input[b21] == 'ك') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\32-س.wav" + "'")

                    elif ((input[a21] == 'َ') and (input[b21] == 'م') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\34-س.wav" + "'")

                    elif ((input[a21] == 'َ') and (input[b21] == 'ن') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\35-س.wav" + "'")

                    elif ((input[a21] == 'َ') and (input[b21] == 'ت') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\15-س.wav" + "'")

                    elif ((input[a21] == 'َ') and (input[b21] == 'أ') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\13-س.wav" + "'")

                    elif ((input[a21] == 'َ') and (input[b21] == 'ل') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\33-س.wav" + "'")

                    elif ((input[a21] == 'َ') and (input[b21] == 'ب') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\14-س.wav" + "'")

                    elif ((input[a21] == 'َ') and (input[b21] == 'ي') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\37-س.wav" + "'")

                    elif ((input[a21] == 'َ') and (input[b21] == 'س') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\23-س.wav" + "'")

                    elif ((input[a21] == 'َ') and (input[b21] == 'ش') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\24-س.wav" + "'")

                    elif ((input[a21] == 'َ') and (input[b21] == 'ظ') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\26-س.wav" + "'")

                    elif ((input[a21] == 'َ') and (input[b21] == 'ز') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\z1.wav" + "'")

                    elif ((input[a21] == 'َ') and (input[b21] == 'و') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\signs.wav" + "'")

                    elif ((input[a21] == 'َ') and (input[b21] == 'ة') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\15-س.wav" + "'")

                    elif ((input[a21] == 'َ') and (input[b21] == 'ر') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\22-س.wav" + "'")

                    elif ((input[a21] == 'َ') and (input[b21] == 'ؤ') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\13-س.wav" + "'")

                    elif ((input[a21] == 'َ') and (input[b21] == 'ء') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\13-س.wav" + "'")

                    elif ((input[a21] == 'َ') and (input[b21] == 'ئ') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\13-س.wav" + "'")



                    elif ((input[a21] == 'ُ') and (input[b21] == 'د') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\45-س.wav" + "'")

                    elif ((input[a21] == 'ُ') and (input[b21] == 'ج') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\42-س.wav" + "'")

                    elif ((input[a21] == 'ُ') and (input[b21] == 'ح') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\43-س.wav" + "'")

                    elif ((input[a21] == 'ُ') and (input[b21] == 'خ') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\44-س.wav" + "'")

                    elif ((input[a21] == 'ُ') and (input[b21] == 'ه') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\61-س.wav" + "'")

                    elif ((input[a21] == 'ُ') and (input[b21] == 'ع') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\53-س.wav" + "'")

                    elif ((input[a21] == 'ُ') and (input[b21] == 'غ') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\54-س.wav" + "'")

                    elif ((input[a21] == 'ُ') and (input[b21] == 'ف') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\55-س.wav" + "'")

                    elif ((input[a21] == 'ُ') and (input[b21] == 'ق') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\56-س.wav" + "'")

                    elif ((input[a21] == 'ُ') and (input[b21] == 'ث') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\41-س.wav" + "'")

                    elif ((input[a21] == 'ُ') and (input[b21] == 'ص') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\50-س.wav" + "'")

                    elif ((input[a21] == 'ُ') and (input[b21] == 'ض') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\51-س.wav" + "'")

                    elif ((input[a21] == 'ُ') and (input[b21] == 'ذ') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\46-س.wav" + "'")

                    elif ((input[a21] == 'ُ') and (input[b21] == 'ط') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\52-س.wav" + "'")

                    elif ((input[a21] == 'ُ') and (input[b21] == 'ك') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\57-س.wav" + "'")

                    elif ((input[a21] == 'ُ') and (input[b21] == 'م') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\59-س.wav" + "'")

                    elif ((input[a21] == 'ُ') and (input[b21] == 'ن') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\60-س.wav" + "'")

                    elif ((input[a21] == 'ُ') and (input[b21] == 'ت') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\40-س.wav" + "'")

                    elif ((input[a21] == 'ُ') and (input[b21] == 'أ') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\38-س.wav" + "'")

                    elif ((input[a21] == 'ُ') and (input[b21] == 'ل') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\58-س.wav" + "'")

                    elif ((input[a21] == 'ُ') and (input[b21] == 'ب') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\39-س.wav" + "'")

                    elif ((input[a21] == 'ُ') and (input[b21] == 'ي') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\62-س.wav" + "'")

                    elif ((input[a21] == 'ُ') and (input[b21] == 'س') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\48-س.wav" + "'")

                    elif ((input[a21] == 'ُ') and (input[b21] == 'ش') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\49-س.wav" + "'")

                    elif ((input[a21] == 'ُ') and (input[b21] == 'ظ') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\51-س.wav" + "'")

                    elif ((input[a21] == 'ُ') and (input[b21] == 'ز') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\z2.wav" + "'")

                    elif ((input[a21] == 'ُ') and (input[b21] == 'و') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\signs.wav" + "'")

                    elif ((input[a21] == 'ُ') and (input[b21] == 'ة') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\40-س.wav" + "'")

                    elif ((input[a21] == 'ُ') and (input[b21] == 'ر') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\47-س.wav" + "'")

                    elif ((input[a21] == 'ُ') and (input[b21] == 'ؤ') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\38-س.wav" + "'")

                    elif ((input[a21] == 'ُ') and (input[b21] == 'ء') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\38-س.wav" + "'")

                    elif ((input[a21] == 'ُ') and (input[b21] == 'ئ') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\38-س.wav" + "'")




                    elif ((input[a21] == 'ِ') and (input[b21] == 'د') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\70-س.wav" + "'")

                    elif ((input[a21] == 'ِ') and (input[b21] == 'ج') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\67-س.wav" + "'")

                    elif ((input[a21] == 'ِ') and (input[b21] == 'ح') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\68-س.wav" + "'")

                    elif ((input[a21] == 'ِ') and (input[b21] == 'خ') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\69-س.wav" + "'")

                    elif ((input[a21] == 'ِ') and (input[b21] == 'ه') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\86-س.wav" + "'")

                    elif ((input[a21] == 'ِ') and (input[b21] == 'ع') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\78-س.wav" + "'")

                    elif ((input[a21] == 'ِ') and (input[b21] == 'غ') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\79-س.wav" + "'")

                    elif ((input[a21] == 'ِ') and (input[b21] == 'ف') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\80-س.wav" + "'")

                    elif ((input[a21] == 'ِ') and (input[b21] == 'ق') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\81-س.wav" + "'")

                    elif ((input[a21] == 'ِ') and (input[b21] == 'ث') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\66-س.wav" + "'")

                    elif ((input[a21] == 'ِ') and (input[b21] == 'ص') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\75-س.wav" + "'")

                    elif ((input[a21] == 'ِ') and (input[b21] == 'ض') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\76-س.wav" + "'")

                    elif ((input[a21] == 'ِ') and (input[b21] == 'ذ') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\71-س.wav" + "'")

                    elif ((input[a21] == 'ِ') and (input[b21] == 'ط') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\77-س.wav" + "'")

                    elif ((input[a21] == 'ِ') and (input[b21] == 'ك') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\82-س.wav" + "'")

                    elif ((input[a21] == 'ِ') and (input[b21] == 'م') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\84-س.wav" + "'")

                    elif ((input[a21] == 'ِ') and (input[b21] == 'ن') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\85-س.wav" + "'")

                    elif ((input[a21] == 'ِ') and (input[b21] == 'ت') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\65-س.wav" + "'")

                    elif ((input[a21] == 'ِ') and (input[b21] == 'أ') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\63-س.wav" + "'")

                    elif ((input[a21] == 'ِ') and (input[b21] == 'ل') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\83-س.wav" + "'")

                    elif ((input[a21] == 'ِ') and (input[b21] == 'ب') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\64-س.wav" + "'")

                    elif ((input[a21] == 'ِ') and (input[b21] == 'ي') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\87-س.wav" + "'")

                    elif ((input[a21] == 'ِ') and (input[b21] == 'س') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\73-س.wav" + "'")

                    elif ((input[a21] == 'ِ') and (input[b21] == 'ش') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\74-س.wav" + "'")

                    elif ((input[a21] == 'ِ') and (input[b21] == 'ظ') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\76-س.wav" + "'")

                    elif ((input[a21] == 'ِ') and (input[b21] == 'ز') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\z3.wav" + "'")

                    elif ((input[a21] == 'ِ') and (input[b21] == 'و') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\signs.wav" + "'")

                    elif ((input[a21] == 'ِ') and (input[b21] == 'ة') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\65-س.wav" + "'")

                    elif ((input[a21] == 'ِ') and (input[b21] == 'ر') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\72-س.wav" + "'")

                    elif ((input[a21] == 'ِ') and (input[b21] == 'ؤ') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\63-س.wav" + "'")

                    elif ((input[a21] == 'ِ') and (input[b21] == 'ء') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\63-س.wav" + "'")

                    elif ((input[a21] == 'ِ') and (input[b21] == 'ئ') and (input[c21] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\s\\63-س.wav" + "'")






                    elif ((input[a21] == 'َ') and ((input[b21] == 'ا') or (input[b21] == 'ى'))):

                        self.z.append('file ' + "'" + "library\\s\\04-س.wav" + "'")

                    elif (input[a21] == 'ُ' and input[b21] == 'و'):

                        self.z.append('file ' + "'" + "library\\s\\05-س.wav" + "'")

                    elif (input[a21] == 'ِ' and input[b21] == 'ي'):

                        self.z.append('file ' + "'" + "library\\s\\06-س.wav" + "'")

                    elif (input[a21] == 'ً'):

                        self.z.append('file ' + "'" + "library\\s\\07-س.wav" + "'")

                    elif (input[a21] == 'ٌ'):

                        self.z.append('file ' + "'" + "library\\s\\08-س.wav" + "'")

                    elif (input[a21] == 'ٍ'):

                        self.z.append('file ' + "'" + "library\\s\\09-س.wav" + "'")

                    elif (input[a21] == 'َ'):

                        self.z.append('file ' + "'" + "library\\s\\01-س.wav" + "'")

                    elif (input[a21] == 'ُ'):

                        self.z.append('file ' + "'" + "library\\s\\02-س.wav" + "'")

                    elif (input[a21] == 'ِ'):

                        self.z.append('file ' + "'" + "library\\s\\03-س.wav" + "'")

                    elif (input[a21] == 'ْ'):

                        self.z.append('file ' + "'" + "library\\s\\signs.wav" + "'")

                    else:

                        self.z.append('file ' + "'" + "library\\s\\signs.wav" + "'")








                else:

                    self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                a21 = 0

                b21 = 0

                d21 = 0

                c21 = 0

            elif (char == 'ش'):

                a22 = i + 1

                b22 = i + 2

                c22 = i + 3

                d22 = i + 4

                if (a22 < (len(input))):

                    if (input[a22] == '\0'):

                        self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                    elif ((input[a22] == 'َ') and (input[b22] == 'د') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\ch\\20-ش.wav' + "'")

                    elif ((input[a22] == 'َ') and (input[b22] == 'ج') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\17-ش.wav" + "'")

                    elif ((input[a22] == 'َ') and (input[b22] == 'ح') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\18-ش.wav" + "'")

                    elif ((input[a22] == 'َ') and (input[b22] == 'خ') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\19-ش.wav" + "'")

                    elif ((input[a22] == 'َ') and (input[b22] == 'ه') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\36-ش.wav" + "'")

                    elif ((input[a22] == 'َ') and (input[b22] == 'ع') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\28-ش.wav" + "'")

                    elif ((input[a22] == 'َ') and (input[b22] == 'غ') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\29-ش.wav" + "'")

                    elif ((input[a22] == 'َ') and (input[b22] == 'ف') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\30-ش.wav" + "'")

                    elif ((input[a22] == 'َ') and (input[b22] == 'ق') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\31-ش.wav" + "'")

                    elif ((input[a22] == 'َ') and (input[b22] == 'ث') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\16-ش.wav" + "'")

                    elif ((input[a22] == 'َ') and (input[b22] == 'ص') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\25-ش.wav" + "'")

                    elif ((input[a22] == 'َ') and (input[b22] == 'ض') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\26-ش.wav" + "'")

                    elif ((input[a22] == 'َ') and (input[b22] == 'ذ') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\21-ش.wav" + "'")

                    elif ((input[a22] == 'َ') and (input[b22] == 'ط') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\27-ش.wav" + "'")

                    elif ((input[a22] == 'َ') and (input[b22] == 'ك') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\32-ش.wav" + "'")

                    elif ((input[a22] == 'َ') and (input[b22] == 'م') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\34-ش.wav" + "'")

                    elif ((input[a22] == 'َ') and (input[b22] == 'ن') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\35-ش.wav" + "'")

                    elif ((input[a22] == 'َ') and (input[b22] == 'ت') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\15-ش.wav" + "'")

                    elif ((input[a22] == 'َ') and (input[b22] == 'أ') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\13-ش.wav" + "'")

                    elif ((input[a22] == 'َ') and (input[b22] == 'ل') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\33-ش.wav" + "'")

                    elif ((input[a22] == 'َ') and (input[b22] == 'ب') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\14-ش.wav" + "'")

                    elif ((input[a22] == 'َ') and (input[b22] == 'ي') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\37-ش.wav" + "'")

                    elif ((input[a22] == 'َ') and (input[b22] == 'س') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\23-ش.wav" + "'")

                    elif ((input[a22] == 'َ') and (input[b22] == 'ش') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\24-ش.wav" + "'")

                    elif ((input[a22] == 'َ') and (input[b22] == 'ظ') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\26-ش.wav" + "'")

                    elif ((input[a22] == 'َ') and (input[b22] == 'ز') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\z1.wav" + "'")

                    elif ((input[a22] == 'َ') and (input[b22] == 'و') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\signs.wav" + "'")

                    elif ((input[a22] == 'َ') and (input[b22] == 'ة') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\15-ش.wav" + "'")

                    elif ((input[a22] == 'َ') and (input[b22] == 'ر') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\22-ش.wav" + "'")

                    elif ((input[a22] == 'َ') and (input[b22] == 'ؤ') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\13-ش.wav" + "'")

                    elif ((input[a22] == 'َ') and (input[b22] == 'ء') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\13-ش.wav" + "'")

                    elif ((input[a22] == 'َ') and (input[b22] == 'ئ') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\13-ش.wav" + "'")



                    elif ((input[a22] == 'ُ') and (input[b22] == 'د') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\45-ش.wav" + "'")

                    elif ((input[a22] == 'ُ') and (input[b22] == 'ج') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\42-ش.wav" + "'")

                    elif ((input[a22] == 'ُ') and (input[b22] == 'ح') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\43-ش.wav" + "'")

                    elif ((input[a22] == 'ُ') and (input[b22] == 'خ') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\44-ش.wav" + "'")

                    elif ((input[a22] == 'ُ') and (input[b22] == 'ه') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\61-ش.wav" + "'")

                    elif ((input[a22] == 'ُ') and (input[b22] == 'ع') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\53-ش.wav" + "'")

                    elif ((input[a22] == 'ُ') and (input[b22] == 'غ') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\54-ش.wav" + "'")

                    elif ((input[a22] == 'ُ') and (input[b22] == 'ف') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\55-ش.wav" + "'")

                    elif ((input[a22] == 'ُ') and (input[b22] == 'ق') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\56-ش.wav" + "'")

                    elif ((input[a22] == 'ُ') and (input[b22] == 'ث') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\41-ش.wav" + "'")

                    elif ((input[a22] == 'ُ') and (input[b22] == 'ص') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\50-ش.wav" + "'")

                    elif ((input[a22] == 'ُ') and (input[b22] == 'ض') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\51-ش.wav" + "'")

                    elif ((input[a22] == 'ُ') and (input[b22] == 'ذ') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\46-ش.wav" + "'")

                    elif ((input[a22] == 'ُ') and (input[b22] == 'ط') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\52-ش.wav" + "'")

                    elif ((input[a22] == 'ُ') and (input[b22] == 'ك') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\57-ش.wav" + "'")

                    elif ((input[a22] == 'ُ') and (input[b22] == 'م') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\59-ش.wav" + "'")

                    elif ((input[a22] == 'ُ') and (input[b22] == 'ن') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\60-ش.wav" + "'")

                    elif ((input[a22] == 'ُ') and (input[b22] == 'ت') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\40-ش.wav" + "'")

                    elif ((input[a22] == 'ُ') and (input[b22] == 'أ') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\38-ش.wav" + "'")

                    elif ((input[a22] == 'ُ') and (input[b22] == 'ل') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\58-ش.wav" + "'")

                    elif ((input[a22] == 'ُ') and (input[b22] == 'ب') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\39-ش.wav" + "'")

                    elif ((input[a22] == 'ُ') and (input[b22] == 'ي') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\62-ش.wav" + "'")

                    elif ((input[a22] == 'ُ') and (input[b22] == 'س') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\48-ش.wav" + "'")

                    elif ((input[a22] == 'ُ') and (input[b22] == 'ش') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\49-ش.wav" + "'")

                    elif ((input[a22] == 'ُ') and (input[b22] == 'ظ') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\51-ش.wav" + "'")

                    elif ((input[a22] == 'ُ') and (input[b22] == 'ز') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\z2.wav" + "'")

                    elif ((input[a22] == 'ُ') and (input[b22] == 'و') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\signs.wav" + "'")

                    elif ((input[a22] == 'ُ') and (input[b22] == 'ة') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\40-ش.wav" + "'")

                    elif ((input[a22] == 'ُ') and (input[b22] == 'ر') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\47-ش.wav" + "'")

                    elif ((input[a22] == 'ُ') and (input[b22] == 'ؤ') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\38-ش.wav" + "'")

                    elif ((input[a22] == 'ُ') and (input[b22] == 'ء') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\38-ش.wav" + "'")

                    elif ((input[a22] == 'ُ') and (input[b22] == 'ئ') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\38-ش.wav" + "'")




                    elif ((input[a22] == 'ِ') and (input[b22] == 'د') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\70-ش.wav" + "'")

                    elif ((input[a22] == 'ِ') and (input[b22] == 'ج') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\67-ش.wav" + "'")

                    elif ((input[a22] == 'ِ') and (input[b22] == 'ح') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\68-ش.wav" + "'")

                    elif ((input[a22] == 'ِ') and (input[b22] == 'خ') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\69-ش.wav" + "'")

                    elif ((input[a22] == 'ِ') and (input[b22] == 'ه') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\86-ش.wav" + "'")

                    elif ((input[a22] == 'ِ') and (input[b22] == 'ع') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\78-ش.wav" + "'")

                    elif ((input[a22] == 'ِ') and (input[b22] == 'غ') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\79-ش.wav" + "'")

                    elif ((input[a22] == 'ِ') and (input[b22] == 'ف') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\80-ش.wav" + "'")

                    elif ((input[a22] == 'ِ') and (input[b22] == 'ق') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\81-ش.wav" + "'")

                    elif ((input[a22] == 'ِ') and (input[b22] == 'ث') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\66-ش.wav" + "'")

                    elif ((input[a22] == 'ِ') and (input[b22] == 'ص') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\75-ش.wav" + "'")

                    elif ((input[a22] == 'ِ') and (input[b22] == 'ض') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\76-ش.wav" + "'")

                    elif ((input[a22] == 'ِ') and (input[b22] == 'ذ') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\71-ش.wav" + "'")

                    elif ((input[a22] == 'ِ') and (input[b22] == 'ط') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\77-ش.wav" + "'")

                    elif ((input[a22] == 'ِ') and (input[b22] == 'ك') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\82-ش.wav" + "'")

                    elif ((input[a22] == 'ِ') and (input[b22] == 'م') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\84-ش.wav" + "'")

                    elif ((input[a22] == 'ِ') and (input[b22] == 'ن') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\85-ش.wav" + "'")

                    elif ((input[a22] == 'ِ') and (input[b22] == 'ت') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\65-ش.wav" + "'")

                    elif ((input[a22] == 'ِ') and (input[b22] == 'أ') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\63-ش.wav" + "'")

                    elif ((input[a22] == 'ِ') and (input[b22] == 'ل') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\83-ش.wav" + "'")

                    elif ((input[a22] == 'ِ') and (input[b22] == 'ب') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\64-ش.wav" + "'")

                    elif ((input[a22] == 'ِ') and (input[b22] == 'ي') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\87-ش.wav" + "'")

                    elif ((input[a22] == 'ِ') and (input[b22] == 'س') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\73-ش.wav" + "'")

                    elif ((input[a22] == 'ِ') and (input[b22] == 'ش') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\74-ش.wav" + "'")

                    elif ((input[a22] == 'ِ') and (input[b22] == 'ظ') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\76-ش.wav" + "'")

                    elif ((input[a22] == 'ِ') and (input[b22] == 'ز') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\z3.wav" + "'")

                    elif ((input[a22] == 'ِ') and (input[b22] == 'و') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\signs.wav" + "'")

                    elif ((input[a22] == 'ِ') and (input[b22] == 'ة') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\65-ش.wav" + "'")

                    elif ((input[a22] == 'ِ') and (input[b22] == 'ر') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\72-ش.wav" + "'")

                    elif ((input[a22] == 'ِ') and (input[b22] == 'ؤ') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\63-ش.wav" + "'")

                    elif ((input[a22] == 'ِ') and (input[b22] == 'ء') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\63-ش.wav" + "'")

                    elif ((input[a22] == 'ِ') and (input[b22] == 'ئ') and (input[c22] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\ch\\63-ش.wav" + "'")






                    elif ((input[a22] == 'َ') and ((input[b22] == 'ا') or (input[b22] == 'ى'))):

                        self.z.append('file ' + "'" + "library\\ch\\04-ش.wav" + "'")

                    elif (input[a22] == 'ُ' and input[b22] == 'و'):

                        self.z.append('file ' + "'" + "library\\ch\\05-ش.wav" + "'")

                    elif (input[a22] == 'ِ' and input[b22] == 'ي'):

                        self.z.append('file ' + "'" + "library\\ch\\06-ش.wav" + "'")

                    elif (input[a22] == 'ً'):

                        self.z.append('file ' + "'" + "library\\ch\\07-ش.wav" + "'")

                    elif (input[a22] == 'ٌ'):

                        self.z.append('file ' + "'" + "library\\ch\\08-ش.wav" + "'")

                    elif (input[a22] == 'ٍ'):

                        self.z.append('file ' + "'" + "library\\ch\\09-ش.wav" + "'")

                    elif (input[a22] == 'َ'):

                        self.z.append('file ' + "'" + "library\\ch\\01-ش.wav" + "'")

                    elif (input[a22] == 'ُ'):

                        self.z.append('file ' + "'" + "library\\ch\\02-ش.wav" + "'")

                    elif (input[a22] == 'ِ'):

                        self.z.append('file ' + "'" + "library\\ch\\03-ش.wav" + "'")

                    elif (input[a22] == 'ْ'):

                        self.z.append('file ' + "'" + "library\\ch\\signs.wav" + "'")

                    else:

                        self.z.append('file ' + "'" + "library\\ch\\signs.wav" + "'")








                else:

                    self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                a22 = 0

                b22 = 0

                d22 = 0

                c22 = 0

            elif (char == 'ظ'):

                a23 = i + 1

                b23 = i + 2

                c23 = i + 3

                d23 = i + 4

                if (a23 < (len(input))):

                    if (input[a23] == '\0'):

                        self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                    elif ((input[a23] == 'َ') and (input[b23] == 'د') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\dha\\20-ض.wav' + "'")

                    elif ((input[a23] == 'َ') and (input[b23] == 'ج') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\17-ض.wav" + "'")

                    elif ((input[a23] == 'َ') and (input[b23] == 'ح') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\18-ض.wav" + "'")

                    elif ((input[a23] == 'َ') and (input[b23] == 'خ') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\19-ض.wav" + "'")

                    elif ((input[a23] == 'َ') and (input[b23] == 'ه') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\36-ض.wav" + "'")

                    elif ((input[a23] == 'َ') and (input[b23] == 'ع') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\28-ض.wav" + "'")

                    elif ((input[a23] == 'َ') and (input[b23] == 'غ') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\29-ض.wav" + "'")

                    elif ((input[a23] == 'َ') and (input[b23] == 'ف') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\30-ض.wav" + "'")

                    elif ((input[a23] == 'َ') and (input[b23] == 'ق') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\31-ض.wav" + "'")

                    elif ((input[a23] == 'َ') and (input[b23] == 'ث') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\16-ض.wav" + "'")

                    elif ((input[a23] == 'َ') and (input[b23] == 'ص') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\25-ض.wav" + "'")

                    elif ((input[a23] == 'َ') and (input[b23] == 'ض') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\26-ض.wav" + "'")

                    elif ((input[a23] == 'َ') and (input[b23] == 'ذ') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\21-ض.wav" + "'")

                    elif ((input[a23] == 'َ') and (input[b23] == 'ط') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\27-ض.wav" + "'")

                    elif ((input[a23] == 'َ') and (input[b23] == 'ك') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\32-ض.wav" + "'")

                    elif ((input[a23] == 'َ') and (input[b23] == 'م') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\34-ض.wav" + "'")

                    elif ((input[a23] == 'َ') and (input[b23] == 'ن') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\35-ض.wav" + "'")

                    elif ((input[a23] == 'َ') and (input[b23] == 'ت') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\15-ض.wav" + "'")

                    elif ((input[a23] == 'َ') and (input[b23] == 'أ') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\13-ض.wav" + "'")

                    elif ((input[a23] == 'َ') and (input[b23] == 'ل') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\33-ض.wav" + "'")

                    elif ((input[a23] == 'َ') and (input[b23] == 'ب') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\14-ض.wav" + "'")

                    elif ((input[a23] == 'َ') and (input[b23] == 'ي') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\37-ض.wav" + "'")

                    elif ((input[a23] == 'َ') and (input[b23] == 'س') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\23-ض.wav" + "'")

                    elif ((input[a23] == 'َ') and (input[b23] == 'ش') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\24-ض.wav" + "'")

                    elif ((input[a23] == 'َ') and (input[b23] == 'ظ') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\26-ض.wav" + "'")

                    elif ((input[a23] == 'َ') and (input[b23] == 'ز') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\z1.wav" + "'")

                    elif ((input[a23] == 'َ') and (input[b23] == 'و') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\signs.wav" + "'")

                    elif ((input[a23] == 'َ') and (input[b23] == 'ة') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\15-ض.wav" + "'")

                    elif ((input[a23] == 'َ') and (input[b23] == 'ر') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\22-ض.wav" + "'")

                    elif ((input[a23] == 'َ') and (input[b23] == 'ؤ') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\13-ض.wav" + "'")

                    elif ((input[a23] == 'َ') and (input[b23] == 'ء') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\13-ض.wav" + "'")

                    elif ((input[a23] == 'َ') and (input[b23] == 'ئ') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\13-ض.wav" + "'")



                    elif ((input[a23] == 'ُ') and (input[b23] == 'د') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\45-ض.wav" + "'")

                    elif ((input[a23] == 'ُ') and (input[b23] == 'ج') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\42-ض.wav" + "'")

                    elif ((input[a23] == 'ُ') and (input[b23] == 'ح') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\43-ض.wav" + "'")

                    elif ((input[a23] == 'ُ') and (input[b23] == 'خ') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\44-ض.wav" + "'")

                    elif ((input[a23] == 'ُ') and (input[b23] == 'ه') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\61-ض.wav" + "'")

                    elif ((input[a23] == 'ُ') and (input[b23] == 'ع') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\53-ض.wav" + "'")

                    elif ((input[a23] == 'ُ') and (input[b23] == 'غ') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\54-ض.wav" + "'")

                    elif ((input[a23] == 'ُ') and (input[b23] == 'ف') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\55-ض.wav" + "'")

                    elif ((input[a23] == 'ُ') and (input[b23] == 'ق') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\56-ض.wav" + "'")

                    elif ((input[a23] == 'ُ') and (input[b23] == 'ث') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\41-ض.wav" + "'")

                    elif ((input[a23] == 'ُ') and (input[b23] == 'ص') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\50-ض.wav" + "'")

                    elif ((input[a23] == 'ُ') and (input[b23] == 'ض') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\51-ض.wav" + "'")

                    elif ((input[a23] == 'ُ') and (input[b23] == 'ذ') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\46-ض.wav" + "'")

                    elif ((input[a23] == 'ُ') and (input[b23] == 'ط') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\52-ض.wav" + "'")

                    elif ((input[a23] == 'ُ') and (input[b23] == 'ك') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\57-ض.wav" + "'")

                    elif ((input[a23] == 'ُ') and (input[b23] == 'م') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\59-ض.wav" + "'")

                    elif ((input[a23] == 'ُ') and (input[b23] == 'ن') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\60-ض.wav" + "'")

                    elif ((input[a23] == 'ُ') and (input[b23] == 'ت') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\40-ض.wav" + "'")

                    elif ((input[a23] == 'ُ') and (input[b23] == 'أ') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\38-ض.wav" + "'")

                    elif ((input[a23] == 'ُ') and (input[b23] == 'ل') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\58-ض.wav" + "'")

                    elif ((input[a23] == 'ُ') and (input[b23] == 'ب') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\39-ض.wav" + "'")

                    elif ((input[a23] == 'ُ') and (input[b23] == 'ي') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\62-ض.wav" + "'")

                    elif ((input[a23] == 'ُ') and (input[b23] == 'س') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\48-ض.wav" + "'")

                    elif ((input[a23] == 'ُ') and (input[b23] == 'ش') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\49-ض.wav" + "'")

                    elif ((input[a23] == 'ُ') and (input[b23] == 'ظ') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\51-ض.wav" + "'")

                    elif ((input[a23] == 'ُ') and (input[b23] == 'ز') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\z2.wav" + "'")

                    elif ((input[a23] == 'ُ') and (input[b23] == 'و') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\signs.wav" + "'")

                    elif ((input[a23] == 'ُ') and (input[b23] == 'ة') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\40-ض.wav" + "'")

                    elif ((input[a23] == 'ُ') and (input[b23] == 'ر') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\47-ض.wav" + "'")

                    elif ((input[a23] == 'ُ') and (input[b23] == 'ؤ') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\38-ض.wav" + "'")

                    elif ((input[a23] == 'ُ') and (input[b23] == 'ء') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\38-ض.wav" + "'")

                    elif ((input[a23] == 'ُ') and (input[b23] == 'ئ') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\38-ض.wav" + "'")




                    elif ((input[a23] == 'ِ') and (input[b23] == 'د') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\70-ض.wav" + "'")

                    elif ((input[a23] == 'ِ') and (input[b23] == 'ج') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\67-ض.wav" + "'")

                    elif ((input[a23] == 'ِ') and (input[b23] == 'ح') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\68-ض.wav" + "'")

                    elif ((input[a23] == 'ِ') and (input[b23] == 'خ') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\69-ض.wav" + "'")

                    elif ((input[a23] == 'ِ') and (input[b23] == 'ه') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\86-ض.wav" + "'")

                    elif ((input[a23] == 'ِ') and (input[b23] == 'ع') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\78-ض.wav" + "'")

                    elif ((input[a23] == 'ِ') and (input[b23] == 'غ') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\79-ض.wav" + "'")

                    elif ((input[a23] == 'ِ') and (input[b23] == 'ف') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\80-ض.wav" + "'")

                    elif ((input[a23] == 'ِ') and (input[b23] == 'ق') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\81-ض.wav" + "'")

                    elif ((input[a23] == 'ِ') and (input[b23] == 'ث') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\66-ض.wav" + "'")

                    elif ((input[a23] == 'ِ') and (input[b23] == 'ص') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\75-ض.wav" + "'")

                    elif ((input[a23] == 'ِ') and (input[b23] == 'ض') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\76-ض.wav" + "'")

                    elif ((input[a23] == 'ِ') and (input[b23] == 'ذ') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\71-ض.wav" + "'")

                    elif ((input[a23] == 'ِ') and (input[b23] == 'ط') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\77-ض.wav" + "'")

                    elif ((input[a23] == 'ِ') and (input[b23] == 'ك') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\82-ض.wav" + "'")

                    elif ((input[a23] == 'ِ') and (input[b23] == 'م') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\84-ض.wav" + "'")

                    elif ((input[a23] == 'ِ') and (input[b23] == 'ن') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\85-ض.wav" + "'")

                    elif ((input[a23] == 'ِ') and (input[b23] == 'ت') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\65-ض.wav" + "'")

                    elif ((input[a23] == 'ِ') and (input[b23] == 'أ') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\63-ض.wav" + "'")

                    elif ((input[a23] == 'ِ') and (input[b23] == 'ل') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\83-ض.wav" + "'")

                    elif ((input[a23] == 'ِ') and (input[b23] == 'ب') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\64-ض.wav" + "'")

                    elif ((input[a23] == 'ِ') and (input[b23] == 'ي') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\87-ض.wav" + "'")

                    elif ((input[a23] == 'ِ') and (input[b23] == 'س') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\73-ض.wav" + "'")

                    elif ((input[a23] == 'ِ') and (input[b23] == 'ش') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\74-ض.wav" + "'")

                    elif ((input[a23] == 'ِ') and (input[b23] == 'ظ') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\76-ض.wav" + "'")

                    elif ((input[a23] == 'ِ') and (input[b23] == 'ز') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\z3.wav" + "'")

                    elif ((input[a23] == 'ِ') and (input[b23] == 'و') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\signs.wav" + "'")

                    elif ((input[a23] == 'ِ') and (input[b23] == 'ة') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\65-ض.wav" + "'")

                    elif ((input[a23] == 'ِ') and (input[b23] == 'ر') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\72-ض.wav" + "'")

                    elif ((input[a23] == 'ِ') and (input[b23] == 'ؤ') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\63-ض.wav" + "'")

                    elif ((input[a23] == 'ِ') and (input[b23] == 'ء') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\63-ض.wav" + "'")

                    elif ((input[a23] == 'ِ') and (input[b23] == 'ئ') and (input[c23] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\dha\\63-ض.wav" + "'")






                    elif ((input[a23] == 'َ') and ((input[b23] == 'ا') or (input[b23] == 'ى'))):

                        self.z.append('file ' + "'" + "library\\dha\\04-ض.wav" + "'")

                    elif (input[a23] == 'ُ' and input[b23] == 'و'):

                        self.z.append('file ' + "'" + "library\\dha\\05-ض.wav" + "'")

                    elif (input[a23] == 'ِ' and input[b23] == 'ي'):

                        self.z.append('file ' + "'" + "library\\dha\\06-ض.wav" + "'")

                    elif (input[a23] == 'ً'):

                        self.z.append('file ' + "'" + "library\\dha\\07-ض.wav" + "'")

                    elif (input[a23] == 'ٌ'):

                        self.z.append('file ' + "'" + "library\\dha\\08-ض.wav" + "'")

                    elif (input[a23] == 'ٍ'):

                        self.z.append('file ' + "'" + "library\\dha\\09-ض.wav" + "'")

                    elif (input[a23] == 'َ'):

                        self.z.append('file ' + "'" + "library\\dha\\01-ض.wav" + "'")

                    elif (input[a23] == 'ُ'):

                        self.z.append('file ' + "'" + "library\\dha\\02-ض.wav" + "'")

                    elif (input[a23] == 'ِ'):

                        self.z.append('file ' + "'" + "library\\dha\\03-ض.wav" + "'")

                    elif (input[a23] == 'ْ'):

                        self.z.append('file ' + "'" + "library\\dha\\signs.wav" + "'")

                    else:

                        self.z.append('file ' + "'" + "library\\dha\\signs.wav" + "'")








                else:

                    self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                a23 = 0

                b23 = 0

                d23 = 0

                c23 = 0

            elif (char == 'ة'):

                a24 = i + 1

                b24 = i + 2

                c24 = i + 3

                d24 = i + 4

                if (a24 < (len(input))):

                    if (input[a24] == '\0'):

                        self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                    elif ((input[a24] == 'َ') and (input[b24] == 'د') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\t\\20-ت.wav' + "'")

                    elif ((input[a24] == 'َ') and (input[b24] == 'ج') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\17-ت.wav" + "'")

                    elif ((input[a24] == 'َ') and (input[b24] == 'ح') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\18-ت.wav" + "'")

                    elif ((input[a24] == 'َ') and (input[b24] == 'خ') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\19-ت.wav" + "'")

                    elif ((input[a24] == 'َ') and (input[b24] == 'ه') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\36-ت.wav" + "'")

                    elif ((input[a24] == 'َ') and (input[b24] == 'ع') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\28-ت.wav" + "'")

                    elif ((input[a24] == 'َ') and (input[b24] == 'غ') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\29-ت.wav" + "'")

                    elif ((input[a24] == 'َ') and (input[b24] == 'ف') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\30-ت.wav" + "'")

                    elif ((input[a24] == 'َ') and (input[b24] == 'ق') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\31-ت.wav" + "'")

                    elif ((input[a24] == 'َ') and (input[b24] == 'ث') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\16-ت.wav" + "'")

                    elif ((input[a24] == 'َ') and (input[b24] == 'ص') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\25-ت.wav" + "'")

                    elif ((input[a24] == 'َ') and (input[b24] == 'ض') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\26-ت.wav" + "'")

                    elif ((input[a24] == 'َ') and (input[b24] == 'ذ') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\21-ت.wav" + "'")

                    elif ((input[a24] == 'َ') and (input[b24] == 'ط') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\27-ت.wav" + "'")

                    elif ((input[a24] == 'َ') and (input[b24] == 'ك') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\32-ت.wav" + "'")

                    elif ((input[a24] == 'َ') and (input[b24] == 'م') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\34-ت.wav" + "'")

                    elif ((input[a24] == 'َ') and (input[b24] == 'ن') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\35-ت.wav" + "'")

                    elif ((input[a24] == 'َ') and (input[b24] == 'ت') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\15-ت.wav" + "'")

                    elif ((input[a24] == 'َ') and (input[b24] == 'أ') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\13-ت.wav" + "'")

                    elif ((input[a24] == 'َ') and (input[b24] == 'ل') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\33-ت.wav" + "'")

                    elif ((input[a24] == 'َ') and (input[b24] == 'ب') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\14-ت.wav" + "'")

                    elif ((input[a24] == 'َ') and (input[b24] == 'ي') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\37-ت.wav" + "'")

                    elif ((input[a24] == 'َ') and (input[b24] == 'س') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\23-ت.wav" + "'")

                    elif ((input[a24] == 'َ') and (input[b24] == 'ش') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\24-ت.wav" + "'")

                    elif ((input[a24] == 'َ') and (input[b24] == 'ظ') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\26-ت.wav" + "'")

                    elif ((input[a24] == 'َ') and (input[b24] == 'ز') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\z1.wav" + "'")

                    elif ((input[a24] == 'َ') and (input[b24] == 'و') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\signs.wav" + "'")

                    elif ((input[a24] == 'َ') and (input[b24] == 'ة') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\15-ت.wav" + "'")

                    elif ((input[a24] == 'َ') and (input[b24] == 'ر') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\22-ت.wav" + "'")

                    elif ((input[a24] == 'َ') and (input[b24] == 'ؤ') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\13-ت.wav" + "'")

                    elif ((input[a24] == 'َ') and (input[b24] == 'ء') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\13-ت.wav" + "'")

                    elif ((input[a24] == 'َ') and (input[b24] == 'ئ') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\13-ت.wav" + "'")



                    elif ((input[a24] == 'ُ') and (input[b24] == 'د') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\45-ت.wav" + "'")

                    elif ((input[a24] == 'ُ') and (input[b24] == 'ج') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\42-ت.wav" + "'")

                    elif ((input[a24] == 'ُ') and (input[b24] == 'ح') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\43-ت.wav" + "'")

                    elif ((input[a24] == 'ُ') and (input[b24] == 'خ') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\44-ت.wav" + "'")

                    elif ((input[a24] == 'ُ') and (input[b24] == 'ه') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\61-ت.wav" + "'")

                    elif ((input[a24] == 'ُ') and (input[b24] == 'ع') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\53-ت.wav" + "'")

                    elif ((input[a24] == 'ُ') and (input[b24] == 'غ') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\54-ت.wav" + "'")

                    elif ((input[a24] == 'ُ') and (input[b24] == 'ف') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\55-ت.wav" + "'")

                    elif ((input[a24] == 'ُ') and (input[b24] == 'ق') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\56-ت.wav" + "'")

                    elif ((input[a24] == 'ُ') and (input[b24] == 'ث') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\41-ت.wav" + "'")

                    elif ((input[a24] == 'ُ') and (input[b24] == 'ص') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\50-ت.wav" + "'")

                    elif ((input[a24] == 'ُ') and (input[b24] == 'ض') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\51-ت.wav" + "'")

                    elif ((input[a24] == 'ُ') and (input[b24] == 'ذ') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\46-ت.wav" + "'")

                    elif ((input[a24] == 'ُ') and (input[b24] == 'ط') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\52-ت.wav" + "'")

                    elif ((input[a24] == 'ُ') and (input[b24] == 'ك') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\57-ت.wav" + "'")

                    elif ((input[a24] == 'ُ') and (input[b24] == 'م') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\59-ت.wav" + "'")

                    elif ((input[a24] == 'ُ') and (input[b24] == 'ن') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\60-ت.wav" + "'")

                    elif ((input[a24] == 'ُ') and (input[b24] == 'ت') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\40-ت.wav" + "'")

                    elif ((input[a24] == 'ُ') and (input[b24] == 'أ') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\38-ت.wav" + "'")

                    elif ((input[a24] == 'ُ') and (input[b24] == 'ل') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\58-ت.wav" + "'")

                    elif ((input[a24] == 'ُ') and (input[b24] == 'ب') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\39-ت.wav" + "'")

                    elif ((input[a24] == 'ُ') and (input[b24] == 'ي') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\62-ت.wav" + "'")

                    elif ((input[a24] == 'ُ') and (input[b24] == 'س') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\48-ت.wav" + "'")

                    elif ((input[a24] == 'ُ') and (input[b24] == 'ش') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\49-ت.wav" + "'")

                    elif ((input[a24] == 'ُ') and (input[b24] == 'ظ') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\51-ت.wav" + "'")

                    elif ((input[a24] == 'ُ') and (input[b24] == 'ز') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\z2.wav" + "'")

                    elif ((input[a24] == 'ُ') and (input[b24] == 'و') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\signs.wav" + "'")

                    elif ((input[a24] == 'ُ') and (input[b24] == 'ة') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\40-ت.wav" + "'")

                    elif ((input[a24] == 'ُ') and (input[b24] == 'ر') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\47-ت.wav" + "'")

                    elif ((input[a24] == 'ُ') and (input[b24] == 'ؤ') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\38-ت.wav" + "'")

                    elif ((input[a24] == 'ُ') and (input[b24] == 'ء') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\38-ت.wav" + "'")

                    elif ((input[a24] == 'ُ') and (input[b24] == 'ئ') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\38-ت.wav" + "'")




                    elif ((input[a24] == 'ِ') and (input[b24] == 'د') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\70-ت.wav" + "'")

                    elif ((input[a24] == 'ِ') and (input[b24] == 'ج') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\67-ت.wav" + "'")

                    elif ((input[a24] == 'ِ') and (input[b24] == 'ح') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\68-ت.wav" + "'")

                    elif ((input[a24] == 'ِ') and (input[b24] == 'خ') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\69-ت.wav" + "'")

                    elif ((input[a24] == 'ِ') and (input[b24] == 'ه') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\86-ت.wav" + "'")

                    elif ((input[a24] == 'ِ') and (input[b24] == 'ع') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\78-ت.wav" + "'")

                    elif ((input[a24] == 'ِ') and (input[b24] == 'غ') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\79-ت.wav" + "'")

                    elif ((input[a24] == 'ِ') and (input[b24] == 'ف') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\80-ت.wav" + "'")

                    elif ((input[a24] == 'ِ') and (input[b24] == 'ق') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\81-ت.wav" + "'")

                    elif ((input[a24] == 'ِ') and (input[b24] == 'ث') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\66-ت.wav" + "'")

                    elif ((input[a24] == 'ِ') and (input[b24] == 'ص') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\75-ت.wav" + "'")

                    elif ((input[a24] == 'ِ') and (input[b24] == 'ض') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\76-ت.wav" + "'")

                    elif ((input[a24] == 'ِ') and (input[b24] == 'ذ') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\71-ت.wav" + "'")

                    elif ((input[a24] == 'ِ') and (input[b24] == 'ط') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\77-ت.wav" + "'")

                    elif ((input[a24] == 'ِ') and (input[b24] == 'ك') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\82-ت.wav" + "'")

                    elif ((input[a24] == 'ِ') and (input[b24] == 'م') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\84-ت.wav" + "'")

                    elif ((input[a24] == 'ِ') and (input[b24] == 'ن') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\85-ت.wav" + "'")

                    elif ((input[a24] == 'ِ') and (input[b24] == 'ت') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\65-ت.wav" + "'")

                    elif ((input[a24] == 'ِ') and (input[b24] == 'أ') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\63-ت.wav" + "'")

                    elif ((input[a24] == 'ِ') and (input[b24] == 'ل') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\83-ت.wav" + "'")

                    elif ((input[a24] == 'ِ') and (input[b24] == 'ب') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\64-ت.wav" + "'")

                    elif ((input[a24] == 'ِ') and (input[b24] == 'ي') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\87-ت.wav" + "'")

                    elif ((input[a24] == 'ِ') and (input[b24] == 'س') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\73-ت.wav" + "'")

                    elif ((input[a24] == 'ِ') and (input[b24] == 'ش') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\74-ت.wav" + "'")

                    elif ((input[a24] == 'ِ') and (input[b24] == 'ظ') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\76-ت.wav" + "'")

                    elif ((input[a24] == 'ِ') and (input[b24] == 'ز') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\z3.wav" + "'")

                    elif ((input[a24] == 'ِ') and (input[b24] == 'و') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\signs.wav" + "'")

                    elif ((input[a24] == 'ِ') and (input[b24] == 'ة') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\65-ت.wav" + "'")

                    elif ((input[a24] == 'ِ') and (input[b24] == 'ر') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\72-ت.wav" + "'")

                    elif ((input[a24] == 'ِ') and (input[b24] == 'ؤ') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\63-ت.wav" + "'")

                    elif ((input[a24] == 'ِ') and (input[b24] == 'ء') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\63-ت.wav" + "'")

                    elif ((input[a24] == 'ِ') and (input[b24] == 'ئ') and (input[c24] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\t\\63-ت.wav" + "'")






                    elif ((input[a24] == 'َ') and ((input[b24] == 'ا') or (input[b24] == 'ى'))):

                        self.z.append('file ' + "'" + "library\\t\\04-ت.wav" + "'")

                    elif (input[a24] == 'ُ' and input[b24] == 'و'):

                        self.z.append('file ' + "'" + "library\\t\\05-ت.wav" + "'")

                    elif (input[a24] == 'ِ' and input[b24] == 'ي'):

                        self.z.append('file ' + "'" + "library\\t\\06-ت.wav" + "'")

                    elif (input[a24] == 'ً'):

                        self.z.append('file ' + "'" + "library\\t\\07-ت.wav" + "'")

                    elif (input[a24] == 'ٌ'):

                        self.z.append('file ' + "'" + "library\\t\\08-ت.wav" + "'")

                    elif (input[a24] == 'ٍ'):

                        self.z.append('file ' + "'" + "library\\t\\09-ت.wav" + "'")

                    elif (input[a24] == 'َ'):

                        self.z.append('file ' + "'" + "library\\t\\01-ت.wav" + "'")

                    elif (input[a24] == 'ُ'):

                        self.z.append('file ' + "'" + "library\\t\\02-ت.wav" + "'")

                    elif (input[a24] == 'ِ'):

                        self.z.append('file ' + "'" + "library\\t\\03-ت.wav" + "'")

                    elif (input[a24] == 'ْ'):

                        self.z.append('file ' + "'" + "library\\t\\signs.wav" + "'")

                    else:

                        self.z.append('file ' + "'" + "library\\t\\signs.wav" + "'")








                else:

                    self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                a24 = 0

                b24 = 0

                d24 = 0

                c24 = 0

            elif (char == 'ر'):

                a25 = i + 1

                b25 = i + 2

                c25 = i + 3

                d25 = i + 4

                if (a25 < (len(input))):

                    if (input[a25] == '\0'):

                        self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                    elif ((input[a25] == 'َ') and (input[b25] == 'د') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\r\\20-ر.wav' + "'")

                    elif ((input[a25] == 'َ') and (input[b25] == 'ج') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\17-ر.wav" + "'")

                    elif ((input[a25] == 'َ') and (input[b25] == 'ح') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\18-ر.wav" + "'")

                    elif ((input[a25] == 'َ') and (input[b25] == 'خ') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\19-ر.wav" + "'")

                    elif ((input[a25] == 'َ') and (input[b25] == 'ه') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\36-ر.wav" + "'")

                    elif ((input[a25] == 'َ') and (input[b25] == 'ع') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\28-ر.wav" + "'")

                    elif ((input[a25] == 'َ') and (input[b25] == 'غ') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\29-ر.wav" + "'")

                    elif ((input[a25] == 'َ') and (input[b25] == 'ف') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\30-ر.wav" + "'")

                    elif ((input[a25] == 'َ') and (input[b25] == 'ق') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\31-ر.wav" + "'")

                    elif ((input[a25] == 'َ') and (input[b25] == 'ث') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\16-ر.wav" + "'")

                    elif ((input[a25] == 'َ') and (input[b25] == 'ص') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\25-ر.wav" + "'")

                    elif ((input[a25] == 'َ') and (input[b25] == 'ض') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\26-ر.wav" + "'")

                    elif ((input[a25] == 'َ') and (input[b25] == 'ذ') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\21-ر.wav" + "'")

                    elif ((input[a25] == 'َ') and (input[b25] == 'ط') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\27-ر.wav" + "'")

                    elif ((input[a25] == 'َ') and (input[b25] == 'ك') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\32-ر.wav" + "'")

                    elif ((input[a25] == 'َ') and (input[b25] == 'م') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\34-ر.wav" + "'")

                    elif ((input[a25] == 'َ') and (input[b25] == 'ن') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\35-ر.wav" + "'")

                    elif ((input[a25] == 'َ') and (input[b25] == 'ت') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\15-ر.wav" + "'")

                    elif ((input[a25] == 'َ') and (input[b25] == 'أ') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\13-ر.wav" + "'")

                    elif ((input[a25] == 'َ') and (input[b25] == 'ل') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\33-ر.wav" + "'")

                    elif ((input[a25] == 'َ') and (input[b25] == 'ب') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\14-ر.wav" + "'")

                    elif ((input[a25] == 'َ') and (input[b25] == 'ي') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\37-ر.wav" + "'")

                    elif ((input[a25] == 'َ') and (input[b25] == 'س') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\23-ر.wav" + "'")

                    elif ((input[a25] == 'َ') and (input[b25] == 'ش') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\24-ر.wav" + "'")

                    elif ((input[a25] == 'َ') and (input[b25] == 'ظ') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\26-ر.wav" + "'")

                    elif ((input[a25] == 'َ') and (input[b25] == 'ز') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\z1.wav" + "'")

                    elif ((input[a25] == 'َ') and (input[b25] == 'و') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\signs.wav" + "'")

                    elif ((input[a25] == 'َ') and (input[b25] == 'ة') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\15-ر.wav" + "'")

                    elif ((input[a25] == 'َ') and (input[b25] == 'ر') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\22-ر.wav" + "'")

                    elif ((input[a25] == 'َ') and (input[b25] == 'ؤ') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\13-ر.wav" + "'")

                    elif ((input[a25] == 'َ') and (input[b25] == 'ء') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\13-ر.wav" + "'")

                    elif ((input[a25] == 'َ') and (input[b25] == 'ئ') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\13-ر.wav" + "'")



                    elif ((input[a25] == 'ُ') and (input[b25] == 'د') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\45-ر.wav" + "'")

                    elif ((input[a25] == 'ُ') and (input[b25] == 'ج') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\42-ر.wav" + "'")

                    elif ((input[a25] == 'ُ') and (input[b25] == 'ح') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\43-ر.wav" + "'")

                    elif ((input[a25] == 'ُ') and (input[b25] == 'خ') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\44-ر.wav" + "'")

                    elif ((input[a25] == 'ُ') and (input[b25] == 'ه') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\61-ر.wav" + "'")

                    elif ((input[a25] == 'ُ') and (input[b25] == 'ع') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\53-ر.wav" + "'")

                    elif ((input[a25] == 'ُ') and (input[b25] == 'غ') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\54-ر.wav" + "'")

                    elif ((input[a25] == 'ُ') and (input[b25] == 'ف') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\55-ر.wav" + "'")

                    elif ((input[a25] == 'ُ') and (input[b25] == 'ق') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\56-ر.wav" + "'")

                    elif ((input[a25] == 'ُ') and (input[b25] == 'ث') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\41-ر.wav" + "'")

                    elif ((input[a25] == 'ُ') and (input[b25] == 'ص') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\50-ر.wav" + "'")

                    elif ((input[a25] == 'ُ') and (input[b25] == 'ض') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\51-ر.wav" + "'")

                    elif ((input[a25] == 'ُ') and (input[b25] == 'ذ') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\46-ر.wav" + "'")

                    elif ((input[a25] == 'ُ') and (input[b25] == 'ط') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\52-ر.wav" + "'")

                    elif ((input[a25] == 'ُ') and (input[b25] == 'ك') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\57-ر.wav" + "'")

                    elif ((input[a25] == 'ُ') and (input[b25] == 'م') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\59-ر.wav" + "'")

                    elif ((input[a25] == 'ُ') and (input[b25] == 'ن') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\60-ر.wav" + "'")

                    elif ((input[a25] == 'ُ') and (input[b25] == 'ت') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\40-ر.wav" + "'")

                    elif ((input[a25] == 'ُ') and (input[b25] == 'أ') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\38-ر.wav" + "'")

                    elif ((input[a25] == 'ُ') and (input[b25] == 'ل') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\58-ر.wav" + "'")

                    elif ((input[a25] == 'ُ') and (input[b25] == 'ب') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\39-ر.wav" + "'")

                    elif ((input[a25] == 'ُ') and (input[b25] == 'ي') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\62-ر.wav" + "'")

                    elif ((input[a25] == 'ُ') and (input[b25] == 'س') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\48-ر.wav" + "'")

                    elif ((input[a25] == 'ُ') and (input[b25] == 'ش') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\49-ر.wav" + "'")

                    elif ((input[a25] == 'ُ') and (input[b25] == 'ظ') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\51-ر.wav" + "'")

                    elif ((input[a25] == 'ُ') and (input[b25] == 'ز') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\z2.wav" + "'")

                    elif ((input[a25] == 'ُ') and (input[b25] == 'و') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\signs.wav" + "'")

                    elif ((input[a25] == 'ُ') and (input[b25] == 'ة') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\40-ر.wav" + "'")

                    elif ((input[a25] == 'ُ') and (input[b25] == 'ر') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\47-ر.wav" + "'")

                    elif ((input[a25] == 'ُ') and (input[b25] == 'ؤ') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\38-ر.wav" + "'")

                    elif ((input[a25] == 'ُ') and (input[b25] == 'ء') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\38-ر.wav" + "'")

                    elif ((input[a25] == 'ُ') and (input[b25] == 'ئ') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\38-ر.wav" + "'")




                    elif ((input[a25] == 'ِ') and (input[b25] == 'د') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\70-ر.wav" + "'")

                    elif ((input[a25] == 'ِ') and (input[b25] == 'ج') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\67-ر.wav" + "'")

                    elif ((input[a25] == 'ِ') and (input[b25] == 'ح') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\68-ر.wav" + "'")

                    elif ((input[a25] == 'ِ') and (input[b25] == 'خ') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\69-ر.wav" + "'")

                    elif ((input[a25] == 'ِ') and (input[b25] == 'ه') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\86-ر.wav" + "'")

                    elif ((input[a25] == 'ِ') and (input[b25] == 'ع') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\78-ر.wav" + "'")

                    elif ((input[a25] == 'ِ') and (input[b25] == 'غ') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\79-ر.wav" + "'")

                    elif ((input[a25] == 'ِ') and (input[b25] == 'ف') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\80-ر.wav" + "'")

                    elif ((input[a25] == 'ِ') and (input[b25] == 'ق') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\81-ر.wav" + "'")

                    elif ((input[a25] == 'ِ') and (input[b25] == 'ث') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\66-ر.wav" + "'")

                    elif ((input[a25] == 'ِ') and (input[b25] == 'ص') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\75-ر.wav" + "'")

                    elif ((input[a25] == 'ِ') and (input[b25] == 'ض') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\76-ر.wav" + "'")

                    elif ((input[a25] == 'ِ') and (input[b25] == 'ذ') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\71-ر.wav" + "'")

                    elif ((input[a25] == 'ِ') and (input[b25] == 'ط') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\77-ر.wav" + "'")

                    elif ((input[a25] == 'ِ') and (input[b25] == 'ك') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\82-ر.wav" + "'")

                    elif ((input[a25] == 'ِ') and (input[b25] == 'م') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\84-ر.wav" + "'")

                    elif ((input[a25] == 'ِ') and (input[b25] == 'ن') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\85-ر.wav" + "'")

                    elif ((input[a25] == 'ِ') and (input[b25] == 'ت') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\65-ر.wav" + "'")

                    elif ((input[a25] == 'ِ') and (input[b25] == 'أ') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\63-ر.wav" + "'")

                    elif ((input[a25] == 'ِ') and (input[b25] == 'ل') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\83-ر.wav" + "'")

                    elif ((input[a25] == 'ِ') and (input[b25] == 'ب') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\64-ر.wav" + "'")

                    elif ((input[a25] == 'ِ') and (input[b25] == 'ي') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\87-ر.wav" + "'")

                    elif ((input[a25] == 'ِ') and (input[b25] == 'س') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\73-ر.wav" + "'")

                    elif ((input[a25] == 'ِ') and (input[b25] == 'ش') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\74-ر.wav" + "'")

                    elif ((input[a25] == 'ِ') and (input[b25] == 'ظ') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\76-ر.wav" + "'")

                    elif ((input[a25] == 'ِ') and (input[b25] == 'ز') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\z3.wav" + "'")

                    elif ((input[a25] == 'ِ') and (input[b25] == 'و') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\signs.wav" + "'")

                    elif ((input[a25] == 'ِ') and (input[b25] == 'ة') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\65-ر.wav" + "'")

                    elif ((input[a25] == 'ِ') and (input[b25] == 'ر') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\72-ر.wav" + "'")

                    elif ((input[a25] == 'ِ') and (input[b25] == 'ؤ') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\63-ر.wav" + "'")

                    elif ((input[a25] == 'ِ') and (input[b25] == 'ء') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\63-ر.wav" + "'")

                    elif ((input[a25] == 'ِ') and (input[b25] == 'ئ') and (input[c25] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\r\\63-ر.wav" + "'")






                    elif ((input[a25] == 'َ') and ((input[b25] == 'ا') or (input[b25] == 'ى'))):

                        self.z.append('file ' + "'" + "library\\r\\04-ر.wav" + "'")

                    elif (input[a25] == 'ُ' and input[b25] == 'و'):

                        self.z.append('file ' + "'" + "library\\r\\05-ر.wav" + "'")

                    elif (input[a25] == 'ِ' and input[b25] == 'ي'):

                        self.z.append('file ' + "'" + "library\\r\\06-ر.wav" + "'")

                    elif (input[a25] == 'ً'):

                        self.z.append('file ' + "'" + "library\\r\\07-ر.wav" + "'")

                    elif (input[a25] == 'ٌ'):

                        self.z.append('file ' + "'" + "library\\r\\08-ر.wav" + "'")

                    elif (input[a25] == 'ٍ'):

                        self.z.append('file ' + "'" + "library\\r\\09-ر.wav" + "'")

                    elif (input[a25] == 'َ'):

                        self.z.append('file ' + "'" + "library\\r\\01-ر.wav" + "'")

                    elif (input[a25] == 'ُ'):

                        self.z.append('file ' + "'" + "library\\r\\02-ر.wav" + "'")

                    elif (input[a25] == 'ِ'):

                        self.z.append('file ' + "'" + "library\\r\\03-ر.wav" + "'")

                    elif (input[a25] == 'ْ'):

                        self.z.append('file ' + "'" + "library\\r\\signs.wav" + "'")

                    else:

                        self.z.append('file ' + "'" + "library\\r\\signs.wav" + "'")








                else:

                    self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                a25 = 0

                b25 = 0

                d25 = 0

                c25 = 0

            elif (char == 'ؤ'):

                a26 = i + 1

                b26 = i + 2

                c26 = i + 3

                d26 = i + 4

                if (a26 < (len(input))):

                    if (input[a26] == '\0'):

                        self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                    elif ((input[a26] == 'َ') and (input[b26] == 'د') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\a\\20-أ.wav' + "'")

                    elif ((input[a26] == 'َ') and (input[b26] == 'ج') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\17-أ.wav" + "'")

                    elif ((input[a26] == 'َ') and (input[b26] == 'ح') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\18-أ.wav" + "'")

                    elif ((input[a26] == 'َ') and (input[b26] == 'خ') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\19-أ.wav" + "'")

                    elif ((input[a26] == 'َ') and (input[b26] == 'ه') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\36-أ.wav" + "'")

                    elif ((input[a26] == 'َ') and (input[b26] == 'ع') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\28-أ.wav" + "'")

                    elif ((input[a26] == 'َ') and (input[b26] == 'غ') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\29-أ.wav" + "'")

                    elif ((input[a26] == 'َ') and (input[b26] == 'ف') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\30-أ.wav" + "'")

                    elif ((input[a26] == 'َ') and (input[b26] == 'ق') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\31-أ.wav" + "'")

                    elif ((input[a26] == 'َ') and (input[b26] == 'ث') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\16-أ.wav" + "'")

                    elif ((input[a26] == 'َ') and (input[b26] == 'ص') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\25-أ.wav" + "'")

                    elif ((input[a26] == 'َ') and (input[b26] == 'ض') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\26-أ.wav" + "'")

                    elif ((input[a26] == 'َ') and (input[b26] == 'ذ') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\21-أ.wav" + "'")

                    elif ((input[a26] == 'َ') and (input[b26] == 'ط') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\27-أ.wav" + "'")

                    elif ((input[a26] == 'َ') and (input[b26] == 'ك') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\32-أ.wav" + "'")

                    elif ((input[a26] == 'َ') and (input[b26] == 'م') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\34-أ.wav" + "'")

                    elif ((input[a26] == 'َ') and (input[b26] == 'ن') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\35-أ.wav" + "'")

                    elif ((input[a26] == 'َ') and (input[b26] == 'ت') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\15-أ.wav" + "'")

                    elif ((input[a26] == 'َ') and (input[b26] == 'أ') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\13-أ.wav" + "'")

                    elif ((input[a26] == 'َ') and (input[b26] == 'ل') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\33-أ.wav" + "'")

                    elif ((input[a26] == 'َ') and (input[b26] == 'ب') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\14-أ.wav" + "'")

                    elif ((input[a26] == 'َ') and (input[b26] == 'ي') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\37-أ.wav" + "'")

                    elif ((input[a26] == 'َ') and (input[b26] == 'س') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\23-أ.wav" + "'")

                    elif ((input[a26] == 'َ') and (input[b26] == 'ش') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\24-أ.wav" + "'")

                    elif ((input[a26] == 'َ') and (input[b26] == 'ظ') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\26-أ.wav" + "'")

                    elif ((input[a26] == 'َ') and (input[b26] == 'ز') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\z1.wav" + "'")

                    elif ((input[a26] == 'َ') and (input[b26] == 'و') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\signs.wav" + "'")

                    elif ((input[a26] == 'َ') and (input[b26] == 'ة') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\15-أ.wav" + "'")

                    elif ((input[a26] == 'َ') and (input[b26] == 'ر') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\22-أ.wav" + "'")

                    elif ((input[a26] == 'َ') and (input[b26] == 'ؤ') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\13-أ.wav" + "'")

                    elif ((input[a26] == 'َ') and (input[b26] == 'ء') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\13-أ.wav" + "'")

                    elif ((input[a26] == 'َ') and (input[b26] == 'ئ') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\13-أ.wav" + "'")



                    elif ((input[a26] == 'ُ') and (input[b26] == 'د') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\45-أ.wav" + "'")

                    elif ((input[a26] == 'ُ') and (input[b26] == 'ج') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\42-أ.wav" + "'")

                    elif ((input[a26] == 'ُ') and (input[b26] == 'ح') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\43-أ.wav" + "'")

                    elif ((input[a26] == 'ُ') and (input[b26] == 'خ') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\44-أ.wav" + "'")

                    elif ((input[a26] == 'ُ') and (input[b26] == 'ه') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\61-أ.wav" + "'")

                    elif ((input[a26] == 'ُ') and (input[b26] == 'ع') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\53-أ.wav" + "'")

                    elif ((input[a26] == 'ُ') and (input[b26] == 'غ') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\54-أ.wav" + "'")

                    elif ((input[a26] == 'ُ') and (input[b26] == 'ف') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\55-أ.wav" + "'")

                    elif ((input[a26] == 'ُ') and (input[b26] == 'ق') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\56-أ.wav" + "'")

                    elif ((input[a26] == 'ُ') and (input[b26] == 'ث') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\41-أ.wav" + "'")

                    elif ((input[a26] == 'ُ') and (input[b26] == 'ص') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\50-أ.wav" + "'")

                    elif ((input[a26] == 'ُ') and (input[b26] == 'ض') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\51-أ.wav" + "'")

                    elif ((input[a26] == 'ُ') and (input[b26] == 'ذ') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\46-أ.wav" + "'")

                    elif ((input[a26] == 'ُ') and (input[b26] == 'ط') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\52-أ.wav" + "'")

                    elif ((input[a26] == 'ُ') and (input[b26] == 'ك') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\57-أ.wav" + "'")

                    elif ((input[a26] == 'ُ') and (input[b26] == 'م') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\59-أ.wav" + "'")

                    elif ((input[a26] == 'ُ') and (input[b26] == 'ن') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\60-أ.wav" + "'")

                    elif ((input[a26] == 'ُ') and (input[b26] == 'ت') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\40-أ.wav" + "'")

                    elif ((input[a26] == 'ُ') and (input[b26] == 'أ') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\38-أ.wav" + "'")

                    elif ((input[a26] == 'ُ') and (input[b26] == 'ل') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\58-أ.wav" + "'")

                    elif ((input[a26] == 'ُ') and (input[b26] == 'ب') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\39-أ.wav" + "'")

                    elif ((input[a26] == 'ُ') and (input[b26] == 'ي') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\62-أ.wav" + "'")

                    elif ((input[a26] == 'ُ') and (input[b26] == 'س') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\48-أ.wav" + "'")

                    elif ((input[a26] == 'ُ') and (input[b26] == 'ش') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\49-أ.wav" + "'")

                    elif ((input[a26] == 'ُ') and (input[b26] == 'ظ') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\51-أ.wav" + "'")

                    elif ((input[a26] == 'ُ') and (input[b26] == 'ز') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\z2.wav" + "'")

                    elif ((input[a26] == 'ُ') and (input[b26] == 'و') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\signs.wav" + "'")

                    elif ((input[a26] == 'ُ') and (input[b26] == 'ة') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\40-أ.wav" + "'")

                    elif ((input[a26] == 'ُ') and (input[b26] == 'ر') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\47-أ.wav" + "'")

                    elif ((input[a26] == 'ُ') and (input[b26] == 'ؤ') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\38-أ.wav" + "'")

                    elif ((input[a26] == 'ُ') and (input[b26] == 'ء') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\38-أ.wav" + "'")

                    elif ((input[a26] == 'ُ') and (input[b26] == 'ئ') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\38-أ.wav" + "'")




                    elif ((input[a26] == 'ِ') and (input[b26] == 'د') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\70-أ.wav" + "'")

                    elif ((input[a26] == 'ِ') and (input[b26] == 'ج') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\67-أ.wav" + "'")

                    elif ((input[a26] == 'ِ') and (input[b26] == 'ح') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\68-أ.wav" + "'")

                    elif ((input[a26] == 'ِ') and (input[b26] == 'خ') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\69-أ.wav" + "'")

                    elif ((input[a26] == 'ِ') and (input[b26] == 'ه') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\86-أ.wav" + "'")

                    elif ((input[a26] == 'ِ') and (input[b26] == 'ع') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\78-أ.wav" + "'")

                    elif ((input[a26] == 'ِ') and (input[b26] == 'غ') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\79-أ.wav" + "'")

                    elif ((input[a26] == 'ِ') and (input[b26] == 'ف') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\80-أ.wav" + "'")

                    elif ((input[a26] == 'ِ') and (input[b26] == 'ق') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\81-أ.wav" + "'")

                    elif ((input[a26] == 'ِ') and (input[b26] == 'ث') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\66-أ.wav" + "'")

                    elif ((input[a26] == 'ِ') and (input[b26] == 'ص') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\75-أ.wav" + "'")

                    elif ((input[a26] == 'ِ') and (input[b26] == 'ض') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\76-أ.wav" + "'")

                    elif ((input[a26] == 'ِ') and (input[b26] == 'ذ') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\71-أ.wav" + "'")

                    elif ((input[a26] == 'ِ') and (input[b26] == 'ط') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\77-أ.wav" + "'")

                    elif ((input[a26] == 'ِ') and (input[b26] == 'ك') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\82-أ.wav" + "'")

                    elif ((input[a26] == 'ِ') and (input[b26] == 'م') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\84-أ.wav" + "'")

                    elif ((input[a26] == 'ِ') and (input[b26] == 'ن') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\85-أ.wav" + "'")

                    elif ((input[a26] == 'ِ') and (input[b26] == 'ت') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\65-أ.wav" + "'")

                    elif ((input[a26] == 'ِ') and (input[b26] == 'أ') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\63-أ.wav" + "'")

                    elif ((input[a26] == 'ِ') and (input[b26] == 'ل') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\83-أ.wav" + "'")

                    elif ((input[a26] == 'ِ') and (input[b26] == 'ب') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\64-أ.wav" + "'")

                    elif ((input[a26] == 'ِ') and (input[b26] == 'ي') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\87-أ.wav" + "'")

                    elif ((input[a26] == 'ِ') and (input[b26] == 'س') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\73-أ.wav" + "'")

                    elif ((input[a26] == 'ِ') and (input[b26] == 'ش') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\74-أ.wav" + "'")

                    elif ((input[a26] == 'ِ') and (input[b26] == 'ظ') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\76-أ.wav" + "'")

                    elif ((input[a26] == 'ِ') and (input[b26] == 'ز') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\z3.wav" + "'")

                    elif ((input[a26] == 'ِ') and (input[b26] == 'و') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\signs.wav" + "'")

                    elif ((input[a26] == 'ِ') and (input[b26] == 'ة') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\65-أ.wav" + "'")

                    elif ((input[a26] == 'ِ') and (input[b26] == 'ر') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\72-أ.wav" + "'")

                    elif ((input[a26] == 'ِ') and (input[b26] == 'ؤ') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\63-أ.wav" + "'")

                    elif ((input[a26] == 'ِ') and (input[b26] == 'ء') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\63-أ.wav" + "'")

                    elif ((input[a26] == 'ِ') and (input[b26] == 'ئ') and (input[c26] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\63-أ.wav" + "'")






                    elif ((input[a26] == 'َ') and ((input[b26] == 'ا') or (input[b26] == 'ى'))):

                        self.z.append('file ' + "'" + "library\\a\\04-أ.wav" + "'")

                    elif (input[a26] == 'ُ' and input[b26] == 'و'):

                        self.z.append('file ' + "'" + "library\\a\\05-أ.wav" + "'")

                    elif (input[a26] == 'ِ' and input[b26] == 'ي'):

                        self.z.append('file ' + "'" + "library\\a\\06-أ.wav" + "'")

                    elif (input[a26] == 'ً'):

                        self.z.append('file ' + "'" + "library\\a\\07-أ.wav" + "'")

                    elif (input[a26] == 'ٌ'):

                        self.z.append('file ' + "'" + "library\\a\\08-أ.wav" + "'")

                    elif (input[a26] == 'ٍ'):

                        self.z.append('file ' + "'" + "library\\a\\09-أ.wav" + "'")

                    elif (input[a26] == 'َ'):

                        self.z.append('file ' + "'" + "library\\a\\01-أ.wav" + "'")

                    elif (input[a26] == 'ُ'):

                        self.z.append('file ' + "'" + "library\\a\\02-أ.wav" + "'")

                    elif (input[a26] == 'ِ'):

                        self.z.append('file ' + "'" + "library\\a\\03-أ.wav" + "'")

                    elif (input[a26] == 'ْ'):

                        self.z.append('file ' + "'" + "library\\a\\signs.wav" + "'")

                    else:

                        self.z.append('file ' + "'" + "library\\a\\signs.wav" + "'")








                else:

                    self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                a26 = 0

                b26 = 0

                d26 = 0

                c26 = 0

            elif (char == 'ء'):

                a27 = i + 1

                b27 = i + 2

                c27 = i + 3

                d27 = i + 4

                if (a27 < (len(input))):

                    if (input[a27] == '\0'):

                        self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                    elif ((input[a27] == 'َ') and (input[b27] == 'د') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\a\\20-أ.wav' + "'")

                    elif ((input[a27] == 'َ') and (input[b27] == 'ج') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\17-أ.wav" + "'")

                    elif ((input[a27] == 'َ') and (input[b27] == 'ح') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\18-أ.wav" + "'")

                    elif ((input[a27] == 'َ') and (input[b27] == 'خ') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\19-أ.wav" + "'")

                    elif ((input[a27] == 'َ') and (input[b27] == 'ه') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\36-أ.wav" + "'")

                    elif ((input[a27] == 'َ') and (input[b27] == 'ع') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\28-أ.wav" + "'")

                    elif ((input[a27] == 'َ') and (input[b27] == 'غ') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\29-أ.wav" + "'")

                    elif ((input[a27] == 'َ') and (input[b27] == 'ف') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\30-أ.wav" + "'")

                    elif ((input[a27] == 'َ') and (input[b27] == 'ق') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\31-أ.wav" + "'")

                    elif ((input[a27] == 'َ') and (input[b27] == 'ث') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\16-أ.wav" + "'")

                    elif ((input[a27] == 'َ') and (input[b27] == 'ص') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\25-أ.wav" + "'")

                    elif ((input[a27] == 'َ') and (input[b27] == 'ض') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\26-أ.wav" + "'")

                    elif ((input[a27] == 'َ') and (input[b27] == 'ذ') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\21-أ.wav" + "'")

                    elif ((input[a27] == 'َ') and (input[b27] == 'ط') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\27-أ.wav" + "'")

                    elif ((input[a27] == 'َ') and (input[b27] == 'ك') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\32-أ.wav" + "'")

                    elif ((input[a27] == 'َ') and (input[b27] == 'م') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\34-أ.wav" + "'")

                    elif ((input[a27] == 'َ') and (input[b27] == 'ن') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\35-أ.wav" + "'")

                    elif ((input[a27] == 'َ') and (input[b27] == 'ت') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\15-أ.wav" + "'")

                    elif ((input[a27] == 'َ') and (input[b27] == 'أ') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\13-أ.wav" + "'")

                    elif ((input[a27] == 'َ') and (input[b27] == 'ل') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\33-أ.wav" + "'")

                    elif ((input[a27] == 'َ') and (input[b27] == 'ب') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\14-أ.wav" + "'")

                    elif ((input[a27] == 'َ') and (input[b27] == 'ي') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\37-أ.wav" + "'")

                    elif ((input[a27] == 'َ') and (input[b27] == 'س') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\23-أ.wav" + "'")

                    elif ((input[a27] == 'َ') and (input[b27] == 'ش') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\24-أ.wav" + "'")

                    elif ((input[a27] == 'َ') and (input[b27] == 'ظ') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\26-أ.wav" + "'")

                    elif ((input[a27] == 'َ') and (input[b27] == 'ز') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\z1.wav" + "'")

                    elif ((input[a27] == 'َ') and (input[b27] == 'و') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\signs.wav" + "'")

                    elif ((input[a27] == 'َ') and (input[b27] == 'ة') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\15-أ.wav" + "'")

                    elif ((input[a27] == 'َ') and (input[b27] == 'ر') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\22-أ.wav" + "'")

                    elif ((input[a27] == 'َ') and (input[b27] == 'ؤ') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\13-أ.wav" + "'")

                    elif ((input[a27] == 'َ') and (input[b27] == 'ء') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\13-أ.wav" + "'")

                    elif ((input[a27] == 'َ') and (input[b27] == 'ئ') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\13-أ.wav" + "'")



                    elif ((input[a27] == 'ُ') and (input[b27] == 'د') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\45-أ.wav" + "'")

                    elif ((input[a27] == 'ُ') and (input[b27] == 'ج') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\42-أ.wav" + "'")

                    elif ((input[a27] == 'ُ') and (input[b27] == 'ح') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\43-أ.wav" + "'")

                    elif ((input[a27] == 'ُ') and (input[b27] == 'خ') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\44-أ.wav" + "'")

                    elif ((input[a27] == 'ُ') and (input[b27] == 'ه') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\61-أ.wav" + "'")

                    elif ((input[a27] == 'ُ') and (input[b27] == 'ع') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\53-أ.wav" + "'")

                    elif ((input[a27] == 'ُ') and (input[b27] == 'غ') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\54-أ.wav" + "'")

                    elif ((input[a27] == 'ُ') and (input[b27] == 'ف') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\55-أ.wav" + "'")

                    elif ((input[a27] == 'ُ') and (input[b27] == 'ق') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\56-أ.wav" + "'")

                    elif ((input[a27] == 'ُ') and (input[b27] == 'ث') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\41-أ.wav" + "'")

                    elif ((input[a27] == 'ُ') and (input[b27] == 'ص') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\50-أ.wav" + "'")

                    elif ((input[a27] == 'ُ') and (input[b27] == 'ض') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\51-أ.wav" + "'")

                    elif ((input[a27] == 'ُ') and (input[b27] == 'ذ') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\46-أ.wav" + "'")

                    elif ((input[a27] == 'ُ') and (input[b27] == 'ط') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\52-أ.wav" + "'")

                    elif ((input[a27] == 'ُ') and (input[b27] == 'ك') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\57-أ.wav" + "'")

                    elif ((input[a27] == 'ُ') and (input[b27] == 'م') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\59-أ.wav" + "'")

                    elif ((input[a27] == 'ُ') and (input[b27] == 'ن') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\60-أ.wav" + "'")

                    elif ((input[a27] == 'ُ') and (input[b27] == 'ت') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\40-أ.wav" + "'")

                    elif ((input[a27] == 'ُ') and (input[b27] == 'أ') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\38-أ.wav" + "'")

                    elif ((input[a27] == 'ُ') and (input[b27] == 'ل') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\58-أ.wav" + "'")

                    elif ((input[a27] == 'ُ') and (input[b27] == 'ب') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\39-أ.wav" + "'")

                    elif ((input[a27] == 'ُ') and (input[b27] == 'ي') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\62-أ.wav" + "'")

                    elif ((input[a27] == 'ُ') and (input[b27] == 'س') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\48-أ.wav" + "'")

                    elif ((input[a27] == 'ُ') and (input[b27] == 'ش') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\49-أ.wav" + "'")

                    elif ((input[a27] == 'ُ') and (input[b27] == 'ظ') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\51-أ.wav" + "'")

                    elif ((input[a27] == 'ُ') and (input[b27] == 'ز') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\z2.wav" + "'")

                    elif ((input[a27] == 'ُ') and (input[b27] == 'و') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\signs.wav" + "'")

                    elif ((input[a27] == 'ُ') and (input[b27] == 'ة') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\40-أ.wav" + "'")

                    elif ((input[a27] == 'ُ') and (input[b27] == 'ر') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\47-أ.wav" + "'")

                    elif ((input[a27] == 'ُ') and (input[b27] == 'ؤ') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\38-أ.wav" + "'")

                    elif ((input[a27] == 'ُ') and (input[b27] == 'ء') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\38-أ.wav" + "'")

                    elif ((input[a27] == 'ُ') and (input[b27] == 'ئ') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\38-أ.wav" + "'")




                    elif ((input[a27] == 'ِ') and (input[b27] == 'د') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\70-أ.wav" + "'")

                    elif ((input[a27] == 'ِ') and (input[b27] == 'ج') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\67-أ.wav" + "'")

                    elif ((input[a27] == 'ِ') and (input[b27] == 'ح') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\68-أ.wav" + "'")

                    elif ((input[a27] == 'ِ') and (input[b27] == 'خ') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\69-أ.wav" + "'")

                    elif ((input[a27] == 'ِ') and (input[b27] == 'ه') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\86-أ.wav" + "'")

                    elif ((input[a27] == 'ِ') and (input[b27] == 'ع') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\78-أ.wav" + "'")

                    elif ((input[a27] == 'ِ') and (input[b27] == 'غ') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\79-أ.wav" + "'")

                    elif ((input[a27] == 'ِ') and (input[b27] == 'ف') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\80-أ.wav" + "'")

                    elif ((input[a27] == 'ِ') and (input[b27] == 'ق') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\81-أ.wav" + "'")

                    elif ((input[a27] == 'ِ') and (input[b27] == 'ث') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\66-أ.wav" + "'")

                    elif ((input[a27] == 'ِ') and (input[b27] == 'ص') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\75-أ.wav" + "'")

                    elif ((input[a27] == 'ِ') and (input[b27] == 'ض') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\76-أ.wav" + "'")

                    elif ((input[a27] == 'ِ') and (input[b27] == 'ذ') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\71-أ.wav" + "'")

                    elif ((input[a27] == 'ِ') and (input[b27] == 'ط') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\77-أ.wav" + "'")

                    elif ((input[a27] == 'ِ') and (input[b27] == 'ك') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\82-أ.wav" + "'")

                    elif ((input[a27] == 'ِ') and (input[b27] == 'م') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\84-أ.wav" + "'")

                    elif ((input[a27] == 'ِ') and (input[b27] == 'ن') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\85-أ.wav" + "'")

                    elif ((input[a27] == 'ِ') and (input[b27] == 'ت') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\65-أ.wav" + "'")

                    elif ((input[a27] == 'ِ') and (input[b27] == 'أ') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\63-أ.wav" + "'")

                    elif ((input[a27] == 'ِ') and (input[b27] == 'ل') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\83-أ.wav" + "'")

                    elif ((input[a27] == 'ِ') and (input[b27] == 'ب') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\64-أ.wav" + "'")

                    elif ((input[a27] == 'ِ') and (input[b27] == 'ي') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\87-أ.wav" + "'")

                    elif ((input[a27] == 'ِ') and (input[b27] == 'س') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\73-أ.wav" + "'")

                    elif ((input[a27] == 'ِ') and (input[b27] == 'ش') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\74-أ.wav" + "'")

                    elif ((input[a27] == 'ِ') and (input[b27] == 'ظ') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\76-أ.wav" + "'")

                    elif ((input[a27] == 'ِ') and (input[b27] == 'ز') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\z3.wav" + "'")

                    elif ((input[a27] == 'ِ') and (input[b27] == 'و') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\signs.wav" + "'")

                    elif ((input[a27] == 'ِ') and (input[b27] == 'ة') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\65-أ.wav" + "'")

                    elif ((input[a27] == 'ِ') and (input[b27] == 'ر') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\72-أ.wav" + "'")

                    elif ((input[a27] == 'ِ') and (input[b27] == 'ؤ') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\63-أ.wav" + "'")

                    elif ((input[a27] == 'ِ') and (input[b27] == 'ء') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\63-أ.wav" + "'")

                    elif ((input[a27] == 'ِ') and (input[b27] == 'ئ') and (input[c27] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\63-أ.wav" + "'")






                    elif ((input[a27] == 'َ') and ((input[b27] == 'ا') or (input[b27] == 'ى'))):

                        self.z.append('file ' + "'" + "library\\a\\04-أ.wav" + "'")

                    elif (input[a27] == 'ُ' and input[b27] == 'و'):

                        self.z.append('file ' + "'" + "library\\a\\05-أ.wav" + "'")

                    elif (input[a27] == 'ِ' and input[b27] == 'ي'):

                        self.z.append('file ' + "'" + "library\\a\\06-أ.wav" + "'")

                    elif (input[a27] == 'ً'):

                        self.z.append('file ' + "'" + "library\\a\\07-أ.wav" + "'")

                    elif (input[a27] == 'ٌ'):

                        self.z.append('file ' + "'" + "library\\a\\08-أ.wav" + "'")

                    elif (input[a27] == 'ٍ'):

                        self.z.append('file ' + "'" + "library\\a\\09-أ.wav" + "'")

                    elif (input[a27] == 'َ'):

                        self.z.append('file ' + "'" + "library\\a\\01-أ.wav" + "'")

                    elif (input[a27] == 'ُ'):

                        self.z.append('file ' + "'" + "library\\a\\02-أ.wav" + "'")

                    elif (input[a27] == 'ِ'):

                        self.z.append('file ' + "'" + "library\\a\\03-أ.wav" + "'")

                    elif (input[a27] == 'ْ'):

                        self.z.append('file ' + "'" + "library\\a\\signs.wav" + "'")

                    else:

                        self.z.append('file ' + "'" + "library\\a\\signs.wav" + "'")








                else:

                    self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                a27 = 0

                b27 = 0

                d27 = 0

                c27 = 0

            elif (char == 'ئ'):

                a28 = i + 1

                b28 = i + 2

                c28 = i + 3

                d28 = i + 4

                if (a28 < (len(input))):

                    if (input[a28] == '\0'):

                        self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                    elif ((input[a28] == 'َ') and (input[b28] == 'د') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\a\\20-أ.wav' + "'")

                    elif ((input[a28] == 'َ') and (input[b28] == 'ج') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\17-أ.wav" + "'")

                    elif ((input[a28] == 'َ') and (input[b28] == 'ح') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\18-أ.wav" + "'")

                    elif ((input[a28] == 'َ') and (input[b28] == 'خ') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\19-أ.wav" + "'")

                    elif ((input[a28] == 'َ') and (input[b28] == 'ه') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\36-أ.wav" + "'")

                    elif ((input[a28] == 'َ') and (input[b28] == 'ع') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\28-أ.wav" + "'")

                    elif ((input[a28] == 'َ') and (input[b28] == 'غ') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\29-أ.wav" + "'")

                    elif ((input[a28] == 'َ') and (input[b28] == 'ف') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\30-أ.wav" + "'")

                    elif ((input[a28] == 'َ') and (input[b28] == 'ق') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\31-أ.wav" + "'")

                    elif ((input[a28] == 'َ') and (input[b28] == 'ث') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\16-أ.wav" + "'")

                    elif ((input[a28] == 'َ') and (input[b28] == 'ص') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\25-أ.wav" + "'")

                    elif ((input[a28] == 'َ') and (input[b28] == 'ض') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\26-أ.wav" + "'")

                    elif ((input[a28] == 'َ') and (input[b28] == 'ذ') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\21-أ.wav" + "'")

                    elif ((input[a28] == 'َ') and (input[b28] == 'ط') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\27-أ.wav" + "'")

                    elif ((input[a28] == 'َ') and (input[b28] == 'ك') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\32-أ.wav" + "'")

                    elif ((input[a28] == 'َ') and (input[b28] == 'م') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\34-أ.wav" + "'")

                    elif ((input[a28] == 'َ') and (input[b28] == 'ن') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\35-أ.wav" + "'")

                    elif ((input[a28] == 'َ') and (input[b28] == 'ت') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\15-أ.wav" + "'")

                    elif ((input[a28] == 'َ') and (input[b28] == 'أ') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\13-أ.wav" + "'")

                    elif ((input[a28] == 'َ') and (input[b28] == 'ل') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\33-أ.wav" + "'")

                    elif ((input[a28] == 'َ') and (input[b28] == 'ب') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\14-أ.wav" + "'")

                    elif ((input[a28] == 'َ') and (input[b28] == 'ي') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\37-أ.wav" + "'")

                    elif ((input[a28] == 'َ') and (input[b28] == 'س') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\23-أ.wav" + "'")

                    elif ((input[a28] == 'َ') and (input[b28] == 'ش') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\24-أ.wav" + "'")

                    elif ((input[a28] == 'َ') and (input[b28] == 'ظ') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\26-أ.wav" + "'")

                    elif ((input[a28] == 'َ') and (input[b28] == 'ز') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\z1.wav" + "'")

                    elif ((input[a28] == 'َ') and (input[b28] == 'و') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\signs.wav" + "'")

                    elif ((input[a28] == 'َ') and (input[b28] == 'ة') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\15-أ.wav" + "'")

                    elif ((input[a28] == 'َ') and (input[b28] == 'ر') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\22-أ.wav" + "'")

                    elif ((input[a28] == 'َ') and (input[b28] == 'ؤ') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\13-أ.wav" + "'")

                    elif ((input[a28] == 'َ') and (input[b28] == 'ء') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\13-أ.wav" + "'")

                    elif ((input[a28] == 'َ') and (input[b28] == 'ئ') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\13-أ.wav" + "'")



                    elif ((input[a28] == 'ُ') and (input[b28] == 'د') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\45-أ.wav" + "'")

                    elif ((input[a28] == 'ُ') and (input[b28] == 'ج') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\42-أ.wav" + "'")

                    elif ((input[a28] == 'ُ') and (input[b28] == 'ح') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\43-أ.wav" + "'")

                    elif ((input[a28] == 'ُ') and (input[b28] == 'خ') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\44-أ.wav" + "'")

                    elif ((input[a28] == 'ُ') and (input[b28] == 'ه') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\61-أ.wav" + "'")

                    elif ((input[a28] == 'ُ') and (input[b28] == 'ع') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\53-أ.wav" + "'")

                    elif ((input[a28] == 'ُ') and (input[b28] == 'غ') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\54-أ.wav" + "'")

                    elif ((input[a28] == 'ُ') and (input[b28] == 'ف') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\55-أ.wav" + "'")

                    elif ((input[a28] == 'ُ') and (input[b28] == 'ق') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\56-أ.wav" + "'")

                    elif ((input[a28] == 'ُ') and (input[b28] == 'ث') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\41-أ.wav" + "'")

                    elif ((input[a28] == 'ُ') and (input[b28] == 'ص') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\50-أ.wav" + "'")

                    elif ((input[a28] == 'ُ') and (input[b28] == 'ض') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\51-أ.wav" + "'")

                    elif ((input[a28] == 'ُ') and (input[b28] == 'ذ') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\46-أ.wav" + "'")

                    elif ((input[a28] == 'ُ') and (input[b28] == 'ط') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\52-أ.wav" + "'")

                    elif ((input[a28] == 'ُ') and (input[b28] == 'ك') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\57-أ.wav" + "'")

                    elif ((input[a28] == 'ُ') and (input[b28] == 'م') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\59-أ.wav" + "'")

                    elif ((input[a28] == 'ُ') and (input[b28] == 'ن') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\60-أ.wav" + "'")

                    elif ((input[a28] == 'ُ') and (input[b28] == 'ت') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\40-أ.wav" + "'")

                    elif ((input[a28] == 'ُ') and (input[b28] == 'أ') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\38-أ.wav" + "'")

                    elif ((input[a28] == 'ُ') and (input[b28] == 'ل') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\58-أ.wav" + "'")

                    elif ((input[a28] == 'ُ') and (input[b28] == 'ب') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\39-أ.wav" + "'")

                    elif ((input[a28] == 'ُ') and (input[b28] == 'ي') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\62-أ.wav" + "'")

                    elif ((input[a28] == 'ُ') and (input[b28] == 'س') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\48-أ.wav" + "'")

                    elif ((input[a28] == 'ُ') and (input[b28] == 'ش') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\49-أ.wav" + "'")

                    elif ((input[a28] == 'ُ') and (input[b28] == 'ظ') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\51-أ.wav" + "'")

                    elif ((input[a28] == 'ُ') and (input[b28] == 'ز') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\z2.wav" + "'")

                    elif ((input[a28] == 'ُ') and (input[b28] == 'و') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\signs.wav" + "'")

                    elif ((input[a28] == 'ُ') and (input[b28] == 'ة') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\40-أ.wav" + "'")

                    elif ((input[a28] == 'ُ') and (input[b28] == 'ر') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\47-أ.wav" + "'")

                    elif ((input[a28] == 'ُ') and (input[b28] == 'ؤ') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\38-أ.wav" + "'")

                    elif ((input[a28] == 'ُ') and (input[b28] == 'ء') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\38-أ.wav" + "'")

                    elif ((input[a28] == 'ُ') and (input[b28] == 'ئ') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\38-أ.wav" + "'")




                    elif ((input[a28] == 'ِ') and (input[b28] == 'د') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\70-أ.wav" + "'")

                    elif ((input[a28] == 'ِ') and (input[b28] == 'ج') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\67-أ.wav" + "'")

                    elif ((input[a28] == 'ِ') and (input[b28] == 'ح') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\68-أ.wav" + "'")

                    elif ((input[a28] == 'ِ') and (input[b28] == 'خ') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\69-أ.wav" + "'")

                    elif ((input[a28] == 'ِ') and (input[b28] == 'ه') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\86-أ.wav" + "'")

                    elif ((input[a28] == 'ِ') and (input[b28] == 'ع') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\78-أ.wav" + "'")

                    elif ((input[a28] == 'ِ') and (input[b28] == 'غ') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\79-أ.wav" + "'")

                    elif ((input[a28] == 'ِ') and (input[b28] == 'ف') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\80-أ.wav" + "'")

                    elif ((input[a28] == 'ِ') and (input[b28] == 'ق') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\81-أ.wav" + "'")

                    elif ((input[a28] == 'ِ') and (input[b28] == 'ث') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\66-أ.wav" + "'")

                    elif ((input[a28] == 'ِ') and (input[b28] == 'ص') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\75-أ.wav" + "'")

                    elif ((input[a28] == 'ِ') and (input[b28] == 'ض') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\76-أ.wav" + "'")

                    elif ((input[a28] == 'ِ') and (input[b28] == 'ذ') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\71-أ.wav" + "'")

                    elif ((input[a28] == 'ِ') and (input[b28] == 'ط') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\77-أ.wav" + "'")

                    elif ((input[a28] == 'ِ') and (input[b28] == 'ك') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\82-أ.wav" + "'")

                    elif ((input[a28] == 'ِ') and (input[b28] == 'م') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\84-أ.wav" + "'")

                    elif ((input[a28] == 'ِ') and (input[b28] == 'ن') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\85-أ.wav" + "'")

                    elif ((input[a28] == 'ِ') and (input[b28] == 'ت') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\65-أ.wav" + "'")

                    elif ((input[a28] == 'ِ') and (input[b28] == 'أ') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\63-أ.wav" + "'")

                    elif ((input[a28] == 'ِ') and (input[b28] == 'ل') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\83-أ.wav" + "'")

                    elif ((input[a28] == 'ِ') and (input[b28] == 'ب') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\64-أ.wav" + "'")

                    elif ((input[a28] == 'ِ') and (input[b28] == 'ي') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\87-أ.wav" + "'")

                    elif ((input[a28] == 'ِ') and (input[b28] == 'س') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\73-أ.wav" + "'")

                    elif ((input[a28] == 'ِ') and (input[b28] == 'ش') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\74-أ.wav" + "'")

                    elif ((input[a28] == 'ِ') and (input[b28] == 'ظ') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\76-أ.wav" + "'")

                    elif ((input[a28] == 'ِ') and (input[b28] == 'ز') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\z3.wav" + "'")

                    elif ((input[a28] == 'ِ') and (input[b28] == 'و') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\signs.wav" + "'")

                    elif ((input[a28] == 'ِ') and (input[b28] == 'ة') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\65-أ.wav" + "'")

                    elif ((input[a28] == 'ِ') and (input[b28] == 'ر') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\72-أ.wav" + "'")

                    elif ((input[a28] == 'ِ') and (input[b28] == 'ؤ') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\63-أ.wav" + "'")

                    elif ((input[a28] == 'ِ') and (input[b28] == 'ء') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\63-أ.wav" + "'")

                    elif ((input[a28] == 'ِ') and (input[b28] == 'ئ') and (input[c28] == 'ْ')):

                        self.z.append('file ' + "'" + "library\\a\\63-أ.wav" + "'")






                    elif ((input[a28] == 'َ') and ((input[b28] == 'ا') or (input[b28] == 'ى'))):

                        self.z.append('file ' + "'" + "library\\a\\04-أ.wav" + "'")

                    elif (input[a28] == 'ُ' and input[b28] == 'و'):

                        self.z.append('file ' + "'" + "library\\a\\05-أ.wav" + "'")

                    elif (input[a28] == 'ِ' and input[b28] == 'ي'):

                        self.z.append('file ' + "'" + "library\\a\\06-أ.wav" + "'")

                    elif (input[a28] == 'ً'):

                        self.z.append('file ' + "'" + "library\\a\\07-أ.wav" + "'")

                    elif (input[a28] == 'ٌ'):

                        self.z.append('file ' + "'" + "library\\a\\08-أ.wav" + "'")

                    elif (input[a28] == 'ٍ'):

                        self.z.append('file ' + "'" + "library\\a\\09-أ.wav" + "'")

                    elif (input[a28] == 'َ'):

                        self.z.append('file ' + "'" + "library\\a\\01-أ.wav" + "'")

                    elif (input[a28] == 'ُ'):

                        self.z.append('file ' + "'" + "library\\a\\02-أ.wav" + "'")

                    elif (input[a28] == 'ِ'):

                        self.z.append('file ' + "'" + "library\\a\\03-أ.wav" + "'")

                    elif (input[a28] == 'ْ'):

                        self.z.append('file ' + "'" + "library\\a\\signs.wav" + "'")

                    else:

                        self.z.append('file ' + "'" + "library\\a\\signs.wav" + "'")








                else:

                    self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                a28 = 0

                b28 = 0

                d28 = 0

                c28 = 0

            elif (char == 'ز'):

                a29 = i + 1

                b29 = i + 2

                c29 = i + 3

                d29 = i + 4

                if (a29 < (len(input))):

                    if (input[a29] == '\0'):

                        self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                    elif ((input[a29] == 'َ') and (input[b29] == 'د') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\20-Audio Track.wav' + "'")

                    elif ((input[a29] == 'َ') and (input[b29] == 'ج') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\17-Audio Track.wav' + "'")

                    elif ((input[a29] == 'َ') and (input[b29] == 'ح') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\18-Audio Track.wav' + "'")

                    elif ((input[a29] == 'َ') and (input[b29] == 'خ') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\19-Audio Track.wav' + "'")

                    elif ((input[a29] == 'َ') and (input[b29] == 'ه') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\37-Audio Track.wav' + "'")

                    elif ((input[a29] == 'َ') and (input[b29] == 'ع') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\29-Audio Track.wav' + "'")

                    elif ((input[a29] == 'َ') and (input[b29] == 'غ') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\30-Audio Track.wav' + "'")

                    elif ((input[a29] == 'َ') and (input[b29] == 'ف') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\31-Audio Track.wav' + "'")

                    elif ((input[a29] == 'َ') and (input[b29] == 'ق') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\32-Audio Track.wav' + "'")

                    elif ((input[a29] == 'َ') and (input[b29] == 'ث') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\16-Audio Track.wav' + "'")

                    elif ((input[a29] == 'َ') and (input[b29] == 'ص') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\26-Audio Track.wav' + "'")

                    elif ((input[a29] == 'َ') and (input[b29] == 'ض') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\27-Audio Track.wav' + "'")

                    elif ((input[a29] == 'َ') and (input[b29] == 'ذ') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\21-Audio Track.wav' + "'")

                    elif ((input[a29] == 'َ') and (input[b29] == 'ط') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\28-Audio Track.wav' + "'")

                    elif ((input[a29] == 'َ') and (input[b29] == 'ك') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\33-Audio Track.wav' + "'")

                    elif ((input[a29] == 'َ') and (input[b29] == 'م') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\35-Audio Track.wav' + "'")

                    elif ((input[a29] == 'َ') and (input[b29] == 'ن') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\36-Audio Track.wav' + "'")

                    elif ((input[a29] == 'َ') and (input[b29] == 'ت') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\15-Audio Track.wav' + "'")

                    elif ((input[a29] == 'َ') and (input[b29] == 'أ') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\13-Audio Track.wav' + "'")

                    elif ((input[a29] == 'َ') and (input[b29] == 'ل') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\34-Audio Track.wav' + "'")

                    elif ((input[a29] == 'َ') and (input[b29] == 'ب') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\14-Audio Track.wav' + "'")

                    elif ((input[a29] == 'َ') and (input[b29] == 'ي') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\38-Audio Track.wav' + "'")

                    elif ((input[a29] == 'َ') and (input[b29] == 'س') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\24-Audio Track.wav' + "'")

                    elif ((input[a29] == 'َ') and (input[b29] == 'ش') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\25-Audio Track.wav' + "'")

                    elif ((input[a29] == 'َ') and (input[b29] == 'ظ') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\27-Audio Track.wav' + "'")

                    elif ((input[a29] == 'َ') and (input[b29] == 'ز') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\23-Audio Track.wav' + "'")

                    elif ((input[a29] == 'َ') and (input[b29] == 'و') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\signs.wav' + "'")

                    elif ((input[a29] == 'َ') and (input[b29] == 'ة') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\15-Audio Track.wav' + "'")

                    elif ((input[a29] == 'َ') and (input[b29] == 'ر') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\22-Audio Track.wav' + "'")

                    elif ((input[a29] == 'َ') and (input[b29] == 'ؤ') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\13-Audio Track.wav' + "'")

                    elif ((input[a29] == 'َ') and (input[b29] == 'ء') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\13-Audio Track.wav' + "'")

                    elif ((input[a29] == 'َ') and (input[b29] == 'ئ') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\13-Audio Track.wav' + "'")



                    elif ((input[a29] == 'ُ') and (input[b29] == 'د') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\46-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ُ') and (input[b29] == 'ج') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\43-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ُ') and (input[b29] == 'ح') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\44-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ُ') and (input[b29] == 'خ') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\45-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ُ') and (input[b29] == 'ه') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\63-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ُ') and (input[b29] == 'ع') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\55-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ُ') and (input[b29] == 'غ') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\56-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ُ') and (input[b29] == 'ف') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\57-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ُ') and (input[b29] == 'ق') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\58-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ُ') and (input[b29] == 'ث') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\42-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ُ') and (input[b29] == 'ص') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\52-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ُ') and (input[b29] == 'ض') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\53-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ُ') and (input[b29] == 'ذ') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\47-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ُ') and (input[b29] == 'ط') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\54-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ُ') and (input[b29] == 'ك') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\59-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ُ') and (input[b29] == 'م') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\61-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ُ') and (input[b29] == 'ن') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\62-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ُ') and (input[b29] == 'ت') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\41-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ُ') and (input[b29] == 'أ') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\39-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ُ') and (input[b29] == 'ل') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\60-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ُ') and (input[b29] == 'ب') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\40-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ُ') and (input[b29] == 'ي') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\64-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ُ') and (input[b29] == 'س') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\50-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ُ') and (input[b29] == 'ش') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\51-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ُ') and (input[b29] == 'ظ') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\53-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ُ') and (input[b29] == 'ز') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\49-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ُ') and (input[b29] == 'و') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\signs.wav' + "'")

                    elif ((input[a29] == 'ُ') and (input[b29] == 'ة') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\41-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ُ') and (input[b29] == 'ر') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\48-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ُ') and (input[b29] == 'ؤ') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\39-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ُ') and (input[b29] == 'ء') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\39-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ُ') and (input[b29] == 'ئ') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\39-Audio Track.wav' + "'")




                    elif ((input[a29] == 'ِ') and (input[b29] == 'د') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\72-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ِ') and (input[b29] == 'ج') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\69-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ِ') and (input[b29] == 'ح') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\70-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ِ') and (input[b29] == 'خ') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\71-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ِ') and (input[b29] == 'ه') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\89-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ِ') and (input[b29] == 'ع') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\81-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ِ') and (input[b29] == 'غ') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\82-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ِ') and (input[b29] == 'ف') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\83-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ِ') and (input[b29] == 'ق') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\84-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ِ') and (input[b29] == 'ث') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\68-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ِ') and (input[b29] == 'ص') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\78-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ِ') and (input[b29] == 'ض') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\79-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ِ') and (input[b29] == 'ذ') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\73-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ِ') and (input[b29] == 'ط') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\80-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ِ') and (input[b29] == 'ك') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\85-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ِ') and (input[b29] == 'م') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\87-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ِ') and (input[b29] == 'ن') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\88-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ِ') and (input[b29] == 'ت') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\67-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ِ') and (input[b29] == 'أ') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\65-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ِ') and (input[b29] == 'ل') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\86-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ِ') and (input[b29] == 'ب') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\66-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ِ') and (input[b29] == 'ي') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\90-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ِ') and (input[b29] == 'س') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\76-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ِ') and (input[b29] == 'ش') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\77-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ِ') and (input[b29] == 'ظ') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\79-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ِ') and (input[b29] == 'ز') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\75-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ِ') and (input[b29] == 'و') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\signs.wav' + "'")

                    elif ((input[a29] == 'ِ') and (input[b29] == 'ة') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\67-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ِ') and (input[b29] == 'ر') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\74-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ِ') and (input[b29] == 'ؤ') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\65-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ِ') and (input[b29] == 'ء') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\65-Audio Track.wav' + "'")

                    elif ((input[a29] == 'ِ') and (input[b29] == 'ئ') and (input[c29] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\z\\65-Audio Track.wav' + "'")






                    elif ((input[a29] == 'َ') and ((input[b29] == 'ا') or (input[b29] == 'ى'))):

                        self.z.append('file ' + "'" + 'library\\z\\04-Audio Track.wav' + "'")

                    elif (input[a29] == 'ُ' and input[b29] == 'و'):

                        self.z.append('file ' + "'" + 'library\\z\\05-Audio Track.wav' + "'")

                    elif (input[a29] == 'ِ' and input[b29] == 'ي'):

                        self.z.append('file ' + "'" + 'library\\z\\06-Audio Track.wav' + "'")

                    elif (input[a29] == 'ً'):

                        self.z.append('file ' + "'" + 'library\\z\\07-Audio Track.wav' + "'")

                    elif (input[a29] == 'ٌ'):

                        self.z.append('file ' + "'" + 'library\\z\\08-Audio Track.wav' + "'")

                    elif (input[a29] == 'ٍ'):

                        self.z.append('file ' + "'" + 'library\\z\\09-Audio Track.wav' + "'")

                    elif (input[a29] == 'َ'):

                        self.z.append('file ' + "'" + 'library\\z\\01-Audio Track.wav' + "'")

                    elif (input[a29] == 'ُ'):

                        self.z.append('file ' + "'" + 'library\\z\\02-Audio Track.wav' + "'")

                    elif (input[a29] == 'ِ'):

                        self.z.append('file ' + "'" + 'library\\z\\03-Audio Track.wav' + "'")

                    elif (input[a29] == 'ْ'):

                        self.z.append('file ' + "'" + 'library\\signs.wav' + "'")

                    else:

                        self.z.append('file ' + "'" + 'library\\signs.wav' + "'")








                else:

                    self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                a29 = 0

                b29 = 0

                d29 = 0

                c29 = 0

            elif (char == 'و'):

                a30 = i + 1

                b30 = i + 2

                c30 = i + 3

                d30 = i + 4

                if (a30 < (len(input))):

                    if (input[a30] == '\0'):

                        self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                    elif ((input[a30] == 'َ') and (input[b30] == 'د') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\20-Audio Track.wav' + "'")

                    elif ((input[a30] == 'َ') and (input[b30] == 'ج') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\17-Audio Track.wav' + "'")

                    elif ((input[a30] == 'َ') and (input[b30] == 'ح') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\18-Audio Track.wav' + "'")

                    elif ((input[a30] == 'َ') and (input[b30] == 'خ') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\19-Audio Track.wav' + "'")

                    elif ((input[a30] == 'َ') and (input[b30] == 'ه') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\37-Audio Track.wav' + "'")

                    elif ((input[a30] == 'َ') and (input[b30] == 'ع') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\29-Audio Track.wav' + "'")

                    elif ((input[a30] == 'َ') and (input[b30] == 'غ') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\30-Audio Track.wav' + "'")

                    elif ((input[a30] == 'َ') and (input[b30] == 'ف') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\31-Audio Track.wav' + "'")

                    elif ((input[a30] == 'َ') and (input[b30] == 'ق') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\32-Audio Track.wav' + "'")

                    elif ((input[a30] == 'َ') and (input[b30] == 'ث') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\16-Audio Track.wav' + "'")

                    elif ((input[a30] == 'َ') and (input[b30] == 'ص') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\26-Audio Track.wav' + "'")

                    elif ((input[a30] == 'َ') and (input[b30] == 'ض') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\27-Audio Track.wav' + "'")

                    elif ((input[a30] == 'َ') and (input[b30] == 'ذ') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\21-Audio Track.wav' + "'")

                    elif ((input[a30] == 'َ') and (input[b30] == 'ط') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\28-Audio Track.wav' + "'")

                    elif ((input[a30] == 'َ') and (input[b30] == 'ك') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\33-Audio Track.wav' + "'")

                    elif ((input[a30] == 'َ') and (input[b30] == 'م') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\35-Audio Track.wav' + "'")

                    elif ((input[a30] == 'َ') and (input[b30] == 'ن') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\36-Audio Track.wav' + "'")

                    elif ((input[a30] == 'َ') and (input[b30] == 'ت') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\15-Audio Track.wav' + "'")

                    elif ((input[a30] == 'َ') and (input[b30] == 'أ') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\13-Audio Track.wav' + "'")

                    elif ((input[a30] == 'َ') and (input[b30] == 'ل') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\34-Audio Track.wav' + "'")

                    elif ((input[a30] == 'َ') and (input[b30] == 'ب') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\14-Audio Track.wav' + "'")

                    elif ((input[a30] == 'َ') and (input[b30] == 'ي') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\38-Audio Track.wav' + "'")

                    elif ((input[a30] == 'َ') and (input[b30] == 'س') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\24-Audio Track.wav' + "'")

                    elif ((input[a30] == 'َ') and (input[b30] == 'ش') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\25-Audio Track.wav' + "'")

                    elif ((input[a30] == 'َ') and (input[b30] == 'ظ') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\27-Audio Track.wav' + "'")

                    elif ((input[a30] == 'َ') and (input[b30] == 'ز') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\23-Audio Track.wav' + "'")

                    elif ((input[a30] == 'َ') and (input[b30] == 'و') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\signs.wav' + "'")

                    elif ((input[a30] == 'َ') and (input[b30] == 'ة') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\15-Audio Track.wav' + "'")

                    elif ((input[a30] == 'َ') and (input[b30] == 'ر') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\22-Audio Track.wav' + "'")

                    elif ((input[a30] == 'َ') and (input[b30] == 'ؤ') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\13-Audio Track.wav' + "'")

                    elif ((input[a30] == 'َ') and (input[b30] == 'ء') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\13-Audio Track.wav' + "'")

                    elif ((input[a30] == 'َ') and (input[b30] == 'ئ') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\13-Audio Track.wav' + "'")



                    elif ((input[a30] == 'ُ') and (input[b30] == 'د') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\46-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ُ') and (input[b30] == 'ج') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\43-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ُ') and (input[b30] == 'ح') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\44-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ُ') and (input[b30] == 'خ') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\45-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ُ') and (input[b30] == 'ه') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\63-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ُ') and (input[b30] == 'ع') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\55-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ُ') and (input[b30] == 'غ') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\56-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ُ') and (input[b30] == 'ف') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\57-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ُ') and (input[b30] == 'ق') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\58-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ُ') and (input[b30] == 'ث') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\42-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ُ') and (input[b30] == 'ص') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\52-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ُ') and (input[b30] == 'ض') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\53-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ُ') and (input[b30] == 'ذ') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\47-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ُ') and (input[b30] == 'ط') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\54-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ُ') and (input[b30] == 'ك') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\59-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ُ') and (input[b30] == 'م') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\61-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ُ') and (input[b30] == 'ن') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\62-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ُ') and (input[b30] == 'ت') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\41-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ُ') and (input[b30] == 'أ') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\39-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ُ') and (input[b30] == 'ل') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\60-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ُ') and (input[b30] == 'ب') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\40-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ُ') and (input[b30] == 'ي') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\64-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ُ') and (input[b30] == 'س') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\50-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ُ') and (input[b30] == 'ش') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\51-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ُ') and (input[b30] == 'ظ') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\53-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ُ') and (input[b30] == 'ز') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\49-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ُ') and (input[b30] == 'و') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\signs.wav' + "'")

                    elif ((input[a30] == 'ُ') and (input[b30] == 'ة') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\41-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ُ') and (input[b30] == 'ر') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\48-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ُ') and (input[b30] == 'ؤ') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\39-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ُ') and (input[b30] == 'ء') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\39-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ُ') and (input[b30] == 'ئ') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\39-Audio Track.wav' + "'")




                    elif ((input[a30] == 'ِ') and (input[b30] == 'د') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\72-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ِ') and (input[b30] == 'ج') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\69-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ِ') and (input[b30] == 'ح') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\70-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ِ') and (input[b30] == 'خ') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\71-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ِ') and (input[b30] == 'ه') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\89-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ِ') and (input[b30] == 'ع') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\81-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ِ') and (input[b30] == 'غ') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\82-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ِ') and (input[b30] == 'ف') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\83-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ِ') and (input[b30] == 'ق') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\84-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ِ') and (input[b30] == 'ث') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\68-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ِ') and (input[b30] == 'ص') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\78-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ِ') and (input[b30] == 'ض') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\79-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ِ') and (input[b30] == 'ذ') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\73-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ِ') and (input[b30] == 'ط') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\80-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ِ') and (input[b30] == 'ك') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\85-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ِ') and (input[b30] == 'م') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\87-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ِ') and (input[b30] == 'ن') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\88-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ِ') and (input[b30] == 'ت') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\67-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ِ') and (input[b30] == 'أ') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\65-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ِ') and (input[b30] == 'ل') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\86-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ِ') and (input[b30] == 'ب') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\66-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ِ') and (input[b30] == 'ي') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\90-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ِ') and (input[b30] == 'س') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\76-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ِ') and (input[b30] == 'ش') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\77-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ِ') and (input[b30] == 'ظ') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\79-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ِ') and (input[b30] == 'ز') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\75-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ِ') and (input[b30] == 'و') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\signs.wav' + "'")

                    elif ((input[a30] == 'ِ') and (input[b30] == 'ة') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\67-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ِ') and (input[b30] == 'ر') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\74-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ِ') and (input[b30] == 'ؤ') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\65-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ِ') and (input[b30] == 'ء') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\65-Audio Track.wav' + "'")

                    elif ((input[a30] == 'ِ') and (input[b30] == 'ئ') and (input[c30] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\w\\65-Audio Track.wav' + "'")






                    elif ((input[a30] == 'َ') and ((input[b30] == 'ا') or (input[b30] == 'ى'))):

                        self.z.append('file ' + "'" + 'library\\w\\04-Audio Track.wav' + "'")

                    elif (input[a30] == 'ُ' and input[b30] == 'و'):

                        self.z.append('file ' + "'" + 'library\\w\\05-Audio Track.wav' + "'")

                    elif (input[a30] == 'ِ' and input[b30] == 'ي'):

                        self.z.append('file ' + "'" + 'library\\w\\06-Audio Track.wav' + "'")

                    elif (input[a30] == 'ً'):

                        self.z.append('file ' + "'" + 'library\\w\\07-Audio Track.wav' + "'")

                    elif (input[a30] == 'ٌ'):

                        self.z.append('file ' + "'" + 'library\\w\\08-Audio Track.wav' + "'")

                    elif (input[a30] == 'ٍ'):

                        self.z.append('file ' + "'" + 'library\\w\\09-Audio Track.wav' + "'")

                    elif (input[a30] == 'َ'):

                        self.z.append('file ' + "'" + 'library\\w\\01-Audio Track.wav' + "'")

                    elif (input[a30] == 'ُ'):

                        self.z.append('file ' + "'" + 'library\\w\\02-Audio Track.wav' + "'")

                    elif (input[a30] == 'ِ'):

                        self.z.append('file ' + "'" + 'library\\w\\03-Audio Track.wav' + "'")

                    elif (input[a30] == 'ْ'):

                        self.z.append('file ' + "'" + 'library\\signs.wav' + "'")

                    else:

                        self.z.append('file ' + "'" + 'library\\signs.wav' + "'")








                else:

                    self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                a30 = 0

                b30 = 0

                d30 = 0

                c30 = 0

            elif (char == 'د'):

                a31 = i + 1

                b31 = i + 2

                c31 = i + 3

                d31 = i + 4

                if (a31 < (len(input))):

                    if (input[a31] == '\0'):

                        self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                    elif ((input[a31] == 'َ') and (input[b31] == 'د') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\20-Audio Track.wav' + "'")

                    elif ((input[a31] == 'َ') and (input[b31] == 'ج') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\17-Audio Track.wav' + "'")

                    elif ((input[a31] == 'َ') and (input[b31] == 'ح') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\18-Audio Track.wav' + "'")

                    elif ((input[a31] == 'َ') and (input[b31] == 'خ') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\19-Audio Track.wav' + "'")

                    elif ((input[a31] == 'َ') and (input[b31] == 'ه') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\37-Audio Track.wav' + "'")

                    elif ((input[a31] == 'َ') and (input[b31] == 'ع') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\29-Audio Track.wav' + "'")

                    elif ((input[a31] == 'َ') and (input[b31] == 'غ') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\30-Audio Track.wav' + "'")

                    elif ((input[a31] == 'َ') and (input[b31] == 'ف') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\31-Audio Track.wav' + "'")

                    elif ((input[a31] == 'َ') and (input[b31] == 'ق') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\32-Audio Track.wav' + "'")

                    elif ((input[a31] == 'َ') and (input[b31] == 'ث') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\16-Audio Track.wav' + "'")

                    elif ((input[a31] == 'َ') and (input[b31] == 'ص') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\26-Audio Track.wav' + "'")

                    elif ((input[a31] == 'َ') and (input[b31] == 'ض') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\27-Audio Track.wav' + "'")

                    elif ((input[a31] == 'َ') and (input[b31] == 'ذ') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\21-Audio Track.wav' + "'")

                    elif ((input[a31] == 'َ') and (input[b31] == 'ط') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\28-Audio Track.wav' + "'")

                    elif ((input[a31] == 'َ') and (input[b31] == 'ك') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\33-Audio Track.wav' + "'")

                    elif ((input[a31] == 'َ') and (input[b31] == 'م') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\35-Audio Track.wav' + "'")

                    elif ((input[a31] == 'َ') and (input[b31] == 'ن') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\36-Audio Track.wav' + "'")

                    elif ((input[a31] == 'َ') and (input[b31] == 'ت') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\15-Audio Track.wav' + "'")

                    elif ((input[a31] == 'َ') and (input[b31] == 'أ') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\13-Audio Track.wav' + "'")

                    elif ((input[a31] == 'َ') and (input[b31] == 'ل') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\34-Audio Track.wav' + "'")

                    elif ((input[a31] == 'َ') and (input[b31] == 'ب') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\14-Audio Track.wav' + "'")

                    elif ((input[a31] == 'َ') and (input[b31] == 'ي') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\38-Audio Track.wav' + "'")

                    elif ((input[a31] == 'َ') and (input[b31] == 'س') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\24-Audio Track.wav' + "'")

                    elif ((input[a31] == 'َ') and (input[b31] == 'ش') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\25-Audio Track.wav' + "'")

                    elif ((input[a31] == 'َ') and (input[b31] == 'ظ') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\27-Audio Track.wav' + "'")

                    elif ((input[a31] == 'َ') and (input[b31] == 'ز') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\23-Audio Track.wav' + "'")

                    elif ((input[a31] == 'َ') and (input[b31] == 'و') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\signs.wav' + "'")

                    elif ((input[a31] == 'َ') and (input[b31] == 'ة') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\15-Audio Track.wav' + "'")

                    elif ((input[a31] == 'َ') and (input[b31] == 'ر') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\22-Audio Track.wav' + "'")

                    elif ((input[a31] == 'َ') and (input[b31] == 'ؤ') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\13-Audio Track.wav' + "'")

                    elif ((input[a31] == 'َ') and (input[b31] == 'ء') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\13-Audio Track.wav' + "'")

                    elif ((input[a31] == 'َ') and (input[b31] == 'ئ') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\13-Audio Track.wav' + "'")



                    elif ((input[a31] == 'ُ') and (input[b31] == 'د') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\46-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ُ') and (input[b31] == 'ج') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\43-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ُ') and (input[b31] == 'ح') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\44-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ُ') and (input[b31] == 'خ') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\45-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ُ') and (input[b31] == 'ه') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\63-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ُ') and (input[b31] == 'ع') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\55-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ُ') and (input[b31] == 'غ') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\56-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ُ') and (input[b31] == 'ف') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\57-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ُ') and (input[b31] == 'ق') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\58-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ُ') and (input[b31] == 'ث') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\42-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ُ') and (input[b31] == 'ص') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\52-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ُ') and (input[b31] == 'ض') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\53-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ُ') and (input[b31] == 'ذ') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\47-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ُ') and (input[b31] == 'ط') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\54-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ُ') and (input[b31] == 'ك') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\59-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ُ') and (input[b31] == 'م') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\61-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ُ') and (input[b31] == 'ن') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\62-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ُ') and (input[b31] == 'ت') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\41-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ُ') and (input[b31] == 'أ') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\39-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ُ') and (input[b31] == 'ل') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\60-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ُ') and (input[b31] == 'ب') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\40-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ُ') and (input[b31] == 'ي') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\64-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ُ') and (input[b31] == 'س') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\50-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ُ') and (input[b31] == 'ش') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\51-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ُ') and (input[b31] == 'ظ') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\53-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ُ') and (input[b31] == 'ز') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\49-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ُ') and (input[b31] == 'و') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\signs.wav' + "'")

                    elif ((input[a31] == 'ُ') and (input[b31] == 'ة') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\41-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ُ') and (input[b31] == 'ر') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\48-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ُ') and (input[b31] == 'ؤ') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\39-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ُ') and (input[b31] == 'ء') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\39-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ُ') and (input[b31] == 'ئ') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\39-Audio Track.wav' + "'")




                    elif ((input[a31] == 'ِ') and (input[b31] == 'د') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\72-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ِ') and (input[b31] == 'ج') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\69-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ِ') and (input[b31] == 'ح') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\70-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ِ') and (input[b31] == 'خ') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\71-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ِ') and (input[b31] == 'ه') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\89-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ِ') and (input[b31] == 'ع') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\81-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ِ') and (input[b31] == 'غ') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\82-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ِ') and (input[b31] == 'ف') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\83-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ِ') and (input[b31] == 'ق') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\84-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ِ') and (input[b31] == 'ث') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\68-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ِ') and (input[b31] == 'ص') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\78-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ِ') and (input[b31] == 'ض') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\79-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ِ') and (input[b31] == 'ذ') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\73-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ِ') and (input[b31] == 'ط') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\80-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ِ') and (input[b31] == 'ك') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\85-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ِ') and (input[b31] == 'م') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\87-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ِ') and (input[b31] == 'ن') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\88-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ِ') and (input[b31] == 'ت') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\67-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ِ') and (input[b31] == 'أ') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\65-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ِ') and (input[b31] == 'ل') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\86-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ِ') and (input[b31] == 'ب') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\66-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ِ') and (input[b31] == 'ي') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\90-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ِ') and (input[b31] == 'س') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\76-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ِ') and (input[b31] == 'ش') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\77-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ِ') and (input[b31] == 'ظ') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\79-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ِ') and (input[b31] == 'ز') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\75-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ِ') and (input[b31] == 'و') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\signs.wav' + "'")

                    elif ((input[a31] == 'ِ') and (input[b31] == 'ة') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\67-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ِ') and (input[b31] == 'ر') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\74-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ِ') and (input[b31] == 'ؤ') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\65-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ِ') and (input[b31] == 'ء') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\65-Audio Track.wav' + "'")

                    elif ((input[a31] == 'ِ') and (input[b31] == 'ئ') and (input[c31] == 'ْ')):

                        self.z.append('file ' + "'" + 'library\\d\\65-Audio Track.wav' + "'")






                    elif ((input[a31] == 'َ') and ((input[b31] == 'ا') or (input[b31] == 'ى'))):

                        self.z.append('file ' + "'" + 'library\\d\\04-Audio Track.wav' + "'")

                    elif (input[a31] == 'ُ' and input[b31] == 'و'):

                        self.z.append('file ' + "'" + 'library\\d\\05-Audio Track.wav' + "'")

                    elif (input[a31] == 'ِ' and input[b31] == 'ي'):

                        self.z.append('file ' + "'" + 'library\\d\\06-Audio Track.wav' + "'")

                    elif (input[a31] == 'ً'):

                        self.z.append('file ' + "'" + 'library\\d\\07-Audio Track.wav' + "'")

                    elif (input[a31] == 'ٌ'):

                        self.z.append('file ' + "'" + 'library\\d\\08-Audio Track.wav' + "'")

                    elif (input[a31] == 'ٍ'):

                        self.z.append('file ' + "'" + 'library\\d\\09-Audio Track.wav' + "'")

                    elif (input[a31] == 'َ'):

                        self.z.append('file ' + "'" + 'library\\d\\01-Audio Track.wav' + "'")

                    elif (input[a31] == 'ُ'):

                        self.z.append('file ' + "'" + 'library\\d\\02-Audio Track.wav' + "'")

                    elif (input[a31] == 'ِ'):

                        self.z.append('file ' + "'" + 'library\\d\\03-Audio Track.wav' + "'")

                    elif (input[a31] == 'ْ'):

                        self.z.append('file ' + "'" + 'library\\signs.wav' + "'")

                    else:

                        self.z.append('file ' + "'" + 'library\\signs.wav' + "'")








                else:

                    self.z.append('file ' + "'" + "library\\signs.wav" + "'")

                a31 = 0

                b31 = 0

                d31 = 0

                c31 = 0

            elif (char == ' '):
                a41 = i + 1
                if (a41 < len(input)):

                    if (input[a41] == '\0'):
                        self.z.append('file ' + "'" + 'library\\signs.wav' + "'")
                    else:
                        self.z.append('file ' + "'" + 'library\\signs.wav' + "'")

                else:
                    self.z.append('file ' + "'" + 'library\\signs.wav' + "'")

                a41 = 0

            i = i + 1

        with io.open('pathss.txt', 'w', encoding='utf8') as f:
            for w in self.z:
                s = w + '\n'
                f.write(s)

        subprocess.call(
            ['ffmpeg', '-f', 'concat', '-safe', '0', '-i', 'pathss.txt', '-c', 'copy', 'os3.wav'])  # concatenate wav file
        subprocess.call(['ffmpeg', '-i', 'os3.wav', '-filter:a', "atempo=1.5", '-vn', 'os4.wav'])



    def playmusicFromLocal(self):
        self.player2.setMedia(self.sound2)
        self.player2.setVolume(100)
        self.player2.play()






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    arts = QtWidgets.QDialog()
    ui = Ui_arts()
    ui.setupUi(arts)
    arts.show()
    sys.exit(app.exec_())

