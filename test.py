class aaa:
    def __init__(self):
        self.printf('aaaa')
    def printf(self,a,end='\n'):
        a=str(a)
        b=a.decode('utf-8')
        if end=='\n':
            print(b)
        else:
            print b+end,
            #print '\b',
            #print end,
if __name__ == '__main__':
    a=aaa()
    a.printf('bbbb',end='')
    a.printf('bbbb',end='')