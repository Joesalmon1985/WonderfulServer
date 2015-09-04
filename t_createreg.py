#!/usr/bin/env python
# vim: tabstop=4 softtabstop=4 shiftwidth=4 smarttab expandtab:

import unittest

# A test for for whole shebang

from createreg import puc

naDataBase = 'test.db'
nauc1 = 'testcouncil1.csv'
nauc2 = 'testcouncil2.csv'

class T( unittest.TestCase ):
	def test_puc (self):
	puc = puc ( )
	puc.thing (naDatabase, nauc1, nauc2)
	with sqlite3.connect( naDataBase ) as conn:
		cursor = conn.cursor()
            	torun = """select * from electoralreg limit 3"""
	        cursor.execute ( torun )
        	r = cursor.fetchone ( )
		foundelect = r [0]
		print foundelect
        	self.assertEqual(0, foundfreshdatanomembers, 'This dont work')
