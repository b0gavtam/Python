from typing import *

text: str = "bonjour le monde"
index: int = text.find("on")
indexRight: int = text.rfind("on")

print(index)
print(indexRight)