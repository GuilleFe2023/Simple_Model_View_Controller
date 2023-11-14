# -*- coding: utf-8 *-*
from db_connection import DBConn


class Persona:

    def __init__(self):
        self.idpersona =''
        self.nombre = ''
        self.apellido = ''
        self.dni = 0
        self.fecha_nacimiento = ''
        self.genero= ''
        self.db = DBConn()

    def create(self):
        """Crear un nuevo registro"""
        query = "INSERT INTO persona VALUES (null,?,?,?,'null','null')"
        values = (self.nombre, self.apellido, self.dni, self.genero)
        self.db.ejecutar(query, values)

    def update(self):
        """Actualizar un registro existente"""
        query = "UPDATE persona SET nombre = ?, apellido = ?, dni = ? WHERE idpersona = ?, genero = ?"
        values = (self.nombre, self.apellido, self.dni, self.idpersona, self.genero)
        return self.db.ejecutar(query, values)

    def read_all(self):
        """Leer todos los registros"""
        query = "SELECT idpersona, nombre , apellido , genero , dni FROM persona"
        return self.db.ejecutar(query)

    def read(self):
        query = "SELECT idpersona, nombre, apellido, genero, dni FROM persona WHERE idpersona = ?"
        values = (self.idpersona)
        return self.db.ejecutar(query, values)
    
    def delete(self):
        """Elimina uno o todos los registros"""
        query = "DELETE FROM persona WHERE idpersona = ?"
        values = self.idpersona
        return self.db.ejecutar(query, values)
    