from flask import Blueprint, jsonify, request
from app.db import get_session
from app.models import Contact, Email, Phone

contact_bp = Blueprint("contacts", __name__, url_prefix="/api/v1/contacts")

def to_dict(contact)->dict:
    return {
        "id": contact.id,
        "first_name": contact.first_name,
        "last_name": contact.last_name,
        "nick_name": contact.nick_name,
        "date_of_birth": contact.date_of_birth,
        "notes": contact.notes,
        "created_at": contact.created_at.isoformat() if contact.created_at else None,
        "updated_at": contact.updated_at.isoformat() if contact.updated_at else None,
        "emails" : [{
            "email": e.email,
            "label": e.label,
            "is_primary": e.is_primary,
        }
        for e in contact.emails
        ],
        "phones": [{
            "numner": p.number,
            "label": p.label,
            "is_primary": p.is_primary,
        }
        for p in contact.phones
        ],
    }
    
@contact_bp.route("", methods=["POST"])
def create_contact():
    data = request.get_json()
    session = get_session()
    try:
        contact = Contact(
            first_name =  data["first_name"],
            last_name = data["last_name"],
            nick_name = data.get("nick_name"),
            date_of_birth = data.get("date_of_birth"),
            notes = data.get("notes"),
        )
        
        for email_data in data.get("emails",[]):
            email = Email(
                email = email_data["email"],
                label = email_data.get("label"),
                is_primary = email_data.get("is_primary", False),
            )
            contact.emails.append(email)

        for phone_data in data.get("phones", []):
            phone = Phone(
                number = data["number"],
                label = data.get("label"),
                is_primary = data.get("is_primary", False)
            )
            contact.phones.append(phone)

        session.add(contact)
        session.commit()
        session.refresh(contact)
        return jsonify(to_dict(contact)), 201
    except Exception as e:
        session.rollback()
        return jsonify({
            "error": str(e)
        }), 500
    finally:
        session.close()

@contact_bp.route("", methods=["GET"])
def list_all_contacts():

    session = get_session()
    try:
        contacts = session.query(Contact).all()
        return jsonify([to_dict(c) for c in contacts]), 200
    finally:
        session.close()
