import re
text = input()

title_content_expr = r'.*?<title>(?P<title>.*?)<\/title>.*?<body>(?P<content>.*?)<\/body>'
remove_tags_expr = r'<.*?>'
remove_line_expr = r'\\n'


for match in re.finditer(title_content_expr, text):
    title = match.group('title')
    content = match.group('content')

content = re.sub(remove_tags_expr, '', content)
content = re.sub(remove_line_expr, '', content)

print(f'Title: {title}')
print(f'Content: {content}')
