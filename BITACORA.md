24/9 Encontre problemas al intentar crear el entorno y al comenzar la estructura inicial pero se soluciono todo de manera correcta.

30/9
Se termino el tutorial con que se aplica la base del blog,ahora hay que conectarlo y complementarlo con mi portfolio 

1/10
Se crea estructura de carpetas modularizada donde se implementa el portfolio junto con su css, html, imágenes y más.
Todavia el blog continua vacío
El unico error que encontre fue que me tiraba un error al poner la información de contacto que solucione
poniendo este token:  {% csrf_token %}

6/10 
Se integra el blog en el proyecto ademas de darle la posibilidad de integrar imagenes en los post 
falta todavia separar el base css del de el portfolio
Los errores que encontre fueron mínimos y fueron solucionados rapidamente

7/10 
-Se mejora visualmente el portfolio y algunos bugs como el no cargado correctamente de imagenes

-Se agregan posts de demostracion junto con sus imagenes, titulos y descripciones de cada uno

-Se modulariza el CSS que antes se encontraba todo en base.css poniendo lo perteneciente al css del portfolio en portfolio.css y lo que combina el blog y el portfolio en base.css

Encontre un problema en la descripcion previa del post.Ya que muchos de estas eran largas e incomodas.
Lo solucione agregando otro campo para completar una breve introduccion

summary = models.CharField(max_length=200, blank=True)

Y si este no se llena la descripcion se autorellena con las primeras 30 palabras del post.

return self.summary or Truncator(self.body).words(30)

8/10 
Se solucionan problemas de distribucion de elementos ya que la distribucion de las tarjetas cambiaba segun el monitor (4 columnas en uno, 3 y 2 en otro) y en las categorias con pocos posts quedaban pegadas a la izquierda. Lo resolvi pasando de grid auto-fit a un contenedor flex con wrap y justify-content: center, con ancho fijo por tarjeta (3 columnas en escritorio, 2 en tablet, 1 en celular):

.blog-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 2rem;
}

.blog-card {
  flex: 0 1 calc((100% - 4rem) / 3);
  min-width: 0;
}

@media (max-width: 991px) {
  .blog-card {
    flex-basis: calc((100% - 2rem) / 2);
  }
}

@media (max-width: 640px) {
  .blog-card {
    flex-basis: 100%;
  }
}

Admemas se arma el README.MD en el cual se encuentra una vision general del proyecto y sus caracteristicas como su estructura 

Por cuestion de tiempo me quedo pendiente el registro de usuarios para comentar que era un aspecto que queria implementar, pero en general y a pesar de algunos errores en el camino, el desarrollo del proyecto fue avanzando correctamente a lo largo del tiempo




