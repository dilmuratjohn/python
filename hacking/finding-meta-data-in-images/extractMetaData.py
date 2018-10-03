import argparse
from PIL import Image
from PIL.ExifTags import TAGS

def getMetaData(imgname, out):
	try:
		metaData = {}

		imgFile = Image.open(imgname)
		print "Getting meta data..."
		info = imgFile._getexif()
		if info:
			print "found meta data!"
			for (tag, value) in info.items():
				tagname = TAGS.get(tag, tag)
				metaData[tagname] = value
				if not out:
					print tagname, value

			if out:
				print "Outputting to file..."
				with open(out, 'w') as f:
					for (tagname, value) in metaData.items():
						f.write(str(tagname)+"\t"+\
							str(value)+"\n")
		
	except:
		print "Failed"

def Main():
	parser = argparse.ArgumentParser()
	parser.add_argument("img", help="Name of an image File")
	parser.add_argument("--output","-o", help="dump data out to File.")
	args = parser.parse_args()
	if args.img:
		getMetaData(args.img, args.output)
	else:
		print parser.usage

if __name__ == '__main__':
	Main()