#! /usr/bin/python

""" Program Aim

    More description about the program
"""

__author__ = "Shreyas"
__email__ = "shreyas@ischool.berkeley.edu"
__python_version = "Python 2.7.3 -- EPD 7.3-2 (32-bit)"


from optparse import OptionParser


def getInput():
	parser = OptionParser()

	parser.add_option('-d', '--dir', dest='dirpath')
	parser.add_option('-t', '--type', dest='filetype', default='xml')

	(option, args) = parser.parse_args()

	if not option.dirpath:
		return parser.error('directory path not given. User --dir="path.to.directory" for file statistics')

	return {'dir': option.dirpath, 'type': option.filetype}


def main():
	userInput = getInput()
	print userInput['dir'], userInput['type']


if __name__ == '__main__':
	main()
