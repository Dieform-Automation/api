from flask import request
from flask_restplus import Resource

from ..util.dto import CustomerDto
from ..util.decorator import token_required
from ..service.customer_service import get_all_customers, get_a_customer, save_new_customer

api = CustomerDto.api
_customer = CustomerDto.customer

@api.route('/')
class CustomerList(Resource):
    @api.doc('list_of_customers')
    @api.marshal_list_with(_customer, envelope='data')
    def get(self):
        """List all customers"""
        return get_all_customers()

    @api.response(201, 'Customer successfully added.')
    @api.doc('add a new customer')
    @api.expect(_customer, validate=True)
    def post(self):
        """Creates a new customer """
        data = request.json
        return save_new_customer(data=data)


@api.route('/<id>')
@api.param('id', 'The Customer id')
@api.response(404, 'Customer not found.')
class Customer(Resource):
    @api.doc('get a customer')
    @api.marshal_with(_customer)
    def get(self, id):
        """get a customer given its id"""
        customer = get_a_customer(id)
        if not customer:
            api.abort(404)
        else:
            return customer