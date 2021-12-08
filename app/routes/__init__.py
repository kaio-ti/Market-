from flask import Flask

def init_app(app: Flask):
    from app.routes.users_blueprints import bp_users
    app.register_blueprint(bp_users)
    from app.routes.products_blueprints import bp_products
    app.register_blueprint(bp_products)
    from app.routes.stores_blueprints import bp_stores
    app.register_blueprint(bp_stores)
    from app.routes.sugestion_blueprints import bp_sugestions
    app.register_blueprint(bp_sugestions)
    from app.routes.favorites_blueprints import bp_favorites
    app.register_blueprint(bp_favorites)
