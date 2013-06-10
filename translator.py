#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author: GrakovNe

import urllib2
import sys

def translate(text='Example',TL='en',CL='auto'):
  query = 'http://translate.google.ru/translate_a/t?client=x&text=%s&sl=%s&tl=%s' % (text,CL,TL)
	headers = { 'User-Agent' : 'Mozilla/5.0' } # Making a fake User-Agent for google cheaping
	req = urllib2.Request(query, None, headers)
	answer = urllib2.urlopen(req).read()
	StartPos=answer.find('"trans":"') # finding start and end segments of translation
	FinPos=answer.find('","orig')
	FinalAnswer = answer[StartPos+9:FinPos] # extracting the tranlation
	return FinalAnswer

def bringing(input):
	output=''
	for x in input:
		if x ==' ': #Server will break the query if it have a '.', '!', '?' and cut the query if it have a SPACE.
			output+='%20'
		elif x =='.' or x == '!' or x=='?':
			pass
		else:
			output+=x
	return output
	
	
# http://translate.google.ru/translate_a/t?client=x&text={TEXT}&sl={LANG_FROM}&tl={LANG_TO} - Example link
