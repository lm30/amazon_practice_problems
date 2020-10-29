class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s = s.strip()
        signCount = 0
        # don't need to lower case b/c according to test, E is not the same as e
        if s.count(".") > 1 or s.count("e") > 1 or s.count("+") > 2 or s.count("-") > 2 or s.count("+") + s.count("-") > 2:
            return False
        
        decimalSeen = None
        signSeen = None
        eSeen = None
        numSeen = None
        
        totalLength = len(s)
        for i in range(totalLength):
            if s[i].isalnum():
                if s[i].isdigit():
                    numSeen = i
                elif s[i] == "e":
                    eSeen = i
                else:
                    return False
            elif s[i] == "-" or s[i] == "+":
                signSeen = i
            elif s[i] == ".":
                decimalSeen = i
            
            if (decimalSeen and eSeen) and decimalSeen > eSeen:
                return False
            if eSeen != None: 
                if eSeen == 0 or eSeen == totalLength - 1 or numSeen == None:
                    return False
            if signSeen != None and (signSeen - 1 == numSeen or signSeen - 1 == decimalSeen):
                return False
            if s[i].isspace():
                if numSeen != None or eSeen != None or signSeen != None or decimalSeen != None:
                    return False
        
        if numSeen == None:
            return False
        if decimalSeen != None and numSeen == None:
            return False
        if signSeen != None:
            if numSeen == None:
                return False
            elif eSeen == None and signSeen != 0:
                return False
            elif eSeen != None and signSeen > eSeen and signSeen > numSeen:
                return False
    
        return True