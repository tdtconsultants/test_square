class Parser:
    @staticmethod
    def _parse_odoo_to_general(partner):

        name = str.split(partner.name)
        general_first_name = name[0]
        general_last_name = name[1]

        if partner.state_id:
            state_id = partner.state_id.code
        else:
            state_id = None

        if partner.country_id:
            country_code = partner.country_id.code
        else:
            country_code = None

        if partner.square_id:
            square_id = partner.square_id
        else:
            square_id = None

        general_dic = {
            'general_first_name': general_first_name,
            'general_last_name': general_last_name,
            'general_company_name': partner.company_name,
            'general_nickname': partner.display_name,
            'general_email_address': partner.email,
            'general_phone_number': partner.mobile,
            'general_note': partner.additional_info,
            'square_id': square_id,
            'odoo_id': partner.id,
            'general_address_line_1': partner.street,
            'general_address_line_2': partner.street2,
            'general_locality': partner.city,
            'general_administrative_district_level_1': state_id,
            'general_postal_code': partner.zip,
            'general_country': country_code,
            'key': 'odoo',
        }
        return general_dic

    @staticmethod
    def _parse_general_to_odoo(self, general_dic):

        if 'country' in general_dic['address'] and general_dic['address']['country'] is not None:
            country_code = general_dic['address']['country']
            country_res = self.env['res.country'].search([('code', '=', country_code)])
            if country_res:
                country = country_res.id
            else:
                country = None
        else:
            country = None

        if 'administrative_district_level_1' in general_dic['address'] and general_dic['address']['administrative_district_level_1'] is not None:
            state_id_code = general_dic['address']['administrative_district_level_1']
            country_res_state = self.env['res.country.state'].search([('code', '=', state_id_code)])
            if country_res_state:
                state_id = country_res_state.id
            else:
                state_id = None
        else:
            state_id = None

        odoo_dic = {
            'name': general_dic['general_first_name'] + ' ' + general_dic['general_last_name'],
            'street': general_dic['general_address_line_1'],
            'street2': general_dic['general_address_line_2'],
            'company_name': general_dic['general_company_name'],
            'display_name': general_dic['general_nickname'],
            'email': general_dic['general_email_address'],
            'mobile': general_dic['general_phone_number'],
            'zip': general_dic['general_postal_code'],
            'country_id': country,
            'city': general_dic['general_locality'],
            'state_id': state_id,
            'square_id': general_dic['square_id'],
            'additional_info': general_dic['general_note']
        }
        return odoo_dic

    def _parse_payment_general_to_odoo(self, general_payment):
        odoo_payment = {}

        odoo_payment['payment_square_id'] = general_payment['general_payment_square_id']
        odoo_payment['amount'] = general_payment['general_payment_amount_money']['amount']
        currency = self.env['res.currency'].search([('name', '=', general_payment['general_payment_amount_money']['currency'])])
        odoo_payment['currency_id'] = currency.id
        if 'tip_money' in general_payment:
            odoo_payment['tip_amount'] = general_payment['tip_money']['general_payment_tip_amount']
            currency_tip = self.env['res.currency'].search([('name', '=', general_payment['tip_money']['general_payment_tip_currency'])])
            odoo_payment['tip_currency_id'] = currency_tip.id
        if 'app_fee_money' in general_payment:
            odoo_payment['app_fee_amount'] = general_payment['app_fee_money']['general_payment_fee_amount']
            currency_fee = self.env['res.currency'].search([('name', '=', general_payment['app_fee_money']['general_payment_fee_currency'])])
            odoo_payment['app_fee_currency_id'] = currency_fee.id
        odoo_payment['payment_status'] = general_payment['general_payment_status']

        shipping_address = self.env['ShippingAddress'].create(general_payment['general_shipping_address'])
        odoo_payment['shipping_address_id'] = shipping_address.id

        billing_address = self.env['BillingAddress'].create(general_payment['general_billing_address'])
        odoo_payment['billing_address_id'] = billing_address.id





