import random
import math
#batas
interval_x = [-1,2]
interval_y = [-1,1]
#kromosom
def kromosom(gen):
    tabkrom=[]
    for i in range(gen):
        tabkrom.append(random.randint(0,9))
    return tabkrom
#populasi
def populasi(pop,gen):
    tabpop=[]
    for i in range(pop):
        tabpop.append(kromosom(gen))
    return tabpop
#bagi array menjadi 2
def split(krom):
    return (krom[:len(krom)//2],krom[len(krom)//2:])
#decode kromosom
def dekode(gamet, interval):
    pembagi = 0
    kali = 0
#rumus integer
    for i in range(len(gamet)) :
        n = gamet[i]
        kali += (n * (10**-(i+1)))
        pembagi += (9 * (10**-(i+1)))
    result = interval[0] + (((interval[1]-interval[0]) / pembagi) * kali)  
    return result
#nilai fungsi
def fungsi (x,y):
    f = x**2 * math.sin(y**2)+(x+y)
    return f
#nilai fitness
def fit(f):
    return f
#hitung fitness
def hitungfitness(populasi):
    fitness_populasi=[]
    for i in range(len(populasi)):
        x,y = split(populasi[i])
        gamet_x = dekode(x,interval_x)
        gamet_y = dekode(y,interval_y)
        f = fungsi(gamet_x,gamet_y)
        fitness = fit(f)
        fitness_populasi.append(fitness)
    return fitness_populasi
#tournament selection
def select (populasi):
    calon = []
    fitness_calon = []
    for i in range(4):
        n = random.randint(0,len(populasi)-1)
        calon.append(populasi[n])
    fitness_calon = hitungfitness(calon)
    parent_1 = max(fitness_calon)
    idx_parent_1 = fitness_calon.index(parent_1)
    fitness_calon.remove(parent_1)
    parent_2 = max(fitness_calon)
    idx_parent_2 = fitness_calon.index(parent_2)
    return (calon[idx_parent_1],calon[idx_parent_2])
#rekombinasi
def cross(krom1,krom2,prob):
    child1 = []
    child2 = []
    #n adalah titik silang
    n = random.randint(1,len(krom1)-1)
    if random.random() <= prob:
        print("titik potong:",n)
        child1[:n]=krom1[:n]
        child1[n:]=krom2[n:]
        child2[:n]=krom2[:n]
        child2[n:]=krom1[n:]
    else:
        child1 = krom1
        child2 = krom2
    return (child1,child2)
#mutasi
def mutation(krom,prob):
    if random.random()<=prob:
        #posisi mutasi
        n = random.randint(0,len(krom)-1)
        print("titik mutasi:",n)
        #nilai mutasi
        m = random.randint(0,9)
        krom[n]=m
    return krom
#seleksi survivor
def elitism(populasi):
    new_pop=[]
    fitness_populasi = hitungfitness(populasi)
    best = max(fitness_populasi)
    idx_best = fitness_populasi.index(best)
    new_pop.append(populasi[idx_best])
    return new_pop
cross_prob = 0.8
mut_prob = 0.01
print("masukan panjang gen:")
gen = int(input())
print("masukan banyak populasi:")
pop = int(input())
tabpop = populasi(pop,gen)
print("masukan generasi yang diinginkan")
generasi = int(input())
for i in range(generasi):
    print("----- generasi ke-",i,"-----")
    print(tabpop)
    new_tab_pop = elitism(tabpop)
    while len(new_tab_pop)<pop:
        parent_1, parent_2 = select(tabpop)
        print("parent1--parent2")
        print(parent_1,parent_2)
        child_1, child_2 = cross(parent_1,parent_2,cross_prob)
        child_1 = mutation(child_1,mut_prob)
        child_2 = mutation(child_2,mut_prob)
        print("child1==child2")
        print(child_1,child_2)
        new_tab_pop.append(child_1)
        if len(new_tab_pop)<pop:
            new_tab_pop.append(child_2)
    tabpop = new_tab_pop
    fitness_tabpop = hitungfitness(tabpop)
#cari max fitness
maks = max(fitness_tabpop)
#cari index max fitness
idx_maks = fitness_tabpop.index(maks)
print("----- generasi ke-",generasi,"-----")
print(tabpop)
print("solusi",tabpop[idx_maks])
print("dengan nilai fitness",fitness_tabpop[idx_maks])
x, y = split(tabpop[idx_maks])
fx = dekode(x,interval_x)
fy = dekode(y,interval_y)
print("nilai x:",fx)
print("milai y:",fy)
print("nilai fungsi:",fungsi(fx,fy))