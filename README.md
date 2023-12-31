# Denetcdf Package

Ini merupakan paket python untuk simpan variabel 3 dimensi ke dalam format netcdf yang bisa dibaca Grads, R, python, matlab dll.

Instalasi: 
```ruby
pip install denetcdf
```

Cara Penggunaan:
```ruby
denetcdf.create('fileoutput.nc', lats, lons, 'Judul', 'datetime_initial', panjangdata, 'namavariabel','var','satuan', data)
```

## Contoh 1 variabel:

```ruby
from denetcdf import denetcdf
import netCDF4 as nc
import numpy as np
from wrf import to_np

fl = 'wrfout'
fh=nc.Dataset(fl[0])
lats=to_np(getvar(fh, "lat"))[:,0]
lons=to_np(getvar(fh, "lon"))[0,:]
fh.close()
fh=[nc.Dataset(i) for i in fl];print(len(fl))
pm_10=[to_np(fh[i]['PM10']) for i in range(len(fl))];pm_10=np.squeeze(np.array(pm_10))

denetcdf.create('test.nc', lats, lons, 'Inaaqm Output', '20230905000000', 73, 'Particulate Matter 10 (g/kg)','pm10','g/kg', pm_10[:,0,:,:])
```

## Contoh multi-variabel:

```ruby
from denetcdf import denetcdf
import netCDF4 as NC
import numpy as np
from wrf import to_np

fl = 'wrfout'
fh=nc.Dataset(fl[0])
lats=to_np(getvar(fh, "lat"))[:,0]
lons=to_np(getvar(fh, "lon"))[0,:]
fh.close()

fh=[nc.Dataset(i) for i in fl]
titles=[];vars=[];units=[];data=[]
titles.append('Particulate Matter 10 (g/kg)')
vars.append('pm10')
units.append('g/kg')
pm_10=[to_np(fh[i]['PM10']) for i in range(len(fl))];data.append(np.squeeze(np.array(pm_10))[:,0,:,:])
titles.append('Particulate Matter 2.5 (g/kg)')
vars.append('pm25')
units.append('g/kg')
pm_25=[to_np(fh[i]['PM2_5_DRY']) for i in range(len(fl))];data.append(np.squeeze(np.array(pm_10))[:,0,:,:])
titles.append('Sulfur dioxide (SO2) (ppm)')
vars.append('so2')
units.append('ppm')
pm_so=[to_np(fh[i]['so2']) for i in range(len(fl))];data.append(np.squeeze(np.array(pm_10))[:,0,:,:])
titles.append('Carbon monoxide (CO) (ppm)')
vars.append('co')
units.append('ppm')
pm_co=[to_np(fh[i]['co']) for i in range(len(fl))];data.append(np.squeeze(np.array(pm_10))[:,0,:,:])
data=np.array(data)

denetcdf.create('testm.nc', lats, lons, 'Inaaqm Output', '20230905000000', len(fl), titles,vars,units, data)
```

