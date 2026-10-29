import datetime
import babel.dates

hoje = datetime.date.today()
data_extenso = babel.dates.format_date(hoje, format='long', locale='pt_BR')
print(data_extenso)