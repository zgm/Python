from multiprocessing import Pool, Process, Manager, Lock, Semaphore

class PoolValue:
    def __init__(self, x):
        self.key = x


def func(value, flag=False, list=None, lock=None):
    if flag:
        value.key *= value.key
    else:
        value.key *= 2
    print "test", value.key
    with lock:
        list.append(value)
    return value


if __name__ == '__main__':
    manager = Manager()
    list = manager.list()
    lock = Lock()
    sem = Semaphore(2)
    
    jobs = []
    for i in range(2,8):
        value = PoolValue(i)
        p = Process(target=func, args=(value,True,list,lock))
        p.start()
        jobs.append(p)
        #p.join()
    for job in jobs:
        job.join()
    print list
    for d in list:
        print d.key,
        #print dict[d].key

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
