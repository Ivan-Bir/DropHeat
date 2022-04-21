from cmath import pi
from math import cos, sin, floor, sqrt



fuel = "Hydogen"
oxidizer = "Oxigen"
edge_mateial = "BrH08"
nozzle_material = "12H21N5T"

pressure_chamber_Pa = 14700000
# pressure_slice = 39500
Km_core = 3.062
Km_wall = 2.278 #
alpha_core = 0.94
alpha_wall = 0.287 #
mass_flow_rate = 526.0
mass_flow_rate_ox = 626.922 #
mass_flow_rate_fuel = 126
temperature_in_chamber = 3516
temperature_wall = 2002
temperature_admissible_coolant = 550 #
temperature_admissible_gas_wall = 800 #
temperature_admissible_coolant_wall = 600 #
temperature_conditional = (temperature_admissible_gas_wall + temperature_admissible_coolant_wall) / 2
loses_admissible = 0.15
k = 1.29
heat_capacity_wall = 2308
heat_capacity_conditional_700K = 1766
gas_constant_wall = 520
viscosity_wall = 0.0000598

# name_section = "Сritical section"
# x_coord = 1.652 #meter
# diametr = 0.49 #meter
# diametr_relative = 1.000
# area = 0.189 #m^2
# area_relative = 1.000
# delta_x_coord = 0.046
# delta_x_s_coord = 0.053
# delta_area = 0.087

def get_lambda(F:float, F_critical:float, sverh_zvuk:bool):
    gdf_q = F_critical/F
    lamb = 1

    find_q = pow(1 - pow(lamb,2)*(k-1)/(k+1), 1/(k-1))*pow((k+1)/2, 1/(k-1)) * lamb

    while((abs(find_q - gdf_q))/(max(find_q, gdf_q)) > 0.08):
        if(sverh_zvuk):
            lamb += 0.01
        else:
            lamb -= 0.01
        find_q = pow(1 - pow(lamb,2)*(k-1)/(k+1), 1/(k-1))*pow((k+1)/2, 1/(k-1)) * lamb
        
    while((abs(find_q - gdf_q))/(max(find_q, gdf_q)) > 0.01):
        if(sverh_zvuk):
            lamb += 0.001
        else:
            lamb -= 0.001
        find_q = pow(1 - pow(lamb,2)*(k-1)/(k+1), 1/(k-1))*pow((k+1)/2, 1/(k-1)) * lamb

    return lamb

print(get_lambda(1.3, 0.273, False)) 
def make_geometry():

    x_coord = [0, 100, 512.4, 589, 629.6, 666.7, 706.6, 724.6, 741.2, 766.4, 802.2, 817.7, 825.5, 833.1, 839.6, 857.9, 
                945.5, 977, 1007.1, 1108, 1210.6, 1303.4, 1389.6, 1494.5, 1621.4, 1710.7, 1829.8, 2002.4, 2191.6, 2463.5]
    NUM_SECTIONS = len(x_coord);
    NUM_SEGMENTS = NUM_SECTIONS - 1;
    for i in range(NUM_SECTIONS):
        x_coord[i] *= 0.001;
    
    # d_critical = 0.272861;
    d_sections = [511, 511, 511, 487.5, 454.7, 412.8, 366.8, 346, 326.8, 299, 276.7, 273.3, 272.861, 282.7, 291.1, 314.5,
                  420.5, 454.6, 485.2, 585.1, 681.1, 759.3, 826.2, 902.5, 986.9, 1041.8, 1109.8, 1197.6, 1283.5, 1388.67]
    for i in range(NUM_SECTIONS):
        d_sections[i] *= 0.001
    d_critical = min(d_sections)
    
    d_relative = [0]*NUM_SECTIONS
    area_sections = [0]*NUM_SECTIONS
    area_relative = [0]*NUM_SECTIONS
    area_critical = pi * d_critical*d_critical / 4
    for i in range(NUM_SECTIONS):
        d_relative[i] = d_sections[i] / d_critical
        area_sections[i] = pi * d_sections[i] * d_sections[i] / 4
        area_relative[i] = area_sections[i] / area_critical
    
    delta_x_coord = [0]*NUM_SEGMENTS
    delta_area = [0]*NUM_SEGMENTS
    for i in range(NUM_SEGMENTS):
        delta_x_coord[i] = x_coord[i+1] - x_coord[i]
        delta_area[i] = pi * (d_sections[i+1] + d_sections[i]) * delta_x_coord[i] / 2
        
    return x_coord, d_sections, d_relative, area_sections, area_relative, delta_x_coord, delta_area


geometry = make_geometry(); # присвоить переменным
print(geometry.__sizeof__())
for i in range(7):
    print(geometry[i])
    


sigma_wall = 0.001
sigma_p = 0.001
sigma_wall_outer = 0.004
heigh_wall = 0.015
betta_p = 0 #град
t_N_min = 0.0025
t_N_max = 0.0065

def make_ribbing(a:list):
    NUM_SECTIONS = len(a)
    d_05_h = [0]*NUM_SECTIONS;
    for i in range(NUM_SECTIONS):
        d_05_h[i] = a[i] * (1 + (2*sigma_wall + heigh_wall) / a[i])
    
    number_rib_cr = pi * min(d_05_h) * cos(betta_p*pi/180) / t_N_min
    # print(min(d_05_h))
    print(number_rib_cr)
    number_rib_cr = floor(number_rib_cr)
    while number_rib_cr % 4 != 0:
        number_rib_cr -= 1

    t_N_crit = pi * min(d_05_h) * cos(betta_p) / number_rib_cr

    d_k = [0]*5
    k = [1, 2, 4, 8, 16]
    for i in range(5):
        d_k[i] = t_N_max * k[i] * number_rib_cr / (pi * cos(betta_p*pi/180)) -  (2 * sigma_wall + heigh_wall)
        
    number_rib = [0] * NUM_SECTIONS
    multiplier = 1
    for i in range(NUM_SECTIONS):
        if d_05_h[i] < d_k[2]:
            multiplier = k[2]
        if d_05_h[i] < d_k[1]:
            multiplier = k[1]
        if d_05_h[i] < d_k[0]:
            multiplier = k[0]
        number_rib[i] = number_rib_cr * multiplier
    # print(number_rib)
    
    t = [0]*NUM_SECTIONS
    t_N = [0]*NUM_SECTIONS
    f = [0]*NUM_SECTIONS
    d_gas = [0]*NUM_SECTIONS
    for i in range(NUM_SECTIONS):
        t[i] = pi * d_05_h[i] / number_rib[i]
        t_N[i] = t[i] * cos(betta_p*pi/180)
        f[i] = t_N[i] * heigh_wall * (1 - sigma_p / t_N[i]) * number_rib[i]
        d_gas[i] = 2 * heigh_wall * (t_N[i] - sigma_p) / (t_N[i] - sigma_p + heigh_wall)
    
    return t, t_N, f, d_gas

ribbing = make_ribbing(geometry[1])

# for i in range(4):
#     print(ribbing[i])


def calc_convective(d:list, d_critical:float):
    NUM_SECTIONS = len(d)
    A = 0.01352
    epsilon = 1
    Prandtl = 0.75
    relate_temperature = 0.35
    
    heat_capacity_mid = (heat_capacity_wall + heat_capacity_conditional_700K) / 2
    alpha = 1.813 * pow((2 / (k + 1)), 0.85/(k - 1)) * pow((2 * k / (k + 1)), 0.425)
    ####
    lamb = [0.19, 0.19, 0.19, 0.196, 0.227, 0.279, 0.362, 0.415, 0.477, 0.612, 0.838, 0.943, 1.0, 1.259, 1.354, 
              1.499, 1.93, 2.01, 2.071, 2.227, 2.337, 2.408, 2.46, 2.512, 2.561, 2.59, 2.622, 2.659, 2.691, 2.725]
    ####
    betta_at_lamb = [0] * NUM_SECTIONS
    for i in range(NUM_SECTIONS):
        betta_at_lamb[i] = lamb[i] * sqrt((k - 1) / (k + 1))#   
    betta_at_lamb_crit = sqrt((k - 1) / (k + 1))
    
    zetta = pow(1.769 * (1 - betta_at_lamb_crit + pow(betta_at_lamb_crit,2) * (1 - 0.086*(1 - pow(betta_at_lamb_crit,2)) / (1 - relate_temperature - 0.1 * pow(betta_at_lamb_crit,2))) ) / (1 - relate_temperature - 0.1 * pow(betta_at_lamb_crit,2)) , 0.54)

    alpha_strih = 1.813*pow(2/(k+1), 0.85/(k - 1)) * pow(2*k/(k+1), 0.425)
    B = 0.4842 * alpha_strih * A * pow(zetta, 0.075)
    
    S = 2.065*heat_capacity_mid*(temperature_wall - temperature_conditional) * pow(viscosity_wall, 0.15) / (pow(gas_constant_wall * temperature_wall, 0.425) * pow((1 + relate_temperature), 0.595) * pow((3 + relate_temperature), 0.15))
    # print(2.065*heat_capacity_mid*(temperature_wall - temperature_usl) * pow(viscosity_wall, 0.15))
    # print(pow(gas_constant_wall * temperature_wall, 0.425) * pow((1 + relate_temperature), 0.595) * pow((3 + relate_temperature), 0.15))
    # print(S)
    
    q_convective = [0] * NUM_SECTIONS
    for i in range(NUM_SECTIONS):
        q_convective[i] = B*(1 - pow(betta_at_lamb[i], 2))*epsilon*pow(pressure_chamber_Pa, 0.85) * S / (pow(d[i],1.82) * pow(d_critical,0.15) * pow(Prandtl, 0.58))
    return q_convective

q = calc_convective(geometry[2], min(geometry[1]))
print(q)

def calc_radiant():
    return 1

sz = False
for i in range(len(geometry[3])):
    if i > 13:
        sz = True
    print(get_lambda(geometry[3][i],min(geometry[3]), sz))