from pathlib import Path


from os import system
base = Path.home()
guia = Path(base,'hello','halo')

system('cls')

print(guia.glob('**'))

print(base)