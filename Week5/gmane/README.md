# Pagerank Example

Assignment included:
	
	*multiple files to generate webpage with d3.js
	*a file called spider.py which is basically a web crawler
	*after spider runs a file called spider.sqlite is created with all the pages in it
	*two maintence programs exist: sprank.py and spreset.py
		*sprank.py calculated page rank of the pages...the more iterations that run, the more normalized your data will be
		*spreset.py resets all the page ranks to 1
	*once sprank.py runs and completes, you can either use spdump.py to dump data to terminal
	*or you can use spjson.py which takes data in database and creates a json formatted js file called force.js
	*once force.js is generated, force.html can use that file to create webpage

COMMAND TO RUN:

	For given file:
		Python spider.py
	
			Enter web url or enter:

				if enter is clicked then chucks homepage is ran

			How many pages: (enter as many as wanted)
				
				keeps prompting until command+c

		Python sprank.py

			How many iterations:

				the more the more normalized data will be

		Python spdump.py

			prints data to screen

		Python spjson.py

			How many nodes:

		Open force.html in browswer
	 

