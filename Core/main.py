import os
from scipy.io import wavfile
import matplotlib.pyplot as plt
from scipy import signal


path = r'C:/Users/EBOHOC/Documents/SoundAnalysis/SoundAnalysis/Sample_Data'

lista = list(os.listdir(path))
lista_enum = list(enumerate(lista))
print(lista_enum)

for item in lista_enum:
    print(str(item[0]) + ' - ' + item[1])

selection = input("Select file for analysis: ")
name = lista_enum[int(selection)]
sample_rate, data = wavfile.read(os.path.join(path, name[1]))
f, t, Sxx = signal.spectrogram(data, sample_rate)
<<<<<<< HEAD
plt.subplot(1,2,1)
plt.plot(data)
plt.subplot(1,2,2)
plt.pcolormesh(t, f, Sxx, shading='gouraud')
=======
plt.plot(data)
>>>>>>> ff6fb4c3ee07fb4ce6e2cb7976045454165c10aa
plt.show()



<<<<<<< HEAD

=======
>>>>>>> ff6fb4c3ee07fb4ce6e2cb7976045454165c10aa
