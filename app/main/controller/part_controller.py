from flask import request
from flask_restplus import Resource

from ..util.dto import PartDto
from ..util.decorator import crossdomain, token_required # will be used later
from ..service.part_service import get_all_parts, get_a_part, save_new_part

api = PartDto.api
_part = PartDto.part

@api.route('/')
class PartList(Resource):
    @api.doc('list_of_parts')
    @crossdomain(origin='*')
    @api.marshal_list_with(_part, envelope='data')
    def get(self):
        """List all parts"""
        return get_all_parts()

    @api.response(201, 'Part successfully added.')
    @api.doc('add a new part')
    @crossdomain(origin='*')
    @api.expect(_part, validate=True)
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
    @api.marshal_with(_part)
    def get(self, id):
        """get a part given its id"""
        part = get_a_part(id)
        if not part:
            api.abort(404)
        else:
            return part