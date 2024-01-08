class HomoSapiens:
    def speak(self):
        print("I can speak")


class Man(HomoSapiens):
    def wear(self):
        print("I can wear")

class ManChild(Man):
    def eat(self):
        print("I can eat")

d =ManChild()
d.wear()
d.speak()
d.wear()
print(ManChild.mro())
