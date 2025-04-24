import django

def setup(set_prefix=True):
    """
    Configure the settings (this happens as a side effect of accessing the
    first setting), configure logging and populate the app registry.
    Set the thread-local urlresolvers script prefix if `set_prefix` is True.
    """
    from django.apps import apps
    from django.conf import settings
    from django.urls import set_script_prefix
    from django.utils.log import configure_logging
    settings.configure()
    configure_logging(settings.LOGGING_CONFIG, settings.LOGGING)
    if set_prefix:
        set_script_prefix(
            "/" if settings.FORCE_SCRIPT_NAME is None else settings.FORCE_SCRIPT_NAME
        )
    apps.populate(settings.INSTALLED_APPS)


setup()

from websockets.sync.server import serve


def handler(websocket):
    sesame = websocket.recv()
    websocket.send(f"Hello!")


def main():
    with serve(handler, "0.0.0.0", 8888) as server:
        server.serve_forever()


if __name__ == "__main__":
    main()