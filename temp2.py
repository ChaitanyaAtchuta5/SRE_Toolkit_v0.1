from cryptography.fernet import Fernet
from datetime import date
import subprocess
import sys

def write_file():
    app_key = b'z4WgegchrnsyRaKJXWg4sN9iaqEvaVjWjfZSI2gH5jE='
    crypto_fer = Fernet(app_key)

    date = str(crypto_fer.encrypt(b'2021-08-23'), 'utf-8') #yyyy-mm-dd

    with open('Licence.key', 'w') as f:
        f.write(date)


def read_file():
    app_key = b'z4WgegchrnsyRaKJXWg4sN9iaqEvaVjWjfZSI2gH5jE='
    crypto_fer = Fernet(app_key)

    with open('Licence.key', 'rb') as f:
        enc_code = f.read()
    
    print(enc_code)
    dec_code = str(crypto_fer.decrypt(enc_code), 'utf-8')
    print(dec_code)
    dec_code = dec_code.split('-')
    print(dec_code)
    exp_date = date(year=int(dec_code[0]), month=int(dec_code[1]), day=int(dec_code[2]))
    curr_date = date.today()

    if(curr_date > exp_date):
        print('App Expired')
    else:
        print('App is Running')

def run_Jmeter(JM_batch, JM_script, JM_res):
    subprocess.run("cmd.exe /c '{JM_batch}' -n -t '{JM_script}' -l '{JM_res}'".format(JM_batch = JM_batch, JM_script = JM_script, JM_res = JM_res))
    print('executed')

def run_Jmeter_sub(JM_batch, JM_script, JM_res):
    process = subprocess.Popen('''"{JM_batch}" -n -t "{JM_script}" -l "{JM_res}"'''.format(JM_batch = JM_batch, JM_script = JM_script, JM_res = JM_res), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #process = subprocess.Popen('''"C:/Users/maxel/Desktop/apache-jmeter-5.2.1/bin/jmeter.bat" -n -t "C:/Users/maxel/Desktop/FINAL/dummy.jmx" -l "C:/Users/maxel/Desktop/JMeter Results/sample.jtl"''', shell=True,stdout=subprocess.PIPE)
    #process = subprocess.Popen('''pip install pandas''', shell=True,stdout=subprocess.PIPE)
    
    for out in iter(process.stdout.readline, b''):
        sys.stdout.write(str(out, 'utf-8'))
    
    print('executed')


write_file()
#read_file()
run_Jmeter_sub(JM_batch='C:/Users/maxel/Desktop/apache-jmeter-5.2.1/bin/jmeter.ba',
           JM_script='C:/Users/maxel/Desktop/FINAL/dummy.jmx',
           JM_res='C:/Users/maxel/Desktop/JMeter Results/sample.jtl')