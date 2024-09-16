def get_grade():
    try:
        score = input("請輸入數字: ")
        score = int(score)
    except ValueError:
        return "輸入錯誤，請輸入數字"
      
      # response = get_grade(scores)
    # print(f"你的等第是 {response}。")
    if not isinstance(score, (int, float)):
        return "不是數字，不能處理"
    if 100 >= score >= 90:
        return '你的等第是 A+'
    elif 90 > score >= 85:
        return '你的等第是 A'
    elif 85 > score >= 80:
         return '你的等第是 A-'
    elif 80 > score >= 75:
        return '你的等第是 B+'
    elif 75 > score >= 70:
        return '你的等第是 B'
    elif 70 > score >= 65:
        return '你的等第是 B-'
    elif 65 > score >= 60:
        return '你的等第是 C+'
    elif 60 > score >= 0:
        return '你的等第是 F'
    
    else:
        return "輸入錯誤，請輸入 0 ~ 100 之間的成績"
def call_utils(codes):
    if codes == 1:
        return get_grade()
    else:
        return "無此功能"
      
try:
    utilties = input("請輸入你要呼叫的功能: ")
    utilties = int(utilties)
    response = call_utils(utilties)
    print(response)
    # response = get_grade(scores)
    # print(f"你的等第是 {response}。")
except ValueError:
    print("輸入錯誤，請輸入數字")
