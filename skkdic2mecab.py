import re
import jctconv
import sys

__cost = 200


def parseline(line):
	obj = line.split('/')
	for word in obj[1:]:
		if word != '':
			word = word.split(';')
			if(len(word) > 1 and re.search('(名詞|組織名|地名|人名)',word[1])):
				hinshi = '名詞'
#				if(re.search('(人名)',word[1])):
#					hinshi = '人名'
#				if(re.search('(地名)',word[1])):
#					hinshi = '地名'
			
				keyword = word[0].replace(',','')
				
				yomi = obj[0].strip()
				kana = jctconv.hira2kata(yomi)
				return ('%s,0,0,%i,%s,%s,*,*,*,*,%s,%s,%s' % (keyword,__cost,hinshi,'一般',yomi,kana,kana))


file = open(sys.argv[1])
for line in file.readlines():
	if(re.search('^[^;]',line)):
		result =parseline(line)
		if(result):
			print(result)
