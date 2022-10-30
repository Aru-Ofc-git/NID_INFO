import os
try:
	from nidinfo import nid
except:
	os.system('pip install bdnidinfo==1.1.2')

nid.linux()