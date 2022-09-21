# MusicVisualisationUsingEmotionRecognition
Currently, this is for Hindustani Classical Music. Aims to apply ML to classify a classical music audio clip into an emotion class, and use this emotion class to visually represent the audio temporally. Future work will look towards applying the same methodology for better visual representation and expansion for all genres of music.


Read the Powerpoint Presentation for the approach, flowcharts and screenshots.
If you want to run the code, download all the files here to your local computer. Run songchoicepage.html on Chrome to choose a songfile out of a few. Run predictmodel1.py and predictmodel2.py if you just want to predict the valence and arousal classes for a songfile. Run the main FAudioWaveform.pde file to see the visualiation for the chosen songfile.

Make sure you have Java, Processing and Python installed on your computer.


If you want to manually extract features from song files to create your own dataset, install Matlab and mirtoolbox, and run the code given in featureextraction_featuresetformodel1.txt & featureextraction_featuresetformodel2.txt on Matlab. 

You would also need to manually classify your music files into Valence & Arousal classes 
on the basis of the below diagram 
![image](https://user-images.githubusercontent.com/57823096/191508988-8413bbaa-ac07-4bf3-a22a-919a61ddec77.png)

to create your own datamodel1.csv and datamodel2.csv (since there is no preexisting dataset of songs and their corresponding valence/arousal emotion class).



You can also access PresentationPPT_HindustaniClassicalMusicVisualisation.pptx in the following Google Drive link:
https://docs.google.com/presentation/d/16tZcGZeqWkJxnQgvCDt5mip9LtM4tCta/edit?usp=sharing&ouid=103916957716059002780&rtpof=true&sd=true


Feel free to contact me at anushabhowmick@ymail.com for more details on the implementation

