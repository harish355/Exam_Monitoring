import database
import cv2
f = open("Student/Login.txt", "r")
mail=f.readline()
number=f.readline()
print(number)
f.close()
announcement=database.read("a!B6")
chat=database.read("a!F"+str(number))
while 1:
	ann=database.read("a!B6")
	if ann==announcement:
		pass
	else:
		print(ann)
		announcement=ann
	ch=database.read("a!F"+number)
	if ch==chat:
		pass
	else:
		print(ch)
		chat=ch
	cv2.waitKey(2000)
