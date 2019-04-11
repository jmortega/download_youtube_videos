import pytube
 
try:

	video = pytube.YouTube('https://www.youtube.com/watch?v=zO23bapRYmE')
	print('-Titulo: ', video.title)
	print('-Descripcion: ', video.description)
	print('-Duracion: ', video.length, ' segundos')
	try:
		print('-Puntuacion: ', video.rating)
	except Exception as error:
		pass
	
	formatos = video.streams.all()
	print('Formatos disponibles:')
	for formato in formatos:
		print(formato)
		
	print('Descargando el video ',video.title)
	video.streams.first().download()
except Exception as error:
	print(error)