from data_import import data_import_func

def salary_calculator():
    dataframe = data_import_func()
    dm_hours = 0
    cs_hours = 0
    data_array = dataframe.to_numpy()
    for row in data_array:
        if row[1] == 'DM':
            dm_hours += row[2]
            dm_hours -= row[3]
        else:
            cs_hours += row[2]
            cs_hours -= row[3]
    
    dm_salary = dm_hours * 13.21
    cs_salary = cs_hours * 12.21
    holiday_pay = (dm_hours/10) * 13.21 +(cs_hours/10) * 12.21
    salary = dm_salary + cs_salary + holiday_pay
    
    print(f'DM rate: {dm_hours} * £13.21 = £{round(dm_salary, 2)}')
    print(f'CSR rate: {cs_hours} * £12.21 = £{round(cs_salary, 2)}')
    print(f'Holiday pay: £{round(holiday_pay, 2)}')
    
    if salary > 1048:
        taxable_amount = salary - 1048
        NI_tax = (taxable_amount * 8) / 100
        print(f'NI tax= £{round(NI_tax, 2)}')
        regular_tax = (taxable_amount * 20) / 100
        print(f'Tax= £{round(regular_tax, 2)}')
        salary -= NI_tax
        salary -= regular_tax
    else:
        pass
    
    print(f'Total= £{round(salary, 2)}')
    
salary_calculator()