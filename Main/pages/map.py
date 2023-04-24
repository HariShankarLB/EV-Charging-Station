import folium
import pandas as pd
m = folium.Map(location=[37.040539, -95.271387], zoom_start=5)

end=20000  #35000

df1=pd.read_csv("E:\\ev_station.csv",usecols=[5])
df2=pd.read_csv("E:\\ev_station.csv",usecols=[6])
df3=pd.read_csv("E:\\ev_station.csv",usecols=[2])
df4=pd.read_csv("E:\\ev_station.csv",usecols=[4])

x=[]
for data in df1:
    for d in df1[data]:
        x.append(d)    
        
y=[]
for data in df2:
    for d in df2[data]:
        y.append(d)    

z=[]
for data in df3:
    for d in df3[data]:
        z.append(d)    
        
zz=[]
for data in df4:
    for d in df4[data]:
        zz.append(d)    

a=0
k=0
for d in x:
    b=x[a],y[a]
    bb=zz[a],z[a]
    
    folium.CircleMarker(
        b,
        popup=bb,
        tooltip=bb,
        radius=2
    ).add_to(m)
    k=k+1
    if a==end:
        break
    a=a+1

m.save(r"C:\Users\srcas\Desktop\Project\Main\pages\map.html")
