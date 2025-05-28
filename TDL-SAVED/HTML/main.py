from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todolist.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Tarea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(200), nullable=False)
    completada = db.Column(db.Boolean, default=False)

@app.route('/')
def index():
    tareas = Tarea.query.all()
    return render_template('index.html', tareas=tareas)

@app.route('/agregar', methods=['POST'])
def agregar_tarea():
    descripcion = request.form.get('descripcion')
    tarea_existente = Tarea.query.filter_by(descripcion=descripcion).first()
    if tarea_existente:
        tareas = Tarea.query.all()
        error = "Ya existe una tarea con ese nombre."
        return render_template('index.html', tareas=tareas, error=error)
    if descripcion:
        nueva_tarea = Tarea(descripcion=descripcion, completada=False)
        db.session.add(nueva_tarea)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/completar/<int:tarea_id>')
def completar_tarea(tarea_id):
    tarea = Tarea.query.get_or_404(tarea_id)
    tarea.completada = True
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/eliminar/<int:tarea_id>')
def eliminar_tarea(tarea_id):
    tarea = Tarea.query.get_or_404(tarea_id)
    db.session.delete(tarea)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
