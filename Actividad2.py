######## Presentacion Ecolog ########

### Librerias ###
import random as random
import networkx as nx
import matplotlib.pyplot as plt

### Conjuntos ###
## Productos
productos = ['Arroz', 'Papa', 'Tomates', 'Camisas', 'Zapatos', 'Air Fryer', 'Licuadora']
              # 0				1					2					3						4						5							6					
tipos = ['Mercado', 'Ropa', 'Hogar']
# Discriminado
mercado = ['Arroz', 'Papa', 'Tomates']
ropa = ['Camisas', 'Zapatos']
hogar = ['Air Fryer', 'Licuadora']

## Tiendas
tiendas = ['Exito', 'Falabella', 'Outlet las Americas', 'Ktronix', 'Carulla', 'Zara', 'Corabastos', 'San Andresito']
 						# 1					 2								3									4						5				6						7							8
# Discriminado
tmercado = ['Exito', 'Carulla', 'Corabastos']
tropa = ['Exito', 'Falabella', 'Outlet las Americas', 'San Andresito', 'Zara']
thogar = ['Exito', 'Falabella', 'Ktronix']

# Dias
dias = list(range(1,32))

### Parametros ###
## Historial de precios
precios = {}
for dia in dias:
    # Arroz
    precios[('Arroz', 'Exito', dia)] = round(random.normalvariate(3500,250))
    precios[('Arroz', 'Corabastos', dia)] = round(random.normalvariate(2000,1000))
    precios[('Arroz', 'Carulla', dia)] = round(random.normalvariate(6000,250))
    
		# Papa
    precios[('Papa', 'Exito', dia)] = round(random.normalvariate(2500,800))
    precios[('Papa', 'Corabastos', dia)] = round(random.normalvariate(1000,1000))
    precios[('Papa', 'Carulla', dia)] = round(random.normalvariate(4000,800))
    
		# Tomates
    precios[('Tomates', 'Exito', dia)] = round(random.normalvariate(1500,200))
    precios[('Tomates', 'Corabastos', dia)] = round(random.normalvariate(800,1000))
    precios[('Tomates', 'Carulla', dia)] = round(random.normalvariate(2500,200))
    
		# Camisas
    precios[('Camisas', 'Exito', dia)] = round(random.normalvariate(40000,3000))
    precios[('Camisas', 'San Andresito', dia)] = round(random.normalvariate(30000,5000))
    precios[('Camisas', 'Zara', dia)] = round(random.normalvariate(75000,13000))
    precios[('Camisas', 'Falabella', dia)] = round(random.normalvariate(45000,3000))
    precios[('Camisas', 'Outlet las Americas', dia)] = round(random.normalvariate(30000,10000))
    
		# Zapatos
    precios[('Zapatos', 'Exito', dia)] = round(random.normalvariate(70000,5000))
    precios[('Zapatos', 'San Andresito', dia)] = round(random.normalvariate(60000,13000))
    precios[('Zapatos', 'Zara', dia)] = round(random.normalvariate(100000,6000))
    precios[('Zapatos', 'Falabella', dia)] = round(random.normalvariate(75000,5000))
    precios[('Zapatos', 'Outlet las Americas', dia)] = round(random.normalvariate(60000,20000))
    
		# Air Fryer
    precios[('Air Fryer', 'Exito', dia)] = round(random.normalvariate(250000, 200))
    precios[('Air Fryer', 'Ktronix', dia)] = round(random.normalvariate(300000,200))
    precios[('Air Fryer', 'Falabella', dia)] = round(random.normalvariate(275000,200))
    
		# Licuadora
    precios[('Licuadora', 'Exito', dia)] = round(random.normalvariate(100000,200))
    precios[('Licuadora', 'Ktronix', dia)] = round(random.normalvariate(200000,200))
    precios[('Licuadora', 'Falabella', dia)] = round(random.normalvariate(130000,200))
	
## Distancias Euclideanas
# Coordenadas
coor = {}
coor['Casa'] = (20,9)
coor['Exito'] = (7,15)
coor['Falabella'] = (17,13)
coor['Outlet las Americas'] = (31,13)
coor['Ktronix'] = (22,8)
coor['Carulla'] = (23,11)
coor['Zara'] = (17,9)
coor['Corabastos'] = (35, 19)
coor['San Andresito'] = (4,3)

# Distancias
distancias = {}
for tienda in tiendas:
	  distancias[('Casa', tienda)] = ((coor[tienda][0] - coor['Casa'][0])**2 + \
                                        (coor[tienda][1] - coor['Casa'][1])**2)**(1/2)
    distancias[(tienda, 'Casa')] = distancias[('Casa', tienda)]
    for tienda2 in tiendas:
        distancias[(tienda,tienda2)] = ((coor[tienda][0] - coor[tienda2][0])**2 + \
                                        (coor[tienda][1] - coor[tienda2][1])**2)**(1/2)

## Graficos				
# Color de las cajas en los boxplots
color = {'Exito': 'yellow', 'Falabella': 'green', 'Outlet las Americas': 'blue', 'Ktronix': 'red', 'Carulla': 'orange',
         'Corabastos': 'pink', 'Zara': 'black', 'San Andresito': 'grey'}
# Etiquetas de los graricos
diccion = {'Casa': 'H','Exito':'E', 'Falabella':'F', 'Outlet las Americas':'OA', 'Ktronix':'K', 'Carulla':'Car', 
           'Zara': 'Z', 'Corabastos': 'Cor', 'San Andresito': 'SA'}
				
### Funciones ###
## Función retorna listado de tiendas en las cuales se ofrece un dado producto cumpliendo con una distancia máxima
def retorno_tiendas(producto, distancia):
    tien = []
    if producto in mercado:
        for i in tmercado:
            if distancias['Casa', i] <= distancia:
                tien.append(i)
    elif producto in ropa:
        for i in tropa:
            if distancias['Casa', i] <= distancia:
                tien.append(i)
    elif producto in hogar:
        for i in thogar:
            if distancias['Casa', i] <= distancia:
                tien.append(i)
    return(tien)

## Función que guarda los valores de los Dropdowns referentes a la selección de tiendas
# Diccionario de decisiones
decision = {}
tiendas_sel = ['Exito']
# Inicialización
for i in productos:
    decision[i] = 'Exito'

## Funciones individuales
def func_Arz(Arroz):
    decision['Arroz'] = Arroz
def func_Mtq(Mantequilla):
    decision['Papa'] = Mantequilla
def func_Tte(Tomate):
    decision['Tomates'] = Tomate
def func_Cam(Camisas):
    decision['Camisas'] = Camisas
def func_Zap(Zapatos):
    decision['Zapatos'] = Zapatos
def func_Air(Air_Fryer):
    decision['Air Fryer'] = Air_Fryer
def func_Lic(Licuadora):
    decision['Licuadora'] = Licuadora

## Funcion que grafica las tiendas que ha seleccionado el usuario
def grafica_tiendas(Listo):
    if Listo == True:
        s = set(['Casa'])
        for i in productos:
            s.add(decision[i])
        
        tiendas_sel.clear()
        tiendas_sel.extend(list(s))
        tiendas_sel.remove('Casa')
        G = nx.Graph()
        G.add_nodes_from(s)
        options = {
                "font_size": 10,
                "node_size": 250,
                "labels": diccion,
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

## Funciones que construye la ruta seleccionada por el usuario
ruta = {1:'Casa'}
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

def constructor():
    ruta1 = []
    for i in range(1,len(ruta)):
        ruta1.append((ruta[i], ruta[i+1]))
    ruta1.append((ruta[len(ruta)], 'Casa'))
    return(ruta1)
  
## Funcion que grafica la ruta deseada
def graficar_rutas(Graficar):   
    if Graficar == True:
        ruta2 = constructor()
        G2 = nx.DiGraph(ruta2)
        options = {
            "font_size": 10,
            "node_size": 300,
            "labels": diccion,
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


