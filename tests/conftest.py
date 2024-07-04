import pytest
import asyncio


# from uuid import UUID
# from store.db.mongo import db_client
# from store.schemas.product import ProductIn, ProductUpdate
# from store.usecases.product import product_usecase
# from tests.factories import product_data, products_data


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()
