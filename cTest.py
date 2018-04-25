class AClass(object):
    aVar = 'testField'
    bVar = (range(3))


bObj, aObj = AClass(), AClass()
aObj.aVar = 'newField'
print(aObj.aVar, bObj.aVar)
