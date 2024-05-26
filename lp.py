import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize production", pulp.LpMaximize)

# Визначення змінних
limonade = pulp.LpVariable('limonade', lowBound=0, cat='Integer')  # Кількість лимонаду
juice = pulp.LpVariable('juice', lowBound=0,cat='Integer')  # Кількість фруктового соку"

# Функція цілі (Максимізація прибутку)
model += limonade + juice, "production"

# Додавання обмежень
model += 2 * limonade + 1 * juice <= 100  # Обмеження для ресурсів води
model += 1 * limonade <= 50  # Обмеження для ресурсів цукру
model += 1 * limonade <= 30  # Обмеження для ресурсів лимонного соку
model += 2 * juice <= 40  # Обмеження для ресурсів фруктового пюре

# Розв'язання моделі
model.solve()

# Вивід результатів
print("Max production of limonade:", limonade.varValue)
print("Max production of juice:", juice.varValue)
print("Status of model:",pulp.LpStatus[model.status])
