from cryptography.fernet import Fernet
from datetime import date

def write_file():
    app_key = b'z4WgegchrnsyRaKJXWg4sN9iaqEvaVjWjfZSI2gH5jE='
    crypto_fer = Fernet(app_key)

    date = str(crypto_fer.encrypt(b'2021-08-13')) #yyyy-mm-dd

    with open('Licence.key', 'w') as f:
        f.write(date[2:-1])


def read_file():
    app_key = b'z4WgegchrnsyRaKJXWg4sN9iaqEvaVjWjfZSI2gH5jE='
    crypto_fer = Fernet(app_key)

    with open('Licence.key', 'rb') as f:
        enc_code = f.read()
    
    print(enc_code)
    dec_code = str(crypto_fer.decrypt(enc_code))
    print(dec_code)
    dec_code = dec_code[2:-1].split('-')
    print(dec_code)
    exp_date = date(year=int(dec_code[0]), month=int(dec_code[1]), day=int(dec_code[2]))
    curr_date = date.today()

    if(curr_date > exp_date):
        print('App Expired')
    else:
        print('App is Running')

write_file()