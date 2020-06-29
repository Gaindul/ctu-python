hourly_wage=int(input("Enter your wage per hour:"))
hours_worked=int(input("Enter hours worked:"))
tax_to_take_out=2000
grosspay=hourly_wage∗hours_worked
netpay=grosspay−tax_to_take_out
print("In a typical week,I get paid" hourly_wage "per hour and work for" + hours_worked + "hoursaweek.Igetpaid"+grosspay,"aweek,but get"+tax_to_take_out)