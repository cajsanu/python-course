# Write your solution here
# Remember the import statement

from datetime import date

def list_years(dates: list):
    years = []
    for date in dates:
        year = date.year
        years.append(year)
    sortd = sorted(years)

  
    return sortd
        
    
    
    
    
# date1 = date(2019, 2, 3)
# date2 = date(2006, 10, 10)
# date3 = date(1993, 5, 9)

# years = list_years([date1, date2, date3])
# print(years)
