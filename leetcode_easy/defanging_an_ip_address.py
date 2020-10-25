class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        
        # python makes string manipulation especially easy
        return address.replace(".", "[.]")
    
        # without replace, probably use .split() on the periods
        # since an IPv4, if index of the split result is odd (1, 3, etc)
        # put an [.] at the beginning. 
        # Would probably work if changed from IPv4 to IPv6 too