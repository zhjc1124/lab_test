import re
with open('shiti.txt', encoding='utf8') as f:
    txt = f.read()
txt = txt.replace('\n）', '）').replace('：A', '：\nA').replace('：\nA）', '：A）').replace('？A', '？\nA')
pat = re.compile(r'）.*?、')
txt = pat.subn('）\n', txt)
pat = re.compile('\n\\d*?、')
txt = pat.subn('\n', txt[0])[0]
with open('answers.txt', 'w', encoding='utf8') as f:
    f.write(txt)