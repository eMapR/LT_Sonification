This folder contains the starting point for sonification. A way to convert data in to sound. Peder N was 
thinking of using a LandTrendr Time Series to make such sounds. According to the link Peder provided it
seems pretty straight forward. (https://medium.com/@astromattrusso/sonification-101-how-to-convert-data-into-music-with-python-71a6dd67751c).
So, I'll try to get this setup with a simple test from the link above. 

This looks like it runs from just python using a csv of data. 

	Python Version:

		2.7

	Python packages :

		Pandas - installed no issuses
		Matplotlib - installed no issuses 
		audiolazy - installed no issues
		midiutil - I can not find this package for Conda 
		pygame - 


	conda :

		conda create --name=lt_song python=2.7

		conda activate lt_song

		conda install pandas

		conda install matplotlib

		conda install -c auto audiolazy

		
			
