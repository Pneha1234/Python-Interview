class HomoSapiens:
    def speak(self):
        print("I can speak")

class Man(HomoSapiens):
    def wear(self):
        print("I can wear")

d =Man()

d.speak()
d.wear()