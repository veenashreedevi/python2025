class Bird:
   def speak(self):
     print("I chirp")
class Parrot(Bird):
    def speak(self):
      print("I mimic")
parrot = Parrot()
parrot.speak()
