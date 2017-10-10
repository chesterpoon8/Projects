import webbrowser
import shutil
import time
from selenium import webdriver

#PGY-4
cloydt = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.2867&Lo=nyuem&Jd=7532'
gallaghert = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.2868&Lo=nyuem&Jd=7532'
guineya = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.2869&Lo=nyuem&Jd=7532'
kauferm = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.2870&Lo=nyuem&Jd=7532'
linb = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.2871&Lo=nyuem&Jd=7532'
mccartym = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.2872&Lo=nyuem&Jd=7532'
mcdonalds = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.2873&Lo=nyuem&Jd=7532'
mikhlym = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.2874&Lo=nyuem&Jd=7532'
mordela = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.2875&Lo=nyuem&Jd=7532'
ortegoa = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.2876&Lo=nyuem&Jd=7532'
pacer = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.2877&Lo=nyuem&Jd=7532'
parisj = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.2878&Lo=nyuem&Jd=7532'
shamoonm = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.2879&Lo=nyuem&Jd=7532'
skeltone = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.2880&Lo=nyuem&Jd=7532'
wug = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.2881&Lo=nyuem&Jd=7532'
#PGY-3
choih = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3023&Lo=nyuem&Jd=7532'
disalvop = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3024&Lo=nyuem&Jd=7532'
dibbleb = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3025&Lo=nyuem&Jd=7532'
gorynskim = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3026&Lo=nyuem&Jd=7532'
hartl = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3027&Lo=nyuem&Jd=7532'
levinj = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3028&Lo=nyuem&Jd=7532'
mcdonaldl = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3029&Lo=nyuem&Jd=7532'
mcfarlandd = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3030&Lo=nyuem&Jd=7532'
mohamedh = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3031&Lo=nyuem&Jd=7532'
muckeye = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3032&Lo=nyuem&Jd=7532'
rajeevs = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3033&Lo=nyuem&Jd=7532'
storchb = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3034&Lo=nyuem&Jd=7532'
suttonramseyd = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3035&Lo=nyuem&Jd=7532'
villegasl = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3036&Lo=nyuem&Jd=7532'
whiter = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3203&Lo=nyuem&Jd=7532'
#PGY-2
aylyarovi = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3216&Lo=nyuem&Jd=7532'
bennettj = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3217&Lo=nyuem&Jd=7532'
bergerm = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3218&Lo=nyuem&Jd=7532'
betancourte = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3219&Lo=nyuem&Jd=7532'
coplinm = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3220&Lo=nyuem&Jd=7532'
farmerc = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3221&Lo=nyuem&Jd=7532'
ferraiolif = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3222&Lo=nyuem&Jd=7532'
millera = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3223&Lo=nyuem&Jd=7532'
mohans = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3224&Lo=nyuem&Jd=7532'
nesheiwatl = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3225&Lo=nyuem&Jd=7532'
ngk = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3226&Lo=nyuem&Jd=7532'
pasternack = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3227&Lo=nyuem&Jd=7532'
robakm = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3228&Lo=nyuem&Jd=7532'
shapiros = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3229&Lo=nyuem&Jd=7532'
unkse = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3230&Lo=nyuem&Jd=7532'
#PGY-1
aulde = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3413&Lo=nyuem&Jd=7532'
castrom = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3414&Lo=nyuem&Jd=7532'
ciardielloa = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3415&Lo=nyuem&Jd=7532'
diazm = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3416&Lo=nyuem&Jd=7532'
dimicelie = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3417&Lo=nyuem&Jd=7532'
doobayk = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3418&Lo=nyuem&Jd=7532'
hughesa = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3419&Lo=nyuem&Jd=7532'
iheagwarao = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3420&Lo=nyuem&Jd=7532'
iscoem = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3421&Lo=nyuem&Jd=7532'
ramadanl = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3422&Lo=nyuem&Jd=7532'
romeom = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3423&Lo=nyuem&Jd=7532'
snavelyc = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3424&Lo=nyuem&Jd=7532'
terentievv = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3425&Lo=nyuem&Jd=7532'
tsaoj = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3426&Lo=nyuem&Jd=7532'
weberl = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3427&Lo=nyuem&Jd=7532'
worthingj = 'http://www.amion.com/cgi-bin/ocs?Vcal=7.3428&Lo=nyuem&Jd=7532'
#Attending calendars
attending_cal = 'http://www.shiftadmin.com/schedule_ical_group.php?cd=AODnD8D82hg0QfAMLYDU2SDheCqhdie4U0%2FpnaWKEP4%3D&gfs=f1,f2,f3,f5,f6,f7,f9,f27,g3,f11,f12,f13,f16,f20'

calendars = [
            #PGY-4
            cloydt, gallaghert, guineya, kauferm, linb, mccartym, mcdonalds,
            mikhlym, mordela, ortegoa, pacer, parisj, shamoonm, skeltone, wug,
            #PGY-3
            choih, disalvop, dibbleb, gorynskim, hartl, levinj, mcdonaldl,
            mcfarlandd, mohamedh, muckeye, rajeevs, storchb, suttonramseyd,
            villegasl, whiter,
            #PGY-2
            aylyarovi, bennettj, bergerm, betancourte, coplinm, farmerc,
            ferraiolif, millera, mohans, nesheiwatl, ngk, pasternack, robakm,
            shapiros, unkse,
            #PGY-1
            aulde, castrom, ciardielloa, diazm, dimicelie, doobayk, hughesa,
            iheagwarao, iscoem, ramadanl, romeom, snavelyc, terentievv, tsaoj,
            weberl, worthingj,
            #Attending
            attending_cal
            ]

#downloads calendars
for calendar in calendars:
    webbrowser.open(calendar)

for downloading in range(20):
    #gives time for the downloads to occur. Increase range to lengthen time
    print('Tick')
    time.sleep(1)
    print('Tock')
    time.sleep(1)

#Move all files to scheduleproj
#PGY-4
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem2867.ics', 'C:\\scheduleproj\\calendars\\rescal\\Cloyd_T.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem2868.ics', 'C:\\scheduleproj\\calendars\\rescal\\Gallagher_T.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem2869.ics', 'C:\\scheduleproj\\calendars\\rescal\\Guiney_A.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem2870.ics', 'C:\\scheduleproj\\calendars\\rescal\\Kaufer_M.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem2871.ics', 'C:\\scheduleproj\\calendars\\rescal\\Lin_B.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem2872.ics', 'C:\\scheduleproj\\calendars\\rescal\\Mccarty_M.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem2873.ics', 'C:\\scheduleproj\\calendars\\rescal\\Mcdonald_S.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem2874.ics', 'C:\\scheduleproj\\calendars\\rescal\\Mikhly_M.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem2875.ics', 'C:\\scheduleproj\\calendars\\rescal\\Mordel_A.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem2876.ics', 'C:\\scheduleproj\\calendars\\rescal\\Ortego_A.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem2877.ics', 'C:\\scheduleproj\\calendars\\rescal\\Pace_R.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem2878.ics', 'C:\\scheduleproj\\calendars\\rescal\\Paris_J.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem2879.ics', 'C:\\scheduleproj\\calendars\\rescal\\Shamoon_M.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem2880.ics', 'C:\\scheduleproj\\calendars\\rescal\\Skelton_E.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem2881.ics', 'C:\\scheduleproj\\calendars\\rescal\\Wu_G.ics')
#PGY-3
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3023.ics', 'C:\\scheduleproj\\calendars\\rescal\\Choi_H.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3024.ics', 'C:\\scheduleproj\\calendars\\rescal\\Disalvo_P.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3025.ics', 'C:\\scheduleproj\\calendars\\rescal\\Dibble_B.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3026.ics', 'C:\\scheduleproj\\calendars\\rescal\\Gorynski_M.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3027.ics', 'C:\\scheduleproj\\calendars\\rescal\\Hart_L.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3028.ics', 'C:\\scheduleproj\\calendars\\rescal\\Levin_J.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3029.ics', 'C:\\scheduleproj\\calendars\\rescal\\Mcdonald_L.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3030.ics', 'C:\\scheduleproj\\calendars\\rescal\\Mcfarland_D.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3031.ics', 'C:\\scheduleproj\\calendars\\rescal\\Mohamed_H.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3032.ics', 'C:\\scheduleproj\\calendars\\rescal\\Muckey_E.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3033.ics', 'C:\\scheduleproj\\calendars\\rescal\\Rajeev_S.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3034.ics', 'C:\\scheduleproj\\calendars\\rescal\\Storch_B.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3035.ics', 'C:\\scheduleproj\\calendars\\rescal\\Sutton-Ramsey_D.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3036.ics', 'C:\\scheduleproj\\calendars\\rescal\\Villegas_L.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3203.ics', 'C:\\scheduleproj\\calendars\\rescal\\White_R.ics')
#PGY-2
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3216.ics', 'C:\\scheduleproj\\calendars\\rescal\\Aylyarov_I.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3217.ics', 'C:\\scheduleproj\\calendars\\rescal\\Bennett_J.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3218.ics', 'C:\\scheduleproj\\calendars\\rescal\\Berger_M.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3219.ics', 'C:\\scheduleproj\\calendars\\rescal\\Betancourt_E.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3220.ics', 'C:\\scheduleproj\\calendars\\rescal\\Coplin_M.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3221.ics', 'C:\\scheduleproj\\calendars\\rescal\\Farmer_C.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3222.ics', 'C:\\scheduleproj\\calendars\\rescal\\Ferraioli_F.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3223.ics', 'C:\\scheduleproj\\calendars\\rescal\\Miller_A.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3224.ics', 'C:\\scheduleproj\\calendars\\rescal\\Mohan_S.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3225.ics', 'C:\\scheduleproj\\calendars\\rescal\\Nesheiwat_L.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3226.ics', 'C:\\scheduleproj\\calendars\\rescal\\Ng_K.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3227.ics', 'C:\\scheduleproj\\calendars\\rescal\\Pasternac_K.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3228.ics', 'C:\\scheduleproj\\calendars\\rescal\\Robak_M.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3229.ics', 'C:\\scheduleproj\\calendars\\rescal\\Shapiro_S.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3230.ics', 'C:\\scheduleproj\\calendars\\rescal\\Unks_E.ics')
#PGY-1
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3413.ics', 'C:\\scheduleproj\\calendars\\rescal\\Auld_E.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3414.ics', 'C:\\scheduleproj\\calendars\\rescal\\Castro_M.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3415.ics', 'C:\\scheduleproj\\calendars\\rescal\\Ciardiello_A.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3416.ics', 'C:\\scheduleproj\\calendars\\rescal\\Diaz_M.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3417.ics', 'C:\\scheduleproj\\calendars\\rescal\\Dimiceli_E.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3418.ics', 'C:\\scheduleproj\\calendars\\rescal\\Doobay_K.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3419.ics', 'C:\\scheduleproj\\calendars\\rescal\\Hughes_A.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3420.ics', 'C:\\scheduleproj\\calendars\\rescal\\Iheagwara_O.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3421.ics', 'C:\\scheduleproj\\calendars\\rescal\\Iscoe_M.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3422.ics', 'C:\\scheduleproj\\calendars\\rescal\\Ramadan_L.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3423.ics', 'C:\\scheduleproj\\calendars\\rescal\\Romeo_M.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3424.ics', 'C:\\scheduleproj\\calendars\\rescal\\Snavely_C.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3425.ics', 'C:\\scheduleproj\\calendars\\rescal\\Terentiev_V.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3426.ics', 'C:\\scheduleproj\\calendars\\rescal\\Tsao_J.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3427.ics', 'C:\\scheduleproj\\calendars\\rescal\\Weber_L.ics')
shutil.move('C:\\Users\\poonc01\\Downloads\\nyuem3428.ics', 'C:\\scheduleproj\\calendars\\rescal\\Worthing_J.ics')
#Attending
shutil.move('C:\\Users\\poonc01\\Downloads\\subscribe.ics', 'C:\\scheduleproj\\calendars\\Attending.ics')
#PA
