hourly_wage = float ( input ( " Enter your wage per hour : " ) )
hours_worked = int ( input ( " Enter hours worked : " ) )
tax_to_take_out = 2000
gross_pay = hourly_wage * hours_worked
net_pay = gross_pay - tax_to_take_out
print ( " In a typical week , for my type of work as a  I get paid " , hourly_wage , " per hour and work for " , hours_worked , " hours a week . I get paid " , gross_pay , " a week , but get " , tax_to_take_out , " taken out . So I get left with " , net_pay )
