class Parser:

    @staticmethod
    def _parse_square_to_general(square_dic):
        general_dic = {
            'key': 'square',
            'type': 'customer',
            'data': square_dic,
        }
        return general_dic

    @staticmethod
    def _parse_general_to_square(general_dic):
        square_dic = {}

        if general_dic['general_first_name']:
            given_name = general_dic['general_first_name']
            square_dic['given_name'] = given_name

        if general_dic['general_last_name']:
            family_name = general_dic['general_last_name']
            square_dic['family_name'] = family_name

        if general_dic['general_company_name']:
            company_name = general_dic['general_company_name']
            square_dic['company_name'] = company_name

        if general_dic['general_nickname']:
            nickname = general_dic['general_nickname']
            square_dic['nickname'] = nickname

        if general_dic['general_email_address']:
            email_address = general_dic['general_email_address']
            square_dic['email_address'] = email_address

        if general_dic['general_phone_number']:
            phone_number = general_dic['general_phone_number']
            square_dic['phone_number'] = phone_number

        if general_dic['odoo_id']:
            reference_id = str(general_dic['odoo_id'])
            square_dic['reference_id'] = reference_id

        if general_dic['general_note']:
            note = general_dic['general_note']
            square_dic['note'] = note

        square_dic['address'] = {}

        if general_dic['general_address_line_1']:
            address_line_1 = general_dic['general_address_line_1']
            square_dic['address']['address_line_1'] = address_line_1

        if general_dic['general_address_line_2']:
            address_line_2 = general_dic['general_address_line_2']
            square_dic['address']['address_line_2'] = address_line_2

        if general_dic['general_locality']:
            locality = general_dic['general_locality']
            square_dic['address']['locality'] = locality

        if general_dic['general_administrative_district_level_1']:
            administrative_district_level_1 = general_dic['general_administrative_district_level_1']
            square_dic['address']['administrative_district_level_1'] = administrative_district_level_1

        if general_dic['general_postal_code']:
            postal_code = general_dic['general_postal_code']
            square_dic['address']['postal_code'] = postal_code

        if general_dic['general_country']:
            country = general_dic['general_country']
            square_dic['address']['country'] = country

        return square_dic

    @staticmethod
    def _parse_square_to_general_payment(square_payment_dic):

        general_payment = {
            'key': 'square',
            'type': 'payment',
            'data': square_payment_dic
        }

        return general_payment

    @staticmethod
    def _parse_square_location_to_general(square_location):
        general_location = {
            'key': 'square',
            'type': 'location',
            'data': square_location
        }

        return general_location

    @staticmethod
    def _parse_square_order_to_general(square_order):
        general_order = {
            'key': 'square',
            'type': 'order',
            'data': square_order
        }

        return general_order

    @staticmethod
    def _parse_square_item_to_general(square_item):
        general_item = {
            'key': 'square',
            'type': 'item',
            'data': square_item
        }

        return general_item

    @staticmethod
    def _parse_square_category_to_general(square_category):
        general_category = {
            'key': 'square',
            'type': 'category',
            'data': square_category
        }

        return general_category

    @staticmethod
    def _parse_square_item_variation_to_general(square_item_variation):
        general_item_variation = {
            'key': 'square',
            'type': 'item_variation',
            'data': square_item_variation
        }

        return general_item_variation

