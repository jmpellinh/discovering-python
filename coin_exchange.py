coin_type = int(input())

if coin_type <= 0:
    print('No change')
    
dollars = coin_type // 100
coin_type %= 100
quarters = coin_type // 25
coin_type %= 25
dimes = coin_type // 10 
coin_type %= 10
nickels = coin_type // 5
coin_type %= 5
pennies = coin_type

if dollars > 1:
    print('%d Dollars' % dollars)
elif dollars == 1:
    print('%d Dollar' % dollars)
if quarters > 1:
    print('%d Quarters' % quarters)
elif quarters ==1:
    print('%d Quarter' % quarters)
if dimes >1:
    print('%d Dimes' % dimes)
elif dimes ==1:
    print('%d Dime' % dimes)
if nickels > 1:
    print('%d Nickels' % nickels)
elif nickels == 1:
    print('%d Nickel' % nickels)
if pennies >1:
    print('%d Pennies' % pennies)
elif pennies ==1:
    print('%d Penny' % pennies)