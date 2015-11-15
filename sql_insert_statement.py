
import csv
import pyodbc

f = open('C:\\Users\\Giuseppe\\Documents\\Bank_account_stats\\TXT151108131747.TAB', 'r')
data = csv.reader(f, delimiter='\t')
print(data)
insert = """
    INSERT INTO Bank_account.dbo.staging_abn (
          Account_number
        , Currency
        , [Date]
        , Balance_before
        , Balance_after
        , Execution_date
        , Transaction_amount
        , [Description]
	)VALUES
	"""

value = "( {Account_number}, {Currency}, {Date}, {Balance_before}, {Balance_after}, {Execution_date}, {Transaction_amount}, {Description} )"

print(value)


values = []
for row in data:
    values.append(
        value.format(
            Account_number=row[0],
            Currency="'" + row[1]+ "'",
            Date="'" + row[2] + "'" ,
            Balance_before=row[3].replace(',','.'),
            Balance_after=row[4].replace(',','.'),
            Execution_date="'" + row[5]+ "'" ,
            Transaction_amount=row[6].replace(',','.'),
            Description="'" + row[7].strip().replace("'","''") + "'"
        )
    )

print(insert + ','.join(values))

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=PEPPEPC\SQLEXPRESS;DATABASE=Bank_account;Trusted_Connection=yes;')
cursor = cnxn.cursor()
cnxn.execute(insert + ','.join(values))
cnxn.commit()
