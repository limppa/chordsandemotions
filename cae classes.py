
class Chord:

    def __init__(self,name):
        self.name = name
        #self.emo = None
        
    class Emotion:

        def __init__(self,name,score):
            self.name = name
            self.score = score

        class Compared:

            def __init__(self,name):
                self.name = name
                

Maj7 = Chord('Maj7')

Maj7angr = Maj7.Emotion('angr',5)


print(Maj7angr.score)



