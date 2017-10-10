from datetime import datetime
import subprocess, time, send2trash, pytz, tzlocal, openpyxl, csv

#below is the path for automation via tableau
#\\homedir-cifs.nyumc.org\home001_10G\POONC01\Personal\Provider Schedule project

subprocess.Popen([
                'C:\\Program Files (x86)\\Python36-32\\python.exe',
                'Calendar_download_script.py'
                ])

try:
    send2trash.send2trash('Attending.csv')
    send2trash.send2trash('Resident.csv')
    send2trash.send2trash('PA.csv')
    send2trash.send2trash('main.csv')
    send2trash.send2trash('main-no-on.csv')
except:
    pass

for downloading in range(8):
    #gives time for the downloads to occur. Increase range to lengthen time
    print('Tick')
    time.sleep(1)
    print('Tock')
    time.sleep(1)

def header(csvs):
    for csv in csvs:
        with open(csv, 'a') as header:
            """First row header for main csv"""
            header.write('Summary, DTStart, DTEnd\n')

def cal_writer_attPA(calendars):
    """takes outlook .ics file and creates a .csv file"""
    for calendar in calendars:
        with open(calendar) as file_object:
            summary = 'SUMMARY:'
            dtstart = 'DTSTART'
            dtend = 'DTEND'
            for shift in file_object:
                if summary in shift:
                    a = shift.strip()
                    with open(csv, 'a') as f:
                        s = (
                            b[8:12] + "-" + b[12:14] + "-" + b[14:16] + " " +
                            b[17:19] + ":" + b[19:21] + ":" + b[21:23]
                            )

                        e = (
                            c[6:10] + "-" + c[10:12] + "-" + c[12:14] + " " +
                            c[15:17] + ":" + c[17:19] + ":" + c[19:21]
                            )
                        local_timezone = tzlocal.get_localzone()
                        start_utc = datetime.strptime(s,'%Y-%m-%d %H:%M:%S')
                        start_localtime = start_utc.replace(tzinfo=pytz.utc).astimezone(local_timezone)
                        end_utc = datetime.strptime(e,'%Y-%m-%d %H:%M:%S')
                        end_localtime = end_utc.replace(tzinfo=pytz.utc).astimezone(local_timezone)
                        f.write(
                                a[8:] + "," +
                                str(start_localtime)[:19] + "," +
                                str(end_localtime)[:19] + "\n"
                                )
                if dtstart in shift:
                    b = shift.strip()
                if dtend in shift:
                    c = shift.rstrip()

def cal_writer_res(calendars):
    """takes outlook .ics file and creates a .csv file"""
    for calendar in calendars:
        with open(calendar) as file_object:
            summary = 'SUMMARY:'
            dtstart = 'DTSTART'
            dtend = 'DTEND'
            for shift in file_object:
                if summary in shift:
                    a = shift.strip()
                    with open(csv, 'a') as f:
                        s = (
                            b[8:12] + "-" + b[12:14] + "-" + b[14:16] + " " +
                            b[17:19] + ":" + b[19:21] + ":" + b[21:23]
                            )

                        e = (
                            c[6:10] + "-" + c[10:12] + "-" + c[12:14] + " " +
                            c[15:17] + ":" + c[17:19] + ":" + c[19:21]
                            )
                        try:
                            local_timezone = tzlocal.get_localzone()
                            start_utc = datetime.strptime(s,'%Y-%m-%d %H:%M:%S')
                            start_localtime = start_utc.replace(tzinfo=pytz.utc).astimezone(local_timezone)
                            end_utc = datetime.strptime(e,'%Y-%m-%d %H:%M:%S')
                            end_localtime = end_utc.replace(tzinfo=pytz.utc).astimezone(local_timezone)
                        except ValueError:
                            pass
                        else:
                            f.write(
                                    a[8:].replace(",","") + " " +
                                    str(calendar) + "," +
                                    str(start_localtime)[:19] + "," +
                                    str(end_localtime)[:19] +"\n"
                                    )
                if dtstart in shift:
                    b = shift.strip()
                if dtend in shift:
                    c = shift.rstrip()
csvs = ['Attending.csv', 'Resident.csv', 'PA.csv']
header(csvs)

calendars = ['calendars\Attending.ics']
csv = 'Attending.csv'
cal_writer_attPA(calendars)

calendars = ['calendars\TischPA.ics']
csv = 'PA.csv'
cal_writer_attPA(calendars)

calendars = [
            'calendars\\rescal\\Auld_E.ics',
            'calendars\\rescal\\Aylyarov_I.ics',
            'calendars\\rescal\\Bennett_J.ics',
            'calendars\\rescal\\Berger_M.ics',
            'calendars\\rescal\\Betancourt_E.ics',
            'calendars\\rescal\\Castro_M.ics',
            'calendars\\rescal\\Choi_H.ics',
            'calendars\\rescal\\Ciardiello_A.ics',
            'calendars\\rescal\\Cloyd_T.ics',
            'calendars\\rescal\\Coplin_M.ics',
            'calendars\\rescal\\Diaz_M.ics',
            'calendars\\rescal\\Dibble_B.ics',
            'calendars\\rescal\\Dimiceli_E.ics',
            'calendars\\rescal\\Disalvo_P.ics',
            'calendars\\rescal\\Doobay_K.ics',
            'calendars\\rescal\\Farmer_C.ics',
            'calendars\\rescal\\Ferraioli_F.ics',
            'calendars\\rescal\\Gallagher_T.ics',
            'calendars\\rescal\\Gorynski_M.ics',
            'calendars\\rescal\\Guiney_A.ics',
            'calendars\\rescal\\Hart_L.ics',
            'calendars\\rescal\\Hughes_A.ics',
            'calendars\\rescal\\Iheagwara_O.ics',
            'calendars\\rescal\\Iscoe_M.ics',
            'calendars\\rescal\\Kaufer_M.ics',
            'calendars\\rescal\\Levin_J.ics',
            'calendars\\rescal\\Lin_B.ics',
            'calendars\\rescal\\Mccarty_M.ics',
            'calendars\\rescal\\Mcdonald_L.ics',
            'calendars\\rescal\\Mcdonald_S.ics',
            'calendars\\rescal\\Mcfarland_D.ics',
            'calendars\\rescal\\Mikhly_M.ics',
            'calendars\\rescal\\Miller_A.ics',
            'calendars\\rescal\\Mohamed_H.ics',
            'calendars\\rescal\\Mohan_S.ics',
            'calendars\\rescal\\Mordel_A.ics',
            'calendars\\rescal\\Muckey_E.ics',
            'calendars\\rescal\\Nesheiwat_L.ics',
            'calendars\\rescal\\Ng_K.ics',
            'calendars\\rescal\\Ortego_A.ics',
            'calendars\\rescal\\Pace_R.ics',
            'calendars\\rescal\\Paris_J.ics',
            'calendars\\rescal\\Pasternac_K.ics',
            'calendars\\rescal\\Rajeev_S.ics',
            'calendars\\rescal\\Ramadan_L.ics',
            'calendars\\rescal\\Robak_M.ics',
            'calendars\\rescal\\Romeo_M.ics',
            'calendars\\rescal\\Shamoon_M.ics',
            'calendars\\rescal\\Shapiro_S.ics',
            'calendars\\rescal\\Skelton_E.ics',
            'calendars\\rescal\\Snavely_C.ics',
            'calendars\\rescal\\Storch_B.ics',
            'calendars\\rescal\\Sutton-Ramsey_D.ics',
            'calendars\\rescal\\Terentiev_V.ics',
            'calendars\\rescal\\Tsao_J.ics',
            'calendars\\rescal\\Unks_E.ics',
            'calendars\\rescal\\Villegas_L.ics',
            'calendars\\rescal\\Weber_L.ics',
            'calendars\\rescal\\White_R.ics',
            'calendars\\rescal\\Worthing_J.ics',
            'calendars\\rescal\\Wu_G.ics'
            ]
csv = 'Resident.csv'
cal_writer_res(calendars)

time.sleep(1)

subprocess.Popen([
                'C:\\Program Files (x86)\\Python36-32\\python.exe',
                'excel_updater.py'
                ])
