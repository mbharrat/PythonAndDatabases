# GEODATA Example

Assignment included:
	
	edit: this is my assignment...in where.data the address Rutgers University-New Brunswick was added
	edit: in geoload.py the service url is switched to the google api instead of dr-chucks
	*multiple files to generate webpage
	*a file called geoload.py that takes the data in where.data and creates a file called geodata.sqlite and populates those location into that database
	*once geoload.py is ended another file called geodump.py reads geodata.sqlite and creates a print on the terminal as well as prints a json javascript file (where.js) to be used by the html
	*once that file has finished running, the html link called where.html is active and markers can be seen

COMMAND TO RUN:

	For given file:
		Python geoload.py
	
			Data is being download: to end control+c

		Python geodump.py

			Runs until ends

		Open where.html in broswer
	 

