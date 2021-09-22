t=[10,5,11,6,7,10,6,8,11,9,7,10,13,15,20,17,7,6,17,9,6,11,21,8]
ora=["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23"]
max=t.index(max(t))
min=t.index(min(t))
#punctul a
print("Temperatura medie este ",sum(t)/24)
#punctul b
print("Maximul temperaturii este ",max(t))
print("Minimul temperaturii este ",min(t))
#punctul c
print("Ora cand sa inregistrat temperatura maxima este ",ora[max])
#punctul d
print("Ora cand sau inregistrat temperatura minima este ",ora[min])
