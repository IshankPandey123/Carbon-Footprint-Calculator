
class Config(object):
	"""
	Configuration base, for all environments.
	"""
	DEBUG = False
	TESTING = False

	# Get your reCaptche key on: https://www.google.com/recaptcha/admin/create
	# RECAPTCHA_PUBLIC_KEY = "6LffFNwSAAAAAFcWVy__EnOCsNZcG2fVHFjTBvRP"
	# RECAPTCHA_PRIVATE_KEY = "6LffFNwSAAAAAO7UURCGI7qQ811SOSZlgU69rvv7"


class ProductionConfig(Config):
	DEBUG = False
	TESTING = False


class DevelopmentConfig(Config):
	DEBUG = True


class TestingConfig(Config):
	TESTING = True
