# importejam urllib2 moduli, kas lauj dabut majas lapu souce kodu (shis modulis ir OSMC raspberijaa)
# kaa ari importejam regex moduli, kas lauj veikt regular expressions.
import urllib2
import re

#this is an Atom test

#1. Atver URL un saglaba response content kaa variable code.
request = urllib2.Request("http://embed.ls.lv/ltv1g/index.php", headers={"Referer" : "http://ltv.lsm.lv/lv/tieshraide/ltv1/live.360/"}) #sheit nodefinee request URL un obligati ari headeri. Ja nebus shis request headeris, tad lapa atgriezis 403 forbidden.
html = urllib2.urlopen(request) #shis saglabaa response html kaa objektu
code = html.read() #shis atver obejktu kaa string

# 2. Atrod source code dalju, kas atrodas starp vardem iOS un Android. Tur ari atrodas velamais URL.
# Taa kaa regex output ir liste [], tad brutali to konvertejam uz parastu string.
ios_list = re.findall('iOS(.*?)Android', code, re.DOTALL)
ios_string = str(ios_list)

# 3. Taja string dalaa atrodas URL, kas saakas ar velamo sintaksi.
url_list = re.findall('http://carrier.ls.lv/ltv1g/smil:ltv1g.smil/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', ios_string)

# 4. Taa kaa regex output ir liste, tad izejam cauri tas vienigajam itemam un saglabajam ka variable url
for item in url_list:
  stream_url = item

# 5. Izprintejam URL - tas ir LTV1 striima URL ar visu token. Shis print nav redzams ieksh kodi log.
# print stream_url

# 6. Atskanojam stream URL tiklidz addons tiek atverts.
xbmc.Player().play(stream_url)

# this is a test
