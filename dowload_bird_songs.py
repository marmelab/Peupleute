from xenocanto import download
import asyncio

scientificNames = ["Parus major","Cyanistes caeruleus","Lophophanes cristatus","Turdus merula","Passer domesticus", "Pica pica","Streptopelia decaocto","Corvus corone","Columba palumbus","Sturnus vulgaris","Periparus ater","Dendrocopos major","Picus viridis","Passer montanus"]

for name in scientificNames:
    asyncio.run(download([name, 'q:A', 'cnt:France', 'len:5-20']))
