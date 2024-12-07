basic_pay=float(input("enter the basic pay"))
hra=0.10*basic_pay
ta=0.05*basic_pay
total=basic_pay+hra+ta
print(f"basic_pay:{basic_pay}, hra:{hra},ta:{ta},total:{total}")
