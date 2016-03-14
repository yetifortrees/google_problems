####
#This program is a more optimized solver for the following problem for n = [2, 50]:
#
#           Imagine a group of n people. Each person can socialize with one other person of their
#           choosing. That person may or may not choose to socialize back with them, and may instead
#           socialize with someone else. This eventually results in groups of individuals who are connected
#           by a network of socialization. Now imagine someone outside this group wants to infect the largest group
#           of people with a virus. If they are always successful in infecting the largest group of socialized individuals,
#           what is the expected average number of people they will infect.
#
#This problem has 3 layers:
#   1. how can the people be socialized/grouped?
#       This problem is answered by finding the possible integer partitions
#       for the number of people overall.
#   2. how can the people be arranged in these groups?
#       This is answered through combinatorics by calculating the number
#       of ways to split n people into some set of partitions.
#   3. how many ways can the socialization edges be arranged in each partition?
#       This is answered through sequence A000435 on the OEIS. The exact reason is unknown to me,
#       but the number is not as easy to find as one might think because a socialization action is
#       akin to an edge in a digraph, but the disease can travel backwards along edges, as in an undirected
#       graph. Thus a graph must be constructed with directed edges with respect to possible configurations, and
#       then converted to an undirected graph.
#
#This program uses the three layers of calculations above to generate the average number of people infected. Above 50 this program
#will not work because it only stores the first 50 values of the third layer sequence. Additionally, the number of partitions grows exponentially,
#so runtime scales accordingly.
####
from fractions import Fraction
import math
s = {}
#the first 50 values of A000435
multipliers = [0,1,8,78,944,13800,237432,4708144,105822432,2660215680,73983185000,2255828154624,74841555118992,2684366717713408,103512489775594200,4270718991667353600,187728592242564421568,8759085548690928992256,432357188322752488126152,22510748754252398927872000,1232926106158164038752479600,70864880389206811919012069376,4264956622099218989964380900408,268233854186801904661404949413888,17596516621570611723107254285860000,1202034287378796801763265196064768000,85369694212882788734452615436623131432,6294445634443154805245648414750533484544,481164307787876713983817697855811244891472,38086159100543376291945674612050231296000000,3117962569860399657478478640723143576082043800,263711778692997479722657378560127779200642842624,23019602620026625886784119896351926037410391377792,2071846675499818842878197235287956993753027358752768,192094716812399052493595004779889746503480732173125000,18331598479550821498637618387125492501532509577674752000,1799128306486873097251634624641612544680165700565794891568,181455277812927984131628207045914510546689975831530576019456,18793558774469620804251752127287685035341811749012764504838392,1997481851773698127207374504024299885204574735495384268800000000,217725066338201044536232277151749132601822287693599525820471957600,24322993207498664811770063992025908744449994272086863441366798565376,2783252962715382903543081261008995076675007754537625408175546581970408,326040422290312358312341535486741187518808190457145240569672167271170048,39078734107607748249951890474620593724028205093939481724417008016906250000,4790020369221769566925830345222465070918938379231286729520950331389352345600,600135530341228889141074788642164985737852858110856472692456945542128324281432,76819732139864778254944970153522541437430179776648013928703825117887136209567744,10041823702864167812042682621441259276711025525338945412768700983639957485080366912,1339928530680358664749551425221017908902142581750156543927120170387232522240000000000]
def answer(n):
    #ignore trivial cases
    if n == 2:
        return "2/2"
    if n == 3:
        return "3/3"
    #This is the max number of configurations
    arrangements = int(math.pow(n-1, n))
    #Used for calculating the arrangements of nodes in partitions
    maximum = int(math.factorial(n))
    #initialize the top and bottom of the fraction that represents average people infected
    top = 0
    bottom = 0
    #find the partitions
    loop = partitions(n)
    #loop through all configurations of partitions
    for i in loop:
        #partition sizes must be all > 2 to be a valid partition scheme
        if i[0] > 1:
            here = maximum
            repeat = 0
            times = 1
            for j in i:
                #the math.factorial takes care of node configs in partitions, and the multipliers
                #account for the number of configs of edges in each partition
                here = int(here / math.factorial(j)) * multipliers[j - 1]
                #if there are partitions of the same size that effects
                #the possibilities and must be accounted for
                if j == repeat:
                    times += 1
                    here = int(here / times)
                else:
                    times = 1
                    repeat = j
            top += int(i[len(i) - 1] * here)
            bottom += here
            #print(str(top) + "/" + str(bottom))
            #arrangements -= here
    #top += int(arrangements * n)
    #print(float(top)/float(bottom))
    return str(Fraction(int(top), int(bottom)))
#the partitions of n-1
#credit to David Eppstein
def partitions(n):
    # base case of recursion: zero is the sum of the empty list
    if n == 0:
        yield []
        return
    # modify partitions of n-1 to form partitions of n
    for p in partitions(n-1):
        yield [1] + p
        if p and (len(p) < 2 or p[1] > p[0]):
            yield [p[0] + 1] + p[1:]
#a decorator function for the choose/combination function
def factWrap(*args):
    if args not in s:
        s[args] = math.factorial(*args)
    return s[args]
#a decorator function for the choose/combination function
def chooseWrap(*args):
    if args not in s:
        s[args] = choose(*args)
    return s[args]
#a function to calculate n choose k or n combination k
def choose(n, k):
    if k > n:
        return 0
    return int(math.factorial(n)/(math.factorial(k) * math.factorial(n - k)))
#testing
for i in range(2, 50):
    print(answer(i))