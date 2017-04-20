#_='_=%r;print _%%_';print _%_


#meme='meme=%r;print meme%%meme';print meme%meme


#a = "b = chr(97) + chr(32) + chr(61) + chr(32) + chr(34); b += a; print b + chr(34); print a"
#b = chr(97) + chr(32) + chr(61) + chr(32) + chr(34); b += a; print b + chr(34); print a


s = r"print 's = r\"' + s + '\"' + '\nexec(s)'"
exec(s)

print open(__file__).read()


