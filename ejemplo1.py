#Represa Hidroituango

#ENTRADAS

nivel_agua = int(input('digite el nivel del agua: '))

#PROCESO

if (nivel_agua >= 0 and nivel_agua <= 250):
    print(f'el nivel del agua {nivel_agua}, muy bajo')
elif (nivel_agua > 250 and nivel_agua <= 400):
    print(f'el nivel del agua {nivel_agua}, medio alto')
else:
    print(f'el nivel del agua {nivel_agua}, alto peligro')
