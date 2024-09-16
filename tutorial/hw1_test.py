def get_grade(score):
    if not isinstance(score, (int, float)):
        return "不是數字，不能處理"
    if 100 >= score >= 90:
        return 'A+'
    elif 90 > score >= 85:
        return 'A'
    elif 85 > score >= 80:
         return 'A-'
    elif 80 > score >= 75:
        return 'B+'
    elif 75 > score >= 70:
        return 'B'
    elif 70 > score >= 65:
        return 'B-'
    elif 65 > score >= 60:
        return 'C+'
    elif 60 > score >= 0:
        return 'F'
    else:
        return "輸入錯誤，請輸入 0 ~ 100 之間的成績"
try:
    scores = input("請輸入數字: ")
    scores = int(scores)
    response = get_grade(scores)
    print(f"你的等第是 {response}。")
except ValueError:
    print("輸入錯誤，請輸入數字")


