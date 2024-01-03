#Fantasy Game Inventory
inventory_Knight={'Shield': 1, 'Sword': 1, 'Armor': 1, 'Helmet': 1, 'Torch': 4, 'Arrows': 20, 'Bow': 1 }
inventory_Wizard={'Toxic poison':5, 'Night Vision Potion': 3, 'Wand': 1}

dragonLoot=['Golden coins', 'Dagger', 'Dragon scale', 'Golden coins', 'Golden coins']

def displayInventory(inventory):
    print('Inventory:')
    total_items=0
    for x,y in inventory.items():
        print(str(y)+' '+x)
        total_items+=y
    print('Total items: '+ str(total_items))

def addToInventory(inventory, addedItems):
    for i in addedItems:
        newOne=False
        for x,y in inventory.items():
            if i==x:
                inventory.update({i: y+1})
                newOne=True
        if newOne==False:
            newItem=i
            inventory.update({newItem: 1})
    print('New items have been added to inventory!')

def removeFromInventory(inventory,item,howMuch):
    for x,y in inventory.items():
        if x==item:
            if y>howMuch:
                inventory[x]-=howMuch
            else:
                inventory.pop(x)
            break
    print('The specified number of items has been removed!')

displayInventory(inventory_Knight)
displayInventory(inventory_Wizard)
addToInventory(inventory_Knight, dragonLoot)
displayInventory(inventory_Knight)
removeFromInventory(inventory_Knight,'Arrows',4)
displayInventory(inventory_Knight)
removeFromInventory(inventory_Knight,'Helmet',1)
displayInventory(inventory_Knight)