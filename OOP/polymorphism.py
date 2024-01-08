class Language:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class French(Language):
    pass
    # def speak(self):
    #     return "Bonjour!"


class Spanish(Language):
    def speak(self):
        return "Hola!"

def intro(language):
    print(language.speak())

neha = French()
john = Spanish()

intro(neha)
intro(john)
