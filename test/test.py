import denetcdf, glob
import netCDF4 as nc
import numpy as np
from wrf import to_np

fl = sorted(glob.glob('/home/satreps/.libraries/test/output/2023090400/wrfout*'))

fh=nc.Dataset(fl[0])
lats=to_np(getvar(fh, "lat"))[:,0]
lons=to_np(getvar(fh, "lon"))[0,:]
fh.close()
fh=[nc.Dataset(i) for i in fl];print(len(fl))
pm_10=[to_np(fh[i]['PM10']) for i in range(len(fl))];pm_10=np.squeeze(np.array(pm_10))
denetcdf.create('test.nc', lats, lons, 'Inaaqm Output', '20230905000000', 73, 'Particulate Matter 10 (g/kg)','pm10','g/kg', pm_10[:,0,:,:])

