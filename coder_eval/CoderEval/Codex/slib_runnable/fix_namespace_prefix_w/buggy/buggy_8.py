def fix_namespace_prefix_w(content):
	content=content.replace(u'w:st="',u'w-st="')
	content=content.replace(u'w:val="',u'w-val="')
	content=content.replace(u'w:rsidRDefault="',u'w-rsidRDefault="')
	content=content.replace(u'w:rsidR="',u'w-rsidR="')
	content=content.replace(u'w:rsidRPr="',u'w-rsidRPr="')
	content=content.replace(u'w:rsidDel="',u'w-rsidDel="')
	content=content.replace(u'w:rsidP="',u'w-rsidP="')
	content=content.replace(u'w:rsidRFonts="',u'w-rsidRFonts="')
	content=content.replace(u'w:rsidSect="',u'w-rsidSect="')
	content=content.replace(u'w:rsidTr="',u'w-rs
