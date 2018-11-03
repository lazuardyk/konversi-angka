def satuan(x):
  if x == 0:
    return 'nol'
  if x == 1:
    return 'satu'
  if x == 2:
    return 'dua'
  if x == 3:
    return 'tiga'
  if x == 4:
    return 'empat'
  if x == 5:
    return 'lima'
  if x == 6:
    return 'enam'
  if x == 7:
    return 'tujuh'
  if x == 8:
    return 'delapan'
  if x == 9:
    return 'sembilan'
  else:
    return 'bukan satuan'

def puluhan(x):
  p = x // 10
  s = x % 10
  if x == 11:
    return 'sebelas'
  elif x == 10:
    return 'sepuluh'
  elif x < 10:
    return satuan(x)
  elif p == 1:
    return satuan(s) + ' belas'
  elif s == 0:
    return satuan(p) + ' puluh'
  else:
    return satuan(p) + ' puluh ' + satuan(s)

def ratusan(x):
  r = x // 100
  p = x % 100
  if x == 100:
    return 'seratus'
  elif 100 < x < 200:
    return 'seratus ' + puluhan(p)
  elif x < 100:
    return puluhan(x)
  elif p == 0:
    return satuan(r) + ' ratus'
  else:
    return satuan(r) + ' ratus ' + puluhan(p)

def ribuan(x):
  r = x // 1000
  ra = x % 1000
  if x == 1000:
    return 'seribu'
  elif 1000 < x < 2000:
    return 'seribu ' + ratusan(ra)
  elif x < 1000:
    return ratusan(x)
  elif ra == 0:
    return satuan(r) + ' ribu'
  else:
    return satuan(r) + ' ribu ' + ratusan(ra)

def puluhanribu(x):
  p = x // 10000
  y = x // 1000
  ra = x % 1000
  if x == 10000:
    return 'sepuluh ribu'
  elif x < 10000:
    return ribuan(x)
  elif ra == 0:
    if x // 10000 == 0:
      return satuan(p) + ' puluh ribu'
    else:
      return puluhan(y) + ' ribu'
  else:
    return puluhan(y) + ' ribu ' + ratusan(ra) 

def ratusanribu(x):
  r = x // 100000
  p = x % 100000
  if x == 100000:
    return 'seratus ribu'
  elif 100000 < x < 200000:
    return 'seratus ' + puluhanribu(p)
  elif x < 100000:
    return puluhanribu(x)
  elif p == 0:
    return satuan(r) + ' ratus ribu'
  else:
    return satuan(r) + ' ratus ' + puluhanribu(p)

def jutaan(x):
  j = x // 1000000
  r = x % 1000000
  if x < 1000000:
    return ratusanribu(x)
  elif r == 0:
    return satuan(j) + ' juta'
  else:
    return satuan(j) + ' juta ' + ratusanribu(r)

def puluhanjuta(x):
  p = x // 10000000
  y = x // 1000000
  r = x % 1000000
  if x == 10000000:
    return 'sepuluh juta'
  elif x < 10000000:
    return jutaan(x)
  elif r == 0:
    if x // 10000000 == 0:
      return satuan(p) + ' puluh juta'
    else:
      return puluhan(y) + ' juta'
  else:
    return puluhan(y) + ' juta ' + jutaan(r)

def ratusanjuta(x):
  r = x // 1000000
  ra = x % 1000000
  if x == 100000000:
    return 'seratus juta'
  elif x < 100000000:
    return puluhanjuta(x)
  elif ra == 0:
    return ratusan(r) + ' juta'
  else:
    return ratusan(r) + ' juta ' + ratusanribu(ra)

def milyar(x):
	m = x // 1000000000
	r = x % 1000000000
	if x < 1000000000:
		return ratusanjuta(x)
	elif r == 0:
		return satuan(m) + ' milyar'
	else:
		return satuan(m) + ' milyar ' + ratusanjuta(r)

def puluhanmilyar(x):
  p = x // 10000000000
  y = x // 1000000000
  r = x % 1000000000
  if x == 10000000000:
    return 'sepuluh milyar'
  elif x < 10000000000:
    return milyar(x)
  elif r == 0:
    if x // 10000000000 == 0:
      return satuan(p) + ' puluh milyar'
    else:
      return puluhan(y) + ' milyar'
  else:
    return puluhan(y) + ' milyar ' + ratusanjuta(r)

def ratusanmilyar(x):
  r = x // 1000000000
  ra = x % 1000000000
  if x == 100000000000:
    return 'seratus milyar'
  elif x < 100000000000:
    return puluhanmilyar(x)
  elif ra == 0:
    return ratusan(r) + ' milyar'
  else:
    return ratusan(r) + ' milyar ' + ratusanjuta(ra)

Message = "PROGRAM MENGUBAH ANGKA MENJADI TULISAN"
Message3 = "by LazuardyK"
Message2 = "#" * 50
print('{:^80}'.format(Message2))
print('{:^80}'.format(Message))
print('{:^80}'.format(Message3))
print('{:^80}'.format(Message2))
try:
    laz = int(input("\nMasukkan angka yang ingin dirubah:\n"))
    print(ratusanmilyar(laz))
except:
    print("Masukkan angka yang benar! <= 9999999999")
