def check_winners(scores, student_score):
    scores.sort(reverse=True)
    if scores[0] == student_score or scores[1] == student_score or scores[2] == student_score:
        return "Вы в тройке победителей!"
    else:
        return "Вы не попали в тройку победителей."
print(check_winners([20, 48, 52, 38, 36, 13, 7, 41, 34, 24, 5, 51, 9, 14, 28], 52))