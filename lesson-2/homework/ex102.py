txt = 'LMaasleitbtui'
i = 0
car1 = "".join(txt[i] for i in range(len(txt)) if i % 2 == 0)
car2 = "".join(txt[i] for i in range(len(txt)) if i % 2 == 1)
print(car1," and ", car2)
