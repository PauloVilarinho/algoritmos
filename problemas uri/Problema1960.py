numero = int(input())

unidades = ["" , "I", "II", "III" , "IV", "V" , "VI" , "VII" , "VIII" , "IX" ]
dezenas = ["" , "X", "XX", "XXX" , "XL", "L" , "LX" , "LXX" , "LXXX" , "XC" ]
centenas = ["" , "C", "CC", "CCC" , "CD", "D" , "DC" , "DCC" , "DCCC" , "CM" ]

centenasvalor = numero//100
numero = numero - centenasvalor*100
dezenasvalor = numero//10
numero = numero - dezenasvalor*10
unidadesvalor = numero

print("%s%s%s" %(centenas[centenasvalor],dezenas[dezenasvalor],unidades[unidadesvalor]))