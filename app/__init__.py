from flask_restplus import Api
from flask import Blueprint

from .main.controller.customer_controller import api as customer_ns
from .main.controller.part_controller import api as part_ns
from .main.controller.order_controller import api as order_ns
from .main.controller.receiving_controller import api as receiving_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Logbook API',
          version='1.0',
          description=''
          )

api.add_namespace(customer_ns, path='/customer')
api.add_namespace(part_ns, path='/part')
api.add_namespace(order_ns, path='/order')
api.add_namespace(receiving_ns, path='/receiving')