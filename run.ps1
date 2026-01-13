Write-Output "reiniciando el contenedor container-postgresdb"
docker restart container-postgresdb

Write-Output "reiniciando el contenedor odoo"
docker restart odoo

Write-Output "Iniciando la pagina"
Start-Process firefox http://localhost:8069/