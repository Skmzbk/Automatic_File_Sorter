import os
import shutil

while True:
    # Asking the user for the binder's path
    path=input("Enter path or exit to exit ")

    if path == 'exit':
        break

    # Confirms if the binder exists
    if not os.path.exists(path):
        print("❌ Path does not exists.")
        continue

    # List of items
    items=os.listdir(path)
        
    # Detects al items in the binder
    for archivo in items:
        ruta_archivo = os.path.join(path, archivo)
        #print(archivo,ruta_archivo)
            
        # If its a binder it skips it
        if os.path.isdir(ruta_archivo):
            continue
            
        # Getting file extensions
        extension = os.path.splitext(archivo)[1][1:].upper()
        #print(extension)
    
        # If the items does not have an extension is sent to "no extension"
        if extension == "":
                extension = "NO_EXTENSION"
                
        # Name of the binder for this extension
        carpeta_destino = os.path.join(path, extension + "_FILES")
        
        # If the binder does not exists, it is created
        if not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)
            print(extension+" was created")
                    
        # Moves the item to the binder
        shutil.move(ruta_archivo, os.path.join(carpeta_destino, archivo))
        print(archivo+" has been moved to "+extension+"_FILES")
    print("✅ Organization is completed!")