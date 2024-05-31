grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
stud_l=sorted(students)
svr_0=(sum(grades[0])/len((grades[0])))
svr_1=(sum(grades[1])/len((grades[1])))
svr_2=(sum(grades[2])/len((grades[2])))
svr_3=(sum(grades[3])/len((grades[3])))
svr_4=(sum(grades[4])/len((grades[4])))
dnevnik = {}
dnevnik.update({stud_l[0]:svr_0,
                stud_l[1]:svr_1,
                stud_l[2]:svr_2,
                stud_l[3]:svr_3,
                stud_l[4]:svr_4})
print(dnevnik)
