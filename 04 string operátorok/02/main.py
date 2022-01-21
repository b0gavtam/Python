from typing import*

text:str="bonjour le mondre"
textAsList:List[str] =text.split()

print(textAsList)

text2:str="hosszabb, több szavas; szöveg"
textAsList:List[str] =text2.split(";")

print(textAsList)