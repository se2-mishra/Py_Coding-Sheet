txt='Python programming is easy.'
result=txt.startswith('programming is',7)
print(result)
result=txt.startswith('programmng is',7,18)
print(result)
result=txt.startswith('program',7,18)
print(result)
