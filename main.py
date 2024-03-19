from flask import Flask
from blueprints import auth

app = Flask(__name__)

# 设置表单交互密钥
app.secret_key = "Lee Blog"

app.register_blueprint(auth.auth_blueprints,url_prefix="/auth")
app.run(debug=True)

