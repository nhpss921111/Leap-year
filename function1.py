# -------------題目---------------
"""
寫一個function來判斷是不是閏年(二月會多一天的年)
  依照 Wikipedia 的定義
   1.公元年分除以4不可整除，為平年
   2.公元年分除以4可整除但除以100不可整除，為潤年
   3.公元年分除以100可整除但除以400不可整除，為平年
   4.公元年分除以400可整除但除以3200不可整除，為潤年
  同學可以依照這個定義直接翻譯成程式碼。
  function 應該要有一個參數值讓使用者投入(傳遞進去)年分
  function 的回傳直(return)應該是布林值，如果是閏年就return True，不就是return False。
  請把function 取名為 is_sleep ，這樣才可以執行測試。
  (P.S. is_sleep就是"是不是閏年"的意思，所以function要取的名副其實)
  提示:要用到 % 這個符號 "來求餘數"
 """

 # ------------------------------

def is_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

y = input('請輸入年份: ')
y = int(y)
print(is_leap(y))

