class Employee:
    def __init__(self,emp_name, desig, salary, dictionary, overtime_status,bonus):
        self.employee_name=emp_name
        self.designation=desig
        self.salary=salary
        self.dictionary=dictionary
        self.overtime_status=overtime_status
        self.bonus=bonus
        

class Organization:
    def __init__(self,l,overtime_threshold,rph):
        self.employee_list=l
        self.threshold_value=overtime_threshold
        self.rph=rph
    def overtime_staus_update(self):
        for i in self.employee_list:
            if sum(i.dictionary.values())>self.threshold_value:
                i.overtime_status=True
                i.bonus=sum(i.dictionary.values())*self.rph
    
        
l=[]
n=int(input())
for i in range(n):
    emp_name=input()
    desig=input()
    salary=int(input())
    dictionary={}
    dn=int(input())
    for i in range(dn):
        k=input()
        v=int(input())
        dictionary[k]=v
    emp_obj=Employee (emp_name, desig, salary, dictionary, overtime_status=False,bonus=0)
    l.append(emp_obj)
overtime_threshold=int(input())
rph=int(input())
org_obj=Organization(l, overtime_threshold,rph)
org_obj.overtime_staus_update()
cost_to_company=0
for i in l:
    print(i.employee_name,i.overtime_status)
    cost_to_company+=i.bonus
print(cost_to_company)
