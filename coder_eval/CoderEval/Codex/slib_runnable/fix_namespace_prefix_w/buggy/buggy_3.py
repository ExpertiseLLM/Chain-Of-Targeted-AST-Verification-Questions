def fix_namespace_prefix_w(content):
	content = re.sub(r'(?<=w:st=)\"', '-', content)
	content = re.sub(r'(?<=w:rsid=)\"', '-', content)
	content = re.sub(r'(?<=w:rsidR=)\"', '-', content)
	content = re.sub(r'(?<=w:rsidRDefault=)\"', '-', content)
	content = re.sub(r'(?<=w:rsidRPr=)\"', '-', content)
	content = re.sub(r'(?<=w:rsidRDefault=)\"', '-', content)
	content = re.sub(r'(?<=w:rsidDel=)\"', '-', content)
	content = re.sub(r'(?<=w:rsidP=)\"', '-', content)
	content = re.sub(r'(?<=w:rsidRDefault=)\"', '-', content)
	content = re
