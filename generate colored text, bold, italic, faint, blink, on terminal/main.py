
def ansi_color(n,s):
	code={"bold":1,"faint":2,"italic":3,"underline":4,"blink_slow":5,"blink_fast":6,"negative":7,"conceal":8,
        "strike_th":9,"black":30,"red":31,"green":32,"yellow":33,"blue":34,"magenda":35,"cyan":36,"white":37,
        "b_black":40,"b_red":41,"b_green":42,"b_yellow":43,"b_blue":44,"b_magenda":45,"b_cyan":46,"b_white":47,}
	try:
		num=str(code[n])
		value="\033["+num+"m"+s+"\033[0m"
		return value
	except:
		pass
def list_code():
	code={"bold":1,"faint":2,"italic":3,"underline":4,"blink_slow":5,"blink_fast":6,"negative":7,"conceal":8,
        "strike_th":9,"black":30,"red":31,"green":32,"yellow":33,"blue":34,"magenda":35,"cyan":36,"white":37,
        "b_black":40,"b_red":41,"b_green":42,"b_yellow":43,"b_blue":44,"b_magenda":45,"b_cyan":46,"b_white":47,}
	for i,j in code.items():
		print (str(j)+"\t"+i)

print (ansi_color('bold',"I love Python."))
print (ansi_color('faint',"I love Python."))
print (ansi_color('blink_slow',"I love Python."))
print (ansi_color('blink_fast',"I love Python."))
