from django.urls import path

from .views import (
    MovimientoListCreateView,
    MovimientoMedicamentoView,
    MovimientoRetrieveDestroyView,
    # MovimientoLoteRetrieveView,
    ConsumoListCreateView,
    ConsumoRetrieveDestroyView,
    ConsumoMedicamentoAPIView,
    DisponibilidadMedicamentoAPIView,
    QuiebreStockAPIView,
    AlertaCaducidadLoteAPIView,
    lista_movimientos,
    lista_caducados,
    lista_disponibilidad_medicamentos
)

app_name = "stock"
urlpatterns = [
    path("consumos", ConsumoListCreateView.as_view(), name="consumo-c"),
    path("consumos/<int:pk>", ConsumoRetrieveDestroyView.as_view(), name="consumo-rud"),
    path("movimientos", MovimientoListCreateView.as_view(), name="movimiento_lc"),
    path("movimientos/<int:pk>", MovimientoRetrieveDestroyView.as_view(), name="movimiento-rud"),
    path("movimientos-medicamento", MovimientoMedicamentoView.as_view(), name="movimiento-medicamento-l"),
    path("movimientos-medicamento/<int:medicamento>", MovimientoMedicamentoView.as_view(), name="movimiento-medicamento-d"),
    # path("movimientos/<int:pk>/lote", MovimientoLoteRetrieveView.as_view(), name="movimiento-lote-lc"),
    path("consumos-medicamento", ConsumoMedicamentoAPIView.as_view(), name="consumo-medicamento-l"),
    path("consumos-medicamento/<int:medicamento>", ConsumoMedicamentoAPIView.as_view(), name="consumo-medicamento-d"),
    path("disponibilidad-medicamento", DisponibilidadMedicamentoAPIView.as_view(), name="disponibilidad-medicamento-l"),
    path("disponibilidad-medicamento/<int:medicamento>", DisponibilidadMedicamentoAPIView.as_view(), name="disponibilidad-medicamento-d"),
    path("quiebre-stock", QuiebreStockAPIView.as_view(), name="quiebre-stock"),
    path("alerta-caducidad-lote", AlertaCaducidadLoteAPIView.as_view(), name="alerta-caducidad-lote"),


    path('movimientos/', lista_movimientos, name='list_movements'),
    path('caducidad/', lista_caducados, name='list_caducados'),
    path('disponibilidad/', lista_disponibilidad_medicamentos, name='list_medicamentos'),


    
]
