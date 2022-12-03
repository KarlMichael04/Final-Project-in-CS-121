class hotelbill:

    def __init__(self,rt='',s=0,p=0,r=0,t=0,a=1800,name='',address='',cindate='',coutdate='',rno=101):

        print ("\t****************************************")
        print ("\t*                                      *")
        print ("\t*    Welcome to LA BATSTATE HOTEL      *")
        print ("\t*                                      *")
        print ("\t****************************************")

        self.rt=rt

        self.r=r

        self.t=t

        self.p=p

        self.s=s
        self.a=a
        self.name=name
        self.address=address
        self.cindate=cindate
        self.coutdate=coutdate
        self.rno=rno
    def inputdata(self):
        self.name=input("\nEnter your name:")
        self.address=input("\nEnter your address:")
        self.cindate=input("\nEnter your check in date:")
        self.coutdate=input("\nEnter your checkout date:")
        print("Your room no.:",self.rno,"\n")
