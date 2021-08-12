from django.apps import AppConfig


class MoviesConfig(AppConfig):
    name = "movies"

    def ready(self):
        import signals
