class MergeSort :
  ' class which performs sort using merge sort'
  numbers = []
  def __init__(self,filename):
    self.input_handle = open(filename)


  def sort(self):
    for line in self.input_handle:
      for number in line.split():
        self.numbers.append(int(number))
    snumber = MergeSort.merge(self,self.numbers)
    print snumber

  def merge(self,numbers):
   if len(numbers) == 1:
    return numbers
   mid = int(len(numbers)/2)
   leftArray = numbers[0:mid]
   arrayB = numbers[mid:]
   res = MergeSort.merge(self,leftArray)
   res1 = MergeSort.merge(self,arrayB)
   result = []
   i,j=0,0
   while i<len(res) and j<len(res1):
     if res[i] > res1[j]:
        result.append(res[i])
        i += 1
     else :
        result.append(res1[j])
        j+= 1
   if  i == len(res):
        while  j < len(res1):
          result.append(res1[j])
          j += 1
   else :
        if j == len(res1) :
         while  i < len(res):
           result.append(res[i])
           i += 1
   return result


try:
    inp = MergeSort('/home/vijay/exercise/mergeinp')
    inp.sort()
except IOError as e:
    print 'Error while opening file ({})'.format(e)
