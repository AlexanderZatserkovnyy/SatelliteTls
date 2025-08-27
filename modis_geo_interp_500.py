import numpy as np

def modis_geo_interp_500(lalo):
    res = np.zeros(2*np.array(lalo.shape))
    nscan = lalo.shape[0]//10
    x = np.arange(res.shape[1])*0.5
    y = np.arange(20)*0.5 -0.25
    Y,X = np.meshgrid(y,x,indexing='ij')
    for sc in range(nscan):
        # Use bilinear interpolation for all 500 meter pixels
        j0 = 10*sc
        k0 = 20*sc
        interp = RegularGridInterpolator((np.arange(10),np.arange(lalo.shape[1])),lalo[j0:j0+10],bounds_error=False, fill_value=None)
        res[k0:k0+20] =  interp((Y,X))
        a = (res[k0+2]-res[k0+1])*2 #/(y[2]-y[1]) == 0.5
        b = res[k0+2] -a*y[2]
        res[k0] = a*y[0] + b
        a = (res[k0+18]-res[k0+17])*2 #/(y[18]-y[17])
        b = res[k0+18] -a*y[18]
        res[k0+19] = a*y[19] + b
    return res
