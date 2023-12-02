"""
Copy Right 2023 Slour
All Methods:
imformation.fake.name
imformation.fake.user
imformation.fake.password
imformation.fake.address
imformation.fake.birth
imformation.fake.email
imformation.fake.getpath
imformation.fake.info
"""
# Start Coding
import random, faker, string, os
fake = faker.Faker()
class information:
    class fake:
        def user(length=12):
            letters = string.ascii_letters 
            numbers = string.digits
            full_chars = letters + numbers + '_____'
            result_str = ''.join(random.choice(full_chars) for i in range(length))
            userres = str(result_str)
            return userres
        def name():
            return fake.name()
        def password(length=10):
            letters = string.ascii_letters 
            numbers = string.digits
            full_chars = letters + numbers + string.punctuation
            result_str = ''.join(random.choice(full_chars) for i in range(length))
            passwordres = str(result_str)
            return passwordres
        def address():
            return fake.address()
        def birth():
            numbers = string.digits
            result_stry = ''.join(random.choice(numbers) for i in range(2))
            result_strm = ''.join(random.choice(numbers) for i in range(2))
            result_strd = ''.join(random.choice(numbers) for i in range(2))
            month = result_strm
            day = result_strd
            year = f"19{result_stry}"
            if(result_stry>='60' and result_strm <= '12' and result_strd <= '30'):
                month = result_strm
                day = result_strd
                year = f"19{result_stry}"
                result = f"{year}-{month}-{day}"
                return result
            else:
                result = information.fake.birth()
                return result
        def email():
            number_of_mails = 100
            list_of_domains = (
                'com',
                'com.br',
                'net',
                'net.br',
                'org',
                'org.br',
                'gov',
                'gov.br'
            )

            for _ in range(number_of_mails):
                first_name = fake.first_name()
                last_name = fake.last_name()
                company = fake.company().split()[0].strip(',')
                dns_org = fake.random_choices(
                    elements=list_of_domains,
                    length=1
                )[0]
                email = f"{first_name}.{last_name}@{company}.{dns_org}".lower()
                return email
        def getpath():
            return os.getcwd().replace('\\','/')
        def info(data_type='txt', loop=1):
            try:
                loop = int(loop)
            except:
                pass
            Fuser = information.fake.user()
            Fname = information.fake.name()
            Fbirth = information.fake.birth()
            Femail = information.fake.email()
            Faddress = str(information.fake.address()).replace('\n',', ')
            Fpassword = information.fake.password().replace('"','').replace("'",'').replace('\\','/')
            if(data_type == 'txt'):
                result = ''
                for i in range(loop):
                    Fuser = information.fake.user()
                    Fname = information.fake.name()
                    Fbirth = information.fake.birth()
                    Femail = information.fake.email()
                    Faddress = str(information.fake.address()).replace('\n',', ')
                    Fpassword = information.fake.password().replace('"','').replace("'",'').replace('\\','/')
                    informationRes = f"""Fake Name: {Fname}
Fake User: {Fuser}
Fake Address: {Faddress}
Fake password: {Fpassword}
Fake Email: {Femail}
Fake Birth: {Fbirth}"""
                    result += '\n' + informationRes + '\n'
                informationRes = result
            elif(data_type=='json'):
                result = ''
                for i in range(loop):
                    Fuser = information.fake.user()
                    Fname = information.fake.name()
                    Fbirth = information.fake.birth()
                    Femail = information.fake.email()
                    Faddress = str(information.fake.address()).replace('\n',', ')
                    Fpassword = information.fake.password().replace('"','').replace("'",'').replace('\\','/')
                    count = i + 1
                    if(count == loop):
                        code = f""""fake_info{count}":{{
"Fake Name": "{Fname}",
"Fake User": "{Fuser}",
"Fake Address": "{Faddress}",
"Fake password": "{Fpassword}",
"Fake Email": "{Femail}",
"Fake Birth": "{Fbirth}"
}}"""
                    else:
                        code = f""""fake_info{count}":{{
"Fake Name": "{Fname}",
"Fake User": "{Fuser}",
"Fake Address": "{Faddress}",
"Fake password": "{Fpassword}",
"Fake Email": "{Femail}"
}},"""
                    result += '\n' + code + '\n'
                informationRes = f"""{{
                        {result}
}}"""
            elif(data_type=='xml'):
                result = ''
                code = ''
                for i in range(loop):
                    count = i + 1
                    informationRes = f"<?xml version='1.0', encoding='utf-8'?>"
                    Fuser = information.fake.user()
                    Fname = information.fake.name()
                    Fbirth = information.fake.birth()
                    Femail = information.fake.email()
                    Faddress = str(information.fake.address()).replace('\n',', ')
                    Fpassword = information.fake.password()
                    code = f"""<fake_info{count}>
<name>{Fname}</name>
<user>{Fuser}</user>
<address>{Faddress}</address>
<password>{Fpassword}</password>
<email>{Femail}</email>
<birth>{Fbirth}</birth>
</fake_info{count}>"""
                    result += '\n' + code + '\n'
                    informationRes += result
            elif(data_type=='sql'):
                result = ''
                code = ''
                for i in range(loop):
                    count = i + 1
                    Fuser = information.fake.user()
                    Fname = information.fake.name()
                    Femail = information.fake.email()
                    Fbirth = information.fake.birth()
                    Faddress = str(information.fake.address()).replace('\n',', ')
                    Fpassword = information.fake.password().replace("'",'')
                    if(count==loop):
                        code = f"('{Fname}','{Fuser}','{Faddress}','{Fpassword}','{Femail}','{Fbirth}');"
                    else:
                        code = f"('{Fname}','{Fuser}','{Faddress}','{Fpassword}','{Femail}','{Fbirth}'),"
                    result += '\n' + code + '\n'
                informationRes = f"""CREATE TABLE fake_info(
name varchar(255),
user varchar(255),
address varchar(255),
password varchar(255),
email varchar(255),
birth varchar(255)
)
INSERT INTO fake_info (name, user, address, password, email,birth)
VALUES {result}"""
            elif(data_type=='html'):
                result = ''
                code = ''
                for i in range(loop):
                    count = i + 1
                    Fuser = information.fake.user()
                    Fname = information.fake.name()
                    Femail = information.fake.email()
                    Fbirth = information.fake.birth()
                    Faddress = str(information.fake.address()).replace('\n',', ')
                    Fpassword = information.fake.password()
                    code = f"""<tr class="values{count}">
<td class='name'>{Fname}</td>
<td class='user'>{Fuser}</td>
<td class='address'>{Faddress}</td>
<td class='password'>{Fpassword}</td>
<td class='email'>{Femail}</td>
<td class='birth'>{Fbirth}</td>
<td class='count'>{count}</td>
</tr>"""
                    result += '\n' + code + '\n'
                informationRes = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fake Information</title>
</head>
<body>
    <table border="1">
        <tr class="title">
            <td>name</td>
            <td>user</td>
            <td>address</td>
            <td>password</td>
            <td>email</td>
            <td>birth</td>
            <td>Count</td>
        </tr>
        {result}
    </table>
</body>
</html>"""
            else:
                informationRes = "[Type Not Found] [types=('json','txt','xml','sql','html')]"
            return informationRes
# END CODE