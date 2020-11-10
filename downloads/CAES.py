
# coding: utf-8

# In[22]:


from CoolProp.CoolProp import PropsSI
# use the letters:
# ... T for (T)emperature 
# ... P for (P)ressure
# ... D for (D)ensity (use the density to calculate the specific volume)
# ... Q for vapor quality x


# In[7]:


fluid="water"
T=99+273.15 #K
p=1.03*10**5   #bar
D=PropsSI("D","P",p,"T",T,fluid)
print(D)


# In[16]:


fluid = "air"

p_Critical = PropsSI("Pcrit",fluid)
T_Critical = PropsSI("Tcrit",fluid)

# get the density at the critical point
rho_Critical = PropsSI("D", "P", p_Critical, "T", T_Critical, fluid) 
specVol_Critical = 1.0/rho_Critical


print("Critical pressure = ", p_Critical/1e5, " [bar]")
print("Critical temperature = ", T_Critical - 273.15, "[°C]")
print("Critical specific volume =",specVol_Critical, "[kg/m3]")


# In[29]:


fluid="R134a"
pin=1.03e5
Tin=225+273.15
Hin=PropsSI("H","P",pin,"T",Tin,fluid)
print("De Enthalphy is {0:1f} kJ/kg".format(Hin/1000))


# In[15]:


p0=1e5 #Pa
pmax=1.1e5 #Pa
Tin=23+273 #K
Tout= 500 #K
fluid='air'
def h(p,T):
    h=PropsSI("H","P",p,"T",T,fluid)
    return h

def work(p1,p2,T1,T2):
    return h(p2,T2)- h(p1,T1)
print(h(pmax,Tout))
print(h(p0,Tin))
print("The work is {} kJ/kg".format(work(p0,pmax**(1/2),Tin,Tout)))


# In[64]:


#Boundary conditions

#Ambiant air
p0 = 1.03e5 #Pa
T0 = 273+12 #K

#Miscellaneous
P = 0 #W
R = 8.3145 #J / mol K  
Mm = 28.97e-3 #kg/mol
cv= 718 #J/ kg K



#Compressor
eff_c   = 1 #[-]
p_ratio_c = 1.01 #[-]

#Turbine
eff_t   = 1 #[-]
p_ratio_t = 1.01 #[-]


#Functions

#Get temperature after (de)pressurising from original temp
def Tpres(T,p_ratio):
    return T*p_ratio**(R/Mm/(cv+R))

#Get enthalpy for known T,p
def hTp(p,T):
    return PropsSI("H","P",p,"T",T,"air")

#First approximation specific work using enthalpy
def W1(p_in,p_ratio,T_in):
    p_out = p_in*p_ratio       
    T_out = Tpres(T_in,p_ratio)
    h_in = hTp(p_in,T_in)
    h_out = hTp(p_in,T_out)
    return h_out-h_in

#Mass flow rate
#Maybe should not be defined as a function...
def mdot(Tmid):
    Work1 = W1(p0,p_ratio_c,T0)
    Work2 = W1(p0*p_ratio,p_ratio_c,Tmid)
    m=P*(Work1/eff_c+Work2/eff_c)**(-1)
    return m

#Second approximation specific work
def W2():
    #...
    return "null"


print(W1(p0,7,T0))

