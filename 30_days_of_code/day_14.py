class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference=0
    # Add your code here
    def computeDifference(self):
        l=len(a)
        for i in range(0,l):
            for j in range(i+1,l):
                most=abs(a[i]-a[j])
                self.maximumDifference=max(most,self.maximumDifference)

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
