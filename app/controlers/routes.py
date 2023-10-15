from flask import render_template,request,redirect,url_for
from app import app,db,login_required,login_user,logout_user
from ..models.tables import User,load_user



# def verificar_credenciais(username1, password1):
#     userr = User.query.filter_by(username=username1).first()
#     # print(userr.password)

#     if userr and userr.password == password1:
#         return userr
#     else:
#         return None

@app.route('/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user1=request.form.get('Username')
        passs=request.form.get('password')
        if load_user(user1):
            user = User.query.filter_by(username=user1).first()
            if user:
                if user.verify_password(passs):
                    print('senha correta')
                    # print(load_user(user.id))
                    login_user(user)
                    return redirect(url_for('homepage'))
                else:
                    print('senha incorreta')

                    return redirect(url_for('login'))
            else:
                print('Usuário Incorreto')
                return redirect(url_for('login'))
                
        # print(User.verify_password(user1,passs))
        
        # return render_template('homepage.html')
    return render_template('login.html')    


    # if  type(user.id)==int :
    #     load_user(user.id)
    #     return redirect(url_for('homepage'))
    #     # return redirect(url_for('homepage'))
    # else:
    #     print('senha_errada')
    #     return render_template('index.html')
    # return render_template('index.html')
    # return redirect(url_for('homepage'))

@app.route('/logout')
# @login_required
def redirecionar1():
    logout_user()
    return redirect(url_for('login'))      
@app.route('/login')
def redirecionar():
    return redirect(url_for('login'))

@app.route('/homepage')
@login_required
def homepage():
    return render_template('homepage.html')
@app.route('/cadastro', methods=['GET','POST'])
def cadastro():
    user=request.form.get('username_cadastro')
    password=request.form.get('password_cadastro')
    password2=request.form.get('password_confir')
    if password != password2:
        infor='Senhas Não são iguais!!!'
        return render_template('cadastro.html', infor=infor)
    else:
        if user and password and password2:
            user_cadas=User(user,password)
            db.session.add(user_cadas)
            db.session.commit()
            infor='Usuário cadastrado'
            return render_template('cadastro.html',  infor=infor)
    return render_template('cadastro.html')