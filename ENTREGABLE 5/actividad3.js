use EstudiantesDB; // Crear o seleccionar la base de datos en MongoDB

db.Estudiantes.insertMany([
    { "nombre": "Juan", "edad": 20, "ciudad": "Bogotá" },
    { "nombre": "Ana", "edad": 22, "ciudad": "Medellín" },
    { "nombre": "Luis", "edad": 19, "ciudad": "Cali" }
]);



db.Estudiantes.find();


db.Estudiantes.find({ ciudad: "Medellín" });


db.Estudiantes.find({ edad: { $gt: 20 } });
