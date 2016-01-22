#!/usr/bin/env python
# Use replacing file to generates citation
# Copyright (C) 2016 James Ruan <ruanbeihong@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import argparse
import re
import csv_db

def replce(db, inf, outf):
	db_id = [x['id'] for x in db]
	for l in inf:
		s = l
		for i in db_id:
			entry = db[db_id.index(i)]
			pattern = re.compile('#'+i+'#')
			s = re.sub(pattern, '[' + str(int(entry['tag'])) + ']', s)
		outf.write(s)

	outf.write("\n")
	for i in db_id:
		entry = db[db_id.index(i)]
		s = '[' + str(int(entry['tag'])) + ']: ' + entry['cite'] + "\n"
		outf.write(s)
	

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Tagging file based on replacing table file.')
	parser.add_argument('table', metavar='TABLE', type=argparse.FileType('r'), help="replacing table.")
	parser.add_argument('in', metavar='IN', type=argparse.FileType('r'), help="file to be replaced, containing #id#.")
	parser.add_argument('out', metavar='OUT', type=argparse.FileType('w'), help="file to write.")
	args = parser.parse_args()
	
	tablefile = vars(args)['table']
	infile = vars(args)['in']
	outfile = vars(args)['out']
	
	db = csv_db.read_db(tablefile)
	replce(db, infile, outfile)

	tablefile.close()
	infile.close()
	outfile.close()
