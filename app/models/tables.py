from app import app,db,login_manager,generate_password_hash,check_password_hash,UserMixin

@login_manager.user_loader
def load_user(username):
    return User.query.filter_by(username=username).first()

class User(db.Model,UserMixin):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))
    name = db.Column(db.String(80))
    email = db.Column(db.String(120),unique=True)

    def __init__(self,username,email,password,name):
        self.username=username
        self.email=email
        self.name=name
        self.password=generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password, password)
    def is_active(self):
        """True, as all users are active."""
        return True
    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def __repr__(self):
        return f'Usuário: {self.username}'
    
    def get_id(self):
        # print('Estou no get_id',str(self.id))
        return self.username
    

    

    
class Post(db.Model):
    __tablename__ = 'posts'
    id= db.Column(db.Integer,primary_key = True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    user = db.relationship('User',foreign_keys = [user_id])

    def __init__(self,content,user_id,user):
        self.content=content
        self.user_id=user_id
        self.user=user

    # def __repr__(self):
    #     return "<Post %t>" % self.id

class Follow(db.Model):
    __tablename__ = "followers"
    id= db.Column(db.Integer,primary_key=True, unique = True)
    user_id= db.Column(db.Integer,db.ForeignKey('users.id'))
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', foreign_keys = [user_id])
    follower = db.relationship('User', foreign_keys = [follower_id])


login_manager.init_app(app)