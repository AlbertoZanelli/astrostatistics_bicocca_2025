path = '/Users/albertozanelli/Desktop/Astrostatistic - appunti/L11_bayesian.ipynb'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

old_block = """    "---\\n",
    "![image.png](attachment:image.png)\\n",
    "\\n",
    "---\\n","""

new_block = """    "***\\n",
    "![image.png](attachment:image.png)\\n",
    "\\n",
    "***\\n","""

if old_block in content:
    content = content.replace(old_block, new_block)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully replaced.")
else:
    print("Block not found!")
