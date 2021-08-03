#!/usr/bin/env python
# coding: utf-8

# In[88]:


#class for bank
class BankAccount():
    def __init__(self):
        self.__AccountNumber=""
        self.Name=""
        self.__Balance=0.0
        self.__Pincode=0
        
    def setAccountNumber(self,a):
        self.__AccountNumber=a
    def getAccountNumber(self):
        return self.__AccountNumber
    
    
    def setName(self,n):
        self.Name=n
    def getName(self):
        return self.Name
    
    
    def setBalance(self,b):
        self.__Balance=b
    def getBalance(self):
        return self.__Balance
    
    
    def setPincode(self,p):
        self.__Pincode=p
    def getPincode(self):
        return self.__Pincode
    
    
     #function for Display
    def Display(self,AccountNo,Pin):
        if (self.__AccountNumber==AccountNo and self.__Pincode==Pin):
            print("AccountNumber ",self.__AccountNumber)
            print("Name :",self.Name)
            print("Balance :",self.__Balance)
        else :
            print("wrong Pincode, try again")
  

 #function for deposit
    def Deposit(self,AccountNum,pincode,Amount):
        if (self.__AccountNumber==AccountNum and self.__Pincode==pincode):
            self.__Balance=self.__Balance+Amount
        else:
            print("wrong Pincode")
            
        
        
        
 #function for withdraw
    def Withdraw(self,AccountNumber,Pincode,WithdrawAmount):
        if (self.__AccountNumber==AccountNumber and self.__Pincode==Pincode):
            if(self.__Balance > WithdrawAmount):
                self.__Balance-=WithdrawAmount
                return self.Display(self.__AccountNumber,self.__Pincode)
        else:
            print("worng Pincode")
       


# In[114]:


B=BankAccount()
B.setAccountNumber("1730113950305")
B.setName("Haseeb")
B.setBalance(10500)
B.setPincode(1234)


# In[121]:


B.Display(B.getAccountNumber(),B.getPincode())


# In[122]:


B.Deposit("1730113950305",1234,10600)


# In[123]:


B.Display(B.getAccountNumber(),B.getPincode())


# In[124]:


B.Withdraw("1730113950305",1234,4555)


# In[ ]:





# In[ ]:




