#load packages
from psychopy import visual, core, event, gui, data
import random
import pandas as pd

#define dialogue box
dialog = gui.Dlg(title = 'Emotions and Chords Experiment')
dialog.addField('Participant ID: ')
dialog.addField('Age: ')
dialog.addField('Gender: ', choices = ['Female','Male','Other'])
#show dialogue 
dialog.show()
if dialog.OK:
    ID = dialog.data[0]
    Age = dialog.data[1]
    Gender = dialog.data[2]
elif dialog.Cancel:
    core.quit()

#define window
win = visual.Window(fullscr=True, color= 'Black')

#define a stopwatch
stopwatch = core.Clock()

#get the date and time to make unique logfile name
date = data.getDateStr()
#define logfile
columns = ['Trial','Timestamp','ID','Age','Gender','Note','Chord','Emotion','NotEmotion','ReactionTime']
DATA = pd.DataFrame(columns=columns)


#the chords being played
stimuli = ['Maj7', 'min7', 'Dom7', 'min7b5', 'Maj7', 'min7', 'Dom7', 'min7b5', 'Maj7', 'min7', 'Dom7', 'min7b5', 'Maj7', 'min7', 'Dom7', 'min7b5']
notes = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b']

#emotions
emotions = ['ANGER', 'DISGUST', 'FEAR', 'HAPPINESS', 'SADNESS', 'SURPRISE']

#left function
def left():
    display_text('left press')
    core.wait(0.5)

#right function
def right():
    display_text('right press')
    core.wait(0.5)
    
def weird():
    display_text('you did something weird')
    core.wait(1)

#randomize the order of stimuli
#random.shuffle(stimuli)

#display text function
def display_text(x):
    txt = visual.TextStim(win, text=x, font='', pos=(0.0, 0.0))
    txt.draw()
    win.flip()
#    event.waitKeys(keyList = ['left', 'right', 'escape'])

def draw_left(x):
    txt = visual.TextStim(win, text=x, font='', pos=(-0.2, 0.0))
    txt.draw()
    
def draw_right(x):
    txt = visual.TextStim(win, text=x, font='', pos=(0.2, 0.0))
    txt.draw()

#display text higher
def display_text2(x):
    txt = visual.TextStim(win, text=x, font='', pos=(0.0, 0.618))
    txt.draw()


display_text('Welcome to the experiment, my dude. Press any key to continue')
event.waitKeys()

#display each picture one by one until key press
for i in stimuli:
    for e in emotions:
        randstim = random.choice(stimuli)
        randnote = random.choice(notes)
        display_text2(str(randnote)+str(randstim))
        randemoleft = random.choice(emotions)
        randemoright = random.choice(emotions)
        while randemoright == randemoleft:
            randemoright = random.choice(emotions)
        draw_left(str(randemoleft))
        draw_right(str(randemoright))
        win.flip()
    stopwatch.reset() #reset stopwatch
    key = event.waitKeys(keyList = ['left', 'right', 'escape'])
    if key[0] == 'left':
        emotion = randemoleft
        notemotion = randemoright
        reaction_time = stopwatch.getTime()
        left()
    elif key[0] == 'right':
        emotion = randemoright
        notemotion = randemoleft
        reaction_time = stopwatch.getTime()
        right()
    elif key[0] == 'escape':
        logfilename = 'logfiles/logfile_{}_{}.csv'.format(ID, date)
        DATA.to_csv(logfilename)
        core.quit()
        win.close()
    else:
        weird()
    DATA = DATA.append({
        'Timestamp': date,
        'ID': ID,
        'Age': Age,
        'Gender': Gender,
        'Note': randnote,
        'Chord': randstim,
        'Emotion': emotion,
        'NotEmotion': notemotion,
        'ReactionTime': reaction_time}, ignore_index = True)

#make file name
logfilename = 'logfiles/logfile_{}_{}.csv'.format(ID, date)
#save the logfile to the hard drive
DATA.to_csv(logfilename)

display_text('The experiment is done. Kthxbye.')
event.waitKeys()
