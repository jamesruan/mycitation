#!/usr/bin/env python
# Building replacing file 
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

def find_index(f, o):
	pattern = re.compile('#(\w+)#')
	odb = csv_db.read_db(o)
	odb_id = [x['id'] for x in odb]
	db = []
	db_id = []

	for l in f:
		match = re.findall(pattern, l)
		if match is not []:
			for i in match:
				if i in db_id: #replicated entry
					continue
				
				if i in odb_id:
					entry = odb[odb_id.index(i)]
					entry['tag'] = len(db) + 1
				else: #new entry
					entry = {'id': i, 'tag':len(db) + 1, 'cite': 'TODO'}
	
				db.append(entry)
				db_id.append(i)

	return db

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Building replacing table file')
	parser.add_argument('--old', metavar='OLD', type=argparse.FileType('r'), help="old replacing table.")
	parser.add_argument('in', metavar='IN', type=argparse.FileType('r'), help="file with indexs marked by #id#.")
	parser.add_argument('out', metavar='OUT', type=argparse.FileType('w'), help="file to write.")
	args = parser.parse_args()
	
	infile = vars(args)['in']
	oldfile = vars(args)['old']
	outfile = vars(args)['out']
	
	db = find_index(infile, oldfile)

	csv_db.write_db(db, outfile)
	
	infile.close()
	outfile.close()
	if oldfile is not None:
		oldfile.close()
