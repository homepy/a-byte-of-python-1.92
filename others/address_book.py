import os, sys, pickle

def findByName(addrDict, name):
    if name in addrDict:
        print('{0} : {1}'.format(name, addrDict[name]))
    else:
        pirnt("The info of {0} does not exist!".format(name))

def saveOrUpdate(addrDict, name, addr):
    print('Save or update addrDict[{0}]'.format(name))
    addrDict[name] = addr

def delete(addrDict, name):
    print("Deleting something")
    del addrDict[name]

def showAll(addrDict):
    print('Name'.rjust(10), 'Address'.rjust(20))
    for name, addr in addrDict.items():
        print(name.rjust(10), addr.rjust(20))

def showUsage():
    '''Usage:
    -?			    show usages
    -s                      show all
    -c <name> <address>	    create or update object
    -u <name> <address>	    update object 
    -d <name>		    delete object
    -q <name>		    search object'''
    pass


addrBookFile = 'address-book.data'
addrDict = None
if not os.path.exists(addrBookFile):
    addrDict = {'Name' : 'Address'}
else:
    with open(addrBookFile, 'rb') as f:
        addrDict = pickle.load(f)

if len(sys.argv) > 1:
    if (sys.argv[1] == '-c') & (len(sys.argv) > 3):
        if sys.argv[2] in addrDict:
            print(sys.argv[2], "'s contact has exist. Please update it")
        else:
            saveOrUpdate(addrDict, name = sys.argv[2],  addr = sys.argv[3])
    elif (sys.argv[1] == '-u') & (len(sys.argv) > 3):
        saveOrUpdate(addrDict, name = sys.argv[2],  addr = sys.argv[3])
    elif (sys.argv[1] == '-d') & (len(sys.argv) > 2):
        if sys.argv[2] in addrDict:
            delete(addrDict, name = sys.argv[2])
        else:
            print(sys.argv[2], " 's contact does not exist! Stop delete!")
    elif (sys.argv[1] == '-q') & (len(sys.argv) > 2):
        findByName(addrDict, name = sys.argv[2])
    elif sys.argv[1] == '-s':
        showAll(addrDict)
    else:
        print(showUsage.__doc__)
else:
    print(showUsage.__doc__)
with open(addrBookFile, 'wb') as f:
    pickle.dump(addrDict, f)
print('end')
