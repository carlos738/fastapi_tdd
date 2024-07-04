import pytest
import asyncio

from uuid import UUID
from store.db.mongo import db_client

# from store.schemas.product import ProductIn, ProductUpdate
# from store.usecases.product import product_usecase
# from tests.factories import product_data, products_data
# from httpx import AsyncClient


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def mongo_client():
    return db_client.get()


@pytest.fixture(autouse=True)
async def clear_collections(mongo_client):
    yield
    collection_names = await mongo_client.get_database().ist_collection_names()
    for collection_name in collection_names:
        if collection_name.startswith("system"):
            continue

        await mongo_client.get_database()[collection_name].delete_many({})


@pytest.fixture
def product_id() -> UUID:
    return UUID("d414fd2c-a21c-4d2c-8d9d-91f099bbf0cf")


@pytest.fixture
def product_in(product_id):
    return ProductIn(**product_data(), id=product_id)
