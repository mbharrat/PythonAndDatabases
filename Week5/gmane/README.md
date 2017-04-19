# GMane Example

Assignment included:
	
	*multiple files to generate webpage with d3.js
	*a file called gmane.py which is basically a web crawler which can crawl on gmane.org (using local copy on chucks website to avoid crashing)
		*this site has GIGS of emails
	*gmane.py creates content.sqlite which is just raw data
	*gmodel.py runs and uses mapping.sqlite to create index.sqlite
	*you have three options now
	*run gbasic.py to debug with histogram and dump to terminal
	*run gline.py / gyear.py which generates gline.js and gline.htm uses that in conjunction with d3.js to display a line graph
	*run gword.py which generates gword.js and gword.htm uses that in conjuction with d3.js to display some cool word art

COMMAND TO RUN:

	For given file:
		Python gmane.py
	
			How many messages:

				Enter as many as you want to retrieve and content.sqlite generated

		Python gmodel.py

			runs mapping process and creates index.sqlite

		Python gbasic.py

			How many to dump?

				Enter how many to print to screen for debugging

		Python gline.py

			populates gline.js

				open gline.htm
		
		Python gword.py

			populates gword.js

				open gword.js
	 

