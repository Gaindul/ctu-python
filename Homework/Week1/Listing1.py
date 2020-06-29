hourly_wage=int(input("Enter your wage per hour:"))
hours_worked=int(input("Enter hours worked:"))
tax_to_take_out=2000
grosspay=hourly_wage*hours_worked
netpay=grosspay-tax_to_take_out
strgrosspay=str(grosspay)
strnetpay=str(netpay)
strhours=str(hours_worked)
strwage=str(hourly_wage)
strtax=str(tax_to_take_out)
print("In a typical week,I get paid "+strwage+" per hour and work for "+strhours+" hours a week.I get paid "+strgrosspay+" a week, but get "+strtax)