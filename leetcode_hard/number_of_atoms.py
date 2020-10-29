class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        atomDict = {}
        formLength = len(formula)
        stack = []
        
        for i in range(formLength):
            if formula[i].isalpha():
                if formula[i].isupper():
                    name, endindex = self.getName(i, formula)
                    number = self.getNumber(endindex, formula)
                    
                    stack.append([name, number])
            elif formula[i] == "(":
                stack.append("(")
            elif formula[i] == ")":
                number = self.getNumber(i + 1, formula)
                self.accumParen(number, stack)
        
        # probably can merge these two together
        self.putToDict(atomDict, stack)
        return self.arrangeToString(atomDict)
    
    def getName(self, i, formula):
        name = formula[i]
        j = i
        for j in range(i + 1, len(formula)):
            if formula[j].islower():
                name += formula[j]
            else:
                break
        return (name, j)
    
    def getNumber(self, i, formula):
        number = ""
        for j in range(i, len(formula)):
            if formula[j].isdigit():
                number += formula[j]
            else:
                break
        
        if number == "":
            return 1
        return int(number)
    
    def accumParen(self, number, stack):
        for i in range(len(stack) -1, -1, -1):
            if stack[i] == "(":
                stack.pop(i)
                return
            stack[i][1] *= number
    
    def putToDict(self, atomDict, stack):
        for item in stack:
            if item[0] in atomDict:
                atomDict[item[0]] += item[1]
            else:
                atomDict[item[0]] = item[1]
    
    def arrangeToString(self, atomDict):
        string = ""
        keyList = atomDict.keys()
        keyList.sort()
        for key in keyList:
            string += key
            if atomDict[key] != 1:
                string += str(atomDict[key])
        return string