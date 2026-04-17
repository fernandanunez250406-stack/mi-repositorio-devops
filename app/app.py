# (Dentro de app.py cambia la línea de retorno, por ejemplo:)
# return "Pipeline CI/CD actualizado automáticamente"

# 2. Guardar cambios y hacer commit
git add app/app.py
git commit -m "Actualizar mensaje en aplicación"

# 3. Subir cambios al repositorio
git push -u origin main

# 4. Esperar que el pipeline corra en GitHub Actions (ver en la pestaña Actions)

# 5. Validar la aplicación desde la terminal del Learner Lab
curl http://localhost:5000
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Pipeline CI/CD funcionando correctamente"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
