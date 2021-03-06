from flask_restplus import Api
from flask import Blueprint

from .main.controller.customer_controller import api as customer_ns
from .main.controller.part_controller import api as part_ns
from .main.controller.purchase_order_controller import api as purchase_order_ns
from .main.controller.receiving_order_controller import api as receiving_order_ns
from .main.controller.shipment_controller import api as shipment_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Logbook API',
          version='1.0',
          description=''
          )

api.add_namespace(customer_ns, path='/customer')
api.add_namespace(part_ns, path='/part')
api.add_namespace(purchase_order_ns, path='/purchase_order')
api.add_namespace(shipment_ns, path='/shipment')
api.add_namespace(receiving_order_ns, path='/receiving_order')