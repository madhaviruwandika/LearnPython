from datetime import datetime
class Dog:
    _legs = 4
    def __init__(self, name):
        self.sound = 'Bark'
        self.name = name

    def getLegs(self):
        print('legs count from instance',self._legs)
        return self._legs
    def speak(self):
        print(f'Dog {self.name} says {self.sound}')

my_dog = Dog('tommy')

my_dog.speak()
my_dog.getLegs()
print(Dog._legs)

## inheritance
print('\n------------------inheritance---------------------')
class Abc(Dog):
    def speak(self):
        print(f'Dog {self.name} says ba ba ba')


my_abc = Abc('Rocky')
my_abc.speak();
my_abc.getLegs()
print(Abc._legs)


print('\n------------Example of Simple Messenger------------------')
### Example of Simple Messenger
class Messenger:
    def __init__(self, listeners = []):
        self.listeners = listeners

    def sendMessage(self, message):
        for listener in self.listeners:
            listener.recieve(message)


class Reciever(Messenger):
    def __init__(self, listeners = []):
        super().__init__( listeners)
        self.messages = []

    def recieve(self,message):
        self.messages.append({'message':message, 'time': datetime.now().strftime('%m-%d-%Y %H:%M:%S') })

    def printMessages(self):
        for m in self.messages:
            print(f'Message: "{m["message"]}" Time "{m["time"]}"')

        self.messages = []

reciever = Reciever()
messenger = Messenger([reciever])

messenger.sendMessage('Hello, This is first message')
messenger.sendMessage('Hello, This is second message')
messenger.sendMessage('Hello, This is third message')

reciever.printMessages()

