print(" dim blok ballarin hesablanmasi")
print(" riyaziyyat balinin hesablanmasi") 
dogru_cavab = input(" duzgun cavablarin sayini daxil edin:")
sehf_cavab = input("sehf cavablarin sayini daxil edin:")
netice_ri= (float(dogru_cavab)-float(sehf_cavab)*100/33)
print(" netice:{0} ".format(netice_ri))
if netice_ri< 0:
  print(" riyaziyyat uzre neticeniz 0-a beraberdir")
else:
  print("imtahandan kecdiz")

print("fizika balinin hesablanmasi")
dogru_cavab = input("fizika uzre dogru cavablarin sayini daxil edin:")
sehf_cavab = input("fizika uzre sehf cavablarin sayini daxil edin:")
netice_fiz = (float(dogru_cavab)-float(sehf_cavab)*100/33)
print("netice:{0}".format(netice_fiz))
if netice_fiz< 0:
  print("fizika uzre neticeniz 0-a beraberdir")
else:
  print("imtahani kecdiz")

print("kimya uzre balin hesablanmasi")
dogru_cavab = input("kimya uzre dogru cavablarin sayini daxil edin:")
sehf_cavab = input("kimya uzre sehf cavablarin sayini daxil edin:")
netice_kim = (float(dogru_cavab)-float(sehf_cavab)*100/33)
print("netice:{0}".format(netice_kim))
if netice_kim< 0:
  print("imtahan neticeniz 0-a beraberdir")


umumi_netice = netice_kim + netice_fiz + netice_ri
print(umumi_netice)
print("yuxarida qeyd edilen reqem sizin blok neticenizdir")
  
