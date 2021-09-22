v=list(eval(input("Introduceti venitul zilnic pe parcursul a unei saptamani: ")))
zi=["Luni","Marti","Miercuri","Joi","Vineri","Sambata","Duminica"]
max=v.index(max(v))
min=v.index(min(v))
#punctul a
print("Venitul saptamanal este ",sum(v))
#punctul b
print("Media venitului zilnic este ",sum(v)/7)
#punctul c
print("Ziua cu cel mai mare venit este ",zi[max])
#punctul d
print("Ziua cu cel mai mic venit este ",zi[min])