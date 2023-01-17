# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = 'лоывапАБВолдпрпр ылрывр абв орлопрЫпр фывоорабв'

text = list(filter(lambda  el: 'абв' not in  el.lower(), text.split()))
print(' '.join(text))