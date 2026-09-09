import theano
import theano.tensor as te

a = te.dscalar('a')
f = theano.function([a],a**2)
print(f(3))


# a = te.vector()
# out = a + a**10
# f = theano.function(a,out)
# print(f([0,2]))