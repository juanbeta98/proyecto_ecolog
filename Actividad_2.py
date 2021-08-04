###### PresentaciÃ³n Ecolog ######

### Librerias 
import random as random
import networkx as nx
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from ipywidgets import interactive, interact
import ipywidgets as widgets

###### Conjuntos
## Productos
# Lista de productos

####### no mantequilla sino papa
productos = ['Arroz', 'Papa', 'Tomates', 'Camisas', 'Zapatos', 'Audifonos', 'Plancha']
#              0         1        2         3           4           5             6 

# Tipos de productos
tipos = ['Mercado', 'Ropa', 'Hogar']

# Productos discriminados por conjuntos
mercado = ['Arroz', 'Papa', 'Tomates']
ropa = ['Camisas', 'Zapatos']
hogar = ['Audifonos', 'Plancha']

##### Es carulla no tienda de barrio
# Lista de tiendas
tiendas = ['Exito', 'Falabella', 'Outlet las Americas', 'Ktronix', 'Carulla', 'Zara', 'Corabastos', 'San Andresito']
#            1          2                    3             4           5        6           7               8

# Tiendas discriminadas por tipos
tmercado = ['Exito', 'Carulla', 'Corabastos']
tropa = ['Exito', 'Falabella', 'Outlet las Americas', 'San Andresito', 'Zara']
thogar = ['Exito', 'Falabella', 'Ktronix']

# Dias
dias = list(range(1,32))

## Parámetros para graficas
# Color de las cajas en los boxplots
color = {'Exito': 'yellow', 'Falabella': 'green', 'Outlet las Americas': 'blue', 'Ktronix': 'red', 'Carulla': 'orange',
         'Corabastos': 'pink', 'Zara': 'black', 'San Andresito': 'grey'}

###### Parámetros
## Historial de precios
precios = {}
for dia in dias:
    # Arroz
    precios[('Arroz', 'Exito', dia)] = round(random.normalvariate(3500,250))
    precios[('Arroz', 'Corabastos', dia)] = round(random.normalvariate(2000,1000))
    precios[('Arroz', 'Carulla', dia)] = round(random.normalvariate(6000,250))
    
    precios[('Papa', 'Exito', dia)] = round(random.normalvariate(2500,800))
    precios[('Papa', 'Corabastos', dia)] = round(random.normalvariate(1000,1000))
    precios[('Papa', 'Carulla', dia)] = round(random.normalvariate(4000,800))
    
    precios[('Tomates', 'Exito', dia)] = round(random.normalvariate(1500,200))
    precios[('Tomates', 'Corabastos', dia)] = round(random.normalvariate(800,1000))
    precios[('Tomates', 'Carulla', dia)] = round(random.normalvariate(2500,200))
    
    precios[('Camisas', 'Exito', dia)] = round(random.normalvariate(40000,3000))
    precios[('Camisas', 'San Andresito', dia)] = round(random.normalvariate(30000,5000))
    precios[('Camisas', 'Zara', dia)] = round(random.normalvariate(75000,13000))
    precios[('Camisas', 'Falabella', dia)] = round(random.normalvariate(45000,3000))
    precios[('Camisas', 'Outlet las Americas', dia)] = round(random.normalvariate(30000,10000))
    
    precios[('Zapatos', 'Exito', dia)] = round(random.normalvariate(60000,5000))
    precios[('Zapatos', 'San Andresito', dia)] = round(random.normalvariate(50000,13000))
    precios[('Zapatos', 'Zara', dia)] = round(random.normalvariate(90000,6000))
    precios[('Zapatos', 'Falabella', dia)] = round(random.normalvariate(65000,5000))
    precios[('Zapatos', 'Outlet las Americas', dia)] = round(random.normalvariate(52000,15000))
    
    precios[('Audifonos', 'Exito', dia)] = round(random.normalvariate(40000, 200))
    precios[('Audifonos', 'Ktronix', dia)] = round(random.normalvariate(60000,200))
    precios[('Audifonos', 'Falabella', dia)] = round(random.normalvariate(50000,200))
    
    precios[('Plancha', 'Exito', dia)] = round(random.normalvariate(55000,200))
    precios[('Plancha', 'Ktronix', dia)] = round(random.normalvariate(39000,200))
    precios[('Plancha', 'Falabella', dia)] = round(random.normalvariate(70000,200))

# Diccionario de medias de precios
medias = {('Arroz', 'Exito'):3500, ('Arroz', 'Corabastos'):2000, ('Arroz', 'Carulla'):6000,
          ('Papa', 'Exito'):2500, ('Papa', 'Corabastos'): 1000, ('Papa', 'Carulla'):4000,
          ('Tomates', 'Exito'):1500,
          ('Tomates', 'Corabastos'):800,
          ('Tomates', 'Carulla'):2500,
    
          ('Camisas', 'Exito'):40000,
          ('Camisas', 'San Andresito'):30000,
          ('Camisas', 'Zara'):75000,
          ('Camisas', 'Falabella'):45000,
          ('Camisas', 'Outlet las Americas'):30000,
    
          ('Zapatos', 'Exito'):60000,
          ('Zapatos', 'San Andresito'):50000,
          ('Zapatos', 'Zara'):90000,
          ('Zapatos', 'Falabella'):65000,
          ('Zapatos', 'Outlet las Americas'):52000,
        
          ('Audifonos', 'Exito'):40000, 
          ('Audifonos', 'Ktronix'):60000,
          ('Audifonos', 'Falabella'):50000,
        
          ('Plancha', 'Exito'):55000,
          ('Plancha', 'Ktronix'):39000,
          ('Plancha', 'Falabella'):70000
        }                                                 

## Distancias Euclideanas
# Coordenadas

coor = {'Hogar':(20, 9), 'Exito': (7, 15), 'Falabella': (17,15), 'Outlet las Americas':(31,13), 
         'Ktronix':(23,7), 'Carulla':(23,11), 'Zara':(17,9), 'Corabastos':(33,19), 'San Andresito':(10,6) }


# Distancias
distancias = {}
for tienda in tiendas:
    for tienda2 in tiendas:
        distancias[(tienda,tienda2)] = ((coor[tienda][0] - coor[tienda2][0])**2 + \
                                        (coor[tienda][1] - coor[tienda2][1])**2)**(1/2)
    
    distancias[('Hogar', tienda)] = ((coor[tienda][0] - coor['Hogar'][0])**2 + \
                                        (coor[tienda][1] - coor['Hogar'][1])**2)**(1/2)

    distancias[(tienda, 'Hogar')] = distancias[('Hogar', tienda)]

###### Funciones
### Función retornando listado de tiendas en las cuales se ofrece un dado producto cumpliendo  
### con una distancia máxima
def retorno_tiendas(producto, distancia):
    tien = []
    if producto in mercado:
        for i in tmercado:
            if distancias['Hogar', i] <= distancia:
                tien.append(i)
        return(tien)
    elif producto in ropa:
        for i in tropa:
            if distancias['Hogar', i] <= distancia:
                tien.append(i)
        return(tien)
    elif producto in hogar:
        for i in thogar:
            if distancias['Hogar', i] <= distancia:
                tien.append(i)
        return(tien)

### Función que guarda los valores de los Dropdowns referentes a la selección de tiendas
# Diccionario de decisiones
decision = {}
tiendas_sel = ['Exito']
tiendas_sele = {'Exito'}

# Inicialización
for i in productos:
    decision[i] = 'Exito'

## Funciones individuales
def func_Arz(Arroz):
    decision['Arroz'] = Arroz
    tiendas_sele.add(Arroz)

def func_Mtq(Mantequilla):
    decision['Papa'] = Mantequilla
    tiendas_sele.add(Mantequilla)

def func_Tte(Tomate):
    decision['Tomates'] = Tomate
    tiendas_sele.add(Tomate)

def func_Cam(Camisas):
    decision['Camisas'] = Camisas
    tiendas_sele.add(Camisas)

def func_Zap(Zapatos):
    decision['Zapatos'] = Zapatos
    tiendas_sele.add(Zapatos)
    
    
def func_Aud(Audifonos):
    decision['Audifonos'] = Audifonos
    tiendas_sele.add(Audifonos)
    
def func_Pla(Plancha):
    decision['Plancha'] = Plancha
    tiendas_sele.add(Plancha)

### Funcíon que grafica las tiendas que ha seleccionado la persona
diccion = {'Hogar': 'H','Exito':'E', 'Falabella':'F', 'Outlet las Americas':'OA', 'Ktronix':'K', 'Carulla':'CA', 
           'Zara': 'Z', 'Corabastos': 'CO', 'San Andresito': 'SA'}
           
def grafica_tiendas(Graficar):
    if Graficar == True or Graficar == False:
        diccioprov = {'Hogar':'H'}
        s = set(['Hogar'])
        for i in productos:
            s.add(decision[i])
            diccioprov[decision[i]] = diccion[decision[i]]
        
        tiendas_sel.clear()
        tiendas_sel.extend(list(s))
        tiendas_sel.remove('Hogar')
        G = nx.Graph()
        G.add_nodes_from(s)
        options = {
                "font_size": 10,
                "node_size": 300,
                "labels": diccioprov,
                "node_color": "white",
                "edgecolors": "black",
                "width": 1,
            }
        fig, ax = plt.subplots()    
        nx.draw_networkx(G, coor, **options)
        ax = plt.gca()
        ax.margins(0.20)
        plt.axis('on')
        ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
        plt.xlabel('Longitud') 
        plt.ylabel('Latitud')
        plt.title('Almacenes seleccionados') 
        plt.show()

### Funciones que construye la ruta seleccionada por el usuario
ruta = {1:'Hogar'}
def constr_ruta_1(primero):
    ruta[2] = primero

def constr_ruta_2(segundo):
    ruta[3] = segundo

def constr_ruta_3(tercero):
    ruta[4] = tercero

def constr_ruta_4(cuarto):
    ruta[5] = cuarto

def constr_ruta_5(quinto):
    ruta[6] = quinto

def constr_ruta_6(sexto):
    ruta[7] = sexto

def constr_ruta_7(septimo):
    ruta[8] = septimo

def constr_ruta_8(octavo):
    ruta[9] = octavo

### Función auxiliar que construye ruta 
def constructor():
    
    ruta1 = []
    for i in list(range(1,len(tiendas_sel)+1)):
        ruta1.append((ruta[i], ruta[i+1]))
    ruta1.append((ruta[len(tiendas_sel)+1], 'Hogar'))
    return(ruta1)
  

### Funcion que grafica la ruta deseada

def graficar_rutas(Graficar):   
    if Graficar == True or Graficar == False:
        ruta2 = constructor()
        diccioprov = {'Hogar':'H'}
        for i in productos:
            diccioprov[decision[i]] = diccion[decision[i]]
        G2 = nx.DiGraph(ruta2)
        options = {
            "font_size": 10,
            "node_size": 300,
            "labels": diccioprov,
            "node_color": "white",
            "edgecolors": "black",
            "linewidths": 1,
            "width": 1,
        }
        fig, ax = plt.subplots()
        nx.draw_networkx(G2, coor, **options)
        # Set margins for the axes so that nodes aren't clipped
        ax = plt.gca()
        ax.margins(0.20)
        plt.axis('on')
        ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
        plt.xlabel('Longitud') 
        plt.ylabel('Latitud')
        plt.title('Ruta Elegida') 
        plt.show()

### Funcion que grafica series de tiempo e intervalos de confianza
def seleccion():
    
    Arz_list = interactive(func_Arz, Arroz = tmercado)
    Mtq_list = interactive(func_Mtq, Mantequilla = tmercado)
    Tte_list = interactive(func_Tte, Tomate = tmercado)
    Cam_list = interactive(func_Cam, Camisas = tropa)
    Zap_list = interactive(func_Zap, Zapatos = tropa)
    Aud_list = interactive(func_Aud, Audifonos = thogar)
    Pla_list = interactive(func_Pla, Plancha = thogar)
    
    return (Arz_list, Mtq_list,Tte_list, Cam_list, Zap_list, Aud_list, Pla_list)

### Función para escoger la ruta
elecciones = []
def elegir_orden():
    # for i in list(range(2,len(ruta))):
    #     ruta.pop(i)
    elecciones.clear()
    primerol = interactive(constr_ruta_1, primero = tiendas_sel)
    elecciones.append(primerol)
    if len(tiendas_sel) >= 2:
        segundol = interactive(constr_ruta_2, segundo = tiendas_sel)
        elecciones.append(segundol)
    if len(tiendas_sel) >= 3:
        tercerol = interactive(constr_ruta_3, tercero = tiendas_sel)
        elecciones.append(tercerol)
    if len(tiendas_sel) >= 4:
        cuartol = interactive(constr_ruta_4, cuarto = tiendas_sel)
        elecciones.append(cuartol)
    if len(tiendas_sel) >= 5:
        quintol = interactive(constr_ruta_5, quinto = tiendas_sel)
        elecciones.append(quintol)
    if len(tiendas_sel) >= 6:
        sextol = interactive(constr_ruta_6, sexto = tiendas_sel)
        elecciones.append(sextol)
    if len(tiendas_sel) >= 7:
        septimol = interactive(constr_ruta_7, septimo = tiendas_sel)
        elecciones.append(septimol)
    if len(tiendas_sel) >= 8:
        octavol = interactive(constr_ruta_8, octavo = tiendas_sel)
        elecciones.append(octavol)
    
def calcula_costos():
    
    costo_compra = 0
    costo_transporte = 0
    
    for prod in productos:
        costo_compra += medias[(prod,decision[prod])]
    
    rutaa = []
    if len(tiendas_sel) > 1:
        for i in list(range(1,len(tiendas_sel)+1)):
            rutaa.append((ruta[i], ruta[i+1]))
        rutaa.append((ruta[len(tiendas_sel)+1], 'Hogar'))
    else:
        rutaa.append(('Hogar', tiendas_sel[0]))
        rutaa.append((tiendas_sel[0], 'Hogar'))


    
    for i in rutaa:
        costo_transporte += distancias[i] * 675.6
    
    costo_total = costo_compra + costo_transporte
    
    print(f'El costo de la compra es: $ {str(round(costo_compra,2))}')
    print(f'El costo de la ruta es: $ {str(round(costo_transporte,2))}')
    print(f'El costo total es: $ {str(round(costo_total,2))}')
    
    return(costo_compra, costo_transporte, costo_total)



