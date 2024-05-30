import re
from os import listdir
from os.path import isfile, join

def convert_case(match_obj):
    return f"![]({match_obj.group(1).replace(' ', '_')})"

files = [f for f in listdir('.') if isfile(join('.', f)) and f.endswith('.md')]

for file in files:
    with open(file, 'r') as f:
        content = f.read()

    p = re.compile(r"!\[\[(.+\.png)]]")

    with open(f'nouveau {file}', 'w+') as f:
        f.write(p.sub(convert_case, content))
