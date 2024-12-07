# Utiliza la imagen oficial de MySQL 8
FROM mysql:8

# Configura variables de entorno para el contenedor
ENV MYSQL_DATABASE=db_itza \
    MYSQL_USER=ownitza \
    MYSQL_PASSWORD=ownitza1 \
    MYSQL_ROOT_PASSWORD=rootpassword

# Exponer el puerto 3306 para conexiones externas
EXPOSE 3306
