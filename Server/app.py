from flask import Flask
import cohere
from cohere.responses.classify import Example

app = Flask(__name__)
class DataBase:
    messages = []

    def __init__(self):
        pass

    def add_message(self, message):

        new_message = MessageData(message)

        self.messages.append(new_message)

    def get_all_messages(self):
        return self.messages

    def get_division(self, division_num) -> list:

        div_messages = []

        for message in self.messages:
            if message.division_num == division_num:
                full_and_summary = []
                full_and_summary.append(message.message)
                full_and_summary.append(message.message_summary)
                div_messages.append(full_and_summary)

        return div_messages


class MessageData:
    key = 'Txu84dIEv7gsiAg0Br6N1NoP2zye56cWJoGZEz6e'
    co = cohere.Client(key)
    message = ""
    division_num = 0

    def __init__(self, message):
        self.message = message
        self.create_classification()

    def message(self) -> str:
        return self.message

    def message_summary(self) -> str:
        text = self.message
        response = self.co.summarize(text=text)
        split_string = str(response).split(",")

        for s in split_string:
            if "summary" in s:
                summary = s.split("'")[1]

        return summary

    def division(self) -> int:
        return self.division_num

    def create_classification(self):

        examples = [
            Example("How long does the battery last on the nokia022", "420"),
            Example("What is a GPU", "420"),
            Example("What the best gaming mouse", "420"),
            Example("Will I get a virus if I visit xxxx website on the newest model", "420"),
            Example("Which phone will be best for my 8 year old", "420"),
            Example("What is the best CPU", "420"),
            Example("What is the gpu on the nexus book", "420"),
            Example("Whats the difference between the lastest model and mine", "420"),
            Example("How long does the nexus phone last", "420"),
            Example("Will the nexus s22 last me 4 years", "420"),
            Example("Which nexus phone should I get", "420"),
            Example("How do I know when the phone is done charging", "420"),
            Example("Will the new nexus TV make my friends jelious", "420"),
            Example("How do I change from one app to the other app for my nexus phone", "420"),
            Example("Will the nexus phone keep me from jumping off a bridge", "420"),
            Example("What is the warranty for the nexus buds", "420"),
            Example("When will the nexus s23 be released?", "420"),
            Example("What happens if my nexus breaks", "420"),
            Example("Will the current nexus perform badly when the new model drops", "420"),
            Example("My nexus phone camera isn't working", "69"),
            Example("Im getting lots of milfs in my area on the screen", "69"),
            Example("When I click the powerbutton twice the phone crashes", "69"),
            Example("The battery only lasts 2 hours", "69"),
            Example("My nexus phone isn't outputting any sound", "69"),
            Example("I keep getting this annoying alert when children who I dont know or give a shit about get abducted at 5 am","69"),
            Example("I keep getting a memory error whenever I try to take more then one photo a second", "69"),
            Example("There is something rattling from inside the device", "69"),
            Example("My flashlight isn't working on my Nexus phone", "69"),
            Example("The screen stops working sometimes", "69"),
            Example("My volume button isn't working on my Nexus phone", "69"),
            Example("I am trying to load photos from my old nexus phone to my new nexus phone but the transfer isnt completeing","69"),
            Example("The photos on my new nexus phone are not very clear especially at night", "69"),
            Example("My Nexus phone isn't turning on", "69"),
            Example("My nexus phone is only giving me 10 fps on minecraft", "69"),
            Example("My Nexus phone isn't receiving any calls", "69"),
            Example("im trying to get a new app onto my nexus book but for some reason whenever I click download nothing comes up","69"),
            Example("whenever I start a video game my nexus book sounds like a jet engine", "69"),
            Example("The nexus ear buds isn't connecting to my nexus phone or my nexus book", "69"),
            Example("When I downloaded more ram from the internet all my files were encrypted", "69"),
            Example("I need to begin a return for a nexus phone I purchased last week", "3"),
            Example("Can I get a refund for my nexus book, its not working anymore", "3"),
            Example("I need to return the 12 vbucks my son bought yesterday", "3"),
            Example("I ordered a Nexus black phone not a white phone so I want to return it", "3"),
            Example("So recently I bought your newest phone so that I could be a part of the herd and now I realize how unoriginal I am and I would like to return it","3"),
            Example("I need to start a refund on a phone I purchased from you guys since my parents actually got me a better one for christmas","3"),
            Example("I ordered a Nexus book not a nexus phone", "3"),
            Example("I need to return the nexus book cause putin attacked ukraine again and now i need gas money", "3"),
            Example("I recieved my nexus phone last week and turns out i am not much of a fan of the operating system, its too basic and restrictive I don't feel like i can do anything with this product","3"),
            Example("The new Nexus phone got released so I would like to return my old one instead", "3"),
            Example("I am having a problem with the new nexus TV I bought and would like to return it please", "3"),
            Example("I need to return my nexus phone and I would be willing to accept sweatshop workers instead of cash","3"),
            Example("I am very unsatisfied with my nexus purchase and wish to take my business elsewhere", "3"),
            Example("I bought my son the newest nexus console but the dumbass spilled my fucking beer all over it u better take it back","3"),
            Example("The nexus phone isn't that big so I wanted to return it", "3"),
            Example("The nexus book isn't turning on anymore so I would like to return it", "3"),
            Example("My printer is not printing correctly", "69"),
            Example("How do I add a new contact in Outlook?", "420"),
            Example("I'm having trouble connecting to the internet", "69"),
            Example("What's the best laptop for gaming?", "420"),
            Example("My phone won't charge", "69"),
            Example("How can I delete a file from my computer?", "420"),
            Example("There's an error message when I try to start the program", "69"),
            Example("What's the difference between OLED and LCD displays?", "420"),
            Example("My computer is running very slowly", "69"),
            Example("How do I set up a VPN on my router?", "420"),
            Example("I can't access my email", "69"),
            Example("What's the best antivirus software?", "420"),
            Example("My laptop keeps overheating", "69"),
            Example("How do I transfer files from my phone to my computer?", "420"),
            Example("The software crashed and I lost all my work", "69"),
            Example("What's the best graphics card for video editing?", "420"),
            Example("My internet connection is very slow", "69"),
            Example("How do I update my phone's operating system?", "420"),
            Example("I accidentally deleted an important file, can I recover it?", "69"),
            Example("What's the best browser for privacy?", "420"),
            Example("My computer won't turn on", "69"),
            Example("How do I customize the settings on my camera?", "420"),
            Example("I'm getting a lot of spam emails", "69"),
            Example("What's the best way to back up my data?", "420"),
            Example("My phone screen is cracked", "69"),
            Example("How do I download and install a new program?", "420"),
            Example("I can't access a website, it says the connection is not secure", "69"),
            Example("What's the best way to optimize my computer's performance?", "420"),
            Example("My printer is jammed and won't print", "69"),
            Example("How do I set up a dual monitor display?", "420"),
            Example("I'm having trouble connecting my Bluetooth headphones", "69"),
            Example("What's the best laptop for video editing?", "420"),
            Example("My computer keeps freezing", "69"),
            Example("How do I set up remote access to my computer?", "420"),
            Example("I'm getting a lot of pop-up ads", "69"),
            Example("What's the best way to secure my home Wi-Fi network?", "420"),
            Example("My mouse isn't working", "69"),
            Example("How do I clear my browser cache?", "420"),
            Example("I can't connect to my wireless printer", "69"),
            Example("What's the best laptop for business?", "420"),
            Example("My computer is making strange noises", "69"),
            Example("How do I set up a password for my wireless network?", "420"),
            Example("I'm having trouble sending emails", "69"),
            Example("What's the best way to clean my computer?", "420"),
            Example("My phone is running out of storage space", "69"),
            Example("How do I uninstall a program?", "420"),
            Example("How do I update my antivirus software?", "420"),
            Example("Can you recommend a good laptop for programming?", "420"),
            Example("I'm having trouble connecting my printer to my Wi-Fi network.", "69"),
            Example("I think there's a bug in the latest update of my video editing software.", "69"),
            Example("My new keyboard isn't working properly. What should I do?", "69"),
            Example("I accidentally deleted an important file. Can I recover it?", "69"),
            Example("What's the best way to protect my online privacy?", "420"),
            Example("My computer keeps crashing. What should I do?", "69"),
            Example("How do I clear my browser history?", "420"),
            Example("I need a new monitor for my gaming setup. Any suggestions?", "420"),
            Example("My phone won't charge. What's the problem?", "69"),
            Example("What's the difference between a solid-state drive and a hard disk drive?", "420"),
            Example("My laptop is overheating. How do I fix it?", "69"),
            Example("How do I set up a home theater system?", "420"),
            Example("My computer won't boot up. What should I do?", "69"),
            Example("How do I backup my data?", "420"),
            Example("I need to upgrade my graphics card. Any recommendations?", "420"),
            Example("I'm having trouble connecting my Bluetooth headphones to my phone.", "69"),
            Example("How do I remove a virus from my computer?", "420"),
            Example("What's the best free antivirus software?", "420"),
            Example("I need to format my external hard drive. How do I do it?", "420"),
            Example("My webcam isn't working. What's the problem?", "69"),
            Example("How do I calibrate my monitor?", "420"),
            Example("What's the best software for video editing?", "420"),
            Example("My computer is running slow. How do I speed it up?", "69"),
            Example("How do I install a new operating system?", "420"),
            Example("What's the difference between RAM and storage?", "420"),
            Example("My mouse isn't working. What should I do?", "69"),
            Example("How do I optimize my computer for gaming?", "420"),
            Example("What's the best way to secure my Wi-Fi network?", "420"),
            Example("I'm having trouble connecting to the internet. What should I do?", "69"),
            Example("How do I delete temporary files?", "420"),
            Example("What's the best antivirus software for Mac?", "420"),
            Example("My laptop battery isn't holding a charge. What should I do?", "69"),
            Example("How do I partition my hard drive?", "420"),
            Example("What's the best software for photo editing?", "420"),
            Example("My computer is making strange noises. What's the problem?", "69"),
            Example("How do I install a new graphics card?", "420"),
            Example("What's the difference between HDMI and DisplayPort?", "420"),
            Example("My printer is printing blank pages. What should I do?", "69"),
            Example("How do I optimize my Wi-Fi network?", "420"),
            Example("The nexus phone isn't that big so I wanted to return it", "3"),
            Example("The nexus book isn't turning on anymore so I would like to return it", "3"),
            Example("I am very unsatisfied with my nexus purchase and wish to take my business elsewhere", "3"),
            Example("I recieved my nexus phone last week and turns out i am not much of a fan of the operating system, its too basic and restrictive I don't feel like i can do anything with this product","3"),
            Example("The new Nexus phone got released so I would like to return my old one instead", "3"),
            Example("I am having a problem with the new nexus TV I bought and would like to return it please", "3"),
            Example("I ordered a Nexus book not a nexus phone", "3"),
            Example("I ordered a Nexus black phone not a white phone so I want to return it", "3"),
            Example("I need to begin a return for a nexus phone I purchased last week", "3"),
            Example("Can I get a refund for my nexus book, its not working anymore", "3"),
            Example("I received the wrong item in my order and I need to return it", "3"),
            Example("The shoes I ordered don't fit, can I exchange them for a different size?", "3"),
            Example("I want to return my laptop because it's not working properly", "3"),
            Example("I accidentally ordered the wrong color, how can I return it?", "3"),
            Example("I want to return this product but I can't find the order number", "3"),
            Example("I want to return a product but the return policy is unclear", "3"),
            Example("I received a damaged product and I need to return it", "3"),
            Example("I want to return an item but I lost the original packaging", "3"),
            Example("Can I return a product I bought online at a physical store location?", "3"),
        ]

        inputs = [self.message]

        response = self.co.classify(inputs=inputs, examples=examples)

        classify = str(response[0])

        split_string = classify.split(',')

        for s in split_string:
            if 'prediction' in s:
                prediction = ''.join(filter(str.isdigit, s))

        self.division_num = int(prediction)



database = DataBase()


@app.route('/newmessage/<message>', methods=['GET'])
def add_new_message(message):  # put application's code here
    database.add_message(message)
    return 'Ok'


@app.route('/getdivmessage/<div>', methods=['GET'])
def get_div_message(div: int):
    messages = database.get_division(div)
    return messages

@app.route('/getallmessages', methods=['GET'])
def get_all():
    messages = database.get_all_messages()
    return str(messages)

if __name__ == '__main__':
    app.run()
