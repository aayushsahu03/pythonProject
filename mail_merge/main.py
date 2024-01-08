import smtplib
import datetime
# Below code for sending personlaized offer mail
"""
text = 'Hi [name],\nyou have a pre-aprroved\noffer of Rs.1,00,000'
with open("names_list.txt", 'r') as file:
    for name in file.readlines():
        with open(f"./{name.strip()}_letter.txt", 'w') as letter:
            letter.write(text.replace('[name]',name.strip()))

"""
my_email = "aayush.sahu.03@gmail.com"
password = "aoktdqtdprgrqbvt"


def send_email(email: str, password: str) -> None:
    """_summary_

    :param email: _description_
    :type email: str
    :param password: _description_
    :type password: str
    :return: _description_
    :rtype: _type_
    
    """
    with smtplib.SMTP(host="SMTP.gmail.com") as conn:
        conn.starttls()
        conn.login(my_email, password)
        conn.sendmail(from_addr=my_email,
                      to_addrs="aayush.sahu.03@outlook.com",
                      msg="Subject:Testing Phase-1\n\n"
                      )
    return None






