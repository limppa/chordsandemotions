
class Chord:    #Maj7, min7, Dom7, min7b5

    def __init__(self,name):
        self.name = name
        
    class Emotion:  #angr, disg, fear, hap, sad, surp

        def __init__(self,name,score=0):
            self.name = name
            self.score = score

        class Compared: #has it been compared to another emotion and what was the result

            def __init__(self,name,result=0):
                self.name = name
                self.result = result
                

Maj7 = Chord('Maj7')

Maj7angr = Maj7.Emotion('angr')

Maj7angrdisg = Maj7angr.Compared('disg', 1) #Maj7 chord played, angr vs disg -> angr won


print(Maj7angr.score)   #how well does angr match the Maj7 chord?

print(Maj7angrdisg.result)  #who won, angr vs disg, when Maj7 was played?



