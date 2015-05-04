"""
	This is using only for convert the .py file to .exe file. 
	For converting this we need to use a software that are 
	avialable on py2exe web site. 
	OK ... Forgot about this. Just think I am using here cx_Freeze which is also avialable. 
	Download this and install this. Then runthe command below.

	__ThankYou__ (:HappY Coding :)
"""

from cx_Freeze import setup, Executable

setup(name='Flag',
	version='0.1',
	description='Setup Files',
	executables = [Executable("flag.py")])
