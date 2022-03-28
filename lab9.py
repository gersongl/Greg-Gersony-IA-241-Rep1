#lab9
#3.1
class my_stat:
    def cal_sigma(self,m,n):
        result = 0
        for i in range(n,m+1):
            result = result + i
        return result
    def cal_pi(self,m,n):
        result = 1
        for i in range(n,m+1):
            result = result * i
        return result
    def cal_factorial(self,m):
        if m == 0:
            return 1
        else:
            return (m * self.cal_factorial(m-1))
    def cal_permutation(self,m,n):
        return self.cal_factorial(m)/self.cal_factorial(m-n)
#3.2
my_cal = my_stat()
print(my_cal.cal_sigma(5,3))
print(my_cal.cal_pi(5,3))
print(my_cal.cal_factorial(5))
print(my_cal.cal_permutation(5,2))
