ageindays = int(input())

years = int(ageindays/365)

ageindays = ageindays - years*365

months = int(ageindays/30)

ageindays = ageindays - months*30

days = ageindays

print(years,"ano(s)")
print(months,"mes(es)")
print(days, "dia(s)")