import pyodbc

server = '192.168.50.53'
database = 'QLHV'
conn = pyodbc.connect(
'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes;')
cursor = conn.cursor()

print('Connected!')
#chương trình select/view dữ liệu từ table hoc_vien
hoc_vien_result = cursor.execute('SELECT * FROM HOC_VIEN')
ds_hv = hoc_vien_result.fetchall()
print(ds_hv)

#chương trình insert/thêm dữ liệu vào table hoc_vien
i = "INSERT INTO HOC_VIEN(MA_HOC_VIEN, TEN_HOC_VIEN, SO_DIEN_THOAI, MON_HOC, HOC_PHI)" \
    "VALUES('{0}','{1}','{2}','{3}','{4}')".format(input(),input(),input(),input(),input())
cursor.execute(i)
cursor.commit()
print('Inserted!')
