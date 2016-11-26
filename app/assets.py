from flask_assets import Bundle

common_css = Bundle(
    'vendor/bootstrap/dist/css/bootstrap.min.css',
    'vendor/bootstrap-select/dist/css/bootstrap-select.min.css',
    'css/main.css',
    filters='cssmin',
    output='public/css/style.css'
)

common_js = Bundle(
    'vendor/jquery/dist/jquery.min.js',
    'vendor/bootstrap/dist/js/bootstrap.min.js',
    'vendor/bootstrap-select/dist/js/bootstrap-select.min.js',
    output='public/js/scripts.js'
)
