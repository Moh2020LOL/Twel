import math


class shapes():
    def tangle(a,b,c) -> int: #if c ==0
        if a or b == 0:
            if a == 0:
                c = c**2
                b = b**2
                a = math.sqrt((c - b))
                return a
            if b == 0:
                a = a**2
                c = c**2
                b = math.sqrt((c - a))
                return b
        if c == 0:
            a = a**2
            b = b**2
            c = math.sqrt(a+b)
            return c
    

    def square_face(x,y) -> int:
        b =x*y
        return b


    def square_around(a,b,c,e):
        x =a+b+c+e
        return x
    


    def cericle_around(b):
        x = math.pi * b
        return x
    
    
    
    def cericle_tall(b):
        x = b * math.pi
        return x

class dvi:
    def sqr(a):
        x = a * a
        return x
    def one_to_infite(a,b):
        return a**b
    def root(a):
        n = 0
        for i in range(a):
            n +=1
            if a == n*n:
                return n
    def cube_root(a):
        n = 0
        for i in range(a):
            n +=1
            if a == n*n*n:
                return n

        

                

    def abst(a):
        return round(a)
    
class Weight:
    def TG_G(a):
        x = a * 10**12
        return x
    def g_TG(a):
        x=  a * 10**-12
        return x
    def Gg_g(a):
        x = a * 10 ** 9
        return x
    def g_Gg(a):
        x = a * 10**-9
        return x
    def Mg_g(a):
        x = a * 10**6
        return x
    def g_MgG(a):
        x = a * 10**-6
        return x
    def kg_g(a):
        x = a * 10**3
        return x
    def g_kg(a):
        x = a * 10**-3
        return x
    def heg_g(a):
        x = a * 10**2
        return x
    def g_heg(a):
        x =  a * 10**-2
        return x
    def dg_g(a):
        x = a * 10
        return x
    def g_dg(a):
        x = a / 10
        return x
    def g_csg(a):
        x = a * 10**2
        return x
    def csg_g(a):
        x = a * 10**-2
        return x
    def g_mlg(a):
        x = a * 10**3
        return x
    def mlg_g(a):
        x = a * 10**-3
        return x
    def g_mrg(a):
        x = a * 10**6
        return x
    def mrg_g(a):
        x = a * 10**-6
        return x
    def g_nag(a):
        x = a * 10**9
        return x
    def nag_g(a):
        x = a  * 10**-9
        return x
    def g_bkg(a):
        x = a* 10**12
        return x
    def bkg_g(a):
        x = a * 10**-12
        return x
    def g_veg(a):
        x = a * 10**15
        return x
    def veg_g(a):
        x= a * 10**-15
        return x






class Length:
    def TM_m(a):
        x = a * 10**12
        return x
    def m_TM(a):
        x=  a * 10**-12
        return x
    def GM_m(a):
        x = a * 10 ** 9
        return x
    def m_Gm(a):
        x = a * 10**-9
        return x
    def Mm_m(a):
        x = a * 10**6
        return x
    def m_Mm(a):
        x = a * 10**-6
        return x
    def km_m(a):
        x = a * 10**3
        return x
    def m_km(a):
        x = a * 10**-3
        return x
    def hem_m(a):
        x = a * 10**2
        return x
    def m_hem(a):
        x =  a * 10**-2
        return x
    def dm_m(a):
        x = a * 10
        return x
    def m_dm(a):
        x = a / 10
        return x
    def m_csm(a):
        x = a * 10**2
        return x
    def csm_m(a):
        x = a * 10**-2
        return x
    def m_mlm(a):
        x = a * 10**3
        return x
    def mlm_m(a):
        x = a * 10**-3
        return x
    def m_mrM(a):
        x = a * 10**6
        return x
    def mrM_m(a):
        x = a * 10**-6
        return x
    def m_nam(a):
        x = a * 10**9
        return x
    def naM_m(a):
        x = a  * 10**-9
        return x
    def m_bkM(a):
        x = a* 10**12
        return x
    def bkM_m(a):
        x = a * 10**-12
        return x
    def m_veM(a):
        x = a * 10**15
        return x
    def veM_m(a):
        x= a * 10**-15
        return x