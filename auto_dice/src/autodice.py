import sys, design
import webbrowser
from PyQt5 import QtWidgets
from telethon.sync import TelegramClient, types

def send_dice(self, api_id, api_hash, chat_id, required_value, emoticon):
    with TelegramClient('auth', api_id, api_hash) as client:
        current_value = 0
        while current_value < required_value:
            client.send_file(chat_id, types.InputMediaDice(emoticon)) #
            getmessage = client.get_messages(chat_id, from_user='me')
            for message_obj in getmessage:
                message = message_obj
            current_value = message.media.value
            if current_value < required_value:
                self.log.append("Выпало " + str(current_value) + ", перекидываю")
                client.delete_messages(chat_id, message.id, revoke=True)
            else:
                self.log.append("Выпало " + str(current_value) + ", завершаю работу")

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tg_button.clicked.connect(self.tg_btn_clicked)
        self.web_button.clicked.connect(self.web_btn_clicked)
        self.qiwi_button.clicked.connect(self.qiwi_btn_clicked)
        self.start_button.clicked.connect(self.start_btn_clicked)

    def start_btn_clicked(self):
        api_id = self.api_id.text()
        api_hash = self.api_hash.text()
        chat_id = self.chat_id.text()
        required_value = self.min_value.value()
        dice_type = self.dice_type.currentIndex()
        if chat_id[0].isdigit() or chat_id.startswith('-'):
            chat_id = int(chat_id)
        if dice_type == 0:
            emoticon = u'\U0001F3B2' #dice
        elif dice_type == 1:
            emoticon = u'\U0001F3AF' #darts
        elif dice_type == 2:
            emoticon = u'\U0001F3C0' #basketball
        self.log.clear()
        self.log.append("=== Скрипт запущен ===")
        send_dice(self, api_id, api_hash, chat_id, required_value, emoticon)
        self.log.append("=== Скрипт завершился ===")
        self.start_button.toggle()

    def qiwi_btn_clicked(self):
        webbrowser.open('https://link.to', new = 2)

    def web_btn_clicked(self):
        webbrowser.open('https://link.to', new = 2)

    def tg_btn_clicked(self):
        webbrowser.open('https://link.to', new = 2)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
