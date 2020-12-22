import sympy as sp
a0 ,a1 ,a2 ,a3 ,a4 ,a5 ,a6 ,a7 ,a8 ,a9 ,a10 = sp.symbols('a_0 a_1 a_2 a_3 a_4 a_5 a_6 a_7 a_8 a_9 a_10')
da0, da1, da2, da3, da4, da5, da6, da7, da8, da9, da10 = sp.symbols('Δa_0 Δa_1 Δa_2 Δa_3 Δa_4 Δa_5 Δa_6 Δa_7 Δa_8 Δa_9 Δa_10')
b0 ,b1 ,b2 ,b3 ,b4 ,b5 ,b6 ,b7 ,b8 ,b9 ,b10 = sp.symbols('b_0 b_1 b_2 b_3 b_4 b_5 b_6 b_7 b_8 b_9 b_10')
db0, db1, db2, db3, db4, db5, db6, db7, db8, db9, db10 = sp.symbols('Δb_0 Δb_1 Δb_2 Δb_3 Δb_4 Δb_5 Δb_6 Δb_7 Δb_8 Δb_9 Δb_10')
m0, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10 = sp.symbols('m_0 m_1 m_2 m_3 m_4 m_5 m_6 m_7 m_8 m_9 m_10')
dm0, dm1, dm2, dm3, dm4, dm5, dm6, dm7, dm8, dm9, dm10 = sp.symbols('Δm_0 Δm_1 Δm_2 Δm_3 Δm_4 Δm_5 Δm_6 Δm_7 Δm_8 Δm_9 Δm_10')
A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z = sp.symbols('A B C D E F G H I J K L M N O P Q R S T U V W X Y Z')
a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = sp.symbols('a b c d e f g h i j k l m n o p q r s t u v w x y z')
dA, dB, dC, dD, dE, dF, dG, dH, dI, dJ, dK, dL, dM, dN, dO, dP, dQ, dR, dS, dT, dU, dV, dW, dX, dY, dZ = sp.symbols('ΔA ΔB ΔC ΔD ΔE ΔF ΔG ΔH ΔI ΔJ ΔK ΔL ΔM ΔN ΔO ΔP ΔQ ΔR ΔS ΔT ΔU ΔV ΔW ΔX ΔY ΔZ')
da, db, dc, dd, de, df, dg, dh, di, dj, dk, dl, dm, dn, do, dp, dq, dr, ds, dt, du, dv, dw, dx, dy, dz = sp.symbols('Δa Δb Δc Δd Δe Δf Δg Δh Δi Δj Δk Δl Δm Δn Δo Δp Δq Δr Δs Δt Δu Δv Δw Δx Δy Δz')

error_dict = {a0:da0, a1:da1, a2:da2, a3:da3, a4:da4, a5:da5, a6:da6, a7:da7, a8:da8, a9:da9, a10:da10, \
b0:db0, b1:db1, b2:db2, b3:db3, b4:db4, b5:db5, b6:db6, b7:db7, b8:db8, b9:db9, b10:db10, \
m0:dm0, m1:dm1, m2:dm2, m3:dm3, m4:dm4, m5:dm5, m6:dm6, m7:dm7, m8:dm8, m9:dm9, m10:dm10, \
A:dA, B:dB, C:dC, D:dD, E:dE, F:dF, G:dG, H:dH, I:dI, J:dJ, K:dK, L:dL, M:dM, N:dN, O:dO, P:dP, Q:dQ, R:dR, S:dS, T:dT, U:dU, V:dV, W:dW, X:dX, Y:dY, Z:dZ, \
a:da, b:db, c:dc, d:dd, e:de, f:df, g:dg, h:dh, i:di, j:dj, k:dk, l:dl, m:dm, n:dn, o:do, p:dp, q:dq, r:dr, s:ds, t:dt, u:du, v:dv, w:dw, x:dx, y:dy, z:dz}

string_to_symbol_dict = {'a0':a0, 'da0':da0, 'a1':a1, 'da1':da1, 'a2':a2, 'da2':da2, 'a3':a3, 'da3':da3, 'a4':a4, 'da4':da4, 'a5':a5, 'da5':da5, 'a6':a6, 'da6':da6, 'a7':a7, 'da7':da7, 'a8':a8, 'da8':da8, 'a9':a9, 'da9':da9, 'a10':a10, 'da10':da10, \
'b0':b0, 'b0':b0, 'b1':b1, 'b1':b1, 'b2':b2, 'b2':b2, 'b3':b3, 'b3':b3, 'b4':b4, 'b4':b4, 'b5':b5, 'b5':b5, 'b6':b6, 'b6':b6, 'b7':b7, 'b7':b7, 'b8':b8, 'b8':b8, 'b9':b9, 'b9':b9, 'b10':b10, 'b10':b10, \
'm0':m0, 'dm0':dm0, 'm1':m1, 'dm1':dm1, 'm2':m2, 'dm2':dm2, 'm3':m3, 'dm3':dm3, 'm4':m4, 'dm4':dm4, 'm5':m5, 'dm5':dm5, 'm6':m6, 'dm6':dm6, 'm7':m7, 'dm7':dm7, 'm8':m8, 'dm8':dm8, 'm9':m9, 'dm9':dm9, 'm10':m10, 'dm10':dm10, \
"A":A, "dA":dA, "B":B, "dB":dB, "C":C, "dC":dC, "D":D, "dD":dD, "E":E, "dE":dE, "F":F, "dF":dF, "G":G, "dG":dG, "H":H, "dH":dH, "I":I, "dI":dI, "J":J, "dJ":dJ, "K":K, "dK":dK, "L":L, "dL":dL, "M":M, "dM":dM, "N":N, "dN":dN, "O":O, "dO":dO, "P":P, "dP":dP, "Q":Q, "dQ":dQ, "R":R, "dR":dR, "S":S, "dS":dS, "T":T, "dT":dT, "U":U, "dU":dU, "V":V, "dV":dV, "W":W, "dW":dW, "X":X, "dX":dX, "Y":Y, "dY":dY, "Z":Z, "dZ":dZ, \
"a":a, "da":da, "b":b, "db":db, "c":c, "dc":dc, "d":d, "dd":dd, "e":e, "de":de, "f":f, "df":df, "g":g, "dg":dg, "h":h, "dh":dh, "i":i, "di":di, "j":j, "dj":dj, "k":k, "dk":dk, "l":l, "dl":dl, "m":m, "dm":dm, "n":n, "dn":dn, "o":o, "do":do, "p":p, "dp":dp, "q":q, "dq":dq, "r":r, "dr":dr, "s":s, "ds":ds, "t":t, "dt":dt, "u":u, "du":du, "v":v, "dv":dv, "w":w, "dw":dw, "x":x, "dx":dx, "y":y, "dy":dy, "z":z, "dz":dz}