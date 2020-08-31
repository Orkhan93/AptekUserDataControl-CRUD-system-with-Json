order=int(input("""=============================================
Aptek/User melumatlarini idare etme sistemi
=============================================
[1] duymesini secerek Yeni User profilinizi yarada bilersiniz 
[2] duymesini secerek Yeni Aptek profilinizi yarada bilersiniz 
[3] duymesini secerek Istifadeci Melumatlarini yenileye bilersiniz 
[4] duymesini secerek Aptek Melumatlarini yenileye bilersiniz
[5] duymesini secerek Istifadeci Melumatlarini sile bilersiniz
[6] duymesini secerek Aptek Melumatlarini sile bilersiniz
==============================================
Secim etdiyiniz duymeni daxil edin : """))
if order==1:
    from writeuser import *
elif order==2:
    from writeaptek import *
elif order==3:
    from updateuser import *
elif order==4:
    from updateaptek import *
elif order==5:
    from deleteuser import *
elif order==6:
    from deleteaptek import *
else:
    print("Duzgun secim edilmedi !")
