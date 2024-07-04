from typing import List
from uuid import UUID

import pytest
from store.core.exceptions import NotFoundException
from store.schemas.product import ProductOut, ProductUpdateOut
from store.usecases.product import product_usecase


async def test_usecases_create_should_return_success(product_in):
    result = await product_usecase.create(body=product_in)

    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 Pro Max"


async def test_usecases_get_should_return_success(produtct_inserted):
    result = await product_usecase.get(id=produtct_inserted.id)

    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 Pro Max"


async def test_usecases_get_should_not_found():
    with pytest.raises(NotFoundException) as err:
        await product_usecase.get(id=UUID("8089c92c-2b3d-40f8-adf4-c352e79df959"))
    # breakpoint()
    assert (
        err.value.message
        == "Product not found with filter: 8089c92c-2b3d-40f8-adf4-c352e79df959 "
    )
