# croting: utf-8
# Credits: github.con/hekelpro

"""
JOIN US:
t.me/tempatconfig
t.me/bebas_berinternet

"""




import requests
import json,string,random,sys,os,re,time,base64
os.system("clear")

daftar_email = [
 "@bestlistbase.com",
 "@besttempmail.com",
 "@meantince.com",
 "@powerency.com",
 "@truthfinderlogin.com",
 "@chasefreedomactive.com",
 "@wellsfargocomcardholders.com"
               ]
class kang:
 def ngewe():
  garis = 25*"="
  print(f"""╔╦╗╔═╗╔╦╗╔═╗   ╔╦╗╔═╗╦╦
 ║ ║╣ ║║║╠═╝───║║║╠═╣║║
 ╩ ╚═╝╩ ╩╩     ╩ ╩╩ ╩╩╩═╝
{garis}
00) EXIT
01) SET EMAIL RANDOM
02) SET EMAIL CUSTOM
03) ABOUT TOOLS
{garis}
""")
  inp = input("?) PILIH > ")
  while inp == "":
   inp = input("?) PILIH > ")
  if inp in ("00","0"):
   exit()
  elif inp in ("01","1"):
   ee("".join(random.choice(string.ascii_letters)
   for x in range(10)), random.choice(daftar_email))
  elif inp in ("02","2"):
   cus(garis)
  elif inp in ("03","3"):
   os.system("clear")
   tentang(garis)
  else:
   exit(f"ERROR: {inp} TIDAK ADA DI DAFTAR MENU")
def cus(garis):
 os.system("clear")
 print(f"""╔╦╗╔═╗╔╦╗╔═╗   ╔╦╗╔═╗╦╦
 ║ ║╣ ║║║╠═╝───║║║╠═╣║║
 ╩ ╚═╝╩ ╩╩     ╩ ╩╩ ╩╩╩═╝""")
 print(garis)
 for daftar in range(len(daftar_email)):
  print(f"{str(daftar+1)}) {daftar_email[daftar]}")
 print(garis)
 dom = input("INPUT MAIL DOMAIN > ")
 while dom == "":
  print("JANGAN KOSONG GBLK")
  dom = input("INPUT MAIL DOMAIN > ")
 nama = input("INPUT NAME MAIL > ")
 while nama == "":
  print("JANGAN KOSONG GBLK")
  nama = input("INPUT NAME MAIL")
 try:
  domm = daftar_email[int(dom)-1]
 except Exception as er:
  print(f"ERROR: {str(er)}")
 ee(nama, domm)
def ee(nama,email):
 garis = 25*"="
 namaa = nama.lower()
 registrasi = requests.get("https://www.temporary-mail.net/change")
 agent = open("ua.txt","r").read()
 agen = random.choice(agent.split("\n"))
 duit = re.search("__cfduid=(.*?)\sfor", str(registrasi.cookies)).group(1)
 tempe = re.search("tempmail=(.*?)\sfor", str(registrasi.cookies)).group(1)
 tete = "&_ts={}".format(int(time.time()))
 head = {
         "X-Requested-With":"XMLHttpRequest",
         "User-Agent":"Mozilla/5.0 (Linux; Android 9; vivo 1904 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36"
        }
 kon = requests.get(f"https://www.temporary-mail.net/api/v1/mailbox/keepalive?force_change=1&mailbox={namaa}{tete}",data={"mailhost":email},headers=head,cookies={"__cfduid":duit,"tempmail":tempe}).text
 print(garis)
 print(f"EMAIL KAMU: {namaa}{email}")
 print(f"CANCEL    : CTRL + C")
 print("Menunggu Pesan Masuk...")
 while True:
  try:
   check = requests.get(f"https://www.temporary-mail.net/api/v1/mailbox/{namaa}").text
   if "[]" in check:
    continue
   elif "mailbox" in check:
    ah = json.loads(check)
    print("==========[ PESAN BARU MASUK ]==========")
    for kyah in ah:
     daftar = kyah["id"]
    try:
     mek = requests.get(f"https://www.temporary-mail.net/api/v1/mailbox/{namaa}/{daftar}").text
     mak = json.loads(mek)
     dari = mak["from"]
     dar = re.search('"(.*?)"', dari).group(1)
     dari_siapa = re.search("<(.*?)>", dari).group(1)
     tanggal = mak["date"]
     sub = mak["subject"]
     pes = mak["body"]["text"].replace("\n","")
     print(f"DI KIRIM OLEH : {dar}")
     print(f"EMAIL PENGIRIM: {dari_siapa}")
     print(f"SUBJEK        : {sub}")
     print(f"DIKIRIM PADA  : {tanggal}")
     print(f"PESAN         : {pes}")
     for f in mak["attachments"]:
      if re.search("image/(\w+)", f["content-type"]).group(1) in f["content-type"]:
       print(f"FILE DIKIRIM   : {file['filename']}")
       crot = requests.get(f["view-link"]).content
       crit = base64.b64encode(crot)
       crat = requests.post("https://api.imgbb.com/1/upload?15552000&key=7a787a0e3e96926f2f75569bb77f6a3b", data={"image":crit}).text
       j = json.loads(crat)
       print(f"      {j['data']['medium']['url']}")
      else:
       continue
     print(garis)
     requests.delete(f"https://www.temporary-mail.net/api/v1/mailbox/{namaa}/{daftar}")
     continue
    except:
     continue
   else:
    continue
  except KeyboardInterrupt:
   exit("KeyboardInterrupt, Berhasil Keluar")

def tentang(garis):
 print(garis)
 print("AUTHOR : Kgyya")
 print("GITHUB : github.com/Kgyya")
 print("CREDITS: RizkyID aka github.com/hekelpro")
 print(garis)
 print("KETIK APA SAJA UNTUK KEMBALI")
 print(garis)
 input("? > ")
 os.system("python " + sys.argv[0])

if __name__=="__main__":
 os.system("clear")
 kang.ngewe()
