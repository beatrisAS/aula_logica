import datetime
import calendar

dias_semana = [
    "segunda-feira", "terça-feira", "quarta-feira",
    "quinta-feira", "sexta-feira", "sábado", "domingo"
]

meses = [
    "janeiro", "fevereiro", "março", "abril", "maio", "junho",
    "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
]

hoje = datetime.date.today()
print(hoje)
print(hoje.strftime("%d/%m/%Y"))
print(f"São Paulo, {dias_semana[hoje.weekday()]}, {hoje.day} de {meses[hoje.month - 1]} de {hoje.year}")

print(f"2024 é bissexto: {calendar.isleap(2024)}")

ultimo_dia = calendar.monthrange(hoje.year, hoje.month)[1]
print(f"Hoje é o último dia do mês? {hoje.day == ultimo_dia}")