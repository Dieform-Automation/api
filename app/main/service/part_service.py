from app.main import db
from app.main.model.part import Part
from app.main.model.part_order import PartOrder

def save_new_part(data):
    part = Part.query.filter_by(number=data['number'], customer_id=int(data['customer_id'])).first()
    
    if not part:
        part = Part(
            customer_id=int(data['customer_id']),
            number=data['number'],
            name=data['name']
        )
        save_changes(part)
        db.session.refresh(part)
        data['id'] = part.id # get id of newly created data
        response_object = {
            'status': 'Success',
            'message': 'Successfully added part.',
            'data': data
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'Fail',
            'message': 'Part for the same customer already exists.',
        }
        return response_object, 409

def update_part(part_id, data):
    part = Part.query.filter_by(id=part_id).first()
    if part:
        part.name=data['name']
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Successfully updated part.',
            'data': data
        }
        return response_object, 204
    else:
        response_object = {
            'status': 'Not Found',
            'message': 'Part does not exist exists.',
        }
        return response_object, 404
    

def get_all_parts():
    return Part.query.all()

def get_all_parts_by_customerID(id):
    return Part.query.filter_by(customer_id=id).all()

def get_all_parts_by_orderID(id):
    return PartOrder.query.filter_by(order_id=id).all()

def get_a_part(id):
    return Part.query.filter_by(id=id).first()

def save_changes(data):
    db.session.add(data)
    db.session.commit()