from flask import request
from flask_restplus import Resource

from ..util.dto import PartDto
from ..util.decorator import crossdomain, token_required # will be used later
from ..service.part_service import get_all_parts, get_a_part, save_new_part, update_part, get_all_parts_by_customerID

api = PartDto.api
_post_part = PartDto.part_post
_get_part = PartDto.part_get
_put_part = PartDto.part_put

@api.route('/')
class PartList(Resource):
    @api.doc('list_of_parts')
    @crossdomain(origin='*')
    def get(self):
        """List all parts"""
        customer_id = request.args.get('customer_id', None)
        if customer_id:
            return get_all_parts_by_customerID(int(customer_id))
        else:
            return get_all_parts()

    @api.response(201, 'Part successfully added.')
    @api.doc('add a new part')
    @crossdomain(origin='*')
    @api.expect(_post_part, validate=True)
    def post(self):
        """Creates a new part """
        data = request.json
        return save_new_part(data=data)

@api.route('/<id>')
@api.param('id', 'The Part id')
@api.response(404, 'Part not found.')
class Part(Resource):
    @api.doc('get a part')
    @crossdomain(origin='*')
    @api.marshal_with(_get_part)
    def get(self, id):
        """get a part given its id"""
        part = get_a_part(id)
        if not part:
            api.abort(404)
        else:
            return part

    @api.response(204, 'Successfully updated part.')
    @api.doc('update a part')
    @crossdomain(origin='*')
    @api.expect(_put_part, validate=True)
    def put(self, id):
        """Updates a part """
        data = request.json
        return update_part(id, data=data)