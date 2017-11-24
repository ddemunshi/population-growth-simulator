import numpy as np
from random import *
import matplotlib.pyplot as plt
import progressbar

# this is basic model of human population growth. It assumes an initial starting population distributed equally among genders within a certain
# initial age limit. Here the death probability is assumed along a distribution with the parameters changing with time as well as for birth


def prob_to_die(age,mu,sig):
    prob_die=(1/(np.sqrt(2*np.pi*sig*sig)))*(np.exp(-(age-mu)**2/(2*sig*2)))
    print ("death",prob_die)
    return prob_die

def life_expentency(civ_time):

    le_mu=20+.01*civ_time
    le_sig=max(60-.1*civ_time,20)
    #print (le_mu,le_sig)
    le_param=(le_mu,le_sig)
    return le_param

def prob_to_procreate(age,mu_age,sig_age,n_child,mu_nch,sig_nch):
    prob_birth_age=(1/(np.sqrt(2*np.pi*sig_age*sig_age)))*(np.exp(-(age-mu_age)**2/(2*sig_age*2)))
    prob_birth_child=(1/(np.sqrt(2*np.pi*sig_nch*sig_nch)))*(np.exp(-(n_child-mu_nch)**2/(2*sig_nch*2)))
    total_proc_prob=prob_birth_age*prob_birth_child
    return total_proc_prob

def procreate_age_param(civ_time):
    pro_mu=20+.01*civ_time
    pro_sig=max(40-.1*civ_time,10)
    #print (le_mu,le_sig)
    pro_param=(pro_mu,pro_sig)
    return pro_param

def procreate_child_param(civ_time):
    pro_mu=2
    pro_sig=max(3-.001*civ_time,1)
    #print (le_mu,le_sig)
    pro_param=(pro_mu,pro_sig)
    return pro_param

time_period=10000

pop=[]
pop_initial=4
init_age_limit=2
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

for t in range(time_period):
    le_param=life_expentency(t)
    proc_param_child=procreate_child_param(t)
    proc_param_age=procreate_age_param(t)
    n_pop=0
    n_ch=0
    for i in pop:
        if i[3] == 1:
            continue
        i[0]=i[0]+1
        if i[0]>=18:            # checking age for birthing and number of children assuming no one has more than 7
            #print (i[2])
            prob_to_give_birth=prob_to_procreate(i[0],proc_param_age[0],proc_param_age[1],i[2],proc_param_child[0],proc_param_child[1])
            print (prob_to_give_birth)
            if random() < prob_to_give_birth: #roll the dice
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

        if random() < prob_to_die(i[0],le_param[0],le_param[1]):
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
