from flask import Flask

app = Flask(__name__)


class DataBase:
    messages: list

    def __init__(self):
        pass

    def add_message(self, message: str):

        new_message = MessageData(message)

        self.messages.append(new_message)

    def get_division(self, division: int) -> list:

        div_messages = []

        for message in self.messages:
            if message.division() == division:
                div_messages.append(message)

        div_messages.sort(key=lambda m: m.urgency, reverse=True)
        return [m.message for m in div_messages]


class MessageData:
    message: str
    division: int
    urgency: int

    def __init__(self, message: str):
        self.message = message
        self.create_classification()

    def message(self) -> str:
        return self.message

    def division(self) -> int:
        return self.division

    def urgency(self) -> int:
        return self.urgency

    def create_classification(self):
        pass


database = DataBase()


@app.route('/newmessage/<message>', methods=['GET'])
def add_new_message(message):  # put application's code here
    database.add_message(message)
    return 'Ok'


@app.route('/getdivmessage/<div>', methods=['GET'])
def get_div_message(div: int):  # put application's code here
    messages = database.get_division(div)
    return messages


if __name__ == '__main__':
    app.run()
