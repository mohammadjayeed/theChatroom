from channels.auth import AuthMiddleware
from channels.routing import ProtocolTypeRouter, URLRouter
import chat_app.routing

application = ProtocolTypeRouter({
    'web_socket': AuthMiddleware(
        URLRouter(

            chat_app.routing.websocket_urlpatterns

        )


    ),


})
