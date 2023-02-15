import pandas as pd 
import matplotlib.pylab as plt
from audiolazy import str2midi, midi2str



df = pd.read_csv('/vol/v1/proj/LT_Sonification/data/testData.csv')  #load data as a pandas dataframe




ages = df['age'].values   #get age values in an array
diameters = df['diameter'].values  #get diameter values in an array
#plt.scatter(ages, diameters, s=diameters)
#plt.xlabel('age [Myrs]')
#plt.ylabel('diameter [km]')
#plt.show()


times_myrs = max(ages) - ages  #measure time from 1st impact in data
#plt.scatter(times_myrs, diameters, s=diameters)
#plt.xlabel('time since impact 0 [Myrs]')
#plt.ylabel('diameter [km]')
#plt.show()


def map_value(value, min_value, max_value, min_result, max_result):

  result = min_result + (value-min_value)/(max_value-min_value)*(max_result-min_result)

  return result



myrs_per_beat = 25  #conversion factor: Myrs for each beat of music
t_data = times_myrs/myrs_per_beat #

duration_beats = 52.8 #desired duration in beats (actually, onset of last note)
t_data = map_value(times_myrs, 0, max(times_myrs), 0,duration_beats)


bpm = 60  #beats per minute, if bpm = 60, 1 beat = 1 sec 
duration_sec = duration_beats*60/bpm #duration in seconds 
#print('Duration:', duration_sec, 'seconds')
##>> Duration: 52.8 seconds


y_data = map_value(diameters, min(diameters), max(diameters), 0, 1) 
#plt.scatter(times_myrs, y_data, s=50*y_data)
#plt.xlabel('time [Myr]')
#plt.ylabel('y data [normalized]')
#plt.show()


y_scale = 0.5  #lower than 1 to spread out more evenly
y_data = y_data**y_scale
#plt.scatter(times_myrs, y_data, s=50*y_data)
#plt.xlabel('time [Myr]')
#plt.ylabel('y data [normalized]')
#plt.show()

#print(str2midi('C3'))
##>> 48
#print(midi2str(63))
##>> 'D#4'

note_names = ['C2','D2','E2','F2','G2','A2','B2','C3','D3','E3','F3','G3','A3','B3','C4','D4','E4','F4','G4','A4','B4']

note_names = ['C2','D2','E2','G2','A2','C3','D3','E3','G3','A3','C4','D4','E4','G4','A4']

note_names = ['C1','C2','G2', 'C3','E3','G3','A3','B3','D4','E4','G4','A4','B4', 'D5','E5','G5','A5','B5','D6','E6','F#6','G6','A6']



note_midis = [str2midi(n) for n in note_names] 
n_notes = len(note_midis)




midi_data = []
for i in range(len(y_data)):
    note_index = int(round(map_value(y_data[i], 0, 1, n_notes-1, 0))) 
    midi_data.append(note_midis[note_index])
#plt.scatter(t_data, midi_data, s=50*y_data)
#plt.xlabel('time [beats]')
#plt.ylabel('midi note numbers')
#plt.show()



vel_min = 35127   #minimum and maximum note velocity
vel_max = 35127   #minimum and maximum note velocity
vel_data = []
print(y_data)
for i in range(len(y_data)):
    note_velocity = int(round(map_value(y_data[i],0,1,vel_min, vel_max))) 
    vel_data.append(note_velocity)
    
#plt.scatter(t_data, midi_data, s=vel_data)
#plt.xlabel('time [beats]')
#plt.ylabel('midi note numbers')
#plt.show()


from midiutil import MIDIFile 
    
#create midi file object, add tempo
my_midi_file = MIDIFile(1) #one track 
my_midi_file.addTempo(track=0, time=0, tempo=bpm) 
#add midi notes
for i in range(len(t_data)):
    my_midi_file.addNote(track=0, channel=0, time=t_data[I], pitch=midi_data[i], volume=vel_data[I], duration=2)
#create and save the midi file itself
with open(filename + '.mid', "wb") as f:
    my_midi_file.writeFile(f)



#import pygame 
#pygame.init()
#pygame.mixer.music.load(filename + '.mid')
#pygame.mixer.music.play()
#pygame.mixer.music.stop() #run this to stop, it's the only way!

