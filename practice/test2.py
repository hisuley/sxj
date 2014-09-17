#以正确的宽度在居中的“盒子”内打印一个句子

scentence = raw_input("scentence: ")

screen_width = 80
text_width = len(scentence)
box_width = text_width + 6
left_margin = (screen_width - box_width)//2

print
print ' '*left_margin + '+' + '-'*(box_width-2) + '+'
print ' '*left_margin = '|' + ' '*text_width	+ '|'
print ' '*left_margin = '|'		  scentence		+ '|'
print ' '*left_margin = '|' + ' '*text_width	+ '|'
print ' '*left_margin = '+' + ' '*(box_width-2)	+ '|'
print