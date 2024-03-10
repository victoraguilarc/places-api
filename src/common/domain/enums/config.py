from src.common.domain import BaseEnum


class AppConfigEnv(BaseEnum):
    DEVELOPMENT = 'development'
    TESTING = 'testing'
    PRODUCTION = 'production'

    @property
    def is_production(self):
        return self == self.PRODUCTION

    @property
    def is_development(self):
        return self == self.DEVELOPMENT

    @property
    def is_testing(self):
        return self == self.TESTING


class AppDeployStage(BaseEnum):
    DEVELOPMENT = 'dev'
    STAGING = 'stg'
    PRODUCTION = 'prod'

    @property
    def is_production(self):
        return self == self.PRODUCTION

    @property
    def is_development(self):
        return self == self.DEVELOPMENT

    @property
    def is_staging(self):
        return self == self.STAGING
