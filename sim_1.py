import numpy
from random import *
import matplotlib.pyplot as plt
import progressbar

# this is basic model of human population growth. It assumes an initial starting population distributed equally among genders within a certain
# initial age limit. It also assumes that people die once they hit a certain age immedialty and there is no death distribution. The probability of
# having children reduces with increasing number of children with the maximum limit set at 6, a hard stop.

time_period=300

pop=[]
pop_initial=4
init_age_limit=2
age_of_dying=50
start_child_birth_age=24
end_child_birth_age=45

# the way attributes are arranged are age, gender, number of children, dead

# defining intial population of 10 kids



while True:
    n_m=0
    n_f=0
    pop=[]
    for i in range(0,pop_initial):
        age=int(random()*init_age_limit)+1
        gender=random()
        if gender < .5:
            gender=0
            n_m=n_m+1
        else:
            gender=1
            n_f=n_f+1
        ch_num=0
        dead=0
        buf=[age,gender,ch_num,dead]
        pop.append(buf)
    if n_m==n_f:
        break

# evolution criteria are people have children after the age of 18 till 40, probability of having children drastically reduces after 2 and life expectancy is 80.
# time step is 1 year

# first_ch_prob=.7
# second_child_prob=.5
# third_child_prob=.1
# fourth_child_prob=.01
birthing_prob=[.7,.5,.1,.01,.0001,.0000001,.000000001]

# print (len(pop))
# for i in pop:
#     print (i[0])

alive_pop_vs_time=[]
tot_pop_vs_time=[]
number_of_child=[]

bar = progressbar.ProgressBar()

plt.ion()

for t in bar(range(time_period)):
    n_pop=0
    n_ch=0
    for i in pop:
        if i[3] == 1:
            continue
        i[0]=i[0]+1
        if i[0]>=start_child_birth_age and i[0]<=end_child_birth_age and i[2]<7:            # checking age for birthing and number of children assuming no one has more than 7
            #print (i[2])
            if random()<birthing_prob[i[2]]: #roll the dice
                i[2]=i[2]+1                  # add a human baby based on outcome
                age=1
                gender=random()
                if gender < .5:
                    gender=0
                else:
                    gender=1
                ch_num=0
                dead=0
                buf=[age,gender,ch_num,dead]
                pop.append(buf)
                partner=pop[int(random()*len(pop))] #selecting the mate
                if i[2] != partner[2] and partner[0]>=18 and partner[0]<=40:              # making sure the mate is of teh opposite sex
                    partner[2]=partner[2]+1                                                # increase the numerb of child of the mate by one

        if i[0]>age_of_dying:
            i[3]=1
        if i[3] == 0:
            n_pop=n_pop+1
        if i[0]<18:
            n_ch=n_ch+1

    alive_pop_vs_time.append(n_pop)
    tot_pop_vs_time.append(len(pop))
    number_of_child.append(n_ch)
    plt.plot(alive_pop_vs_time)
    plt.pause(0.05)
# plt.plot(tot_pop_vs_time)
# plt.plot(alive_pop_vs_time,'r')
