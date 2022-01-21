
iterable: List[str] = ["alma", "körte", "dió",]
result: str = "," .join(iterable)
print(result)

text: str = "bonjour le monde"
textAsList: List = text.split()
print(textAsList)

text = "Katarzyna Skoworonska Dolata; Polland; 190; center"
textAsList = text.split(";")
print(textAsList)

