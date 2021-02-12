if 'type' in parsed_message and parsed_message['type'] == 'inventory':
    inventory_lines = parsed_message['data']
    square_inv = self.env['stock.inventory'].create({'name': 'Square inventory adjustment ' + str(datetime.datetime.now())})
    square_inv.action_start()
    for line in inventory_lines:
        inventory_line = line['adjustment']
        is_existing_adjustment = self.env['stock.inventory.line'].search([('square_inv_line_id', '=', inventory_line['id'])])
        if not is_existing_adjustment:
            warehouse = self.env['stock.warehouse'].search([('square_location_id', '=', inventory_line['location_id'])])
            location_view = self.env['stock.location'].search([('id', '=', warehouse.view_location_id.id)])
            location_stock_name = location_view.name + '/Stock'
            location_stock = self.env['stock.location'].search([('complete_name', '=', location_stock_name), ('location_id', '=', location_view.id)])
            item = self.env['product.product'].search([('square_item_id', '=', inventory_line['catalog_object_id'])])
            line_in_odoo = False
            i = 0
            while not line_in_odoo and i < len(square_inv.line_ids):
                line = square_inv.line_ids[i]
                if line.product_id.id == item.id and line.location_id.id == location_stock.id:
                    if inventory_line['to_state'] == 'IN_STOCK':
                        new_qty = line.product_qty + int(inventory_line['quantity'])
                    else:
                        new_qty = line.product_qty - int(inventory_line['quantity'])
                    line.update({'product_qty': new_qty, 'square_inv_line_id': inventory_line['id']})
                    line_in_odoo = True
                i = i + 1
            if not line_in_odoo:
                new_inventory_line = {
                    'product_id': item.id,
                    'location_id': location_stock.id,
                    'product_qty': int(inventory_line['quantity']),
                    'product_uom_id': 1,
                    'company_id': 1,
                    'inventory_id': square_inv.id,
                    'square_inv_line_id': inventory_line['id']
                }
                self.env['stock.inventory.line'].create(new_inventory_line)
    square_inv.action_validate()

if 'type' in parsed_message and parsed_message['type'] == 'inventory_re_count':
    inventory_recount_lines = parsed_message['data']
    square_inv = self.env['stock.inventory'].create({'name': 'Square inventory adjustment ' + str(datetime.datetime.now())})
    square_inv.action_start()
    for inventory_recount_line in inventory_recount_lines:
        warehouse = self.env['stock.warehouse'].search([('square_location_id', '=', inventory_recount_line['location_id'])])
        location_view = self.env['stock.location'].search([('id', '=', warehouse.view_location_id.id)])
        location_stock_name = location_view.name + '/Stock'
        location_stock = self.env['stock.location'].search([('complete_name', '=', location_stock_name), ('location_id', '=', location_view.id)])
        item = self.env['product.product'].search([('square_item_id', '=', inventory_recount_line['catalog_object_id'])])
        line_in_odoo = False
        i = 0
        while not line_in_odoo and i < len(square_inv.line_ids):
            line = square_inv.line_ids[i]
            if line.product_id.id == item.id and line.location_id.id == location_stock.id:
                if inventory_recount_line['state'] == 'IN_STOCK':
                    new_qty = int(inventory_recount_line['quantity'])
                else:
                    new_qty = line.product_qty - int(inventory_recount_line['quantity'])
                line.update({'product_qty': new_qty})
                line_in_odoo = True
            i = i + 1
        if not line_in_odoo:
            new_inventory_recount_line = {
                'product_id': item.id,
                'location_id': location_stock.id,
                'product_qty': int(inventory_recount_line['quantity']),
                'product_uom_id': 1,
                'company_id': 1,
                'inventory_id': square_inv.id,
            }
            self.env['stock.inventory.line'].create(new_inventory_recount_line)
    square_inv.action_validate()
