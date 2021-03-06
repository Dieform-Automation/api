from flask import jsonify

from app.main import db
from app.main.model.shipment import Shipment
from app.main.model.customer import Customer
from app.main.model.shipped_part import ShippedPart
from app.main.service.shipped_part_service import save_new_shipped_part
from app.main.service.part_service import get_a_part

from ..util.validate import validate

def save_new_shipment(data):
    shipment = None

    if "date" in data.keys():
        shipment = Shipment(
            date=data['date'],
            customer_id=data['customer_id'],
            shipping_method=data['shipping_method'],
        )
    else:
        shipment = Shipment(
            shipping_method=data['shipping_method'],
        )

    save_changes(shipment)
    db.session.refresh(shipment)
    data['id'] = shipment.id # get id of newly created data
    data['shipping_method'] = shipment.shipping_method
    data['date'] = str(shipment.date)

    shipped_parts = []

    if 'shipped_parts' in data.keys():
        shipped_parts = data['shipped_parts']

    for part in shipped_parts:
        shipped_part = {
            "part_id": part['part_id'],
            "shipment_id": shipment.id,
            "bins": part['bins'],
            "quantity": part['quantity']
        }
        
        response = validate(shipped_part)

        if response:
            shipped_parts_to_delete = ShippedPart.query.filter_by(shipment_id=shipment.id).all()
            try:
                for shipped_parts in shipped_parts_to_delete:
                    shipped_parts.delete()
                    db.session.commit()
            except:
                db.session.rollback()

            try:
                Shipment.query.filter_by(id=shipment.id).delete()
                db.session.commit()
            except:
                db.session.rollback()
            
            return response # not validated

        save_new_shipped_part(shipped_part)

    return get_shipment(data['id'])[0], 201

def update_shipment(id, data):
    response = validate(data)

    if response: 
        return response # not validated

    shipment = Shipment.query.filter_by(id=id).first()
    if shipment and 'shipping_method' in data.keys():
        shipment.shipping_method = data['customer_packing_slip']
        db.session.commit()
    else:
        response_object = {
            'status': 'Not Found',
            'message': 'Shipment could not be updated.',
        }
        return response_object, 404
    
    return shipment, 204

def shipment_as_list(shipments):
    response_object = []

    for shipment in shipments:
        response_object.append(create_shipment_json(shipment))

    return jsonify(response_object), 200

def get_all_shipments():
    shipments = Shipment.query.all()

    return shipment_as_list(shipments)

def create_shipment_json(shipment):
    customer = Customer.query.filter_by(id=shipment.customer_id).first()

    return {
        'id': shipment.id,
        'date': shipment.date,
        'customer': customer.name,
        'customer_id': shipment.customer_id,
        'shipping_method': shipment.shipping_method,
        'shipped_parts': get_all_shipped_parts_from_shipment(shipment.shippedParts)
    }

def get_all_shipped_parts_from_shipment(shipped_parts):
    all_parts = []
    for shipped_part in shipped_parts:
        shipped_part_dict = shipped_part.as_dict()
        
        part = get_a_part(shipped_part_dict['part_id'])
        shipped_part_dict['part_number'] = part['number']
        shipped_part_dict['purchase_order'] = part['purchase_order']

        all_parts.append(shipped_part_dict)
    
    return all_parts

def get_shipment(id):
    shipment = Shipment.query.filter_by(id=id).first()

    if (not shipment):
        response_object = {
            'status': 'Not Found',
            'message': 'No shipment could be found with id: '+ str(id),
        }
        return response_object, 404

    return create_shipment_json(shipment), 200

def save_changes(data):
    db.session.add(data)
    db.session.commit()