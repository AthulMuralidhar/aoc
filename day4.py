"""
Part 1: 87681
Part 2: 136461

real	0m0.159s
user	0m0.067s
sys	0m0.021s

"""
import pendulum as p
from collections import Counter, defaultdict

data = sorted(
    open('r_input.txt').read().splitlines(),
    key=lambda x: p.parse(x[1:17])
)

guards = defaultdict(Counter)

for x in data:
    ts = int(x[15:17])
    if 'begins' in x:
        gid = int(x.split()[3][1:])
    if 'falls asleep' in x:
        sleep_ts = ts
    if 'wakes up' in x:
        for y in range(sleep_ts, ts):
            guards[gid][y] += 1

# max sum minutes x max minute
sleepy_af = max(guards, key=lambda k: sum(guards[k].values()))

print('Part 1: ' + str(max(guards[sleepy_af], key=lambda k: guards[sleepy_af][k]) * sleepy_af))

# max minute accross all gids
sleepy_af = max(guards, key=lambda x: max(guards[x].values()))
minute = max(guards[sleepy_af], key=lambda y: guards[sleepy_af][y])

print('Part 2: ' + str(sleepy_af * minute))
