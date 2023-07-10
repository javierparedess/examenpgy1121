import os
os.system("cls")

entradas=[1,2,3,4,5,6,7,8,9,10,11,12,13,"X",15,16,17,18,19,20,
21,22,23,24,25,26,27,28,29,30,31,"X",33,34,35,36,37,38,39,40,41,42,43,44,"X",46,47,48,49,50,
51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90
,91,92,93,94,95,96,97,98,99,100]

registro=[]
valorntradatotal=[]


def escenario():
      print(f"""
                
                        ******** ESCENARIO ********


                    {entradas[0]} {entradas[1]} {entradas[2]} {entradas[3]} {entradas[4]} {entradas[5]} {entradas[6]} {entradas[7]} {entradas[8]} {entradas[9]}
                    {entradas[10]} {entradas[11]} {entradas[12]} {entradas[13]} {entradas[14]} {entradas[15]} {entradas[16]} {entradas[17]} {entradas[18]} {entradas[19]}
                    {entradas[20]} {entradas[21]} {entradas[22]} {entradas[23]} {entradas[24]} {entradas[25]} {entradas[26]} {entradas[27]} {entradas[28]} {entradas[29]}
                    {entradas[30]} {entradas[31]} {entradas[32]} {entradas[33]} {entradas[34]} {entradas[35]} {entradas[36]} {entradas[37]} {entradas[38]} {entradas[39]}
                    {entradas[40]} {entradas[41]} {entradas[42]} {entradas[43]} {entradas[44]} {entradas[45]} {entradas[46]} {entradas[47]} {entradas[48]} {entradas[49]}
                    {entradas[50]} {entradas[51]} {entradas[52]} {entradas[53]} {entradas[54]} {entradas[55]} {entradas[56]} {entradas[57]} {entradas[58]} {entradas[59]}
                    {entradas[60]} {entradas[61]} {entradas[62]} {entradas[63]} {entradas[64]} {entradas[65]} {entradas[66]} {entradas[67]} {entradas[68]} {entradas[69]}
                    {entradas[70]} {entradas[71]} {entradas[72]} {entradas[73]} {entradas[74]} {entradas[75]} {entradas[76]} {entradas[77]} {entradas[78]} {entradas[79]}
                    {entradas[80]} {entradas[81]} {entradas[82]} {entradas[83]} {entradas[84]} {entradas[85]} {entradas[86]} {entradas[87]} {entradas[88]} {entradas[89]}
                    {entradas[90]} {entradas[91]} {entradas[92]} {entradas[93]} {entradas[94]} {entradas[95]} {entradas[96]} {entradas[97]} {entradas[98]} {entradas[99]}
                """)
      
def mostrar_asiento():
             for mostrar in registro:
                  print(mostrar)

    

        

while True:
    print("""

        ******** Concierto Michael Jam ********


            1.- comprar entradas
            2.- Mostrar ubicaciones disponible
            3.- Ver listado de asistente
            4.- Mostrar ganancias totales
            5.- Salir
    
    """)
    opcion=input("ingresar opcion : ")
    match opcion:
        case "1":
            cantidadentrada=int(input("Cuantas entradas desea ? maximo 3 entradas por persona : "))
            if cantidadentrada <=3 and cantidadentrada >0:
                escenario()
                asiento=int(input("seleccione su asiento : "))
                if asiento in entradas:
                        rut=input("ingrese rut sin punto , giones ni digito verificador :")
                        registroasiento=asiento,rut
                        registro.append(registroasiento)
                        print("registro completado")
                        asientorem=asiento-1
                        entradas[asientorem]="X"  

                        if asiento in range(0,21):
                              valorentrada=120000
                              
                              costo=cantidadentrada*valorentrada
                              valorntradatotal.append(costo)
                              print(f"""
                                rut : {rut}
                                asiento : {asiento}
                                total : $ {costo}
                                """)
                        elif asiento in range(20,51):
                              valorentrada=80000
                              
                              costo=cantidadentrada*valorentrada
                              valorntradatotal.append(costo)
                              print(f"""
                                rut : {rut}
                                asiento : {asiento}
                                total : $ {costo}
                                """)
                        elif asiento in range(50,101):
                              valorentrada=50000
                              
                              costo=cantidadentrada*valorentrada
                              valorntradatotal.append(costo)
                              print(f"""
                                rut : {rut}
                                asiento : {asiento}
                                total : $ {costo}
                                """)

                              
                              

                                      
                else:
                    print("asiento no disponible")

            else:
                print("Exede el maximo de entradas por persona ")
        case "2":
                   escenario()
        case "3":
            for mostrar in registro:
                  print(f"""
                  rut : {mostrar[1]}
                  asiento : {mostrar[0]}
                  """)
        case "4":
            print(f"recudacion total {sum(valorntradatotal)}")
        case "5":
            print("saliendo ....")
            break
        case other:
            print("opcion incorrecta...")