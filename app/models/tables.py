from app import db,app,UserMixin,login_manager,check_password_hash,generate_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
class User(db.Model,UserMixin):
    __tablename__='users'    
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(50))
    password=db.Column(db.String(200))

    def __init__(self,username,password):
        self.username=username
        # self.password=password
        self.password = generate_password_hash(password)
    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.username

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False
    def verify_password(self,password1):
        return check_password_hash(self.password, password1)

app.app_context().push()
