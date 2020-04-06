import sys
import os
import json


def get_lines(file_path):
	lines = []
	f = open(file_path, 'r').readlines()
	f = [i.strip() for i in f]
	print(f)
	c = 0
	for line in f:
		if line.startswith('#Text='):
			line = line[6:]
			nextline = f[c+1]
			emotions = None
			try:
				emotion = nextline.split('\t')[3]
				emotions = emotion.split('|')
			except IndexError:
				emotions = None
			lines.append((line, emotions))
		c+=1
	return lines


def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        p = root.replace(startpath, '')
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))
            if f == 'gesine.fuhrmann.tsv':
                print(os.path.basename(root))
                filename = startpath+'/'+p+'/'+f
                #print(filename)
                newname = os.path.basename(root).split('.')[0] + '.gesine.json'
                #print(newname)
                save_poem(filename, newname)

def save_poem(filepath, filename):
	lines = get_lines(filepath)
	f = open('GermanRebuild/'+filename, 'w')
	json.dump(lines, f)


#get_lines(sys.argv[1])
list_files(sys.argv[1])
