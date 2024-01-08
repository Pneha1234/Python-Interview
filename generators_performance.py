import random
import time
time.clock = time.time

import memory_profiler as mem_profile

names = ['Wes', 'Katie', 'Ryan', 'Kieran', 'John', 'Tom', 'Matt', 'Craig', 'David', 'Chris', 'Brian', 'Chad', 'Jim']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']
print('Memory (Before): {}Mb'.format(mem_profile.memory_usage()))

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'naame': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result


def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'naame': random.choice(names),
            'major': random.choice(majors)
        }
        yield person


# t1 = time.clock()
# people = people_list(1000000)
# t2 = time.clock()

t1 = time.clock()
people = people_generator(1000000)
t2 = time.clock()



print('Memory (After) : {}Mb'.format(mem_profile.memory_usage()))
print('Took {} Seconds'.format(t2-t1))