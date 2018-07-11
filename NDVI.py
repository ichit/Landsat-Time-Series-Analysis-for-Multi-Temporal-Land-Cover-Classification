
# coding: utf-8

# In[ ]:


def NDVI(ndvi_input_band4, ndvi_input_band5, ndvi_path, c):
    from osgeo import gdal, gdal_array

    file1 = gdal.Open(str(ndvi_input_band4))
    file2 = gdal.Open(str(ndvi_input_band5))


    file1 = file1.ReadAsArray()
    file2 = file2.ReadAsArray()

    a, b = file1.shape
    a,b


# In[56]:


import numpy as np

final_arr = np.zeros((a, b))
# print(final_arr)
# print(final_arr)
for i in range(a):
    for j in range(b):
        final_arr[i][j] = (file2[i][j] - file1[i][j])*100/(file1[i][j] + file2[i][j])#-100 to +100




# In[58]:


inRaster = str(ndvi_input_band5)
inDS=gdal.Open(inRaster,1)
geoTransform = inDS.GetGeoTransform()
band=inDS.GetRasterBand(1)
datatype=band.DataType
proj = inDS.GetProjection()


# In[59]:


outRaster = str(ndvi_path + "\NDVI"+ c + ".tif")
driver=inDS.GetDriver()
outDS = driver.Create(outRaster, b,a, 1,datatype)
geoTransform = inDS.GetGeoTransform()


# In[60]:


outDS.SetGeoTransform(geoTransform)
proj = inDS.GetProjection()
outDS.SetProjection(proj)
outBand = outDS.GetRasterBand(1)
outBand.WriteArray(final_arr,0,0)
#data is the output array to written in tiff file
outDS=None

