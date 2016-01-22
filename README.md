Python scripts that help to generate citatation notes.

#build.py

	usage: build.py [-h] [--old OLD] IN OUT

	Building replacing table file

	positional arguments:
	  IN          file with indexs marked by #id#.
	  OUT         file to write.

	optional arguments:
	  -h, --help  show this help message and exit
	  --old OLD   old replacing table.

Any plain text file IN that has 'id' marked by '#': `#id#`.

	build.py IN db.csv

will generate a replacing table file 'db.csv' that has following format:

	'id','tag','cite'
	...

in which 'cite' field need to be manually edited to the right citation string.

If IN file is changed,

	build.py IN --old db.csv new_db.csv

will generate a replacing table file 'new_db.csv' with 'cite' field imported from 'db.csv'.


#replace.py

	usage: replace.py [-h] TABLE IN OUT

	Tagging file based on replacing table file.

	positional arguments:
	  TABLE       replacing table.
	  IN          file to be replaced, containing #id#.
	  OUT         file to write.

	optional arguments:
	  -h, --help  show this help message and exit

Given replacing table file TABLE and file IN, this file replaces `#id#` in file IN to `[tag]`, with `tag` a field defined int TABLE file.
And a reference list is appended end of file in format:

	[tag]: cite
	...
