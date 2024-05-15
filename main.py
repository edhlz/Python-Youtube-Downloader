import videofuncs
import os

def startDownload():
        
        try:  
            
            print("1. Download vídeo\n2. Download playlist inteira\n ")
            inp_1 = int(input("Insira o numero de o que você deseja: "))

            if inp_1 == 1:
                inp_2 = str(input("Insira o link do video: "))
                videofuncs.videoDownload(inp_2)

            elif inp_1 == 2:
                inp_2 = str(input("Insira o link da playlist: "))     
                videofuncs.playlistDownload(inp_2)

            else:
                "Aceitamos apenas"       
        
        except ValueError:
            print("Aceitamos apenas numeros!")


startDownload()
