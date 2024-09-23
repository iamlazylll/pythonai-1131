def get_grade():
    try:
        score = input("請輸入數字: ")
        # score = int(score)
        score = float(score)
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
    elif score == 114514:
        return "怎麼哪裡都有Homo阿(惱"
    
    else:
        return "輸入錯誤，請輸入 0 ~ 100 之間的成績"
def cal_mean():
    try:
        score_arr = []
        mean = 0
        ppl = int(input("請輸入數字數量: "))
        for i in range(0, ppl):
            score = input("輸入一數字: ")
            score_arr.append(score)
        for i in range(0, ppl):
            mean += int(score_arr[i])
        mean /= ppl
        return f"平均為 {mean}"
        # score = input("請輸入一些數字: ")
        # score = int(score)
        
    except ValueError:
        return "輸入錯誤，請輸入數字"
def eng_or_spa():
      try:
          whatlang = input("English or Spanish: ")
      except ValueError:
          return "輸入錯誤"
      if whatlang == "English":
          return "Hello my friend!"
      elif whatlang == "Spanish":
          return "Hola mi amiga/amigo!"
      else:
          return "こんにちわ"
def call_utils(codes):
    codes = int(codes)
    if codes == 1:
        return get_grade()
    elif codes == 2:
        return cal_mean()
    elif codes == 3:
        return eng_or_spa()
    else:
        return "錯誤，無此功能"
      
try:
    print("[1]: 成績等第")
    print("[2]: 計算平均值")
    print("[3]: English or Spanish?")
    utilties = input("請輸入你要呼叫的功能: ")
    # print("test")
    # utilties = int(utilties)
    response = call_utils(utilties)
    print(response)
    # response = get_grade(scores)
    # print(f"你的等第是 {response}。")
except ValueError:
    print("輸入錯誤，請輸入數字")
