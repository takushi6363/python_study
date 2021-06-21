japanese = ["りんご","本","猫","犬","卵",]
english = ["apple","book","cat","dog","egg"]

n = len(japanese)
rigth = 0
for i in range(n):
  a = input(japanese[i]+"英単語は？")
  if a==english[i]:
     print("正解です")
     rigth = rigth + 1
  else:
     print("違います")
     print("正しくは"+english[i])
  
print("終了です")
print("正解数は",rigth,"です。")
print("間違いは", n-rigth ,"です。")