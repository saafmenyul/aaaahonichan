def check_winners(scores, student_score):
    # Сортируем по убыванию и берем топ-3
    top_three = sorted(scores, reverse=True)[:3]
    
    if student_score in top_three:
        return "Вы в тройке лучших!"
    return "Вы не в тройке лучших."


print(check_winners([20, 48, 52, 38, 36, 13, 7, 41, 34, 24, 5, 51, 9, 14, 28], 52))
