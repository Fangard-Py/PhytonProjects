immutable_var = 1, 2.0, "цифра", True
print(immutable_var)

# Тип данных (tuple) - неизменяемый(программа не сможет обращаться с его элементами)
# Но мы можем добавить в картеж(tuple) список, который будет изменяемым

immutable_var = (["меняюсь"], "не меняюсь")
immutable_var[0][0] = "изменился"
print(immutable_var)


mutable_list = ["Список", "Записка", "Табуретка"]
mutable_list[0] = "Косипс"
mutable_list[1] = "Аксипаз"
mutable_list[2] = "Актерубат"
print(mutable_list)
