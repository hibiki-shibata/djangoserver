# This is for handle app-specific route multiple databases.

# https://docs.djangoproject.com/en/5.2/topics/db/multi-db/#topics-db-multi-db-hints

class drfBackendPostgresRouter:
    
    drfBackend_app_labels = {'hibikiApp'} 

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.drfBackend_app_labels:
            return "HibikiPostgres"
        return "default"
    
    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.drfBackend_app_labels:
            return "HibikiPostgres"
        return "default"
    
# python3 manage.py migrate --database=HibikiPostgres
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.drfBackend_app_labels:
            return db == "HibikiPostgres"
        return "default"

    

    # Model specifc
    # class PostgresRouter:
    # def db_for_read(self, model, **hints):
    #     if model.__name__ == 'Answer':
    #         return 'postgres'
    #     return 'default'

 