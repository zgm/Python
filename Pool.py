from multiprocessing import Pool
from multiprocessing import Process

class PoolValue:
    def __init__(self, x):
        self.key = x

result = []

def func(value, flag=False):
    if flag:
        value.key *= value.key
    else:
        value.key *= 2
    result.append(value)
    print "test", value.key, len(result)
    return value


if __name__ == '__main__':
    for i in range(3):
        value = PoolValue(i)
        p = Process(target=func, args=(value,True))
        p.start()
        p.join()
        print "done"
    for r in result:
        print r.key

'''
    pool = Pool(4)
    result = []
    for i in range(3):
        value = PoolValue(i)
        result.append( pool.apply_async(func,[value]) )
        r = pool.apply_async(func,[value])
        print r.get().key
        print result[-1].get().key
    pool.close()
    pool.join()

    for job in result:
        p = job.get()
        print p.key, job.get().key
'''
