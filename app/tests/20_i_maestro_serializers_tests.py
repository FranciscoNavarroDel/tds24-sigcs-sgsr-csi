import pytest
import json
from maestro.models import Item, Equipamiento


@pytest.mark.django_db
def test_institucion_serializer():
    pass


@pytest.mark.django_db
def test_medicamento_serializer():
    pass


@pytest.mark.django_db
def test_item_serializer():
    from maestro.serializers import ItemSerializer

    item = Item.objects.create(
        nombre="Respirador Mecánico prueba",
        tipo="soporte_vital",
    )

    data = {
        "nombre": item.nombre,
        "tipo": item.tipo,
    }

    serialized_data = ItemSerializer(data=data)
    serializer_item = ItemSerializer(item)
    serialized_data.is_valid()
    assert json.dumps(serializer_item.data) == json.dumps(data), "data serializada no tiene el mismo orden"
    assert serialized_data.errors == {}, f"Errores: {serialized_data.errors}"


@pytest.mark.django_db
def test_equipamiento_serializer():
    from maestro.serializers import EquipamientoSerializer

    item = Item.objects.create(
        nombre="Respirador Mecánico prueba",
        tipo="soporte_vital",
    )

    equipamiento = Equipamiento.objects.create(
        item=item,
        marca="GE Healthcare prueba",
        modelo="Dash 5000 prueba",
    )

    data = {"id": equipamiento.id, "item": equipamiento.item.id, "marca": equipamiento.marca, "modelo": equipamiento.modelo}

    serialized_data = EquipamientoSerializer(data=data)
    serializer_item = EquipamientoSerializer(equipamiento)
    serialized_data.is_valid()
    assert json.dumps(serializer_item.data) == json.dumps(data), "data serializada no tiene el mismo orden"
    assert serialized_data.errors == {}, f"Errores: {serialized_data.errors}"


@pytest.mark.django_db
def test_quiebre_serializer():
    from maestro.serializers import EquipamientoSerializer
