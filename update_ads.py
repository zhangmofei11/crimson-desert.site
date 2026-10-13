import os

ad_head = '''<script async="async" data-cfasync="false" src="https://bauval.org/21/2ce7c1bdd4928115c06a7d9b7af9c11c"></script>
<script data-cfasync="false" src="https://bauval.org/14/a79596e9a159638cbd2aa6adacc6bc16"></script>
<script>
  atOptions = {
    'key' : '7861b7d51bf6ce6f9b97395619af77e4',
    'format' : 'iframe',
    'height' : 250,
    'width' : 300,
    'params' : {}
  };
</script>
<script src="https://bauval.org/22/7861b7d51bf6ce6f9b97395619af77e4"></script>'''

ad_body = '''<div style="display: flex; justify-content: center; margin: 20px 0;">
    <div id="container-2ce7c1bdd4928115c06a7d9b7af9c11c"></div>
</div>'''

files = ['index.html', 'walkthrough.html', 'bosses.html', 'combat.html', 'weapons.html', 'mounts.html', 'beginner.html']

for f in files:
    if not os.path.exists(f):
        print(f'Skipping: {f}')
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()

    if '7861b7d51bf6ce6f9b97395619af77e4' not in content:
        content = content.replace('</head>', ad_head + '\n</head>')
        print(f'Added head scripts: {f}')

    if 'container-2ce7c1bdd4928115c06a7d9b7af9c11c' not in content:
        content = content.replace('<footer', ad_body + '\n\n<footer')
        print(f'Added container div: {f}')

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f'Updated: {f}')
