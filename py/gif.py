from PIL import Image
import os

#imagens PNG
image_paths = ["01-06-2023.png", "01-07-2023.png", "01-08-2023.png", "01-09-2023.png","01-10-2023.png","01-11-2023.png","01-12-2023.png"]

#Abra as imagens
images = [Image.open(path) for path in image_paths]

#Especifique o caminho do arquivo GIF de saída
output_gif_path = "output.gif"

#Salve as imagens como um arquivo GIF
images[0].save(
    output_gif_path,
    save_all=True,
    append_images=images[1:],
    duration=500,  # Especifica a duração de cada frame em milissegundos
    loop=0  # 0 significa loop infinito; use 1 para loop único, 2 para loop duplo, etc.
)

print(f"GIF criado com sucesso em: {output_gif_path}")
#as imagens que usei de exemplo estao na pasta e o gif ficara la tambem