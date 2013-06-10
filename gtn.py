#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Author: GrakovNe

import translator # My module
import sys
args = sys.argv[1:]
if args==[]:
  print'''GTN - Simple translator working through the Google server,
which allows to translate any text in multiple languages​​. 
To use, simply type the quoted text, the language to which you want to 
translate the original language. The second and third 
parameters can not be specified. In this case, the target language 
will be English and the original language will be defined automatically. 

	EXAMPLE: 
	
		GTN 'Hello World' ru

	ADDITIONAL KEYS: 
	--help   - will showthis text 
	--author - will show information about the author 
	--donate - will show ways to donate to the project 
	--langs  - will show list of supported languages 
	
P.S. I ask Google to forgive me for the free use of the translator!
And i'm sorry for my English. I'm russian and know it not enough good but i'm learn'''
else:
	if args[0][0]=='-':
		if args[0]=='--help':
			print '''GTN - Simple translator working through the Google server,
which allows to translate any text in multiple languages​​. 
To use, simply type the quoted text, the language to which you want to 
translate the original language. The second and third 
parameters can not be specified. In this case, the target language 
will be English and the original language will be defined automatically. 

	EXAMPLE: 
	
		GTN 'Hello World' ru

	ADDITIONAL KEYS: 
	--help   - will showthis text 
	--author - will show information about the author 
	--donate - will show ways to donate to the project 
	--langs  - will show list of supported languages 
	
P.S. I ask Google to forgive me for the free use of the translator!
And i'm sorry for my English. I'm russian and know it not enough good but i'm learn'''
	
		if args[0]=='--author':print '''AUTHOR: 
	GrakovNe
		
CONTACTS: 
	ICQ: 562-83-10
	E-MAIL: grakovne@yandex.ru
	WEB: http://grakovne.org'''
		if args[0]=='--donate':
			print '''If you liked this program you may give me some money for next projects
			
	WebMoney-R: R274072587184
	WebMoney-Z: Z324248665519
	Yandex.Money: 410011029076689
	
Thank you anyway!'''
		if args[0]=='--langs':
			print '''
		Azerbaijan - az
		Albanian   - sq
		English    - en
		Arabic     - ar
		Armenian   - hy
		Afrikaanas - af
		Basksy     - eu
		Belarus    - be
		Bengali    - bn
		Bulgarian  - bg
		Bosnian    - bs
		Welsh      - cy
		Hungarian  - hy
		Vietnamese - vi
		Galician   - gl
		Dutch      - nl
		Greek      - el
		Georgia    - ka
		Gujarati   - gu
		Danish     - da
		Hebrew     - iw
		Yiddish    - yi
		Indonesian - id
		Irish      - ga
		Icelandic  - is
		Spanish    - es
		Italian    - it
		Kannada    - kn
		Catalan    - ca
		Chinese    - zn-CN
		Korean     - ko
		Creole     - ht
		Khmer      - km
		Laos       - lo
		Latin      - la
		Latvian    - lv
		Lithuanian - lt
		Macedonian - mk
		Malay      - ms
		Malta      - mt
		Marathi    - mr
		German     - de
		Norwegian  - no
		Farsi      - fa
		Polish     - pl
		Portuguese - pt
		Romanian   - ro
		Russian    - ru
		Sebuansky  - ceb
		Serbian    - sr
		Slovak     - sk
		Slovenian  - sl
		Swahili    - sw
		Tagalog    - tl
		Thai       - th
		Tamil      - ta
		Telugu     - te
		Turkish    - tr
		Ukrainian  - uk
		Urdu       - ur
		Finnish    - fi
		French     - fr
		Hindi      - hi
		Hmong      - hmn
		Croatian   - hr
		Czech      - cs
		Swedish    - sv
		Esperanto  - eo
		Estonian   - et
		Javanese   - jw
		Japanese   - ja'''
	else:
		TextToTranslate = args[0]
		if len (args)>1:
			TargetLanguage = args[1]
		else:
			TargetLanguage = 'en'
		if len (args)>2:
			CurrentLanguage = args[2]
		else:
			CurrentLanguage = 'auto'
			
		print translator.translate(translator.bringing(TextToTranslate),TargetLanguage,CurrentLanguage)
