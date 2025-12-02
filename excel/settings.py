from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# La SECRET_KEY se toma de una variable de entorno en producción por seguridad.
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-@^gleq)jv@x*6ybecfnupb*tr^@f0$f97a24cb9adsc@0ra3(b')

# DEBUG se controla con una variable de entorno. Será 'False' en producción.
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

ALLOWED_HOSTS = []
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Inventario.apps.InventarioConfig', 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Añadir WhiteNoise aquí
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'excel.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'excel.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static'] # Directorio de estáticos en desarrollo
STATIC_ROOT = BASE_DIR / 'staticfiles' # Directorio para estáticos en producción
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' # Para WhiteNoise

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = 'lista_inventario'
LOGOUT_REDIRECT_URL = '/accounts/login/'

# --- Configuración de Envío de Correo ---

# Para desarrollo: Imprime el correo en la consola en lugar de enviarlo.
# Esto es ideal para probar sin configurar un servidor de correo real.
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# --- Configuración para enviar correos reales con Resend (vía SMTP) ---
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.resend.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'resend'  # Este valor es siempre 'resend' para Resend
# La API Key de Resend se toma de una variable de entorno.
EMAIL_HOST_PASSWORD = os.environ.get('RESEND_API_KEY')

# El correo desde el que se enviarán los mensajes.
# DEBE ser un correo de un dominio que hayas verificado en Resend.
# Por ejemplo: 'noreply@tudominio.com'
# El correo remitente se toma de una variable de entorno.
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', 'onboarding@resend.dev')
