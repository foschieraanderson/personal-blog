from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def get_application() -> FastAPI:
    """ Init application FastAPI """
    
    application = FastAPI()

    # CORS Settings
    origins = ['*']
    application.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )

    # Register routes
    application.include_router(routes, prefix='api/v1')

    return application

api = get_application()
