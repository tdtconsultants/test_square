class Parser:

    @staticmethod
    def _parse_square_to_general(square_dic):
        if 'given_name' in square_dic:
            general_first_name = square_dic['given_name']
        else:
            general_first_name = None

        if 'family_name' in square_dic:
            general_last_name = square_dic['family_name']
        else:
            general_last_name = None

        if 'company_name' in square_dic:
            general_company_name = square_dic['company_name']
        else:
            general_company_name = None

        if 'nickname' in square_dic:
            general_nickname = square_dic['nickname']
        else:
            general_nickname = None

        if 'email_address' in square_dic:
            general_email_address = square_dic['email_address']
        else:
            general_email_address = None

        if 'phone_number' in square_dic:
            general_phone_number = square_dic['phone_number']
        else:
            general_phone_number = None

        if 'note' in square_dic:
            general_note = square_dic['note']
        else:
            general_note = None

        if 'id' in square_dic:
            square_id = square_dic['id']
        else:
            square_id = None

        if 'reference_id' in square_dic:
            odoo_id = square_dic['reference_id']
        else:
            odoo_id = None

        if 'address' in square_dic:

            if 'address_line_1' in square_dic['address']:
                general_address_line_1 = square_dic['address']['address_line_1']
            else:
                general_address_line_1 = None

            if 'address_line_2' in square_dic['address']:
                general_address_line_2 = square_dic['address']['address_line_2']
            else:
                general_address_line_2 = None

            if 'locality' in square_dic['address']:
                general_locality = square_dic['address']['locality']
            else:
                general_locality = None

            if 'administrative_district_level_1' in square_dic['address']:
                general_administrative_district_level_1 = square_dic['address']['administrative_district_level_1']
            else:
                general_administrative_district_level_1 = None

            if 'postal_code' in square_dic['address']:
                general_postal_code = square_dic['address']['postal_code']
            else:
                general_postal_code = None

            if 'country' in square_dic['address']:
                general_country = square_dic['address']['country']
            else:
                general_country = None

        else:
            general_address_line_1 = None
            general_address_line_2 = None
            general_locality = None
            general_administrative_district_level_1 = None
            general_postal_code = None
            general_country = None

        general_dic = {
            'general_first_name': general_first_name,
            'general_last_name': general_last_name,
            'general_company_name': general_company_name,
            'general_nickname': general_nickname,
            'general_email_address': general_email_address,
            'general_phone_number': general_phone_number,
            'general_note': general_note,
            'square_id': square_id,
            'odoo_id': odoo_id,
            'general_address_line_1': general_address_line_1,
            'general_address_line_2': general_address_line_2,
            'general_locality': general_locality,
            'general_administrative_district_level_1': general_administrative_district_level_1,
            'general_postal_code': general_postal_code,
            'general_country': general_country,
            'key': 'square',
        }

        return general_dic

    @staticmethod
    def _parse_general_to_square(general_dic):
        square_dic = {}

        if general_dic['general_first_name']:
            given_name = general_dic['general_first_name']
            square_dic['given_name'] = given_name
        else:
            given_name = ''

        if general_dic['general_last_name']:
            family_name = general_dic['general_last_name']
            square_dic['family_name'] = family_name
        else:
            family_name = ''

        if general_dic['general_company_name']:
            company_name = general_dic['general_company_name']
            square_dic['company_name'] = company_name
        else:
            company_name = ''

        if general_dic['general_nickname']:
            nickname = general_dic['general_nickname']
            square_dic['nickname'] = nickname
        else:
            nickname = ''

        if general_dic['general_email_address']:
            email_address = general_dic['general_email_address']
            square_dic['email_address'] = email_address
        else:
            email_address = ''

        if general_dic['general_phone_number']:
            phone_number = general_dic['general_phone_number']
            square_dic['phone_number'] = phone_number
        else:
            phone_number = ''

        if general_dic['odoo_id']:
            reference_id = str(general_dic['odoo_id'])
            square_dic['reference_id'] = reference_id
        else:
            reference_id = ''

        if general_dic['general_note']:
            note = general_dic['general_note']
            square_dic['note'] = note
        else:
            note = ''

        square_dic['address'] = {}

        if general_dic['general_address_line_1']:
            address_line_1 = general_dic['general_address_line_1']
            square_dic['address']['address_line_1'] = address_line_1
        else:
            address_line_1 = ''

        if general_dic['general_address_line_2']:
            address_line_2 = general_dic['general_address_line_2']
            square_dic['address']['address_line_2'] = address_line_2
        else:
            address_line_2 = ''

        if general_dic['general_locality']:
            locality = general_dic['general_locality']
            square_dic['address']['locality'] = locality
        else:
            locality = ''

        if general_dic['general_administrative_district_level_1']:
            administrative_district_level_1 = general_dic['general_administrative_district_level_1']
            square_dic['address']['administrative_district_level_1'] = administrative_district_level_1
        else:
            administrative_district_level_1 = ''

        if general_dic['general_postal_code']:
            postal_code = general_dic['general_postal_code']
            square_dic['address']['postal_code'] = postal_code
        else:
            postal_code = ''

        if general_dic['general_country']:
            country = general_dic['general_country']
            square_dic['address']['country'] = country
        else:
            country = ''

        # square_dic ={
        #     'given_name': given_name,
        #     'family_name': family_name,
        #     'company_name': company_name,
        #     'nickname': nickname,
        #     'email_address': email_address,
        #     'phone_number': phone_number,
        #     'reference_id': reference_id,
        #     'note': note,
        #     'address': {'address_line_1': address_line_1, 'address_line_2': address_line_2,
        #                 'locality': locality, 'administrative_district_level_1': administrative_district_level_1,
        #                 'postal_code': postal_code, 'country': country}
        # }
        return square_dic

    @staticmethod
    def _parse_square_to_general_payment(square_payment_dic):

        general_payment = {}
        general_payment['general_payment_square_id'] = square_payment_dic['id']

        general_payment['general_payment_amount_money'] = {'amount': square_payment_dic['amount_money']['amount'], 'currency': square_payment_dic['amount_money']['currency']}

        if 'tip_money' in square_payment_dic:
            general_payment_tip_amount = square_payment_dic['tip_money']['amount']
            general_payment_tip_currency = square_payment_dic['tip_money']['currency']
            general_payment['tip_money'] = {'general_payment_tip_amount': general_payment_tip_amount, 'general_payment_tip_currency': general_payment_tip_currency}

        if 'app_fee_money' in square_payment_dic:
            general_payment_app_fee_amount = square_payment_dic['app_fee_money']['amount']
            general_payment_app_fee_currency = square_payment_dic['app_fee_money']['currency']
            general_payment['app_fee_money'] = {'general_payment_fee_amount': general_payment_app_fee_amount, 'general_payment_fee_currency': general_payment_app_fee_currency}

        general_payment['general_payment_status'] = square_payment_dic['status']

        general_payment['general_source_type'] = square_payment_dic['source_type']

        general_payment['general_card_details'] = {
            'card_brand': square_payment_dic['card_details']['card']['card_brand'],
            'last_4': square_payment_dic['card_details']['card']['last_4'],
            'exp_month': square_payment_dic['card_details']['card']['exp_month'],
            'exp_year': square_payment_dic['card_details']['card']['exp_year'],
            'fingerprint': square_payment_dic['card_details']['card']['fingerprint'],
            'card_type': square_payment_dic['card_details']['card']['card_type'],
            'prepaid_type': square_payment_dic['card_details']['card']['prepaid_type'],
            'bin': square_payment_dic['card_details']['card']['bin'],
        }

        general_payment['general_buyer_email_address'] = square_payment_dic['buyer_email_address']

        general_payment['square_location_id'] = square_payment_dic['location_id']
        general_payment['square_order_id'] = square_payment_dic['order_id']
        general_payment['square_customer_id'] = square_payment_dic['customer_id']

        general_payment['general_billing_address'] = square_payment_dic['billing_address']
        general_payment['general_shipping_address'] = square_payment_dic['shipping_address']

        general_payment['general_note'] = square_payment_dic['note']
        if square_payment_dic['reference_id']:
            general_payment['general_payment_odoo_id'] = square_payment_dic['reference_id']

        return general_payment
