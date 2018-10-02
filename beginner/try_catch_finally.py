#basic exercise for try...catch...else...finally
def func(x):
    try:
        print ('print try')
        #return 'return try'
    except:

        print ('print except')
        return 'return except'
    else:
        print ('print else')
        return 'return else'
    finally:
        print ('print finally')
        return 'return finally'
print (func(12))

#print try->print finally->return finally               (all have return)
#print try->print else   ->print finally->None             (no return)
#print try->print finally->return try                   (try)
#print try->print else   ->print finally->return else      (else)
#print try->print else   ->print finally->return finally   (finally)
#print try->print finally->return try                   (try else)
#print try->print finally->return finally               (try finally)
#print try->print else->print finally->return finally   (else finally)

#1.return : finall>tyr>else
#2.if try has return then no else
#3.if no return then return None
#4.try finall always do
