-- TRIGGER substract item from items when a new order is placed
CREATE TRIGGER items_substract_quantity
AFTER INSERT ON orders FOR EACH ROW
UPDATE items SET items.quantity = items.quantity - NEW.number
WHERE items.name = NEW.item_name;
