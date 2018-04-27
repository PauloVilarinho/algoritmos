Value = int(input())

ValueAux = Value

hundrednote = int(Value/100)

Value = Value - (hundrednote*100)

fiftynote = int(Value/50)

Value = Value - (fiftynote*50)

twentynote = int(Value/20)

Value = Value - (twentynote*20)

tennote = int(Value/10)

Value = Value - (tennote*10)

fivenote = int(Value/5)

Value = Value - (fivenote*5)

twonote = int(Value/2)

Value = Value - (twonote*2)

onenote = int(Value/1)

print(ValueAux)
print(hundrednote, "nota(s) de R$ 100,00")
print(fiftynote, "nota(s) de R$ 50,00")
print(twentynote, "nota(s) de R$ 20,00")
print(tennote, "nota(s) de R$ 10,00")
print(fivenote, "nota(s) de R$ 5,00")
print(twonote, "nota(s) de R$ 2,00")
print(onenote, "nota(s) de R$ 1,00")
