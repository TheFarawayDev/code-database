def calculate_score(judge_scores):
    score1 = judge_scores[0]
    score2 = judge_scores[1]
    score3 = judge_scores[2]
    total_score = score1 + score2 + score3
    return total_score

print(calculate_score((10, 10, 10)))
print(calculate_score((9, 9, 6)))