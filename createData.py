def userData(st,en):
    si = '['
    sl = '''
    ]'''
    s1 = '''
        {
            "model": "auth.user",
            "pk": '''
    s2 = ''',
            "fields": {
                "password": "pbkdf2_sha256$390000$kZVLqVCnRNdog5WgYkmDKG$hz/RB6Y7fEKWl064DzhylixEcBeX9clJ0a2AoUVGsp0=",
                "last_login": null,
                "is_superuser": false,
                "username": "vatsa'''
    s3 = '''",
                "first_name": "",
                "last_name": "",
                "email": "",
                "is_staff": false,
                "is_active": true,
                "date_joined": "2023-01-29T05:10:00.265Z",
                "groups": [],
                "user_permissions": []
            }
        },'''
    s3l = '''",
                "first_name": "",
                "last_name": "",
                "email": "",
                "is_staff": false,
                "is_active": true,
                "date_joined": "2023-01-29T05:10:00.265Z",
                "groups": [],
                "user_permissions": []
            }
        }'''

    s = ''
    for i in range(st,en+1):
        if i == en:
            s = s + s1 + str(i) + s2 + str(i) + s3l
        else:
            s = s + s1 + str(i) + s2 + str(i) + s3
    s = si + s + sl
    fh = open('data1.json', 'w')
    fh.write(s)
    fh.close()
userData(5,14000)