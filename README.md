# EDA de precios y prestaciones de smartphones 

Fecha: 12/12/2026 

## Introducción 

Con este EDA se trata de determinar las características más habituales de los teléfonos inteligentes y los factores que más influyen en su precio, en base a un dataset que incluye precios, valoraciones y datos técnicos de teléfonos de varias marcas.

## Datos 

Se utiliza un dataset procedente de la siguiente url: 
https://www.kaggle.com/datasets/agarwalyashhh/smartphones-complete-data/data
Resumen del dataset (extraído de https://www.kaggle.com/code/msjahid/smartphone-insights-exploratory-data-analysis): 
1.	Brand Name: The name of the smartphone brand.
2.	Model: The model name of the smartphone.
3.	Price: The price of the smartphone.
4.	Rating: The rating of the smartphone, typically based on user reviews or expert evaluations.
5.	Has 5G: Indicates whether the smartphone has 5G connectivity capability.
6.	Has NFC: Indicates whether the smartphone has Near Field Communication (NFC) technology.
7.	Has IR Blaster: Indicates whether the smartphone has an Infrared (IR) blaster for remote control functionality.
8.	Processor Brand: The brand of the processor used in the smartphone.
9.	Num Cores: The number of cores in the smartphone processor.
10.	Processor Speed: The speed of the smartphone processor.
11.	Battery Capacity: The capacity of the smartphone battery, usually measured in milliampere-hours (mAh).
12.	Fast Charging Available: Indicates whether the smartphone supports fast charging technology.
13.	Fast Charging: Details about the fast charging capability, such as the type of fast charging technology.
14.	RAM Capacity: The amount of Random Access Memory (RAM) in the smartphone, usually measured in gigabytes (GB).
15.	Internal Memory: The internal storage capacity of the smartphone, usually measured in gigabytes (GB) or terabytes (TB).
16.	Screen Size: The size of the smartphone screen, typically measured diagonally in inches.

Además del dataset indicado, se ha utilizado otro ubicado en la siguiente dirección: 
https://www.kaggle.com/datasets/sumanbera19/phone-price-dataset/data 
Este segundo dataset tiene mejor valoración de usabilidad en Kaggle que el anterior. Por otra parte, no está tan bien preparado para el análisis como el primero, ya que algunas de sus columnas contienen frases con más de un dato que sería necesario parsear. Por eso, el EDA se ha hecho con el primer dataset, y el segundo se ha utilizado únicamente para comparar algunos de los datos del primero. Con esta comparación, hecha en la hoja comp del Excel ./src/xls/ smartphones.xls, se ha comprobado que en los modelos de móviles incluidos en ambos datasets, los datos técnicos comparados son iguales en ambos datasets, y los precios muy similares. 

Tanto este dataset como el anterior son del año 2023, y los datos de ambos son de la India. 

Se resume a continuación el perfil central de los modelos de este dataset. Los datos numéricos son rangos intercuartílicos. 
-	Marcas con más modelos: Xiaomi, Samsung, Vivo y Realme. 
-	RAM: 4-8 GB. 
-	Memoria interna: 64–128 GB. 
-	Procesador: 2.05–2.84 GHz y normalmente 8 núcleos. 
-	Batería: 4500–5000 mAh. 
-	Resolución de cámara trasera principal: 24–64 MP. 
-	Precio: 144–394 €. 

## Métodos de análisis 

Como herramienta principal del análisis se ha usado Python (principalmente Pandas). También se ha usado Excel para chequeo, filtrado y graficado (ver Excel ./src/xls/ smartphones.xls). 

Para los análisis univariante se han empleado histogramas, box-plots y gráficos de barras. También se han segmentado los modelos en distintos rangos de precio. 

Los análisis multivariante se han hecho en base a cálculo de matrices de correlación entre variables, ANOVAs, test de Tukey para comparativa entre marcas y graficado (principalmente gráficos de dispersión). 

## Resultados 

- Se observa correlación entre varias características técnicas y el precio de los móviles, siendo estas las características en las que se observa una correlación más clara con el precio: ram_capacity, processor_speed, internal_memory, has_nfc y has_5g.
- Se observan indicios de que hay un factor marca que también influye en el precio, pero se requiere un análisis más detallado para confirmarlo.
- Se observan indicios de que la relación calidad-precio tiende a disminuir en gamas de precio más altas, pero se requiere un análisis más detallado para confirmarlo. 

## Próximos pasos 

- Ajustar modelo de ML para predecir precios y rating de los smartphones. 
- Hacer un análisis de mercado. 
- Estudiar la evolución a lo largo del tiempo de las características técnicas y precios de los móviles. 
- Incluir datos de otras regiones en el estudio. 

