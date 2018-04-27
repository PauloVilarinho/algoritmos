Value = float(input())

hundrednote=fiftynote=twentynote=tennote=fivenote=twonote=onecoin=halfcoin=quartercoin=dimecoin=nickelcoin=pennycoin=0

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

onecoin = int(Value/1)

Value = Value - (onecoin*1)

halfcoin = int(Value/0.5)

Value = Value - (halfcoin*0.5)

quartercoin = int(Value/0.25)

Value = Value - (quartercoin*0.25)

dimecoin = int(Value/0.10)

Value = Value - (dimecoin*0.10)

nickelcoin = int(Value/0.05)

Value = Value - (nickelcoin*0.05)

pennycoin = round(Value/0.01)

print("NOTAS:")
print("%d nota(s) de R$ 100.00" %hundrednote)
print("%d nota(s) de R$ 50.00" %fiftynote) 
print("%d nota(s) de R$ 20.00" %twentynote)
print("%d nota(s) de R$ 10.00" %tennote)
print("%d nota(s) de R$ 5.00" %fivenote)
print("%d nota(s) de R$ 2.00" %twonote)
print("MOEDAS:")
print("%d moeda(s) de R$ 1.00" %onecoin)
print("%d moeda(s) de R$ 0.50" %halfcoin)
print("%d moeda(s) de R$ 0.25" %quartercoin)
print("%d moeda(s) de R$ 0.10" %dimecoin)
print("%d moeda(s) de R$ 0.05" %nickelcoin)
print("%d moeda(s) de R$ 0.01" %pennycoin)
