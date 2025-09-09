from app import app,db,login_user,login_required,logout_user
from flask import render_template,redirect,url_for,request
from app.models.tables import User,load_user




@app.route('/', methods=['GET','POST'])
@login_required
def index():
    # usuarios1=User.query.all()
    user=request.form.get('apagar')
    if user:
      usu=User.query.get(user)
      # print(usu)
      db.session.delete(usu)
      db.session.commit()
      texto='usuario deletado'
      usuarios1=User.query.all()

      return render_template('homepage.html',usuarios=usuarios1,texto=texto)
    else:
      usuarios1=User.query.all()
      return render_template('homepage.html',usuarios=usuarios1)

@app.route('/cadastro',methods=['GET','POST'])
# @app.route('/homepage/<name>')
@login_required
def cadastro():
  usuario=request.form.get('usuario')
  email=request.form.get('email')
  password=request.form.get('password')
  nome=request.form.get('nome')
  if not usuario:
    info = "Usuário não informado"
  elif not email:
    info = "E-mail não informado"
  elif not password:
    info = "Senha não informada"
  elif not nome:
    info = "Nome não informado"
  else:
     user_log=User(username=usuario,email=email,password=password,name=nome)
     db.session.add(user_log)
     db.session.commit()
     info='Usuário cadastrado'
    
  
  return render_template('cadastro.html',texto1=info)

@app.route('/login',methods=['GET','POST'])
def login():
  usuario=request.form.get('usuario')
  senha=request.form.get('password')
  print(usuario)
  user=User.query.filter_by(username=usuario).first()
  if user:
    print('usuario correto')
    if user and user.verify_password(senha):
      # if user.verify_password(senha):
        print('senha correta')
        login_user(user)
        return redirect(url_for('index'))
  else:
    print('Usuário incorreto')
  # User.query.filter_by(username=usuario,)
  return render_template('login.html')

@app.route('/logout')
def redirecionar():
  logout_user()
  return redirect(url_for('login'))