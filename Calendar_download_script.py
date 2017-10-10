import webbrowser
import shutil
import time
from selenium import webdriver

#PGY-4
#list of links assigned to variables removed for security concerns
#PGY-3
#list of links assigned to variables removed for security concerns
#PGY-2
#list of links assigned to variables removed for security concerns
#PGY-1
#list of links assigned to variables removed for security concerns
#Attending calendars
#list of links assigned to variables removed for security concerns

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
